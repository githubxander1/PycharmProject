import requests
import json

baseurl = "http://192.168.7.45:32019"

# 加好友
def addFriend(friendid,userid):
    headers = {
        'content-type': 'application/json',
    }

    requestsjson = {
        "friendId": friendid,
        "friendNoteName": "string",
        "friendPhoneNumber": "string",
        "userId": userid,
        "userNoteName": "string"
    }

    r = requests.post(url=baseurl + '/api/userFriend/addFriend', data=json.dumps(requestsjson), headers=headers)
    if r.json()['message'] =='该用户已经是您的好友了':
        deleteFriend(friendid,userid)
    else:
        pass
    return r.json()

# 删除好友
def deleteFriend(friendid, userid):
    json = {
        "friendId": friendid,
        "userId": userid
    }
    r = requests.delete(url =baseurl+'/api/userFriend/deleteFriend', data=json)
    if r.json()['message'] =='该用户不存在此好友':
        addFriend(friendid,userid)
    else:
        pass
    return r.json()


# add = addFriend(1002295,1004535)
# print(add)
delete=deleteFriend(1002295,1004535)
print(delete)

# 发送添加好友请求receivePhoneNumber,receiveUserId,sendUserId,userNoteName,verificationMsg
# def sendAddFriendNotice():
#     headers={
#         'content-type':'application/json'
#     }
#     data={
#             "receivePhoneNumber": 16666666662,
#             "receiveUserId": 1002295,
#             "sendUserId": 1004535,
#             "userNoteName": '昵称',
#             "verificationMsg": '验证'
#     }
#     r=requests.post(url=baseurl+'/api/userFriend/sendAddFriendNotice', headers=headers, data=data)
#     return r.json()
#
# notice=sendAddFriendNotice()
# print(notice)
# def getUserFriend(friendid, userid):
#     json = {
#         "friendId": friendid,
#         "userId": userid
#     }
#     r = requests.delete(url=baseurl+'/api/userFriend/getUserFriend', data=json)
#
# get=getUserFriend(1004535,1002295)
# print(get)
