#!/usr/bin/env python3
"""
Messaging Load Test
Tests messaging functionality including viewing messages and submitting new messages
"""

import sys
import os
import base64
import json
import struct
import time
import uuid
from locust import task, between

# Add parent directory to path to import from common
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.auth import AuthenticatedUser

class MessagingLoadTest(AuthenticatedUser):
    """
    Load test for messaging functionality.
    
    Tests both viewing the messaging interface and submitting messages
    via the gRPC-Web API that was discovered in the HAR file.
    
    Environment Variables:
    - MESSAGE_ID: Specific message ID to test with (required)
    - CHANNEL_ID: Specific channel ID to test with (required)
    """
    
    wait_time = between(2, 6)  # Wait 2-6 seconds between requests
    
    # Use environment variables directly - required
    MESSAGE_ID = os.getenv('MESSAGE_ID', "dd6ddd7e-8c25-4b5c-a59b-c8389307252a")  # Default from HAR
    CHANNEL_ID = os.getenv('CHANNEL_ID', "dd6ddd7e-8c25-4b5c-a59b-c8389307252a")  # Default from HAR
    TEST_MESSAGE_TEXT = "loadtest"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Track created message IDs for cleanup
        self.created_message_ids = []
        self.messages_to_cleanup = []
    
    @task(4)  # Primary task - weight 4
    def view_messaging_page(self):
        """Test viewing the messaging page with specific message/channel"""
        endpoint = "/messaging"
        params = {
            'messageKey': 'channelId',
            'messageId': self.MESSAGE_ID,
            'channelId': self.CHANNEL_ID
        }
        
        # Construct URL with query parameters
        url = f"{endpoint}?messageKey={params['messageKey']}&messageId={params['messageId']}&channelId={params['channelId']}"
        
        with self.client.get(url, catch_response=True, name="view_messaging") as response:
            if response.status_code == 200:
                response.success()
                print(f"✅ Successfully loaded messaging page")
            elif response.status_code == 404:
                response.failure("Message or channel not found")
                print(f"❌ Message/channel not found: {url}")
                print(f"💡 Check your MESSAGE_ID and CHANNEL_ID environment variables")
            elif response.status_code == 403:
                response.failure("Access denied to messaging")
                print(f"❌ Access denied to messaging: {url}")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
                print(f"⚠️ Unexpected response: {response.status_code} for {url}")
    
    @task(3)  # Secondary task - weight 3
    def submit_message_grpc(self):
        """Test submitting a message via the gRPC-Web API (discovered in HAR)"""
        try:
            # Create a unique message for each request
            timestamp = int(time.time())
            unique_id = uuid.uuid4().hex[:8]
            dynamic_message = f"{self.TEST_MESSAGE_TEXT}-{timestamp}-{unique_id}"
            
            # Create properly formatted gRPC-Web payload
            grpc_payload = self._create_grpc_message_payload(
                channel_id=self.CHANNEL_ID,
                message_text=dynamic_message
            )
            
            # Fix Origin header generation - extract subdomain properly
            # For email like mhansen+thundercats@guidecx.com, we want thundercats.staging.guidecx.io
            email = os.getenv('LOGIN_EMAIL', '')
            if '+' in email and '@' in email:
                subdomain = email.split('+')[1].split('@')[0]
                origin_host = f"https://{subdomain}.staging.guidecx.io"
            else:
                origin_host = self.host
            
            # Headers from HAR analysis
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text',
                'x-grpc-web': '1',
                'Origin': origin_host,
                'Referer': f'{origin_host}/messaging?messageKey=channelId&messageId={self.MESSAGE_ID}&channelId={self.CHANNEL_ID}'
            }
            
            # Use the access token from initial authentication (stored in session_data)
            print(f"🔍 Using stored session data: {list(self.session_data.keys()) if isinstance(self.session_data, dict) else 'Not a dict'}")
            
            if self.session_data and isinstance(self.session_data, dict) and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
                print(f"🔑 Using stored auth token: {self.session_data['accessToken'][:50]}...")
            else:
                print(f"❌ No access token available in stored session data!")
                print(f"🔍 Available data: {self.session_data}")
                return
            
            # Make the gRPC-Web request to k2-web subdomain
            grpc_host = self.host.replace('app.', 'k2-web.')
            grpc_url = f"{grpc_host}/manager.message.messages.MessageService/SaveMessage"
            
            print(f"🌐 gRPC URL: {grpc_url}")
            print(f"🌐 Origin: {origin_host}")
            
            with self.client.post(
                grpc_url,
                data=grpc_payload,
                headers=headers,
                catch_response=True,
                name="submit_message_grpc"
            ) as response:
                if response.status_code == 200:
                    # Check for gRPC-level errors in headers
                    grpc_status = response.headers.get('grpc-status', '0')
                    grpc_message = response.headers.get('grpc-message', '')
                    
                    if grpc_status == '0':
                        response.success()
                        print(f"✅ Successfully submitted message: '{dynamic_message}'")
                        
                        # Debug: Log response details
                        print(f"🔍 gRPC Response Status: {response.status_code}")
                        if response.text:
                            print(f"🔍 gRPC Response Body: {response.text[:200]}...")
                            # Try to extract message ID from the response for cleanup
                            self._extract_message_id_from_response(response.text)
                        
                        # CRITICAL: Call LoadRecentActivity immediately after message submission
                        # This is what the HAR file shows the browser does to refresh the message list
                        self._refresh_message_list_after_submission()
                        self.created_message_ids.append(dynamic_message) # Track created message
                    else:
                        response.failure(f"gRPC error: {grpc_message} (status: {grpc_status})")
                        print(f"❌ gRPC-level error: {grpc_message} (status: {grpc_status})")
                        print(f"🔍 Full headers: {dict(response.headers)}")
                        
                elif response.status_code == 401:
                    response.failure("Authentication failed for gRPC")
                    print(f"❌ Authentication failed for gRPC message submission")
                elif response.status_code == 403:
                    response.failure("Access denied for gRPC")
                    print(f"❌ Access denied for gRPC message submission")
                else:
                    response.failure(f"gRPC request failed: {response.status_code}")
                    print(f"⚠️ gRPC request failed: {response.status_code}")
                    
        except Exception as e:
            print(f"❌ Error submitting gRPC message: {e}")
    
    def _refresh_message_list_after_submission(self):
        """
        Call LoadRecentActivity after message submission to refresh the UI.
        This mimics what the browser does in the HAR file after successful message submission.
        """
        try:
            print(f"🔄 Refreshing message list after submission...")
            
            # Use the same payload as in the HAR file for LoadRecentActivity
            grpc_payload = "AAAAAAIYHg=="  # From HAR analysis
            
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text',
                'x-grpc-web': '1'
            }
            
            # Use stored authentication token
            if self.session_data and isinstance(self.session_data, dict) and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
            else:
                print(f"❌ No valid token for refresh")
                return
            
            # Make request to k2-web subdomain
            grpc_host = self.host.replace('app.', 'k2-web.')
            
            response = self.client.post(
                f'{grpc_host}/com.guidecx.ks.ChannelService/LoadRecentActivity',
                data=grpc_payload,
                headers=headers,
                name='refresh_after_message'
            )
            
            if response.status_code == 200:
                print(f"✅ Message list refreshed successfully")
            else:
                print(f"❌ Failed to refresh message list. Status: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error refreshing message list: {e}")
    
    @task(2)  # Lower frequency - weight 2
    def load_recent_activity(self):
        """Test loading recent messaging activity (discovered in HAR)"""
        try:
            # Simple gRPC payload for loading recent activity
            grpc_payload = "AAAAAAIYHg=="  # From HAR analysis
            
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text',
                'x-grpc-web': '1'
            }
            
            # Use stored authentication token
            if self.session_data and isinstance(self.session_data, dict) and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
            else:
                print(f"❌ No valid token for load recent activity")
                return
            
            # Make request to k2-web subdomain
            grpc_host = self.host.replace('app.', 'k2-web.')
            
            response = self.client.post(
                f'{grpc_host}/com.guidecx.ks.ChannelService/LoadRecentActivity',
                data=grpc_payload,
                headers=headers,
                name='load_recent_activity_grpc'
            )
            
            if response.status_code == 200:
                print(f"✅ Successfully loaded recent activity")
            else:
                print(f"❌ Failed to load recent activity. Status: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error loading recent activity: {e}")
    
    @task(1)  # Least frequent - weight 1
    def load_mentions(self):
        """Test loading mentions (discovered in HAR)"""
        try:
            # gRPC payload for loading mentions
            grpc_payload = "AAAAAAQYFCAB"  # From HAR analysis
            
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text', 
                'x-grpc-web': '1'
            }
            
            # Use stored authentication token
            if self.session_data and isinstance(self.session_data, dict) and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
            else:
                print(f"❌ No valid token for load mentions")
                return
            
            # Make request to k2-web subdomain
            grpc_host = self.host.replace('app.', 'k2-web.')
            
            response = self.client.post(
                f'{grpc_host}/com.guidecx.ks.ChannelService/LoadMentions',
                data=grpc_payload,
                headers=headers,
                name='load_mentions_grpc'
            )
            
            if response.status_code == 200:
                print(f"✅ Successfully loaded mentions")
            else:
                print(f"❌ Failed to load mentions. Status: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Error loading mentions: {e}")
    
    def _create_grpc_message_payload(self, channel_id, message_text):
        """
        Create a properly formatted gRPC-Web payload for message submission.
        Uses the exact HAR structure but dynamically replaces channel ID and message text.
        
        This approach ensures wire format compatibility while allowing dynamic content.
        """
        try:
            print(f"🔧 Creating payload for channel: {channel_id}, message: '{message_text}'")
            
            # Use the exact working HAR payload as template and modify it
            # Original HAR payload (base64): AAAAAJoSJgokZGQ2ZGRkN2UtOGMyNS00YjVjLWE1OWItYzgzODkzMDcyNTJhGg88cD5sb2FkdGVzdDwvcD4iXXsidHlwZSI6ImRvYyIsImNvbnRlbnQiOlt7InR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJsb2FkdGVzdCJ9XX1dfTAA
            
            # Decode the original to understand the exact structure
            original_payload_b64 = "AAAAAJoSJgokZGQ2ZGRkN2UtOGMyNS00YjVjLWE1OWItYzgzODkzMDcyNTJhGg88cD5sb2FkdGVzdDwvcD4iXXsidHlwZSI6ImRvYyIsImNvbnRlbnQiOlt7InR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJsb2FkdGVzdCJ9XX1dfTAA"
            original_bytes = base64.b64decode(original_payload_b64)
            
            # Parse the structure:
            # Bytes 0-4: gRPC frame header (00 00 00 00 9A) 
            # Byte 5+: Protobuf message content
            
            frame_header = original_bytes[:5]  # Keep exact frame header
            original_message = original_bytes[5:]  # Extract message part
            
            # Now we need to replace the channel ID and message content
            # Original channel: dd6ddd7e-8c25-4b5c-a59b-c8389307252a
            # Original message: loadtest
            
            # Create new content with same structure but different values
            new_message_content = {
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text", 
                                "text": message_text
                            }
                        ]
                    }
                ]
            }
            
            new_html = f"<p>{message_text}</p>"
            new_json = json.dumps(new_message_content)
            
            # Rebuild the protobuf message with exact field structure from HAR
            # Field 1 (0x12): Channel ID - field 2, wire type 2, length-delimited with nested structure
            channel_bytes = channel_id.encode('utf-8')
            # The channel ID has a nested field structure: tag 0x24 (field 4, wire type 4) + length + data
            nested_channel = bytes([0x0a, len(channel_bytes)]) + channel_bytes  # 0x0a = field 1, wire type 2
            field1 = bytes([0x12, len(nested_channel)]) + nested_channel
            
            # Field 2 (0x1a): HTML content - field 3, wire type 2, length-delimited
            html_bytes = new_html.encode('utf-8')
            field2 = bytes([0x1a, len(html_bytes)]) + html_bytes
            
            # Field 3 (0x22): JSON content - field 4, wire type 2, length-delimited  
            json_bytes = new_json.encode('utf-8')
            field3 = bytes([0x22, len(json_bytes)]) + json_bytes
            
            # Field 4 (0x30): Unknown field - field 6, wire type 0, value 0
            field4 = bytes([0x30, 0x00])
            
            # Combine fields in exact order from HAR
            new_message = field1 + field2 + field3 + field4
            
            # Update frame header with new message length
            new_frame_header = bytes([0x00, 0x00, 0x00, 0x00, len(new_message)])
            
            # Combine frame and message
            final_payload = new_frame_header + new_message
            
            # Encode as base64
            encoded_payload = base64.b64encode(final_payload).decode('ascii')
            
            print(f"🔧 Generated HAR-compatible payload: {encoded_payload[:100]}...")
            return encoded_payload
            
        except Exception as e:
            print(f"❌ Error creating HAR-compatible payload: {e}")
            # If our smart approach fails, fall back to original hardcoded payload
            print(f"🔄 Falling back to original HAR payload")
            return "AAAAAJoSJgokZGQ2ZGRkN2UtOGMyNS00YjVjLWE1OWItYzgzODkzMDcyNTJhGg88cD5sb2FkdGVzdDwvcD4iXXsidHlwZSI6ImRvYyIsImNvbnRlbnQiOlt7InR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJsb2FkdGVzdCJ9XX1dfTAA"
    
    def _extract_message_id_from_response(self, response_text):
        """Extract message ID from gRPC response for cleanup tracking"""
        try:
            # gRPC-Web responses are base64 encoded
            decoded = base64.b64decode(response_text)
            # Look for UUID patterns in the response
            import re
            uuid_pattern = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
            
            # Convert to string and search for UUIDs
            readable = ''
            for byte in decoded:
                if 32 <= byte <= 126:  # Printable ASCII
                    readable += chr(byte)
                else:
                    readable += ' '
            
            found_uuids = re.findall(uuid_pattern, readable)
            if found_uuids:
                # The first UUID is likely the message ID
                message_id = found_uuids[0]
                if message_id not in self.messages_to_cleanup:
                    self.messages_to_cleanup.append(message_id)
                    print(f"🗂️ Tracked message ID for cleanup: {message_id}")
                    
        except Exception as e:
            print(f"⚠️ Could not extract message ID from response: {e}")
    
    def _create_delete_message_payload(self, message_id):
        """
        Create gRPC payload for deleting a message.
        Based on the HAR file: AAAAACgKJgokZTI2ZTAyYzUtYTJmZC00MDMxLTlmMWQtNzRmZmQ1MGViNDBi
        
        Decoded HAR structure analysis:
        00 00 00 28 - gRPC frame header (4 bytes) + message length (40 bytes)
        0a 26 - field 1, wire type 2, length 38
        0a 24 - field 1, wire type 2, length 36  
        [36 bytes: "e26e02c5-a2fd-4031-9f1d-74ffd50eb40b"] - message ID with dashes as UTF-8
        """
        try:
            # The message ID is stored as UTF-8 string WITH dashes (36 characters)
            message_id_bytes = message_id.encode('utf-8')
            
            # Build protobuf structure exactly like HAR:
            # Inner field: field 1, wire type 2, length 36, message_id_string
            inner_field = bytes([0x0a, len(message_id_bytes)]) + message_id_bytes
            
            # Outer field: field 1, wire type 2, length 38, inner_field
            outer_field = bytes([0x0a, len(inner_field)]) + inner_field
            
            # gRPC-Web frame: 5-byte header like HAR (00 00 00 00 28)
            frame_header = bytes([0x00, 0x00, 0x00, 0x00])  # 4-byte header
            frame_length = bytes([len(outer_field)])         # 1-byte length (40 = 0x28)
            
            # Combine all parts
            payload = frame_header + frame_length + outer_field
            
            # Encode as base64 for gRPC-Web-text
            encoded_payload = base64.b64encode(payload).decode('ascii')
            
            print(f"🔧 Created delete payload for {message_id}: {encoded_payload}")
            return encoded_payload
            
        except Exception as e:
            print(f"❌ Error creating delete payload for {message_id}: {e}")
            return None
    
    def _create_delete_payload_template(self, message_id):
        """Fallback method using template-based payload creation"""
        try:
            # Use the structure from HAR but substitute the message ID
            # Original: e26e02c5-a2fd-4031-9f1d-74ffd50eb40b
            # Convert new message ID to the same format
            message_id_clean = message_id.replace('-', '')
            
            # Build similar structure to HAR payload
            payload_template = f"AAAAACgKJgok{message_id_clean}"
            
            # Convert to proper base64 format
            return base64.b64encode(payload_template.encode()).decode('ascii')
            
        except Exception as e:
            print(f"❌ Error creating template delete payload: {e}")
            return None
    
    def delete_message(self, message_id):
        """
        Delete a specific message using the gRPC DeleteMessage API.
        Based on HAR file analysis: /manager.message.messages.MessageService/DeleteMessage
        """
        try:
            print(f"🗑️ Attempting to delete message: {message_id}")
            
            # Create delete payload
            delete_payload = self._create_delete_message_payload(message_id)
            if not delete_payload:
                print(f"❌ Could not create delete payload for {message_id}")
                return False
            
            # Headers from HAR analysis
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text',
                'x-grpc-web': '1'
            }
            
            # Use stored authentication token
            if self.session_data and isinstance(self.session_data, dict) and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
            else:
                print(f"❌ No valid token for message deletion")
                return False
            
            # Make request to k2-web subdomain (from HAR)
            grpc_host = self.host.replace('app.', 'k2-web.')
            delete_url = f"{grpc_host}/manager.message.messages.MessageService/DeleteMessage"
            
            response = self.client.post(
                delete_url,
                data=delete_payload,
                headers=headers,
                name='delete_message'
            )
            
            if response.status_code == 200:
                # Check for gRPC-level errors
                grpc_status = response.headers.get('grpc-status', '0')
                if grpc_status == '0':
                    print(f"✅ Successfully deleted message: {message_id}")
                    return True
                else:
                    grpc_message = response.headers.get('grpc-message', 'Unknown error')
                    print(f"❌ gRPC error deleting message: {grpc_message}")
                    return False
            else:
                print(f"❌ Failed to delete message. Status: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error deleting message {message_id}: {e}")
            return False
    
    def cleanup_created_messages(self):
        """Clean up all messages created during this test session"""
        if not self.messages_to_cleanup:
            print(f"🧹 No messages to clean up")
            return
        
        print(f"🧹 Cleaning up {len(self.messages_to_cleanup)} created messages...")
        
        success_count = 0
        for message_id in self.messages_to_cleanup:
            if self.delete_message(message_id):
                success_count += 1
                time.sleep(0.5)  # Small delay between deletions
        
        print(f"🧹 Cleanup completed: {success_count}/{len(self.messages_to_cleanup)} messages deleted")
        self.messages_to_cleanup.clear()
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"🚀 Starting messaging load test")
        print(f"📧 Testing message: '{self.TEST_MESSAGE_TEXT}' (with dynamic timestamps)")
        print(f"🔗 Channel ID: {self.CHANNEL_ID}")
        print(f"📱 Message ID: {self.MESSAGE_ID}")
        
        # Show configuration source
        env_channel = os.getenv('CHANNEL_ID')
        env_message = os.getenv('MESSAGE_ID') 
        if env_channel:
            print(f"📋 Using CHANNEL_ID from environment: {env_channel}")
        else:
            print(f"📋 Using default CHANNEL_ID from HAR analysis")
        if env_message:
            print(f"📋 Using MESSAGE_ID from environment: {env_message}")
        else:
            print(f"📋 Using default MESSAGE_ID from HAR analysis")
    
    def on_stop(self):
        """Called when user stops"""
        print(f"🛑 Messaging load test completed for user: {self.login_email}")
        # Clean up created messages to avoid filling up the messaging system
        self.cleanup_created_messages()

