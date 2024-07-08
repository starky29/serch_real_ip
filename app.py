import os, re, requests


def serch_ip(user, file):
    last_ip = []
    serch = f"TLS: Username/Password authentication succeeded for username '{user}' [CN SET]"
    with open(file) as f:
        for str in f.readlines():
            if serch in str:
                ip_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", str)
                if not ip_list:
                    continue
                ip = ip_list[0]
                if ip not in last_ip:
                    last_ip.append(ip)
    return last_ip


def location(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
    if response.status_code == 200:
        result = response.json()
        return result['query'], result['country'], result['regionName'], result['city']
    else:
        return "Oops"


user = input('Введите пользователя: ')
files = os.listdir()
for file in files:
    if file.endswith('.log'):
        ips = serch_ip(user, file)
        for ip in ips:
            print(location(ip))




