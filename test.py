import requests
import json

f  = requests.post("http://paas.bking.com/login/?c_url=http%3A//paas.bking.com/platform/",data=json.dumps({"username": "admin","password":"blueking"}))
print(f.text)



# url = "http://paas.bking.com/api/c/compapi/cc/get_app_by_user_role/"
# param = {
#     "app_code": "cdn-refresh",
#     "app_secret": "337d1ea4-8137-405e-8dfd-58a0d39e9b1d",
#     "bk_token": "ZihIsSNfM3FG21OEavbfNaWZPSu_ldjPeN9oKXkTd5U",
#     "user_role": "Maintainers,ProductPm"
# }

url = "http://paas.bking.com/api/c/compapi/cmsi/send_mail/"
param = {
    # "username": "admin",
    "sender": "monitor@wonhigh.cn",
    # "is_data_base64": True,
    "app_code": "cdn-refresh",
    "app_secret": "337d1ea4-8137-405e-8dfd-58a0d39e9b1d",
    "content": "<html>Welcome to Blueking</html>",
    "receiver__username": "hand",
    "bk_token": "HuP3iD4qKzReMGc2p8ADiwmey_7_clAwLl60yX-KcHI",
}
ret = requests.post(url, data=json.dumps(param))
print(json.dumps(ret.json(), ensure_ascii=False,  indent=4))