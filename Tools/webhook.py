import json
import requests
from Config.Env_config import web_hook_url


def web_hook(text, mobile):
    url = web_hook_url
    program = {
        "msgtype": "text",
        "text": {"content": text},
        "at": {
            "atMobiles": mobile,
            "isAtAll": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    requests.post(url, data=json.dumps(program), headers=headers)


# class WebHook:
#
#     # def __init__(self):
#     #     self.url = web_hook_url
#
#     @staticmethod
#     def web_hook(text, mobile):
#         url = web_hook_url
#         program = {
#             "msgtype": "text",
#             "text": {"content": text},
#             "at": {
#                 "atMobiles": mobile,
#                 "isAtAll": False
#             }
#         }
#         headers = {'Content-Type': 'application/json'}
#         requests.post(url, data=json.dumps(program), headers=headers)
