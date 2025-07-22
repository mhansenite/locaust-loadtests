from locust import task, run_single_user
from locust import FastHttpUser


class LoadProjects(FastHttpUser):
    host = "https://thundercats.staging.guidecx.io"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:140.0) Gecko/20100101 Firefox/140.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/v2/projects?_rsc=1xj1t",
            headers={
                "Accept": "*/*",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%2Cnull%2C%22refetch%22%5D%7D%5D%7D%5D",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://thundercats.staging.guidecx.io/tasks",
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
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.staging.guidecx.io/auth/session",
            headers={
                "Accept": "application/json",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
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
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "app.staging.guidecx.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
            },
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Length": "12",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "7dde6021d1d552016a324b86aabc828d90123a87",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
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
            "POST",
            "https://k2-web.staging.guidecx.io/manager.project.project_list.ProjectListService/LoadTagsDropdown",
            headers={
                "Accept": "application/grpc-web-text",
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
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzE0NTI5MywiaWF0IjoxNzUzMTQzNDkzLCJqdGkiOiI0ZWNmODllMS00YmY3LTRiZDQtYTY5My1mZTQ4ODJlMjUzMjgiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.b5lTt-0lD5-y9WQZSQaCVDO797VTYF7s8_7BdGic-qVV02iGC2fU8B_P44CUAXvgez1pvsC5__yGEztkitm5esaVlVmzHksFFTh0byOgcZWSEH1OkxlimKv-4GYzEXR3-oax16HqlopO-seYcKF_mx3afw88aSL-C_6Kw3qKB0UhQ7-2e7y6FB83nl1k3Fps9oTWUT-CrHKuLA37-1UeK0x1Yl7xHS132ytsEeX-0aoALY1k6XoR_UPffJ4umBZqdE7l426H3zq7HCJast2MuAgBFikLYbklyh0EHVBnDC9iBc8YiFp-wfS6uqhs55adps-RjfZkTVTSWFYYWxJnFQ",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.staging.guidecx.io/manager.project.project_list.ProjectListService/LoadProjectManagersDropdown",
            headers={
                "Accept": "application/grpc-web-text",
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
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzE0NTI5MywiaWF0IjoxNzUzMTQzNDkzLCJqdGkiOiI0ZWNmODllMS00YmY3LTRiZDQtYTY5My1mZTQ4ODJlMjUzMjgiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.b5lTt-0lD5-y9WQZSQaCVDO797VTYF7s8_7BdGic-qVV02iGC2fU8B_P44CUAXvgez1pvsC5__yGEztkitm5esaVlVmzHksFFTh0byOgcZWSEH1OkxlimKv-4GYzEXR3-oax16HqlopO-seYcKF_mx3afw88aSL-C_6Kw3qKB0UhQ7-2e7y6FB83nl1k3Fps9oTWUT-CrHKuLA37-1UeK0x1Yl7xHS132ytsEeX-0aoALY1k6XoR_UPffJ4umBZqdE7l426H3zq7HCJast2MuAgBFikLYbklyh0EHVBnDC9iBc8YiFp-wfS6uqhs55adps-RjfZkTVTSWFYYWxJnFQ",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.staging.guidecx.io/manager.project.project_list.ProjectListService/LoadActiveMilestonesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
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
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzE0NTI5MywiaWF0IjoxNzUzMTQzNDkzLCJqdGkiOiI0ZWNmODllMS00YmY3LTRiZDQtYTY5My1mZTQ4ODJlMjUzMjgiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.b5lTt-0lD5-y9WQZSQaCVDO797VTYF7s8_7BdGic-qVV02iGC2fU8B_P44CUAXvgez1pvsC5__yGEztkitm5esaVlVmzHksFFTh0byOgcZWSEH1OkxlimKv-4GYzEXR3-oax16HqlopO-seYcKF_mx3afw88aSL-C_6Kw3qKB0UhQ7-2e7y6FB83nl1k3Fps9oTWUT-CrHKuLA37-1UeK0x1Yl7xHS132ytsEeX-0aoALY1k6XoR_UPffJ4umBZqdE7l426H3zq7HCJast2MuAgBFikLYbklyh0EHVBnDC9iBc8YiFp-wfS6uqhs55adps-RjfZkTVTSWFYYWxJnFQ",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.staging.guidecx.io/manager.project.project_list.ProjectListService/LoadProjectStatusesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
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
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjgyY2RjNDU3LTAwYjYtNDg1Ni1hZDI2LTFkMDlmMzQyZGM0NyIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMTEwMmMzYmMtNGQ1Yy00ODgzLTgzZGUtMTAyOTRlMzFiZWMzIiwiYXVkIjpbIjE4NTQ4ZGU5LWY1ZTQtNDQ0MS05YzE5LWYxMDA0Y2Q0ZGVhMSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzE0NTI5MywiaWF0IjoxNzUzMTQzNDkzLCJqdGkiOiI0ZWNmODllMS00YmY3LTRiZDQtYTY5My1mZTQ4ODJlMjUzMjgiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIxMTAyYzNiYy00ZDVjLTQ4ODMtODNkZS0xMDI5NGUzMWJlYzMifQ.b5lTt-0lD5-y9WQZSQaCVDO797VTYF7s8_7BdGic-qVV02iGC2fU8B_P44CUAXvgez1pvsC5__yGEztkitm5esaVlVmzHksFFTh0byOgcZWSEH1OkxlimKv-4GYzEXR3-oax16HqlopO-seYcKF_mx3afw88aSL-C_6Kw3qKB0UhQ7-2e7y6FB83nl1k3Fps9oTWUT-CrHKuLA37-1UeK0x1Yl7xHS132ytsEeX-0aoALY1k6XoR_UPffJ4umBZqdE7l426H3zq7HCJast2MuAgBFikLYbklyh0EHVBnDC9iBc8YiFp-wfS6uqhs55adps-RjfZkTVTSWFYYWxJnFQ",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Length": "4",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
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
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Length": "4",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
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
            "/v2/zz9r8h6v3b6e0bem2j05j2ag3g7v",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Priority": "u=5, i",
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
            "/v2/rxn9aje8cpxprjash1c45lt5d1sc",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Priority": "u=5, i",
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
            "/v2/rsgipbrzbdigpruppkojkhms2jw4",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Priority": "u=5, i",
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
            "POST",
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Length": "4",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; s_fid=0EE7024574418985-3EF65E226A056508; s_cc=true; s_sq=guidecxstaging%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fthundercats.staging.guidecx.io%25252Fv2%25252Fprojects%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-vtlfk4ov=K20wdUY3ZmFLMC9lSnFzcHRtL25sS3hWYTUzbTlKTzMrM1FsNmltd3dpWm5zWHNLSXAwSFJ6bDg2azJCUGNRckZXSjJsUS9uOWJSWGdrU1lXQWZxVFhZd25JNk5pRlBYcEVERTdnd2pVcW89LS16cndEbmtOOGhveDlRYW5jL1RpdnFRPT0=--7ff7774a454f85f9fe1be7a1fc0324067030a904; intercom-device-id-vtlfk4ov=3e1d9f0e-6543-41e0-9f07-faaf3e6a8dd5; _gcx.nav-expanded=true; _gcx.staging-session.v2=Fe26.2*1*93deea5090120bfbda4cb842c1032cced0b33991457c7242013bbe30d57c3d68*_b5rKnEwVySBmA3Hr072wQ*alp-T2EzjFlwXAG_EFGqboWep1GmC83WCZNL-yHjMRp5qPB_m1Q-8QtmJGEexGFG0Wd4Ct_kiIjdzIZ886gZXlB1QUw80LEpq0e-1NzAD_X9InG2ZZeu2WLcVMvYddbkvTbMwlt_AhnzkMkKdnUuDvMtZleno9XLpXXogyiqmGjhO5C4ABAa5HOEaHAzvB26S0lSnK_rQZvBnhwJeNmcBTlGmKT5dv7KpEZd3OR-tquG2I9IzFTI0V0fxFccsEKulDQ1Iy5ArcTQ0srW9uuEhBOaruvRxyV_PlKTG6CJn19S0Dt2WXuoPti7JnLxKR-JOa8MX156ZqfJLP0DZimDKSf_rQ_ktva1cartrI0fSi2-igdM8ObU1Ev6oBStRnvFzmUEUFehkqLDOOrqouhl6lAqH2zD_yNwLpj2DdjCM3Dk0IBmK3v7iJRXghewgsA9s-CGvgNh28BjD93MgMoJ-w6i02By0bPU7V113ImL7n5M9KsITjGjbHuxLRHIfbQ5pxULRbgIamHLm0UR3CEVAa5YPjHA6ykYcxaOLFPKKTiRoaTzwvfx1b8LY8gBlOJ9bWys43EWevDSOj7MtXYyodjg0blsbuFeCyoTeN5NQGtrpj8-9uNbZB9S_G0ZH2ss7yOLy4xW_YT-xZ66YTHH99jKQUojEeSwR4mIb5jR33yABBxQNc0CSCrMTGxowIfJovDD24GuCha-1rXphW89C4LFo7Qa3KmyGHQ3PEPk9ohEpd2TXrWuu9SbmeIcPIxCgCV-CV09TMEXO1AV9pj2bsTwE483TCi_sDzRf25cAbBcYTxuPaV3gb0sUA3W-UGmMkZDcOpR6S20pK5C_OW8HvhH83Wu7rrwpzZ2rfFgN5qumyS9OKOie785ECPafjeB-F3GIxINyMminJIWyLz1uJ10M2GDrnvyl9Pn6VQNoubEGWHdGYd_lA6_lOW1THc3VX3aMl3qXfN2hglSZwxPDs-EoIzHXxgZ2AfySSzDjlOes417DTcowuTYKV-K3Pw09ALCj1aZuCkcd9zbvOjdXY2fcwwfC3IXYLZoY8j8HvvvmW09mmwKoYrWCEruFDKg538Y5RH9HI93uV53ucywHkZ7YL2AhltIBWkVeQPJzuFDqRKGOdBH14NHeblsFKwp5OBvonj1lAbqWgLbR26mzMrekYmeLEqhUxeRWCd5Xj-As5c85Ioq_lM_7dImDlt70W8bXq9zrctcf7YOxJ12atayCkublyzBjf7-qKPX-PM1kfq09JrK_BXXOdhoiWy-QlkPZ3jX37euT48DdrFcKiqjtWUKTceVHH_UoTgiu8W3smAkaS9kAVzLzXltaPvyxuBWmZiVVxVueiO_diCZkUoWmJt072dypHY6GKRw0J5MF7QUCEfontkt6GJ5hjSvS7NLZDBPJCgMKCMzC-zIcsON3aWLk9e4F1gQK05LDt8cZi5WFfyJe3yxW06lJWOYcctLQ6dMv6LmGg6kfhtiRn8yqtdEV_f_RcgJAJbZZ1tKds1el-ayG99-8raptVxATF-FqH-D0dWsPBqqQ9zRFx29N_F538J1Oo9wuVSOg9w*1754353093405*0acee6a6c764084783162b54dd9707f8fb3ce8bc0a8b6537489b1a72ab633d50*4OLOAYF8m8TcDnFAit94ktLZPOBlhngknDsxeQ8dwFU~2; _gcx.staging-session.v1=Fe26.2*1*ab9ca1598d0d48e6eabc306a3b70bb19fd638ebda34f313b7aed74251311eb9e*iwfTKZz7xOcO3TbUV5mhbQ*PSiUnJbGKHidHBLY1o0Gc50g8MTFTvIGgjuYWRKHRW78yVyP0nJCOaASZKboL0XSiHawCUIQnDp6jb0NtWN2zwAeRo_EqME12ppRVVnA47meRHkfF-O3x8mixObnIaQIrS2RxXIDzAZnFMcbHuxpu0OE2rAvzF1c5B1XUhorpEJ5-DK5arBTZb1BB4ZnTshcauPll9xskkJUwBvFyImNMEHND-gx89XSBOlDxVvFbTWnbqm0sN188SRmOGTCfGQnGdh4cXKdCUL1qQrSyTOx4yY6AcpYtm3WhA8sHOooY6wU0QobQfzdFpzy2GRUoupQSJZlY9i-sRbDAw8nR22Dnuo-CKa3aipdqgBSuQl1_csuGZiPXKo5yglyJeTS-MAtbGPiTcfOQOpBa0GgNT8Tuan4RD-n6B1CqTuobpQvRzXpfTN3b6khVMca53RtC9uiyUoAJaTp3q3qIvktE84Vjf2IH_7n6nRNJtplNywgI_89HLFZtv_WozvCpIFXU1mfpaINCkOf4_mIJ2MzxTjPo6TEmIHw5ngTMi17-l0vO6BjwwQgeZ7GeGTu2S3FyESstNb1xdbWF0Klw053yXvjDHw4VIcqHJ1Pg5XPFZVvTIg2M2_s2sm8a6zzduMs72dd0ffgXEw94ffRlzZcF-0FIJ7jkb9E3uHY_uJT6cNY-pWr_fMNGXsMhz-Jy0p93xZSYbbg85kFYRr4oD1Rn4JhzHsqtT6_PIPMcufQKXhttBDJxfQ3hvB1y-g96zOGMZ2BWwDgYslVH7ZsFHOl78p9KGE0Cz4eFNP9-BTCrGmMCQZp_feCNcAylLCSc9Iywhet0mbspwBxx2NDx_jaCK9KLz-ABKbogzJn4UoacQudvUM*1754353093740*e797d998270ebfc79e3ed82f1201a59e83474ea66aaa2011d4455e5a578b8931*scuXpV3hI1vFoDBc0RFMu1eHmQBxPXz8LPG00adK20Y~2",
                "Host": "thundercats.staging.guidecx.io",
                "Next-Action": "d460095e80259ffd0e3377f81ff6d3eb70666bda",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
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
            "https://streaming.split.io/sse?channels=MjQ2OTYxMTc2Nw%3D%3D_MTI4MjY3MDc0Mg%3D%3D_control,MjQ2OTYxMTc2Nw%3D%3D_MTI4MjY3MDc0Mg%3D%3D_mySegments,MjQ2OTYxMTc2Nw%3D%3D_MTI4MjY3MDc0Mg%3D%3D_splits,%5B%3Foccupancy%3Dmetrics.publishers%5Dcontrol_pri,%5B%3Foccupancy%3Dmetrics.publishers%5Dcontrol_sec&accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6IkRQVkE3QS44czhnaVEiLCJ0eXAiOiJKV1QifQ.eyJ4LWFibHktY2FwYWJpbGl0eSI6IntcIk1qUTJPVFl4TVRjMk53PT1fTVRJNE1qWTNNRGMwTWc9PV9jb250cm9sXCI6W1wic3Vic2NyaWJlXCJdLFwiTWpRMk9UWXhNVGMyTnc9PV9NVEk0TWpZM01EYzBNZz09X215U2VnbWVudHNcIjpbXCJzdWJzY3JpYmVcIl0sXCJNalEyT1RZeE1UYzJOdz09X01USTRNalkzTURjME1nPT1fc3BsaXRzXCI6W1wic3Vic2NyaWJlXCJdLFwiY29udHJvbF9wcmlcIjpbXCJzdWJzY3JpYmVcIixcImNoYW5uZWwtbWV0YWRhdGE6cHVibGlzaGVyc1wiXSxcImNvbnRyb2xfc2VjXCI6W1wic3Vic2NyaWJlXCIsXCJjaGFubmVsLW1ldGFkYXRhOnB1Ymxpc2hlcnNcIl19IiwieC1hYmx5LWNsaWVudElkIjoiY2xpZW50SWQiLCJleHAiOjE3NTMxNDgxNzAsImlhdCI6MTc1MzE0NDU3MH0.8et0NHpFWJDGL-zethA99wq9KLmh3cB4KVfroWUyg9E&v=1.1&heartbeats=true&SplitSDKVersion=react-1.11.1&SplitSDKClientKey=5c0p",
            headers={
                "Accept": "text/event-stream",
                "Cache-Control": "no-cache",
                "Host": "streaming.split.io",
                "Origin": "https://thundercats.staging.guidecx.io",
                "Pragma": "no-cache",
                "Priority": "u=4",
                "Referer": "https://thundercats.staging.guidecx.io/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "Sec-GPC": "1",
                "TE": "trailers",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/mySegments/18548de9-f5e4-4441-9c19-f1004cd4dea1",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
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
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "https://sdk.split.io/api/splitChanges?since=1753135864962",
            headers={
                "Accept": "application/json",
                "Authorization": "Bearer 2vuekfqg5932jhetguo0cc9taj864hjh5c0p",
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
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(LoadProjects)
