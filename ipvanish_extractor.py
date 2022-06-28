import os,sys,os.path,re
from requests import session
from colorama import Fore
from datetime import date
file_name_proxy = date.today().strftime('%d_%m_%Y')
green_color = Fore.GREEN
red_color = Fore.RED
os.system('cls')
os.system('title Ipvanish Extractor by hungsaki2003@gmail.com')
ss = session()
def proxy_extractor(cookie_ipvanish):
    proxy_count = 0
    header_ipvanish = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie_ipvanish,
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    api_get_pwd = f'https://account.ipvanish.com/index.php?t=SOCKS5%20Proxy'
    get_pwd = ss.get(api_get_pwd,headers=header_ipvanish).text
    username_account = re.findall(r'Username:</b>(.*?)</p>',get_pwd)[0].strip()
    pwd_account = re.findall(r'Password:</b>(.*?)<br>',get_pwd)[0].strip()
    api_get_proxy = f'https://account.ipvanish.com/index.php?t=Server%20List'
    get_proxy_data = ss.get(api_get_proxy,headers=header_ipvanish).text
    proxy_data = re.findall(r'(.*-.*.ipvanish.com)',get_proxy_data)
    for x in proxy_data:
        if '<td class="StatTDLabel' in x:
            proxy = x.replace('<td class="StatTDLabel">','')+f':1080:{username_account}{pwd_account}'.strip()
            with open(f'{file_name_proxy}_{username_account}.txt','a',encoding='utf-8') as save_proxy:
                save_proxy.write(proxy+'\n')
                print(f'{green_color}{proxy} ===> Extract by t.me/mailngon')
                proxy_count +=1
                if proxy_count == len(proxy_data) - 1:
                    input(f'{red_color}Extract Done !')
                    sys.exit()
print(f'{red_color}              Join me: t.me/mailngon\n\n')
cookie_ipvanish = input(f'{green_color}Enter your account cookie: ')
os.system('cls')
proxy_extractor(cookie_ipvanish)