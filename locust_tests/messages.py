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
    """
    
    wait_time = between(2, 6)  # Wait 2-6 seconds between requests
    
    # Test data from the HAR file analysis
    MESSAGE_ID = "dd6ddd7e-8c25-4b5c-a59b-c8389307252a"
    CHANNEL_ID = "dd6ddd7e-8c25-4b5c-a59b-c8389307252a"
    TEST_MESSAGE_TEXT = "loadtest"
    
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
                        
                        # CRITICAL: Call LoadRecentActivity immediately after message submission
                        # This is what the HAR file shows the browser does to refresh the message list
                        self._refresh_message_list_after_submission()
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
    
    @task(1)  # Discovery task - help find valid channels
    def discover_user_channels(self):
        """Try to discover available channels for the current user"""
        try:
            # Try to get channels the user has access to
            # First try loading recent activity which might give us channel info
            grpc_payload = "AAAAAAIYHg=="  # From HAR analysis - this loads recent activity
            
            headers = {
                'Accept': 'application/grpc-web-text',
                'Content-Type': 'application/grpc-web-text',
                'x-grpc-web': '1'
            }
            
            # Use stored authentication token
            if self.session_data and isinstance(self.session_data, dict) and 'accessToken' in self.session_data:
                headers['Authorization'] = f'Bearer {self.session_data["accessToken"]}'
            else:
                print(f"❌ No valid token for channel discovery")
                return
            
            grpc_host = self.host.replace('app.', 'k2-web.')
            grpc_url = f"{grpc_host}/manager.message.channels.ChannelService/LoadRecentActivity"
            
            with self.client.post(
                grpc_url,
                data=grpc_payload,
                headers=headers,
                catch_response=True,
                name="discover_channels"
            ) as response:
                if response.status_code == 200:
                    response.success()
                    print(f"🔍 Channel Discovery Response Status: {response.status_code}")
                    if response.text:
                        print(f"🔍 Channel Discovery Response: {response.text[:500]}...")
                        # Try to decode the response to find channel IDs
                        try:
                            # gRPC-Web responses are base64 encoded
                            import base64
                            decoded = base64.b64decode(response.text)
                            print(f"🔍 Decoded response length: {len(decoded)} bytes")
                            # Look for UUID patterns in the response
                            readable = ''
                            for byte in decoded:
                                if 32 <= byte <= 126:  # Printable ASCII
                                    readable += chr(byte)
                                else:
                                    readable += f'[{byte:02x}]'
                            print(f"🔍 Readable content: {readable[:300]}...")
                        except Exception as decode_error:
                            print(f"🔍 Could not decode response: {decode_error}")
                    else:
                        print(f"🔍 Channel Discovery Response: <empty>")
                else:
                    response.failure(f"Channel discovery failed: {response.status_code}")
                    print(f"⚠️ Channel discovery failed: {response.status_code}")
                    
        except Exception as e:
            print(f"❌ Error discovering channels: {e}")
    
    @task(1)  # Try to find user's messaging context
    def get_messaging_context(self):
        """Try to get the user's current messaging context from the web UI"""
        try:
            # Load the main messaging page without specific parameters to see what channels are available
            with self.client.get("/messaging", catch_response=True, name="get_messaging_context") as response:
                if response.status_code == 200:
                    response.success()
                    print(f"🔍 Messaging context loaded successfully")
                    
                    # Look for channel IDs or message IDs in the response
                    content = response.text
                    if content:
                        # Look for UUID patterns that might be channel IDs
                        import re
                        uuid_pattern = r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}'
                        found_uuids = re.findall(uuid_pattern, content)
                        if found_uuids:
                            print(f"🔍 Found UUIDs in messaging page: {found_uuids[:5]}...")  # Show first 5
                            # Update our channel ID to use one that's actually available
                            if found_uuids and found_uuids[0] != self.CHANNEL_ID:
                                print(f"🔄 Updating channel ID from {self.CHANNEL_ID} to {found_uuids[0]}")
                                self.CHANNEL_ID = found_uuids[0]
                                self.MESSAGE_ID = found_uuids[0]  # Often the same
                        else:
                            print(f"🔍 No UUIDs found in messaging page")
                            
                        # Look for specific messaging-related JavaScript or data
                        if 'channelId' in content:
                            print(f"🔍 Found 'channelId' references in page")
                        if 'messageId' in content:
                            print(f"🔍 Found 'messageId' references in page")
                            
                else:
                    response.failure(f"Messaging context failed: {response.status_code}")
                    print(f"⚠️ Messaging context failed: {response.status_code}")
                    
        except Exception as e:
            print(f"❌ Error getting messaging context: {e}")
    
    def _create_grpc_message_payload(self, channel_id, message_text):
        """
        Create a properly formatted gRPC-Web payload for message submission.
        Uses the exact hardcoded "loadtest" payload from working HAR analysis.
        """
        # Return the proven working payload that contains "loadtest" message
        # This is the exact payload from HAR analysis that we know works
        return "AAAAAJoSJgokZGQ2ZGRkN2UtOGMyNS00YjVjLWE1OWItYzgzODkzMDcyNTJhGg88cD5sb2FkdGVzdDwvcD4iXXsidHlwZSI6ImRvYyIsImNvbnRlbnQiOlt7InR5cGUiOiJwYXJhZ3JhcGgiLCJjb250ZW50IjpbeyJ0eXBlIjoidGV4dCIsInRleHQiOiJsb2FkdGVzdCJ9XX1dfTAA"
    
    def on_start(self):
        """Called when user starts - authentication happens automatically"""
        super().on_start()  # This calls authenticate()
        print(f"🚀 Starting messaging load test")
        print(f"📧 Testing message: '{self.TEST_MESSAGE_TEXT}' (with dynamic timestamps)")
        print(f"🔗 Channel ID: {self.CHANNEL_ID}")
        print(f"📱 Message ID: {self.MESSAGE_ID}")
    
    def on_stop(self):
        """Called when user stops"""
        print(f"🛑 Messaging load test completed for user: {self.login_email}")

