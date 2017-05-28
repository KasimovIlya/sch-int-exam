# coding=utf-8
import requests
import json
from firebase import firebase


class User:
    sex = ''
    l_name = ''
    f_name = ''

    def __init__(self, city, l_name, f_name):
        self.sex = sex
        self.l_name = l_name
        self.f_name = f_name


url = "https://api.vk.com/method/groups.getMembers?group_id=98666498&fields=sex"
firebase_url = "https://exam-76a95.firebaseio.com/"

information = requests.get(url).text
dic = json.loads(information)
print(dic)


allUsers = []

if "response" in dic:
    people = dic["response"]
    if "users" in people:
        people_list = people["users"]

        for user in people_list:
            if "sex" in user and "first_name" in user and "last_name" in user:
                sex = user["sex"]
                l_name = user["last_name"]
                f_name = user["first_name"]

                allUsers.append(User(sex, l_name, f_name))
# print(allUsers)


db = firebase.FirebaseApplication(firebase_url)

for user in allUsers:
    print(user.__dict__)
    db.post("/users", user.__dict__)