# Additional test class for different messaging scenarios
class MessageStressTest(AuthenticatedUser):
    """
    Stress test for messaging with rapid message submission.
    Uses environment variables for CHANNEL_ID and MESSAGE_ID.
    """
    
    wait_time = between(1, 2)  # Faster pace for stress testing
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Track created message IDs for cleanup
        self.created_message_ids = []
        self.messages_to_cleanup = []
        # Use same environment variables as main test
        self.CHANNEL_ID = os.getenv('CHANNEL_ID', "dd6ddd7e-8c25-4b5c-a59b-c8389307252a")
        self.MESSAGE_ID = os.getenv('MESSAGE_ID', "dd6ddd7e-8c25-4b5c-a59b-c8389307252a")
    
    @task
    def rapid_message_submission(self):
        """Submit messages rapidly for stress testing"""
        try:
            # Generate unique test messages
            timestamp = int(time.time())
            random_id = uuid.uuid4().hex[:8]
            test_message = f"stress-test-{timestamp}-{random_id}"
            
            # Create dynamic gRPC payload using the same system as the main test
            grpc_payload = self._create_dynamic_payload(self.CHANNEL_ID, test_message)
            
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text',
                'x-grpc-web': '1'
            }
            
            if self.session_data and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
            
            grpc_host = self.host.replace('app.', 'k2-web.')
            grpc_url = f"{grpc_host}/manager.message.messages.MessageService/SaveMessage"
            
            response = self.client.post(
                grpc_url,
                data=grpc_payload,
                headers=headers,
                name="stress_message_submit"
            )
            
            if response.status_code == 200:
                print(f"✅ Stress test message sent: {test_message}")
                # Try to extract message ID from response for cleanup
                if response.text:
                    self._extract_message_id_from_response(response.text)
            else:
                print(f"⚠️ Stress test failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Stress test error: {e}")
    
    def _create_dynamic_payload(self, channel_id, message_text):
        """
        Create dynamic gRPC payload for stress testing using HAR-compatible structure.
        Uses the same approach as the main test to ensure wire format compatibility.
        """
        try:
            print(f"🔧 Creating stress test payload for channel: {channel_id}, message: '{message_text}'")
            
            # Use the same HAR-compatible approach as the main test
            # Create new content with same structure but different values
            new_message_content = {
                "type": "doc",
                "content": [
                    {
                        "type": "paragraph", 
                        "content": [
                            {
                                "type": "text",
                                "text": message_text
                            }
                        ]
                    }
                ]
            }
            
            new_html = f"<p>{message_text}</p>"
            new_json = json.dumps(new_message_content)
            
            # Rebuild the protobuf message with exact field structure from HAR
            # Field 1 (0x12): Channel ID - field 2, wire type 2, length-delimited with nested structure  
            channel_bytes = channel_id.encode('utf-8')
            # The channel ID has a nested field structure: 0x0a = field 1, wire type 2
            nested_channel = bytes([0x0a, len(channel_bytes)]) + channel_bytes
            field1 = bytes([0x12, len(nested_channel)]) + nested_channel
            
            # Field 2 (0x1a): HTML content - field 3, wire type 2, length-delimited
            html_bytes = new_html.encode('utf-8')
            field2 = bytes([0x1a, len(html_bytes)]) + html_bytes
            
            # Field 3 (0x22): JSON content - field 4, wire type 2, length-delimited  
            json_bytes = new_json.encode('utf-8')
            field3 = bytes([0x22, len(json_bytes)]) + json_bytes
            
            # Field 4 (0x30): Unknown field - field 6, wire type 0, value 0
            field4 = bytes([0x30, 0x00])
            
            # Combine fields in exact order from HAR
            new_message = field1 + field2 + field3 + field4
            
            # Update frame header with new message length
            new_frame_header = bytes([0x00, 0x00, 0x00, 0x00, len(new_message)])
            
            # Combine frame and message
            final_payload = new_frame_header + new_message
            
            # Encode as base64
            encoded_payload = base64.b64encode(final_payload).decode('ascii')
            
            return encoded_payload
            
        except Exception as e:
            print(f"❌ Error creating HAR-compatible stress test payload: {e}")
            # Return None to skip this message rather than fallback
            return None
    
    def _extract_message_id_from_response(self, response_text):
        """Extract message ID from gRPC response for cleanup tracking"""
        try:
            # gRPC-Web responses are base64 encoded
            decoded = base64.b64decode(response_text)
            # Look for UUID patterns in the response
            import re
            uuid_pattern = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
            
            # Convert to string and search for UUIDs
            readable = ''
            for byte in decoded:
                if 32 <= byte <= 126:  # Printable ASCII
                    readable += chr(byte)
                else:
                    readable += ' '
            
            found_uuids = re.findall(uuid_pattern, readable)
            if found_uuids:
                # The first UUID is likely the message ID
                message_id = found_uuids[0]
                if message_id not in self.messages_to_cleanup:
                    self.messages_to_cleanup.append(message_id)
                    print(f"🗂️ Tracked stress test message ID for cleanup: {message_id}")
                    
        except Exception as e:
            print(f"⚠️ Could not extract message ID from stress test response: {e}")
    
    def _create_delete_message_payload(self, message_id):
        """Create gRPC payload for deleting a message (corrected version for stress test)"""
        try:
            # Use the same corrected structure as the main test
            # The message ID is stored as UTF-8 string WITH dashes (36 characters)
            message_id_bytes = message_id.encode('utf-8')
            
            # Build protobuf structure exactly like HAR:
            # Inner field: field 1, wire type 2, length 36, message_id_string
            inner_field = bytes([0x0a, len(message_id_bytes)]) + message_id_bytes
            
            # Outer field: field 1, wire type 2, length 38, inner_field
            outer_field = bytes([0x0a, len(inner_field)]) + inner_field
            
            # gRPC-Web frame: 5-byte header like HAR (00 00 00 00 28)
            frame_header = bytes([0x00, 0x00, 0x00, 0x00])  # 4-byte header
            frame_length = bytes([len(outer_field)])         # 1-byte length (40 = 0x28)
            
            # Combine all parts
            payload = frame_header + frame_length + outer_field
            
            # Encode as base64 for gRPC-Web-text
            encoded_payload = base64.b64encode(payload).decode('ascii')
            
            print(f"🔧 Created stress test delete payload for {message_id}: {encoded_payload}")
            return encoded_payload
            
        except Exception as e:
            print(f"❌ Error creating stress test delete payload: {e}")
            return None

    def delete_message(self, message_id):
        """
        Delete a specific message using the gRPC DeleteMessage API.
        Based on HAR file analysis: /manager.message.messages.MessageService/DeleteMessage
        """
        try:
            print(f"🗑️ Attempting to delete stress test message: {message_id}")
            
            # Create delete payload
            delete_payload = self._create_delete_message_payload(message_id)
            if not delete_payload:
                print(f"❌ Could not create delete payload for {message_id}")
                return False
            
            # Headers from HAR analysis
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text',
                'x-grpc-web': '1'
            }
            
            # Use stored authentication token
            if self.session_data and isinstance(self.session_data, dict) and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
            else:
                print(f"❌ No valid token for message deletion")
                return False
            
            # Make request to k2-web subdomain (from HAR)
            grpc_host = self.host.replace('app.', 'k2-web.')
            delete_url = f"{grpc_host}/manager.message.messages.MessageService/DeleteMessage"
            
            response = self.client.post(
                delete_url,
                data=delete_payload,
                headers=headers,
                name='delete_stress_message'
            )
            
            if response.status_code == 200:
                # Check for gRPC-level errors
                grpc_status = response.headers.get('grpc-status', '0')
                if grpc_status == '0':
                    print(f"✅ Successfully deleted stress test message: {message_id}")
                    return True
                else:
                    grpc_message = response.headers.get('grpc-message', 'Unknown error')
                    print(f"❌ gRPC error deleting stress test message: {grpc_message}")
                    return False
            else:
                print(f"❌ Failed to delete stress test message. Status: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error deleting stress test message {message_id}: {e}")
            return False
    
    def cleanup_created_messages(self):
        """Clean up all messages created during this stress test session"""
        if not self.messages_to_cleanup:
            print(f"🧹 No stress test messages to clean up")
            return
        
        print(f"🧹 Cleaning up {len(self.messages_to_cleanup)} stress test messages...")
        
        success_count = 0
        for message_id in self.messages_to_cleanup:
            if self.delete_message(message_id):
                success_count += 1
                time.sleep(0.2)  # Shorter delay for stress test cleanup
        
        print(f"🧹 Stress test cleanup completed: {success_count}/{len(self.messages_to_cleanup)} messages deleted")
        self.messages_to_cleanup.clear()
    
    def on_stop(self):
        """Called when stress test user stops"""
        print(f"🛑 Stress test completed for user: {self.login_email}")
        # Clean up created messages to avoid filling up the messaging system
        self.cleanup_created_messages()

# Test runner for development
if __name__ == "__main__":
    # Test the messaging load test directly
    print("Testing Messaging Load Test...")
    
    try:
        from locust.env import Environment
        from locust.log import setup_logging
        
        setup_logging("INFO", None)
        
        # Test MessagingLoadTest
        env = Environment(user_classes=[MessagingLoadTest])
        user = MessagingLoadTest(env)
        
        if user.is_authenticated:
            print("🎉 Authentication successful - ready for messaging tests")
            
            # Test the main messaging page
            try:
                user.view_messaging_page()
                print("🎉 Messaging page test: PASSED")
            except Exception as e:
                print(f"❌ Messaging page test: {e}")
                
            # Test gRPC message submission with dynamic content
            try:
                user.submit_message_grpc()
                print("🎉 gRPC message submission test: PASSED")
                print("🔍 Check your messaging app - you should see a new message!")
            except Exception as e:
                print(f"❌ gRPC message submission test: {e}")
        else:
            print("❌ Authentication failed - check your .env file")
            
    except ImportError:
        print("Install locust to run the test: pip install locust")
    except Exception as e:
        print(f"Test failed: {e}")
        print("Make sure you have a .env file with LOGIN_EMAIL, LOGIN_PASSWORD, and LOCUST_HOST")
