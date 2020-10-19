# json.dumps() => python 对象转化为 json
# json.loads() => json数据转化为python对象

import json

jsondata = '''
{
"Uin":0,
"UserName":"@c482d142bc698bc3971d9f8c26335c5c",
"NickName":"猫九大大",
"HeadImgUrl":"/cgi-bin/mmwebwx-bin/webwxgeticon?seq=500080&username=@c482d142bc698bc3971d9f8c26335c5c&skey=@crypt_b0f5e54e_b80a5e6dffebd14896dc9c72049712bf",
"DisplayName":"",
"ChatRoomId":0,
"KeyWord":"che",
"EncryChatRoomId":"",
"IsOwner":0,
"List": [
    {
    "UserName":"小帅b",
    "sex":"男"
    },
    {
    "UserName":"小帅b的1号女朋友",
    "sex":"女"
    },
    {
    "UserName":"小帅b的2号女朋友",
    "sex":"女"
    }]
}
'''

myfriend = json.loads(jsondata)
print(myfriend.get('NickName'))
for item in myfriend.get('List'):
    print(item.get('UserName'))