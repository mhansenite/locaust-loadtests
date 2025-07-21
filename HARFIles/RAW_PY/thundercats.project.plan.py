from locust import task, run_single_user
from locust import FastHttpUser


class thundercats_project_plan(FastHttpUser):
    host = "https://k2-web.staging.guidecx.io"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    }

    @task
    def t(self):
        with self.client.request(
            "POST",
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "132",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c275ad5-c255-4d97-98e2-f1ad06a3cd03/plan?phase=&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "60",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "112",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "60",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c275ad5-c255-4d97-98e2-f1ad06a3cd03/plan?phase=&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Priority": "u=0, i",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Sec-GPC": "1",
                "TE": "trailers",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/1deb064b09960669.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/4618509861d898fa.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/1719019430b7439d.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/66cebb5664caca87.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/a7b00d07ec9604e3.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/2a5a2335ac212898.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/4f018e262d0d51a8.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/5704f770b6fbeef3.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/21ef8ef640edc928.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/ff3d59903da5c547.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/4e6947756d0fd8cb.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/ba2312bac09b74d9.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/c26966f88d6bf431.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/c0938f9aa519bfd7.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/8538ca369e8c5cd8.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/398a35ad78e114f2.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/2757b5a4d3c06116.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/0fc54bae693dbf39.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/bfab40f7f683d7af.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/8e4eb7f90df20e40.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/eef5237e71e64b63.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/7207e57b3cd5d4db.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/cd12ec5806346ab1.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/b7bbc95a1e47bf03.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/2bf55e5451438699.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/5820cabd6d7b5b71.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/ce287cfa81ac4bc5.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/7663a168be438e27.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/cdd3b779c5250dc2.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/2b0fc8d913d355a8.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/dc45ff914c2a5e0a.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/f81d5a6a5d0ac049.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://cdn.guidecx.com/static/fonts/graphik/fonts.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "cdn.guidecx.com"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/webpack-13f26fb5782377f4.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/618f8807-111b1fb9b7fc3166.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/68832168-744a1c23b1f3f2f2.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/832-7c64f3766e770f2f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/main-app-8cd37b7f020fb318.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/9115-e2eb5ed181a55645.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8214-4f9b59663df268f0.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/522-820a2e644fbfb54e.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/v2/projects/(list)/loading-9f36450eedeb3c28.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/de2117cc-47c4f2c0107c3d14.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8008-fab0ed8140c56970.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4594-a61f44a864072dc7.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4953-e8dc574999376bd3.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4165-2109df75cf3ffbe3.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/layout-cb630112d8e41bf2.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/5294-4cac37303f812ebb.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/9948-25ac39e1a977d8ab.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/7498-7e4a30ffdefb8f8f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/6810-404aeda8e6c35bc0.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8301-f25100e8103624d9.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/7620-35b457970a1cd144.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/7362-79ddbdea3840b8a9.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/5459-bb2efb55beac7b32.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/6-9cb605f005d1fe12.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/1638-467dda8999311e31.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4989-c27b751eea8588b6.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4550-5cd91812d51532da.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/1081-b0fd64baf2ac6503.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/1386-a5d2ea9ea7633a29.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2470-b7f3e28654f257f3.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/9321-a633b7f4e984ec2a.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4575-a7857b313102fbaf.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/v2/projects/(list)/page-a979e5ecd054659f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/error-df9ba9cbcd9f33bf.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/global-error-7740bec360706bca.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://assets.adobedtm.com/03dee6567a5e/6130f48717bd/launch-062bf29b71ae-staging.min.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Host": "assets.adobedtm.com",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/1285-59535ca4c4f2895f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8295-59b6bef2cc558f4a.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8284-7c69186a07e17bd2.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/9492-6be425ff29fe1a2f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2887-276630815c094661.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/9895-6417a173d7779ca7.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4684-de38868294d588a8.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/6324-2b4731b4d69c0353.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/720-dc44b92d62549cdc.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/@navigation/default-2aff4c85ccb4a2d8.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/9522-be5a6ad0d079f6fd.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/9451-e8034833a462de5d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/layout-141513450bcacb08.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2233-9418376233612bc4.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/error-7af2d82a9ec12835.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "wss://api.staging.guidecx.io/subscriptions",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive, Upgrade",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; user.id=1102c3bc-4d5c-4883-83de-10294e31bec3; gcx.session=AzbEyof6RSZM7T1X8qYfHa3xH4kB%2FjRu8%2Fu%2BXc6iEXB8mHRUdf%2FxLryrs77Le2JfiJn0zUHZNbgtZSsOTdgiCycWzGkA6R351Jk267ulOQuTrU296BBN%2FEmVnsK66pC7Q3BSATiN30sr6PLiTsw%2F5%2FjTUU3C7U%2Bg18GE05BhGbl87vEZWPIY%2BghtZfMY0mvy8Deq--HXFIHRAkq72tDBCg--8CjowBwlCQ022RiTGV4n3g%3D%3D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "api.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Pragma": "no-cache",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "websocket",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "Sec-WebSocket-Extensions": "permessage-deflate",
                "Sec-WebSocket-Key": "KVXLm7r4nGnA1E77KQwAog==",
                "Sec-WebSocket-Protocol": "actioncable-v1-json, actioncable-unsupported",
                "Sec-WebSocket-Version": "13",
                "Upgrade": "websocket",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://assets.adobedtm.com/extensions/EPbf7b42aa08bc4f10879b1484195e80d1/AppMeasurement.min.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Host": "assets.adobedtm.com",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://assets.adobedtm.com/extensions/EPbf7b42aa08bc4f10879b1484195e80d1/AppMeasurement_Module_ActivityMap.min.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Host": "assets.adobedtm.com",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/mySegments/18548de9-f5e4-4441-9c19-f1004cd4dea1",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Host": "sdk.split.io",
                "If-None-Match": '"1428624753"',
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "SplitSDKVersion": "react-1.11.1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/splitChanges?since=-1",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Host": "sdk.split.io",
                "If-Modified-Since": "Tue, 08 Jul 2025 18:36:29 GMT",
                "If-None-Match": '"1751999789511"',
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "SplitSDKVersion": "react-1.11.1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "POST",
            "https://api.staging.guidecx.io/graphql?CountNotifications",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Content-Length": "233",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; user.id=1102c3bc-4d5c-4883-83de-10294e31bec3; gcx.session=AzbEyof6RSZM7T1X8qYfHa3xH4kB%2FjRu8%2Fu%2BXc6iEXB8mHRUdf%2FxLryrs77Le2JfiJn0zUHZNbgtZSsOTdgiCycWzGkA6R351Jk267ulOQuTrU296BBN%2FEmVnsK66pC7Q3BSATiN30sr6PLiTsw%2F5%2FjTUU3C7U%2Bg18GE05BhGbl87vEZWPIY%2BghtZfMY0mvy8Deq--HXFIHRAkq72tDBCg--8CjowBwlCQ022RiTGV4n3g%3D%3D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "api.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "x-graphql-version": "1.0",
            },
            json={
                "operationName": "CountNotifications",
                "variables": {},
                "query": "query CountNotifications {\n  notifications: unreadNotificationsCount(types: [SCHEDULE, NOTIFICATION])\n  mentions: unreadNotificationsCount(types: [COMMUNICATION])\n}\n",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/app/support?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/app/notifications?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/messaging?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/tasks?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/app/reports?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://auth.split.io/api/v2/auth?users=18548de9-f5e4-4441-9c19-f1004cd4dea1",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
                "Connection": "keep-alive",
                "Host": "auth.split.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "SplitSDKVersion": "react-1.11.1",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/templates?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/time-tracking?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.authn.workspaces.WorkspaceService/LoadMyWorkspaces",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/resource-management/project-roles?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/tasks/error-18e6f4a3e0a8fe94.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/customers?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/templates/projects",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.message.channels.ChannelService/LoadTotalUnreadMentionCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/messaging/error-23e720ff5d2946f0.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "12",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "7dde6021d1d552016a324b86aabc828d90123a87",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data='[{"type":2}]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://guidecx.sc.omtrdc.net/b/ss/guidecxstaging/1/JS-2.23.0-LDQM/s6993965865396?AQB=1&ndh=1&pf=1&t=21%2F6%2F2025%2014%3A58%3A4%201%20360&fid=0EE7024574418985-3EF65E226A056508&ce=UTF-8&g=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fv2%2Fprojects&cc=USD&events=event1&c.&a.&activitymap.&page=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fv2%2Fprojects&link=Projects&region=BODY&.activitymap&.a&.c&pid=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fv2%2Fprojects&oid=Projects&oidt=3&ot=SUBMIT&s=3840x2160&c=24&j=1.6&v=N&k=Y&bw=3824&bh=1584&AQE=1",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Host": "guidecx.sc.omtrdc.net",
                "Referer": "https://thundercats.staging.guidecx.io/",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://widget.intercom.io/widget/vtlfk4ov",
            headers={
                "Accept": "*/*",
                "Alt-Used": "widget.intercom.io",
                "Connection": "keep-alive",
                "Host": "widget.intercom.io",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://js.intercomcdn.com/frame.7ddf246e.js",
            headers={
                "Accept": "*/*",
                "Alt-Used": "js.intercomcdn.com",
                "Connection": "keep-alive",
                "Host": "js.intercomcdn.com",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://js.intercomcdn.com/vendor.99d59aeb.js",
            headers={
                "Accept": "*/*",
                "Alt-Used": "js.intercomcdn.com",
                "Connection": "keep-alive",
                "Host": "js.intercomcdn.com",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.project.project_list.ProjectListService/LoadTagsDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.project.project_list.ProjectListService/LoadActiveMilestonesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.project.project_list.ProjectListService/LoadProjectManagersDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "4",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="[{}]",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.project.project_list.ProjectListService/LoadProjectStatusesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "8",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "4",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="[{}]",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/zz9r8h6v3b6e0bem2j05j2ag3g7v",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Priority": "u=4, i",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/rxn9aje8cpxprjash1c45lt5d1sc",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Priority": "u=4, i",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/rsgipbrzbdigpruppkojkhms2jw4",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Priority": "u=4, i",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/projects?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects/timeline?_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "4",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "d460095e80259ffd0e3377f81ff6d3eb70666bda",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="[{}]",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=1&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=2&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=3&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=4&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=0&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=9&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=5&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=6&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/v2/projects?sortBy=7&sortOrder=asc&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/0a770dc5-1cef-4538-9773-935db0345c31/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/0a770dc5-1cef-4538-9773-935db0345c31/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/5a253507-1bec-4a02-ac70-e8365e6a9d46/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/5a253507-1bec-4a02-ac70-e8365e6a9d46/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/192a7fe7-07ba-4a8b-9f91-596d31c463fd/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/192a7fe7-07ba-4a8b-9f91-596d31c463fd/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23c5a2-fd66-4897-984d-98f3d2051885/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23c5a2-fd66-4897-984d-98f3d2051885/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c234694-12ec-4969-b402-727587b7463e/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c234694-12ec-4969-b402-727587b7463e/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c2287c1-c46c-438a-b88d-ea65269d4259/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/plan/error-99a34b3deaab551c.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/a9ba94e6-5d62d8c1f7aeb0f0.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/538b4055-396755c9f2e73495.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/689cf043-4d94d4cc0678cf7a.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2f7efde8-45c097ab86aac5e8.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/b616be5b-2f3ad0c86d9f32d4.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/5f9909de-8735536ee9430f2a.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/d384f6f5-e2f87951f46ad0f3.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/cc40c94c-4f084320be55d1e6.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/f35cabfc-0e37b5810f8fc31a.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/c7a7ea33-e7483b1c8dad42bf.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8db15f2a-8419a0c1dce4e1c6.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/6553-7accc63c152641c9.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2934-03f422ef4a29410a.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/1329-18afa1c10f65cc88.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/5326-a1528b75d4b5d6ed.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8523-6832f33ca4e3b83e.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4020-4a0902f4c4b9890e.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/3534-b308e7e95be899e3.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4786-8a1bb2c6f0e6d819.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2903-b7b41ca1edd2b107.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/7237-cce47f544c237d7b.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/4267-1358a5cb8c732383.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8867-60c38ad0e5cb9bd5.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2439-98ee2ed93c31c818.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8725-364b5bfd26998347.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/102-6cbd18c7e8e34841.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/861-c167e6c479ccbf93.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/plan/page-8732ae7e30557386.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/2011-f329e5c561c03c48.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/3848-7c111015f2f2cc17.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/layout-1b49cc40311b6666.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c2287c1-c46c-438a-b88d-ea65269d4259/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c275ad5-c255-4d97-98e2-f1ad06a3cd03/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c275ad5-c255-4d97-98e2-f1ad06a3cd03/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23b957-8131-4fda-9c34-3a039cd506c6/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/7019-85b5bb6fbe5ab1c9.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/plan/layout-e85197d9c6708256.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/adobe-client-data-layer.min.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23b957-8131-4fda-9c34-3a039cd506c6/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c211d0e-bfc5-487d-9f6b-05eb91029024/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c211d0e-bfc5-487d-9f6b-05eb91029024/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c233659-f1cc-446d-aa7d-56b31f63eeba/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c233659-f1cc-446d-aa7d-56b31f63eeba/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23a119-fd22-423b-8623-02db0640a749/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23a119-fd22-423b-8623-02db0640a749/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23a3f9-0efd-496d-96ba-3d7e49a37670/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23a3f9-0efd-496d-96ba-3d7e49a37670/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c232123-d314-4d33-b100-a93112abf293/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c232123-d314-4d33-b100-a93112abf293/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23af54-a3e5-4c5a-ae56-2ec1cbbd2528/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c23af54-a3e5-4c5a-ae56-2ec1cbbd2528/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c233243-0326-4273-bc1e-51705bbe40bc/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c233243-0326-4273-bc1e-51705bbe40bc/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c230684-731e-41a6-9fe2-e30b9448dc16/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c230684-731e-41a6-9fe2-e30b9448dc16/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235b03-d4ea-4d0d-a499-a466b43a3c83/plan?_rsc=1tzeg",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235b03-d4ea-4d0d-a499-a466b43a3c83/messages?messageKey=projectId&_rsc=cyzz9",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=%5B%5BB%5D%5D; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/v2/projects",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/e4fa05bbeff903d1.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/03afdd70ad25fd34.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/ebb131334889d476.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/26a80b2a6cab2865.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/00316870ed1dc6df.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/0b5e490155c27bed.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/170b0a3761d10a26.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/35e465b88aa66ad1.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/d8c9b7d9b1997477.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/dae0e8c712ff2e96.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/5d15467cd21af210.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/c4aa9bf51ebcc1c5.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/7b8638c33b6e5544.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/css/8d51b2c58c0fe886.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/mySegments/BASIC",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Host": "sdk.split.io",
                "If-None-Match": '"1000002"',
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "SplitSDKVersion": "react-1.11.1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://api-iam.intercom.io/messenger/web/launcher_settings",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Content-Length": "932",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=79f82d4f-ec95-4d60-b3ed-8bf091550127&r=&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=fa4d508edee9c706&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan&anonymous_session=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0%3D--46bbe57f43c68e1b180b1e82c85afacb5c679437&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/splitChanges?since=-1",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
                "Connection": "keep-alive",
                "Content-Type": "application/json",
                "Host": "sdk.split.io",
                "If-Modified-Since": "Tue, 08 Jul 2025 18:36:29 GMT",
                "If-None-Match": '"1751999789511"',
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "SplitSDKVersion": "react-1.11.1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://api-iam.intercom.io/messenger/web/ping",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Content-Length": "1314",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=b412a858-c64c-4d70-ab82-b64a3534cbaf&r=&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=65d84089c8486182&internal=%7B%7D&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%2C%22name%22%3A%22Mike%20Hansen%22%2C%22company%22%3A%7B%22company_id%22%3A%2218548de9-f5e4-4441-9c19-f1004cd4dea1%22%2C%22name%22%3A%22ThunderCats%22%2C%22website%22%3A%22thundercats.guidecx.io%22%7D%2C%22role%22%3A%22ADMIN%22%2C%22org_type%22%3A%22PROVIDER%22%2C%22trial%22%3Afalse%7D&source=apiBoot&sampling=false&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%3Fphase%3D6ee23d15-5122-4788-beaa-7b3f3b3976ab%26view%3Dboard&anonymous_session=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0%3D--46bbe57f43c68e1b180b1e82c85afacb5c679437&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "84",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=SU9qWFlOVkN3dXlWK2l5dEQ0R21jeCtvMXlCMkp6S2VpWjUwVTJpN0dtejZqSVFaOVRlU1U4UWNLVHJWWWlONHYwdWFuS0plZG9LVkZUKzljeXcySDZSNlBpcXNQekRaRzlNT2tGQ3NCREk9LS1mdkpZellJS0NIR2dCOXh3dmpYYWR3PT0=--46bbe57f43c68e1b180b1e82c85afacb5c679437; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "9704e78ed7422ab571bfa4456b0aab6b24b8d6b6",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data='[{"unitId":{"uuid":"6ee23d15-5122-4788-beaa-7b3f3b3976ab"},"excludeInternal":false}]',
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://auth.split.io/api/v2/auth?users=BASIC",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
                "Connection": "keep-alive",
                "Host": "auth.split.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "SplitSDKVersion": "react-1.11.1",
            },
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "wss://nexus-websocket-a.intercom.io/pubsub/5-xD4udfgvhHUbKH4v9hNL16PheeeMncqhkHuLTb8apJrh3Eu2Zj6BzhqS1qMYQGpRvgrGLR004itSIW3gTiyx7zOE8tdPKbKcwLMK?X-Nexus-New-Client=true&X-Nexus-Version=0.14.0&user_role=user",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive, Upgrade",
                "Host": "nexus-websocket-a.intercom.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Pragma": "no-cache",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "websocket",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "Sec-WebSocket-Extensions": "permessage-deflate",
                "Sec-WebSocket-Key": "AROeOGHEBSKkPhOlbV+NIA==",
                "Sec-WebSocket-Version": "13",
                "Upgrade": "websocket",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://api-iam.intercom.io/messenger/web/page_view_events",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Content-Length": "1021",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=b412a858-c64c-4d70-ab82-b64a3534cbaf&r=&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=3388a1d4762b01f0&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=18548de9-f5e4-4441-9c19-f1004cd4dea1&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%3Fphase%3D6ee23d15-5122-4788-beaa-7b3f3b3976ab%26view%3Dboard&anonymous_session=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0%3D--131dd1e1ab73af54263fda1f1f091d6c3c8730a5&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://api.staging.guidecx.io/query?query=%7B%22dimensions%22%3A%5B%22workspace_unit_status.label%22%2C%22workspace_unit_status.status_category%22%5D%2C%22measures%22%3A%5B%22unit.count%22%5D%2C%22filters%22%3A%5B%7B%22member%22%3A%22unit.project_id%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%227c235972-a318-430e-b83e-e0c4af6e616b%22%5D%7D%2C%7B%22member%22%3A%22unit.type%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22ACTION%22%5D%7D%2C%7B%22member%22%3A%22unit_status.active%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22true%22%5D%7D%5D%7D",
            headers={
                "Accept": "*/*",
                "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; user.id=1102c3bc-4d5c-4883-83de-10294e31bec3; gcx.session=rTuM8KTb0FqNmsrsddKp2L1nn5CKrgF71VPDCaynLeoCCsr0XP1Qgocur5RDtkCGK68eDiedm7xW6ZB9PmHoC9dXoh5jwczJHjrRRVoco%2FQio0tMBD9zkTITE7iQTRfkiv4IFM4Q3%2BJzt%2F%2BSR9oCIP1CIZnJT%2BII74WtnO4sBLNAIY92iSKSnU7ZH0ybqjQGUMoi--cvqVbyHVH1qyYMrF--aYe1Av54BEIOTHonZP%2Fy1A%3D%3D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "api.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "112",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAE4KJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZiEiQ4YjQ1MjcxMy0yMWZiLTQ3OWYtOTM0My1hMjAxZjYwZjA2NGQ=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "60",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzEzMzIwMSwiaWF0IjoxNzUzMTMxNDAxLCJqdGkiOiI1YzYzYmI2OC0zNGY4LTQwY2QtOWNiYS05MDk0NTQ4ZGU3M2MiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.m1TfHy-7J9NjICClpqn4H9L7eHEj76FLAdC11QHvutIBiaHW4BtSU0uSxm1IWh6F8qD1rQjCx-4yFnChdevWiv4OXOZq2B5Bs7eoFOnwfKdcO1vVDuQE81G9ZsOaPaQnrmd1QRlf1uFWkiklGX3Pb_ke9AC0IE0QkyVPX5QvhvowDJKMwiWPwGCdxfCR4W7DLZf1Kyiw_OD5XShER_waQyRx1hntPw9r2jKzJlUT7JSBo3asEwLHALSPyv0b_K5G-FNFsbz9Eu_SaNX820_cP3hancwzOnNkZJ_FE9wmhNKEjY93jFmKs-7cg8Ae3psE1z-OiXpBLkE0VQNDE6Bshw",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAACgKJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZi",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/team?_rsc=1v6nc",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/overview?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/messages?messageKey=projectId&messageId=7c235972-a318-430e-b83e-e0c4af6e616b&_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/attachments?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/custom-fields?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "155",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "4f122631d19346579dd7c91cdfe7c24281bbc02a",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"startDate":{"seconds":"1668384000","nanos":0},"dueDate":{"seconds":"1674777600","nanos":0}}]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/custom-fields/error-a2277441fd4e4b6c.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/history?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/303-e6a413730e26b787.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/messages/page-e2f36bf620fa5a84.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/overview/error-c662038742273f3d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/team/error-1637546820862b92.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/7466-2a26921771cff368.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/overview/page-0838ed393d1a5a8a.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8963-55fceb97a97c5a0f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/custom-fields/page-4018370a35412fd8.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/history/error-1ad433aceda9bcfa.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "134",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "f0dcb167bb0486ad2aff91c85d8f91b40996dd37",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"phaseId":{"uuid":"6ee23d15-5122-4788-beaa-7b3f3b3976ab"},"filters":[]}]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/8140-92de6ffe2711173d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/attachments/page-81e602ba060ffa0b.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "134",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "f0dcb167bb0486ad2aff91c85d8f91b40996dd37",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%227c235972-a318-430e-b83e-e0c4af6e616b%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"phaseId":{"uuid":"6ee23d15-5122-4788-beaa-7b3f3b3976ab"},"filters":[]}]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://thundercats.staging.guidecx.io/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/history/page-c5e094c1b1fea978.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.staging-session.v2=Fe26.2*1*6058813aab6a62fa9bf05083f33e89f005a5e306ea7c5ec4ed7456ca77d6b4e2*fEYXxWcTAdu_ticbO_aVrw*Ig386MsECAMCCbcyr2bS2zt1gvDN1RzqTJuxvTLutPeq4_7p7wbFfiq-k-xysLMfRBmjEXjj-eefiLjaQ8n0Z1f5OSkNsUAZbI10PbuT_qWdfbjC_v5b1Z7OoS-CuLmp9Tz4Es198Jv5Vlt3MoE6cPldnHWSuOOuQvgBNNiuO3fCocNT4ZWLbzRZPkLsrkG5u_s3KxaeD4azOk_W-qnETnICPF3N_c0zgCwrWA3m0pTwvMhjDDDNsZfW42TmvuHuqv6KUpMrH06cxuaOZ2WegVJCgYeyIBsjUUs63a-Fh1admmlXDmUiv0B7v3Sc0WffSNDsIBtUkz9VQT1gelbF_wXWYPQL_h08NGMpI27cgV2ICo-p4MVYZDh8Vg-s4pi2RQyqlGJYgLJUDBb6LlvFYTa0Xrjisgcmr_v3mLlj1NG9W6ZmdG_00VPMBHjclqlX3sXSMUiL-NTu7f-E4q202P2wZJ5b8q50n79HcTJsO5QZ_dvXLR3-8HbyY4r0AqnTrjFgx_CBDzu8YL-t5N2V18K0OBtNjbipeGdkFY-m9JzE2NEfDd_y2oqjEnex4ARNuKRISgaxP_rzBAbFQajpfAx-ZxPzfsTHQLf4mPZrMeO2dp9emhO22DNcMzzDrUCmLiKFbB4OJIaPK3vzlzVquhCySTqk42EFd1HeTZK4qiN6SrJFuIAAo0MBaiF84gd7CPholt29TAAHim12vcLq00rUrRWbSNCp5Q7c9vIa43iYX1UGgctKG0f0hprrWWaQzW4-WzoR6wUOqFhD85LiyPH6OILrRLV_sgPG5wma4wWg59GwkMVN0kmOupLGkHHnD6E8tKgfWY323FOIM1-dd7Fi-qasHl8_wBi6JZc_84wVGXASo2b3Vr5bdHdxFPH3tPpG1EWsBb5EYi-YFtWtbdb8tIqqf8GTE5lF7WDRms5nckvRWsHp3D-Gp251vxi63b_nli1HQGXxvsLoaUnWKp2QdjieqzzT5jisFyJKRq7JwplKjK0W5mBeLjcaJmoujirTP7ZTk-MmxY74lVvifttuvGOQpzo5MIZy4QIqMgI9lVviLUIu4np7zlU9CQ7TbUmuaCRnJBzWmySmZFmuvsFkTeufKKY-RBIZ3PvK7CDIOx7HLy5s2dAnB_8_c-NPj-sdzV0ru1RmRod1PrlHm1zMJ2HjakHJFtrvq8Wj2QfiWIT448iKb_zbACN7Gu0UAY3Yungc2s_hcMq5--9LtwXeHvOTas1G6PssG4sLcRE85PHqJP8GJm240Y5e-wo4EoV_4C1iPGc1HHXiOLBM6eRL0YU79UvZoGAholmStDbf9gzd0s7yohdtr88EJw4lPvnyz18NbmSVayZQuNhNgxCW_Yv8QjwDSG3ZP_keDYNpM2UzjSs1rT-iJlI-wB-96y4Vl8N2KGUMLZlbwxMhCW88ECOMSz9oGRA5L9iGIqHvlg65vITCL27j_21DFVWLIbtOYw6ZXDQJP7MvYmY_STysQpDa4Mk1KHbmGFePf_h1TbApF60aakZXHdJxbvzfE2TNl06IxjjCJKz33YdOlw_869QRvuDtVaHjVRakESk*1754341001507*55d98f2f9b8d03c61492283de39b8c4911719d43b8b6e8b6c3b7077ffe0f9a42*E8-Igu3ve86Eb5EB1e2yR3UQSw7fj4L9DOWTu1nd_ko~2; _gcx.staging-session.v1=Fe26.2*1*e0b3ce2a7ca7b8d5fc7488543eb30845b90a517eb4e3ac474ee83e1c9dbb0878*KLnpOGafg-lnfnvMpuI_Hw*mcVXDiKgcxzGHKX4dpNgPQImKPq-HKB3ACbf8izNk13cnxKYmr1rQgY4sc7Q6nWoE8gWIm9ZiUvI5Y_XS6pbiDW6q9jbvmB0GfVv0H_XMboLqfuIX-0tdsKMBIzUEYpydIK-H9Th2FAuGBtpLENzD29tBKtbqYMBJ5ibbXp84mRXCEigpyZkgD37TlMwAMVf7ssiDPwcEsxAk4sTm4Ui_sGiTHeQ3Vh57gZlctKeZ7x6Dv6vN-O4mZc1YCb_1qh10-vVTfRSBHzk8hNIK3M7dERMV9N2j4wQeVwD_3m7Qu-uDQuEIpQ9d7J6WzcbP6LllGqDuszgTwmVP6j-oEcNWnuV71beTT-BRKIpmpudzufkQUQ6lsICthFuTPy7Mp2F9D_EMrbbmfDzrhwYbBKwIC6cSBpIdbhWHmzfdl1HnRCNLwOzMd7tAGyZjQ_qatowUq-Og1tvPu_ntJOesf-C5uvtNGKrX2lL6lYYJFI8h_LQeb-mUDA-d1aGjgsPPw8nFWLhZ0DcoPdOisZlLO4wGufrkMDiA7KbHtvrfNOaqYua_PV61hqQ49hP9NamJuf1df0QXwXYS1irA1ZKZ5Pb7zBhgMiT_yKg2FnAAe0bX_TXnZ8Bet6Wht_bs9FYkN8dHnWF042YpKaiyn6m0jZmKBDRj6x9p12swN_yU0uqST501OCroq02cyI5EZ_dlOmbSvMe4UoZY9RFART07fPNi-CMIf7qV0Js_CUmR-rAAoHJZf3byvv2UFSOd4N0TFluLSyTflBS95NMD-uvK2k2J43QBlS9_2ETq_wwqSACw8kR0CTrUqmHi7P2XszZb_hX5dZR3xFxbu1t0uZVNgqS6Jj71P8rxPOk03ayGYlRfU4*1754333834322*d47951023574adda90f74b11f4c5c98c335c599dca6ffd8ef1986a9879badea4*SslwNDJAYQlC0ssxFMuVs-yq7cGCocFfOvoncDdjuM4~2; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=UWlJa1hYN1NJekJRbjBlSXE5c0Mva2FGU2NOdDAvY0taaXBCQ1picUsyS280WXZEc3RJOEg0VHVudzlIUFFQZUlaK1psRWRmSURVN0E0cTZsaW9sVnduczZvMHhtdk1YR3ZCOFd4SXZITms9LS1KWEhrNkhncVJpM1o1QTdhdS9xWFNRPT0=--131dd1e1ab73af54263fda1f1f091d6c3c8730a5; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(thundercats_project_plan)
