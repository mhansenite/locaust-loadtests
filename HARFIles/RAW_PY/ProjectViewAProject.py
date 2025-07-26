from locust import task, run_single_user
from locust import FastHttpUser


class ProjectViewAProject(FastHttpUser):
    host = "https://app.staging.guidecx.io"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/_next/static/css/03afdd70ad25fd34.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/ebb131334889d476.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/26a80b2a6cab2865.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/00316870ed1dc6df.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/0b5e490155c27bed.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/170b0a3761d10a26.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/35e465b88aa66ad1.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/d8c9b7d9b1997477.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/dae0e8c712ff2e96.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/5d15467cd21af210.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/c4aa9bf51ebcc1c5.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/7b8638c33b6e5544.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/8d51b2c58c0fe886.css",
            headers={"Accept": "text/css,*/*;q=0.1", "Host": "app.staging.guidecx.io"},
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
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/",
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
                "Content-Length": "1078",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="app_id=vtlfk4ov&v=3&g=8da7acc4564510bc4deb7718e05690090a73e9fd&s=341ce6ad-dcab-46c1-8edb-ada3ef083046&r=https%3A%2F%2Fapp.staging.guidecx.io%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%3Fphase%3Dea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a%26view%3Dboard&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=064fe255e39ea934&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fapp.staging.guidecx.io%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan&anonymous_session=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0%3D--ae8d26ca1566cdf6190218c5df549b054b21f542&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0=--ae8d26ca1566cdf6190218c5df549b054b21f542; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0=--ae8d26ca1566cdf6190218c5df549b054b21f542; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0=--ae8d26ca1566cdf6190218c5df549b054b21f542; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
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
                "If-Modified-Since": "Tue, 22 Jul 2025 03:13:29 GMT",
                "If-None-Match": '"1753154009848"',
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/",
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
                "Content-Length": "1460",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="app_id=vtlfk4ov&v=3&g=8da7acc4564510bc4deb7718e05690090a73e9fd&s=9199d791-e0f4-4fd1-9ce0-be874524a6a5&r=https%3A%2F%2Fapp.staging.guidecx.io%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%3Fphase%3Dea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a%26view%3Dboard&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=93110cf6fb51f4c1&internal=%7B%7D&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%2C%22name%22%3A%22Mike%20Hansen%22%2C%22company%22%3A%7B%22company_id%22%3A%2218548de9-f5e4-4441-9c19-f1004cd4dea1%22%2C%22name%22%3A%22ThunderCats%22%2C%22website%22%3A%22thundercats.guidecx.io%22%7D%2C%22role%22%3A%22ADMIN%22%2C%22org_type%22%3A%22PROVIDER%22%2C%22trial%22%3Afalse%7D&source=apiBoot&sampling=false&referer=https%3A%2F%2Fapp.staging.guidecx.io%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%3Fphase%3Dea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a%26view%3Dboard&anonymous_session=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0%3D--ae8d26ca1566cdf6190218c5df549b054b21f542&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "84",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0=--ae8d26ca1566cdf6190218c5df549b054b21f542; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Action": "9704e78ed7422ab571bfa4456b0aab6b24b8d6b6",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data='[{"unitId":{"uuid":"ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a"},"excludeInternal":false}]',
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
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "SplitSDKVersion": "react-1.11.1",
            },
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://api.staging.guidecx.io/query?query=%7B%22dimensions%22%3A%5B%22workspace_unit_status.label%22%2C%22workspace_unit_status.status_category%22%5D%2C%22measures%22%3A%5B%22unit.count%22%5D%2C%22filters%22%3A%5B%7B%22member%22%3A%22unit.project_id%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%5D%7D%2C%7B%22member%22%3A%22unit.type%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22ACTION%22%5D%7D%2C%7B%22member%22%3A%22unit_status.active%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22true%22%5D%7D%5D%7D",
            headers={
                "Accept": "*/*",
                "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzQwOTU3MiwiaWF0IjoxNzUzNDA3NzcyLCJqdGkiOiIzM2ViNmQwZC1hOGQ3LTQ5MmUtYjliMC00NzA3M2VmNzMzNDMiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.Bod5K1iCvOmxaEI_Ubbe74y4D_KXP8YG2xWPEjiD_Asb6T4LNga4YZ4kwLy3K1aCP5BRiEReTj0oL-GrlHnP10t_wddZWfKDBIDXcsNjc0fRS9Ek_YhranK9in9icpg4jayDSUzhB5TY7OXaQFuLLxyQ4JGB-Dfx6uzeQXuDhD0HjPU6ECg82KcezNq5FYooqrBe_GLX-swACKervv08IneDFE9AeF70NyrfbPiABdTDwHj2E4a5hQm2hk5kmKYFGZ9WXi1blIwCoXrMvKRj4nhJhuQj-gLKbVf5XWpEAeoRQ9bk_nmGdUw2fbpZ6-THHcHvICqMFz9QwqDzrICtzA",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0=--ae8d26ca1566cdf6190218c5df549b054b21f542; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; user.id=1102c3bc-4d5c-4883-83de-10294e31bec3; gcx.session=T3zi02BeWuHfeKPd6qAYnHnlkjgO1vNJVE%2FvRrYqyFHcOmj1KwluqQ1MWgw5yUQZJHmr18BAiL%2B1RJ3EhtvMWCeTgeaS8qFcHH92uJ2T0S5LDaj0ASxMTw76Wq%2FEIb6IAzLWhKQ5dkvbN8Nx6ofsICcIJzlnoB5D4eAIuz0j2U0ddR09DobWoEBucJ5Ab2SQk%2F5J--3Rg3jWSXO2GVzETe--ex2sc37C6IQcZocr2lzv1A%3D%3D; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "api.staging.guidecx.io",
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
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
            "https://k2-web.staging.guidecx.io/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "112",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzQwOTU3MiwiaWF0IjoxNzUzNDA3NzcyLCJqdGkiOiIzM2ViNmQwZC1hOGQ3LTQ5MmUtYjliMC00NzA3M2VmNzMzNDMiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.Bod5K1iCvOmxaEI_Ubbe74y4D_KXP8YG2xWPEjiD_Asb6T4LNga4YZ4kwLy3K1aCP5BRiEReTj0oL-GrlHnP10t_wddZWfKDBIDXcsNjc0fRS9Ek_YhranK9in9icpg4jayDSUzhB5TY7OXaQFuLLxyQ4JGB-Dfx6uzeQXuDhD0HjPU6ECg82KcezNq5FYooqrBe_GLX-swACKervv08IneDFE9AeF70NyrfbPiABdTDwHj2E4a5hQm2hk5kmKYFGZ9WXi1blIwCoXrMvKRj4nhJhuQj-gLKbVf5XWpEAeoRQ9bk_nmGdUw2fbpZ6-THHcHvICqMFz9QwqDzrICtzA",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAE4KJgokZWEyYzMyYTEtZWM4NS00MjI4LWJiNjYtYjlmOTQyY2ViNmE0EiRlYTJjMzJhMS1lYzg1LTQyMjgtYmI2Ni1iOWY5NDJjZWI2YTQ=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.staging.guidecx.io/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "60",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzQwOTU3MiwiaWF0IjoxNzUzNDA3NzcyLCJqdGkiOiIzM2ViNmQwZC1hOGQ3LTQ5MmUtYjliMC00NzA3M2VmNzMzNDMiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.Bod5K1iCvOmxaEI_Ubbe74y4D_KXP8YG2xWPEjiD_Asb6T4LNga4YZ4kwLy3K1aCP5BRiEReTj0oL-GrlHnP10t_wddZWfKDBIDXcsNjc0fRS9Ek_YhranK9in9icpg4jayDSUzhB5TY7OXaQFuLLxyQ4JGB-Dfx6uzeQXuDhD0HjPU6ECg82KcezNq5FYooqrBe_GLX-swACKervv08IneDFE9AeF70NyrfbPiABdTDwHj2E4a5hQm2hk5kmKYFGZ9WXi1blIwCoXrMvKRj4nhJhuQj-gLKbVf5XWpEAeoRQ9bk_nmGdUw2fbpZ6-THHcHvICqMFz9QwqDzrICtzA",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAACgKJgokZWEyYzMyYTEtZWM4NS00MjI4LWJiNjYtYjlmOTQyY2ViNmE0",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=MnVmcVA3L3VxRko5Y3Z5SU95YzJOcjhrNnU2YU5HeDhBaC9ad3FvOVVNMmZxTkRzemJSalp6bXZKUitSMWtXUU9HMXlkRkxqOEZIWWQyblkrdlRjTzR4VHdtN1lMeWFjZ3lzUXdZazdwcmM9LS1GUm5DVzZkc1o3T1RITEd5S0J3SCtnPT0=--ae8d26ca1566cdf6190218c5df549b054b21f542; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
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
                "Content-Length": "1167",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data="app_id=vtlfk4ov&v=3&g=8da7acc4564510bc4deb7718e05690090a73e9fd&s=9199d791-e0f4-4fd1-9ce0-be874524a6a5&r=https%3A%2F%2Fapp.staging.guidecx.io%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%3Fphase%3Dea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a%26view%3Dboard&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=0fb4be4c70938672&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=18548de9-f5e4-4441-9c19-f1004cd4dea1&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fapp.staging.guidecx.io%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%3Fphase%3Dea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a%26view%3Dboard&anonymous_session=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0%3D--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "wss://nexus-websocket-a.intercom.io/pubsub/5-qG1Le76hkI-fSkSL1gS4qrfUhJ6HaOZeQuu2mS_KaJiLuVkH9DJiLCBJrk1W07IlPOOAPw3sKwTej58zbJiAA52U6oopopcgGCyv?X-Nexus-New-Client=true&X-Nexus-Version=0.14.0&user_role=user",
            headers={
                "Accept": "*/*",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive, Upgrade",
                "Host": "nexus-websocket-a.intercom.io",
                "Origin": "https://app.staging.guidecx.io",
                "Pragma": "no-cache",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "websocket",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "Sec-WebSocket-Extensions": "permessage-deflate",
                "Sec-WebSocket-Key": "GK3oCLB0d0A2ryOmpWftsw==",
                "Sec-WebSocket-Version": "13",
                "Upgrade": "websocket",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.staging.guidecx.io/manager.project.plan.ProjectPlanService/StreamProjectDetails",
            headers={
                "Accept": "application/grpc-web-text",
                "Connection": "keep-alive",
                "Content-Length": "60",
                "Host": "k2-web.staging.guidecx.io",
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzQwOTU3MiwiaWF0IjoxNzUzNDA3NzcyLCJqdGkiOiIzM2ViNmQwZC1hOGQ3LTQ5MmUtYjliMC00NzA3M2VmNzMzNDMiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.Bod5K1iCvOmxaEI_Ubbe74y4D_KXP8YG2xWPEjiD_Asb6T4LNga4YZ4kwLy3K1aCP5BRiEReTj0oL-GrlHnP10t_wddZWfKDBIDXcsNjc0fRS9Ek_YhranK9in9icpg4jayDSUzhB5TY7OXaQFuLLxyQ4JGB-Dfx6uzeQXuDhD0HjPU6ECg82KcezNq5FYooqrBe_GLX-swACKervv08IneDFE9AeF70NyrfbPiABdTDwHj2E4a5hQm2hk5kmKYFGZ9WXi1blIwCoXrMvKRj4nhJhuQj-gLKbVf5XWpEAeoRQ9bk_nmGdUw2fbpZ6-THHcHvICqMFz9QwqDzrICtzA",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/team?_rsc=1wiip",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Router-Prefetch": "1",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
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
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/overview?_rsc=mcf87",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
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
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/messages?messageKey=projectId&messageId=ea2c32a1-ec85-4228-bb66-b9f942ceb6a4&_rsc=mcf87",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
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
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/attachments?_rsc=mcf87",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
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
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/custom-fields?_rsc=mcf87",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
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
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "155",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Action": "4f122631d19346579dd7c91cdfe7c24281bbc02a",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data='[{"projectId":{"uuid":"ea2c32a1-ec85-4228-bb66-b9f942ceb6a4"},"startDate":{"seconds":"1753408091","nanos":0},"dueDate":{"seconds":"1754012891","nanos":0}}]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/team/error-1637546820862b92.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/history?_rsc=mcf87",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Next-Url": "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/overview/error-c662038742273f3d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/custom-fields/error-a2277441fd4e4b6c.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/8817-22718a6d28849e8e.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/messages/page-8e1e31eef5e32c74.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/history/error-1ad433aceda9bcfa.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/7466-7b671011427134ac.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/overview/page-2c0e4ea1cf3c977e.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "134",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Next-Action": "f0dcb167bb0486ad2aff91c85d8f91b40996dd37",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22project%22%2C%7B%22children%22%3A%5B%5B%22projectId%22%2C%22ea2c32a1-ec85-4228-bb66-b9f942ceb6a4%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22plan%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fproject%2Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%2Fplan%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://app.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            data='[{"projectId":{"uuid":"ea2c32a1-ec85-4228-bb66-b9f942ceb6a4"},"phaseId":{"uuid":"ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a"},"filters":[]}]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/8140-92de6ffe2711173d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/attachments/page-da9efe3c8ad35c29.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/8963-55fceb97a97c5a0f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/custom-fields/page-d963f45ccffa7113.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=bjMyNVVqSTBiTVk4WlJGeFg3WE5NdzF3dnhEZ0M3eHRJek1jU2tnUHdhU1dkQU9FOEFLV3Z2cHRrbXBFSTNIOWpocHpCS0MvSmNOOGo4aWdhem04ZWoxYjZiTTAzejhGTWdwQ3Bxa2V5OU09LS1uZitrOWJjZlZXUzBHdVVHVUxzL2F3PT0=--e936f177e35ae5f6e5075aa2b1ab99ba19ddbc10; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DLoadTestProject-1753408090-02ded2e4%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fapp.staging.guidecx.io%25252Fproject%25252Fea2c32a1-ec85-4228-bb66-b9f942ceb6a4%25252Fplan%2526ot%253DA; _gcx.project-plan-view=board; _gcx.staging-session.v2=Fe26.2*1*68aacb3da8f1e407a6646dcf90aabd996eac85ee048f85c69f82cef244ba61a1*LToU-xkyckgyXbIy17uClQ*FAQEwfVyfeWCm9KCl2X0vsxzfaPOHp5wm9O3p5R_D9KZ0BoG1WkVmPGrFTQP93cLAN6v9qQE5B8DmPpbRjH_SQ-YzLI_a2fwK5l6YYuBgaCD7W1nBugHrYgvLLss9BCPu-p_kExb0Wbkta-BDApKn1H26afM3oGfEaYXfOSFjUgcuD_Zgcanb_BPY7-fkxWq_E-snPESz2rwreVTnMUTFvklEbsx3I0ZoWiiTf0XD_k2V9Gryl_YQ3W70evRx5aGdyy7hczC-_NFlQeHASGj_YczDTwzerW7F26ZXdv9yZGWMYOkrhcCTOhI1F38KZa4aUzU7IKG5D8EMZGtZGvRU-u4vZvJQ5wuQISE6i7Fk5rNzH9kcRRZ4HY1Bd6Gotehdu1KlHmYt3sKpKRK47xCwewKtHM1bxqsL_fnCUkm-XyNokPuhOY13PGcb1HydPWp2TWg8dol8E9-OgfLPsAtT5PbED10EN1oCYAUDFW-RL83CeVX13RAigHXcVBVJQaKeejpMZhcLc5zvEKbsFdH8xgKqA-L5KSr7IlQprmAwd3-mwtZvnwIC7OePR4Tm9hqag_eRWw7O2_qaY1VX4A70Ogz3D-47n2LutBwf6RphH1tMC8OaTjwTyRY1F6ge5K3nxE-DIoViku4wFxGOnRfhkiwb_UOhl62EQRcOCjXHkL_hwMkyZrCT3zLVPEM6UxD4j4AHsWiCh03o1MkgYjkyoeHGy5JvnITJn4MHtzl8i-nIYAdQck3wH1aluFo9JoEWimvsu4tBJM7MX9CrF7FOpF-h_Dfa7_wKsy1y4MAv0kTmF9EUmYFTmmd5mv4XZjQHle7T4ZltfxcY3rdwhr0In0ccLQzygw14bM7L_P0-RBiCbknub81SC87g74go8S9agaDzZKnin8qFwC7MN505t1IfEIBMd_cCE3UjCus3AR3k5gfjUYX5SGgth3QIpQ1ICsIlzstAiHS5AhAMdBB4VHoF1OC__oSlAUGcWDsIaBzockB_6N-n7O_PzPmBaZa7REQWavp2q-ooXdqVEIiDqnMmIRa36sJebeFodsOv-g1E4WgIgY0tWAnKoAcXsCbCOi7XM1_nsuuMve08EViecvem_u-hLEqZA5AAvN1lHw__7yNB-DRSWwVlaD7_4NHiqLK9wcNmgKFS8-2mRPUoi1O2SbZhmYryWjN3Z60KcPTMOar6voNPF4q7aC3MdZDfTYlEf8CSiVqzZVgdwlmxRuMFBCE_NnjBzEFfBLqsdIIfKrgcAAnkOA4ul2GrgEauHmzx7uuDMkBxZ4uKKcxVy5yLIN_gwwC-4kJX66-excBMVjnUrTyDcFfR8J-74XWzomEt8sNctcmY9bRG0ZqIQD-bMbxIo5j4JEg2Rnh0lzOpwR53iwcvgUICz0xRGF43iDF97c0vCViqI8E3fLhzBeDuk8nMiRqGVC8NJcr9MFMi9rCQpWBosm9ei57iwyjdsdooIs7JP4zbEDMjnmf7Z5ktiB_xPsxBWKWM7yaqKpZi--3idMrfjzkFlPm8r5it-vLjGCkZlhs0VG5F0bCTWzviZa_l7fs3JYLgFeHLko*1754617372574*dd2ac57e8206b658abbbcf7aab63825eea9afa27d358194b96fc27e193535b62*dyF7PqfPl-gbPSc0CK_8yV5YPsdNCqYkUlAbQ8gUcSI~2; _gcx.staging-session.v1=Fe26.2*1*ee8be089b31b942c85d19e32b7aba5124e38c5463915e8e9c3333444a7040719*f95oCGlEDgdfUGT0c3TEnQ*NSXZmpuj6XiZKYLy8bnikVGM5KywK0fV3xkWGQMPuRSt--idOEmPBvBTQ6aahO9-ENI-M0ng2WkHDuAPC2ZTJnI5anlGnFeKnRRyEfP_yKv7SYx50_NiLTzEBj_ifAR0Yx0gFBfkZu29HUhNRFEwfOrfmCGJiwM1_34FELqkXYYsR-8r9d_L8__aRs31GZf1hlU2C1wn6iZdp5BpxauthwBIUV4KJjumntKA46LYyi2k2SngEl06DhK6VTfRzdDu5eXMghLnWskgERMeIslcQvSiznxfkaCJUxg3eEVmt4MaKmDcytQ46c7oEvucWpqZYToSt0988ObcziEEr8QU4ywqTmwx3xmc8WJOliP0BwnNXf8pAT9k3ocxuYpm9rlwhx95YAtUODSDxUIb-4lx5-N-Si8lYc71x7VYIy4MMD9NPjBgvsb9s5Z1oJ9xPdREb6RTLITWyI04x8IkpZkFJf_3CMiLeNkTrRNUhoOGE99P0Hl8i51g9PopRWtqphucqeQr3myfLi3AnosTVSjzPV5YuVhcUqD-i3RAcHehlUa-ABUkfQiOJlii2UB9HJ0tvQuSdC5-6S1djrz1r6f3mTnqOtFvbXW6xOFY3Mep8Bw48R_n37Dfc0PI3BqaZgV8aAIotTqIQSeCUFe4gOQkGkSk_q9Z23aAKLd3uMKNtuSd7Ot0YiAmR6fRUPIoeW3rYJTylxCwZz0RYTzvkxz8Qc1aJJJt7HVs3-_rzdZ7WlmbzpfGiVjjQxV35fowdKVgdiEPxKfgZzl6x9nHLBzFYNmkfUw0DGBn5q_DOm7MGQdCqOiLTOV2d0A2zZeO5xN0sI_4EV4ahNTWFH_e6_NWmm6Zq6iq4ucrsvBfI-spVRI*1754511857659*3bd60a0429cfd82048639068bc136ac8e25e4c9c5fc2a91e445cc123e11dfb15*Pdl0tKuj9mym8SvL0NpzEilIt6q3ldLMOoGvy632RM8~2; _gcx.create-project-method-preference=quick; _gcx.project-view-v2=list",
                "Host": "app.staging.guidecx.io",
                "Referer": "https://app.staging.guidecx.io/project/ea2c32a1-ec85-4228-bb66-b9f942ceb6a4/plan?phase=ea2c957a-cbf5-4d7f-a0bd-7ae3adf8ce6a&view=board",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(ProjectViewAProject)
