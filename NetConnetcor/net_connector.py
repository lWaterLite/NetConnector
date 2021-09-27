import requests
from lxml import etree
from os import system

# 打开xml
fp = open('network.xml', 'r', encoding='utf-8')
tree = etree.parse(fp)

# 读取数据
account = tree.xpath('//account/text()')[0]
password = tree.xpath('//password/text()')[0]
yys_id = tree.xpath('//yys/text()')[0]

fp.close()

yyd = ('', 'mobile', 'unicom', 'telecom')

# UA伪装和引用定义
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Referer': 'http://202.117.144.205:8601/snnuportal/userstatus.jsp'
}


# 表单数据
data = {
    'sourceurl': 'null',
    'account': account,
    'password': password,
    'yys': yyd[int(yys_id)-1],
    'issave': ''
}

login_url = 'http://202.117.144.205:8601/snnuportal/login'  # 登录链接
url = 'http://202.117.144.205:8601/snnuportal/logoff'   # cookie获取
session = requests.session()

page_text = session.get(url=url, headers=headers).text

login_task = session.post(url=login_url, headers=headers, data=data).status_code

print(login_task)

system('pause')