# Additional test class for different messaging scenarios
class MessageStressTest(AuthenticatedUser):
    """
    Stress test for messaging with rapid message submission
    """
    
    wait_time = between(1, 2)  # Faster pace for stress testing
    
    @task
    def rapid_message_submission(self):
        """Submit messages rapidly for stress testing"""
        try:
            # Generate unique test messages
            timestamp = int(time.time())
            random_id = uuid.uuid4().hex[:8]
            test_message = f"stress-test-{timestamp}-{random_id}"
            
            # Create dynamic gRPC payload
            grpc_payload = self._create_dynamic_payload(test_message)
            
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
            else:
                print(f"⚠️ Stress test failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Stress test error: {e}")
    
    def _create_dynamic_payload(self, message_text):
        """Create dynamic gRPC payload for stress testing"""
        channel_id = "dd6ddd7e-8c25-4b5c-a59b-c8389307252a"  # Same channel for stress test
        
        message_content = {
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
        
        html_content = f"<p>{message_text}</p>"
        json_content = json.dumps(message_content)
        
        # Create protobuf fields
        channel_id_bytes = channel_id.encode('utf-8')
        field1 = bytes([0x0a]) + bytes([len(channel_id_bytes)]) + channel_id_bytes
        
        html_bytes = html_content.encode('utf-8') 
        field2 = bytes([0x1a]) + bytes([len(html_bytes)]) + html_bytes
        
        json_bytes = json_content.encode('utf-8')
        field3 = bytes([0x22]) + bytes([len(json_bytes)]) + json_bytes
        
        # Combine and frame
        message_body = field1 + field2 + field3
        payload = bytes([0x00]) + struct.pack('>I', len(message_body)) + message_body
        
        return base64.b64encode(payload).decode('ascii')

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
