from locust import task, run_single_user
from locust import FastHttpUser


class GlobalProjects(FastHttpUser):
    host = "https://arches.guidecx.com"
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
            "/v2/projects?_rsc=d8sqm",
            headers={
                "Accept": "*/*",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refetch%22%5D%7D%5D%7D%5D%7D%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%5D%7D%5D",
                "Priority": "u=4",
                "RSC": "1",
                "Referer": "https://arches.guidecx.com/tasks",
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
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Referer": "https://arches.guidecx.com/v2/projects",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.rest(
            "GET",
            "https://app.guidecx.com/auth/session",
            headers={
                "Accept": "application/json",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
            "https://app.guidecx.com/auth/session",
            headers={
                "Accept": "application/json",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
            "https://app.guidecx.com/auth/session",
            headers={
                "Accept": "application/json",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
            "https://app.guidecx.com/auth/session",
            headers={
                "Accept": "application/json",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "app.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
            "/v2/projects",
            headers={
                "Accept": "text/x-component",
                "Content-Length": "12",
                "Content-Type": "text/plain;charset=UTF-8",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Next-Action": "7dde6021d1d552016a324b86aabc828d90123a87",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
            "https://k2-web.guidecx.com/manager.project.project_list.ProjectListService/LoadTagsDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Content-Length": "8",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhZjQ0NDJkLTRkZGYtNGE0ZS1hNmQzLTVhY2NlZTMxMmEzNCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMzhiOTY4N2UtNWVlNy00MTgwLWE1NjgtYmRkYTBmZGYxZTE0IiwiYXVkIjpbIjFiM2U3MWYyLWUxNGMtNGY0NC1hMWM1LTNkYzg4ZDM5NTJiNSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzExMzQwOSwiaWF0IjoxNzUzMTEyNTA5LCJqdGkiOiI4ZTMwZTdkMy0wYjdiLTQwMjMtODI3NS0wYjRkMjJmNzQwODUiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIzOGI5Njg3ZS01ZWU3LTQxODAtYTU2OC1iZGRhMGZkZjFlMTQifQ.Up4Mbr6KmqQk1P-ZHf9FswU0bM7EDJMIkb9bEtmZxFXGSUHkbEkqcU3jX0V4R2_m_RrlugmWSuIViO8DHIvwyfU9j8hir6kybCTtRqWcjCLqC3RlhXIMmEhZCvV0WXI6M7s05YYmY0dgkoxOQlg2j4xkuZ1O29CjVNDV5QobNyBpcx1H1P4IRoQ0TO0h8svstbC5-MTmsO6BQdnXpjevccGyb4paXeSCs94AvAR4xq3T6iBmT8GGZaGA9Dq01Ws1QzcLJGC74Ng-oQmsQybnl9vAw1aCrC9VfyiC75NpL8zOGfD81EEMRvJ_V9lM40iZycjH9mglw4ZfOoWIX-Ay6g",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.guidecx.com/manager.project.project_list.ProjectListService/LoadProjectManagersDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Content-Length": "8",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhZjQ0NDJkLTRkZGYtNGE0ZS1hNmQzLTVhY2NlZTMxMmEzNCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMzhiOTY4N2UtNWVlNy00MTgwLWE1NjgtYmRkYTBmZGYxZTE0IiwiYXVkIjpbIjFiM2U3MWYyLWUxNGMtNGY0NC1hMWM1LTNkYzg4ZDM5NTJiNSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzExMzQwOSwiaWF0IjoxNzUzMTEyNTA5LCJqdGkiOiI4ZTMwZTdkMy0wYjdiLTQwMjMtODI3NS0wYjRkMjJmNzQwODUiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIzOGI5Njg3ZS01ZWU3LTQxODAtYTU2OC1iZGRhMGZkZjFlMTQifQ.Up4Mbr6KmqQk1P-ZHf9FswU0bM7EDJMIkb9bEtmZxFXGSUHkbEkqcU3jX0V4R2_m_RrlugmWSuIViO8DHIvwyfU9j8hir6kybCTtRqWcjCLqC3RlhXIMmEhZCvV0WXI6M7s05YYmY0dgkoxOQlg2j4xkuZ1O29CjVNDV5QobNyBpcx1H1P4IRoQ0TO0h8svstbC5-MTmsO6BQdnXpjevccGyb4paXeSCs94AvAR4xq3T6iBmT8GGZaGA9Dq01Ws1QzcLJGC74Ng-oQmsQybnl9vAw1aCrC9VfyiC75NpL8zOGfD81EEMRvJ_V9lM40iZycjH9mglw4ZfOoWIX-Ay6g",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.guidecx.com/manager.project.project_list.ProjectListService/LoadProjectStatusesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Content-Length": "8",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhZjQ0NDJkLTRkZGYtNGE0ZS1hNmQzLTVhY2NlZTMxMmEzNCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMzhiOTY4N2UtNWVlNy00MTgwLWE1NjgtYmRkYTBmZGYxZTE0IiwiYXVkIjpbIjFiM2U3MWYyLWUxNGMtNGY0NC1hMWM1LTNkYzg4ZDM5NTJiNSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzExMzQwOSwiaWF0IjoxNzUzMTEyNTA5LCJqdGkiOiI4ZTMwZTdkMy0wYjdiLTQwMjMtODI3NS0wYjRkMjJmNzQwODUiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIzOGI5Njg3ZS01ZWU3LTQxODAtYTU2OC1iZGRhMGZkZjFlMTQifQ.Up4Mbr6KmqQk1P-ZHf9FswU0bM7EDJMIkb9bEtmZxFXGSUHkbEkqcU3jX0V4R2_m_RrlugmWSuIViO8DHIvwyfU9j8hir6kybCTtRqWcjCLqC3RlhXIMmEhZCvV0WXI6M7s05YYmY0dgkoxOQlg2j4xkuZ1O29CjVNDV5QobNyBpcx1H1P4IRoQ0TO0h8svstbC5-MTmsO6BQdnXpjevccGyb4paXeSCs94AvAR4xq3T6iBmT8GGZaGA9Dq01Ws1QzcLJGC74Ng-oQmsQybnl9vAw1aCrC9VfyiC75NpL8zOGfD81EEMRvJ_V9lM40iZycjH9mglw4ZfOoWIX-Ay6g",
                "content-type": "application/grpc-web-text",
                "x-grpc-web": "1",
            },
            data="AAAAAAA=",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "POST",
            "https://k2-web.guidecx.com/manager.project.project_list.ProjectListService/LoadActiveMilestonesDropdown",
            headers={
                "Accept": "application/grpc-web-text",
                "Content-Length": "8",
                "Host": "k2-web.guidecx.com",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhZjQ0NDJkLTRkZGYtNGE0ZS1hNmQzLTVhY2NlZTMxMmEzNCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhdXRoLmd1aWRlY3guY29tIiwic3ViIjoiMzhiOTY4N2UtNWVlNy00MTgwLWE1NjgtYmRkYTBmZGYxZTE0IiwiYXVkIjpbIjFiM2U3MWYyLWUxNGMtNGY0NC1hMWM1LTNkYzg4ZDM5NTJiNSIsImd1aWRlY3guY29tIl0sImV4cCI6MTc1MzExMzQwOSwiaWF0IjoxNzUzMTEyNTA5LCJqdGkiOiI4ZTMwZTdkMy0wYjdiLTQwMjMtODI3NS0wYjRkMjJmNzQwODUiLCJ2ZXJzaW9uIjoiVjIiLCJyb2xlIjoiQURNSU4iLCJ2aWV3TWVtYmVySWQiOiIzOGI5Njg3ZS01ZWU3LTQxODAtYTU2OC1iZGRhMGZkZjFlMTQifQ.Up4Mbr6KmqQk1P-ZHf9FswU0bM7EDJMIkb9bEtmZxFXGSUHkbEkqcU3jX0V4R2_m_RrlugmWSuIViO8DHIvwyfU9j8hir6kybCTtRqWcjCLqC3RlhXIMmEhZCvV0WXI6M7s05YYmY0dgkoxOQlg2j4xkuZ1O29CjVNDV5QobNyBpcx1H1P4IRoQ0TO0h8svstbC5-MTmsO6BQdnXpjevccGyb4paXeSCs94AvAR4xq3T6iBmT8GGZaGA9Dq01Ws1QzcLJGC74Ng-oQmsQybnl9vAw1aCrC9VfyiC75NpL8zOGfD81EEMRvJ_V9lM40iZycjH9mglw4ZfOoWIX-Ay6g",
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
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Next-Action": "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Next-Action": "9cb89b8dd11737a7e53fe43e87eeac4bc9f9c181",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
            "/v2/c68g69wqqoz7s703zulqktnhxess",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Priority": "u=5, i",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
            "/v2/TESTETSETSETSETSETESTSETESETESTSETSET",
            headers={
                "Accept": "image/avif,image/webp,image/png,image/svg+xml,image/*;q=0.8,*/*;q=0.5",
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Priority": "u=5, i",
                "Referer": "https://arches.guidecx.com/v2/projects",
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
                "Cookie": "_gcx.theme=default; _gcx.project-sort-by=%5B%7B%22id%22%3A%22project-name%22%2C%22desc%22%3Afalse%7D%5D; intercom-session-crui9hdm=MFlzRnJGT2tmTVZPbUZ0YWIyL2lEWUdIbEdxQUNkd3RYanZPcDFsOVpzb240NEZuRHhZTjJ1eHlzTkpFbmhFOWcvUTd3d0tRMFlCbllaL0Nkc1c2aDEyc3R5Zjd0aHc0KzhreGdYRFc1VU09LS1UZGFJQVFXY0xTR0RVazBhalZhaW5nPT0=--a013d39cd90dcc771c19b2ebe7c39a7da2a2e772; intercom-device-id-crui9hdm=00694d8a-f30d-415e-bfa7-4779236202f4; _gcx.nav-expanded=true; s_fid=2E4F0E132D4735EF-3D5439C2555C8991; s_cc=true; s_sq=guidecxprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526link%253DProjects%2526region%253DBODY%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Farches.guidecx.com%25252Ftasks%2526oid%253DProjects%2526oidt%253D3%2526ot%253DSUBMIT; _gcx.session.v2=Fe26.2*1*f7b0476beb29039d05d977e2013b04454dc97760c933d2ebc656c4ed4241a498*kk6NITiuTSL_9ZW0pquuWQ*dog0H5pLwU7JXM2biGYYY_4e1k8XnUwne5hPvNKFmQEYF93u_FtzqGy8pPgZrHPPG1CKUVa8OO9rJyDj7rOp90GcN4ZpMQIKHXv0ltxvygfXTdpBd7CemtfCbY_UoUDM9BFUM9kJp9aBc9htkk24v4AibcI9cpmcpE2e87fwNgUDER8sQ8YmzAXT32wTCqCM_D67KrFkW1UFOsBpA-CTtj3W9I6ESp3IpZMJ91n2wG5O0ZDJqIUeDwNjHDT167Upo6qUDR4yz25vhuvWzn8CcaL3fsO6sUSqaSs24ZBKzedEWzYHRwzigHmZBqUn_OJ-g9ukzOUYSPlY0ZInyJ-IbuG1gDU8Vt31v16RLCcb2PqupHj9mqqRR9uajJ9xUm4ysAtndW31vsjaOUvEnB-1or5GNLmxPrD8BNvtkuaJRILMq22k3oWmLyb7X4Xa3GhLa3-oXAv-yZUr6QQKCinnAIGtsA_Wy9p-TT4v5ZDsG2dd9fG0OkkdBTA2GZr2fEDNBorgHFe6D8D_SfhUah8NUjDVsjV22Y-90FLlISerdGYDXIzdqbzQWvc40XosoDY8nwTvBavfTlM3LTWsxn0MEYEOfwvNjVZ3agThc3a4UAPw6853aMBQa_V8_YS0210002Axq4Qf7im4uxF22Ecu4WdWrkiA-15fJyk0XkAl8gHDArmrBsQrfblqOA1WH136F8uRqnJbiNrU8ru_SKHlbNB5PVeLKwzLjBddPHj3q5o54jCOdebjWCdB3NdnJkLW8NP2fq2EdYlu5RPET6GgUMJR6PMvxfueNjTQ_Bn2j1WlAJnPLx5RZKARMguwvWjIrujM_1pNxFEuXA0SM2fKpfsCZz1SMYGgk-dBTIVrxAZqLTZ85KXghpFGZVL1rxzpIyLpJe68ZIgTcz8tHoPA76ow-bTxkXHZ7BJ4rXhFgjrKDc4zmVXcRjVwsdRy-r_19RzQpfBZwHh67_bKmMdZVFwpeljxaKrnl09n9YxqZxoESDESEo-sBf193ak3qkcSlr9JttoSzvWwmp9fvtCJN_TkEU1L0kYKiSlk84qnlZG6D4CyMErnXmJUlrwXtZq3Wsw3YPuQ6BWDL-z0QyM9iaGMiQd6SXFLvTMfsM1PykBrtaJGpR4fwvpXoyf-i2-wcXcZGGgHa7f6y-Uprmuhnh-0v2XEeei0UyVvunSqNLl1ojQWpVCh7B-zLmF7Z62nygSLl0f2ghRWGXLTI6h4PLKJm4iqe1vn_lP5q-l3LuL3HWHNrJeSK2aaodDwmIJx0e3GT0c3H6t4N2_3tBB_NWh5L5B_rlDND0MXLEk3JQbF83WA9JqU5VL-1zXqpQdPeQPx-p5WuWTCE2GwYHag-vXTVeImlQ1PkO5BGay1w5y989TdwTXGUGzI-6U_zbLK7TME5LzhqU70FWtDKOt32ayFnzYJmuOB-oJJMsR-A_botjCrQMBnlwiq_HO7efogVEcW5-vNseFXfqiS7W6HYQhhPwJLOIkXbcd7vK7wGXQ28bpNEFVNR0-5itgw7CzPhqMdGSYT3fyjaoc6a-1dAg*1754322110155*c3abc80735910da51a19c73f9155d592435173f4ec32473bc220ece9b6858385*9g7JVoNy1dBL1_G_0CVQhGp1L8VV38Klqrsex_GZrT0~2; _gcx.session.v1=Fe26.2*1*4c17eee65213ab66fcd6c386e3e70b2a0cc1b1c011402e257438429f8a8db094*6sySKPmYgo7nrokHkMizQg*pmFCBKbCHgq2bHF83VYA3UtqEnQ2McCJ_ERsAHN1PMq3dCWtS1QQkZTyDm_vzHKCZWvcEXa_I2tEUT-toeGCneXxWObp49UlQompjUnaYwDFBuUcSvUxuFlfkjTHq95p6gKRPT-FZ3RyHdIXnLBlE7wZ3Yiacp5GOe0XYs3MgYaESrLYq3MkH1LFwgxlEDLwY4nVRYxqZcdNGIKGsaitO4lwvnlDu1utZDZJMVsx6k5pP_SboWpQZDK5mS5jLdyHue5dXcr2cvTQMcZsbTNE6PQW951xEIWxUfWg7cHb9pxmLYmM8PSzhAr4TqtPGhJ87R4YrEYZXrFnQlP-PktEbc2oPhseppYejZG9Cjf76CsVOF9TUy8RMh4xjUNKn87l3oYVFY1y5kDxp2_68gIu_LoI-Gmmfez_Pwrk18SRrzIS-zuXknRi6xwCxxlhlMbbpLCuDGt-jNLCdSKHOnGwBGrTNoCL6t1LvC1xwGzQ6iJHY1NjP6SovpAQCMcfNAbyFbMt4LKceRI8-7t_KwyX_Ux8l4qO7CCJISLx9NIlo0cl7-qSim175XvUUwKRuxtgZi-eL4_7vYmqPnxM7bOk3MRrzDg2pnXojsxUmiQkPAnJDDceUd2NNf6feIQ_KSuI2DTtFw8v1gQjhgmRgiqXR6CnMNzR0kpi1lpFuz6V5CEIyFxJoIuLjD6M4uqHiyxxoHogZLUDklrDBQy1etA1CMKlYdOlWx6rShUPx_hgE0McwGFQal4Gk2nAY6Z1Yn7A_iPLjQavAs8xaW2OZBCks01ngMiF45A4FHByjbStFFY3x4q8PaDr2zClzItwlvTs*1754322110452*9ae036de5b57de4f084e46c20001220f767a2f49dc1fe627919d117f4ef43658*ZheR0wJzMOkwUnXDzD-zn3ud3vSbCv5lzUhO9YHMt3A~2",
                "Host": "arches.guidecx.com",
                "Next-Action": "d460095e80259ffd0e3377f81ff6d3eb70666bda",
                "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(protected)%22%2C%7B%22children%22%3A%5B%22v2%22%2C%7B%22children%22%3A%5B%22projects%22%2C%7B%22children%22%3A%5B%22(list)%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fv2%2Fprojects%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%2C%22navigation%22%3A%5B%22__DEFAULT__%22%2C%7B%7D%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
                "Origin": "https://arches.guidecx.com",
                "Priority": "u=4",
                "Referer": "https://arches.guidecx.com/v2/projects",
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


if __name__ == "__main__":
    run_single_user(GlobalProjects)
