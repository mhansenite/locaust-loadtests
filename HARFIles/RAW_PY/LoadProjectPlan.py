from locust import task, run_single_user
from locust import FastHttpUser


class LoadProjectPlan(FastHttpUser):
    host = "https://thundercats.staging.guidecx.io"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/_next/static/css/e4fa05bbeff903d1.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/26a80b2a6cab2865.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/00316870ed1dc6df.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/170b0a3761d10a26.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/35e465b88aa66ad1.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Host": "thundercats.staging.guidecx.io",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/css/d8c9b7d9b1997477.css",
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
                "Content-Length": "987",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
            },
            data="app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=ee82653a-96a3-4747-94ed-88b18165d1b1&r=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fprojects&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=6ada5b7ae4c38e79&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan&anonymous_session=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0%3D--7ff7774a454f85f9fe1be7a1fc0324067030a904&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
                "If-Modified-Since": "Mon, 21 Jul 2025 22:11:04 GMT",
                "If-None-Match": '"1753135864962"',
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
                "Content-Length": "1369",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
            },
            data="app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=d3d79041-7649-4e06-b48a-fd7b4dd73ee0&r=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fprojects&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=3ea906022cd90e3d&internal=%7B%7D&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=undefined&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%2C%22name%22%3A%22Mike%20Hansen%22%2C%22company%22%3A%7B%22company_id%22%3A%2218548de9-f5e4-4441-9c19-f1004cd4dea1%22%2C%22name%22%3A%22ThunderCats%22%2C%22website%22%3A%22thundercats.guidecx.io%22%7D%2C%22role%22%3A%22ADMIN%22%2C%22org_type%22%3A%22PROVIDER%22%2C%22trial%22%3Afalse%7D&source=apiBoot&sampling=false&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%3Fphase%3D6ee23d15-5122-4788-beaa-7b3f3b3976ab%26view%3Dboard&anonymous_session=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0%3D--7ff7774a454f85f9fe1be7a1fc0324067030a904&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "84",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://api.staging.guidecx.io/query?query=%7B%22dimensions%22%3A%5B%22workspace_unit_status.label%22%2C%22workspace_unit_status.status_category%22%5D%2C%22measures%22%3A%5B%22unit.count%22%5D%2C%22filters%22%3A%5B%7B%22member%22%3A%22unit.project_id%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%227c235972-a318-430e-b83e-e0c4af6e616b%22%5D%7D%2C%7B%22member%22%3A%22unit.type%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22ACTION%22%5D%7D%2C%7B%22member%22%3A%22unit_status.active%22%2C%22operator%22%3A%22equals%22%2C%22values%22%3A%5B%22true%22%5D%7D%5D%7D",
            headers={
                "Accept": "*/*",
                "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzE0NTI5MywiaWF0IjoxNzUzMTQzNDkzLCJqdGkiOiI0ZWNmODllMS00YmY3LTRiZDQtYTY5My1mZTQ4ODJlMjUzMjgiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.b5lTt-0lD5-y9WQZSQaCVDO797VTYF7s8_7BdGic-qVV02iGC2fU8B_P44CUAXvgez1pvsC5__yGEztkitm5esaVlVmzHksFFTh0byOgcZWSEH1OkxlimKv-4GYzEXR3-oax16HqlopO-seYcKF_mx3afw88aSL-C_6Kw3qKB0UhQ7-2e7y6FB83nl1k3Fps9oTWUT-CrHKuLA37-1UeK0x1Yl7xHS132ytsEeX-0aoALY1k6XoR_UPffJ4umBZqdE7l426H3zq7HCJast2MuAgBFikLYbklyh0EHVBnDC9iBc8YiFp-wfS6uqhs55adps-RjfZkTVTSWFYYWxJnFQ",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; user.id=1102c3bc-4d5c-4883-83de-10294e31bec3; gcx.session=5NEkf%2Fy29qvuF8TCMMom5i7Vk3H2tZbclM5xzYeS6DkSaqORo4KmzTQN0%2Bf3P2ES2buMyXx7zoL2euHbfbWUctLeco2HtHgwHxPSS6DYqqgzh%2BhuEEVHuvPLf8HKBqF7s7xQMfCIc57fKTPhzzXkn6Nljpw9TZHBik1Tl3Mn5fAF25OuK7gx8yJRYPOY1K2OVGwj--LoPQN3owUEGDsamH--VKLHoEuBD5bVgJoUGZaJ4A%3D%3D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "https://k2-web.staging.guidecx.io/manager.message.channels.ChannelService/GetTotalUnreadMessageCount",
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
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzE0NTI5MywiaWF0IjoxNzUzMTQzNDkzLCJqdGkiOiI0ZWNmODllMS00YmY3LTRiZDQtYTY5My1mZTQ4ODJlMjUzMjgiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.b5lTt-0lD5-y9WQZSQaCVDO797VTYF7s8_7BdGic-qVV02iGC2fU8B_P44CUAXvgez1pvsC5__yGEztkitm5esaVlVmzHksFFTh0byOgcZWSEH1OkxlimKv-4GYzEXR3-oax16HqlopO-seYcKF_mx3afw88aSL-C_6Kw3qKB0UhQ7-2e7y6FB83nl1k3Fps9oTWUT-CrHKuLA37-1UeK0x1Yl7xHS132ytsEeX-0aoALY1k6XoR_UPffJ4umBZqdE7l426H3zq7HCJast2MuAgBFikLYbklyh0EHVBnDC9iBc8YiFp-wfS6uqhs55adps-RjfZkTVTSWFYYWxJnFQ",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAE4KJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZiEiQ4YjQ1MjcxMy0yMWZiLTQ3OWYtOTM0My1hMjAxZjYwZjA2NGQ=",
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
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzE0NTI5MywiaWF0IjoxNzUzMTQzNDkzLCJqdGkiOiI0ZWNmODllMS00YmY3LTRiZDQtYTY5My1mZTQ4ODJlMjUzMjgiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.b5lTt-0lD5-y9WQZSQaCVDO797VTYF7s8_7BdGic-qVV02iGC2fU8B_P44CUAXvgez1pvsC5__yGEztkitm5esaVlVmzHksFFTh0byOgcZWSEH1OkxlimKv-4GYzEXR3-oax16HqlopO-seYcKF_mx3afw88aSL-C_6Kw3qKB0UhQ7-2e7y6FB83nl1k3Fps9oTWUT-CrHKuLA37-1UeK0x1Yl7xHS132ytsEeX-0aoALY1k6XoR_UPffJ4umBZqdE7l426H3zq7HCJast2MuAgBFikLYbklyh0EHVBnDC9iBc8YiFp-wfS6uqhs55adps-RjfZkTVTSWFYYWxJnFQ",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAACgKJgokN2MyMzU5NzItYTMxOC00MzBlLWI4M2UtZTBjNGFmNmU2MTZi",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "wss://nexus-websocket-a.intercom.io/pubsub/5-xCf11hDKhYL1u6c9XY69Pee-cYJvVSX3HMkdXazsHdUo2EfpxeL04jPYeKJ8ozOfrQ57gId6pkZmrKI5Z3Cj4HetWXeFBpWS_kK-?X-Nexus-New-Client=true&X-Nexus-Version=0.14.0&user_role=user",
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
                "Sec-WebSocket-Key": "cIDV3BWktOre98MTKpGI0Q==",
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
                "Content-Length": "1076",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "api-iam.intercom.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
            },
            data="app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=d3d79041-7649-4e06-b48a-fd7b4dd73ee0&r=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fprojects&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=68098fdb14213b5f&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=18548de9-f5e4-4441-9c19-f1004cd4dea1&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%3Fphase%3D6ee23d15-5122-4788-beaa-7b3f3b3976ab%26view%3Dboard&anonymous_session=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0%3D--dbc463d083e20a1cdceb68f46b5e83a6819a598b&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/team?_rsc=1v6nc",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/overview?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "GET",
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/messages?messageKey=projectId&messageId=7c235972-a318-430e-b83e-e0c4af6e616b&_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/attachments?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/custom-fields?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "POST",
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "155",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
                "TE": "trailers",
            },
            data='[{"projectId":{"uuid":"7c235972-a318-430e-b83e-e0c4af6e616b"},"startDate":{"seconds":"1668384000","nanos":0},"dueDate":{"seconds":"1674777600","nanos":0}}]',
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/_next/static/chunks/8817-e4b57d1cad2814c6.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/messages/page-4f211fac95281e0b.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
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
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/history?_rsc=l0jup",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/history/error-1ad433aceda9bcfa.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/custom-fields/error-a2277441fd4e4b6c.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/overview/error-c662038742273f3d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/team/error-1637546820862b92.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "134",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/8963-55fceb97a97c5a0f.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/custom-fields/page-2677adce10030add.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
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
            "/_next/static/chunks/7466-7b7b8ab274a1435d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/overview/page-4a4a874a94502ada.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
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
            "/_next/static/chunks/8140-92de6ffe2711173d.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/attachments/page-81e602ba060ffa0b.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/project/7c235972-a318-430e-b83e-e0c4af6e616b/plan?phase=6ee23d15-5122-4788-beaa-7b3f3b3976ab&view=board",
            headers={
                "Accept": "text/x-component",
                "Connection": "keep-alive",
                "Content-Length": "134",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "/_next/static/chunks/app/(protected)/project/%5BprojectId%5D/history/page-c5e094c1b1fea978.js",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253D1NovemberTesting2022%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fproject%25252F7c235972-a318-430e-b83e-e0c4af6e616b%25252Fplan%2526ot%253DA; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0=--dbc463d083e20a1cdceb68f46b5e83a6819a598b; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
            "https://api-iam.intercom.io/messenger/web/home",
            headers={
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Content-Length": "1076",
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
            data="app_id=vtlfk4ov&v=3&g=792c1eab01c0e85d9f858ecffb583407f7c332e0&s=d3d79041-7649-4e06-b48a-fd7b4dd73ee0&r=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fprojects&platform=web&installation_type=js-snippet&installation_version=undefined&Idempotency-Key=7f6d584913ec335b&internal=&is_intersection_booted=false&page_title=GUIDEcx&user_active_company_id=18548de9-f5e4-4441-9c19-f1004cd4dea1&user_data=%7B%22email%22%3A%22mhansen%2Bthundercats%40guidecx.com%22%2C%22user_id%22%3A%221102c3bc-4d5c-4883-83de-10294e31bec3%22%2C%22user_hash%22%3A%22c3f6009c9d67757302c38417f9ff5d4308c06ed9fff5e7579277e5cb57a67a06%22%7D&referer=https%3A%2F%2Fthundercats.staging.guidecx.io%2Fproject%2F7c235972-a318-430e-b83e-e0c4af6e616b%2Fplan%3Fphase%3D6ee23d15-5122-4788-beaa-7b3f3b3976ab%26view%3Dboard&anonymous_session=c3I0Q3lVNllScTUvaXExRWZ6bnNXMi84bDFUWkQvdW1sd1hITHNRT0hoTmRCSlVBMFZpU2N0Vk1SVFBsUnV2dU5SQVozNWVubjZwOVhVN24wOW0zSHI2djJlYkNjRkV2SW5kcmpLNWRoZmc9LS1jUG1jdjdsZ2NGcll4Rm1YNUk2Rkl3PT0%3D--dbc463d083e20a1cdceb68f46b5e83a6819a598b&device_identifier=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5",
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(LoadProjectPlan)
