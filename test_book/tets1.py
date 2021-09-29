import requests

url='http://192.168.1.52/api/saas/ss-crm-provider/wx/auth/login'
data={'account':'17376504323','password':'12345678'}
r=requests.post(url=url,data=data)
print(r.json())
