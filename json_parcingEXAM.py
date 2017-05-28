#importimg everything we need
import requests
import json
from firebase import firebase

#introducing classes, in order to save information in the right way
class User:
    sex = ''
    l_name = ''
    f_name = ''

    def __init__(self, sex, l_name, f_name):
        self.sex = sex
        self.l_name = l_name
        self.f_name = f_name

#VK API method and link to our FireBase-DataBase
url = "https://api.vk.com/method/groups.getMembers?group_id=98666498&fields=sex"
firebase_url = "https://exam-76a95.firebaseio.com/"
#making request to VK
information = requests.get(url).text
#putting out our JSON-object
dic = json.loads(information)
#printing^ in order to find the right keys
print(dic)

#making empty list for saving info about users
allUsers = []

# "cutting down" our JSON-object, it is made by finding keys, which contain our Users-info
if "response" in dic:
    people = dic["response"]
    print(people)
    if "users" in people:
        people_list = people["users"]

        #Print, because we want to see that everything is allright
        print(people_list)

        #putting info from JSON-object to our User-class object
        for user in people_list:
            if "sex" in user and "first_name" in user and "last_name" in user:
                sex = user["sex"]
                l_name = user["last_name"]
                f_name = user["first_name"]

                #appending final version of User-class object to our list
                allUsers.append(User(sex, l_name, f_name))

#connecting to our FireBase DataBase
db = firebase.FirebaseApplication(firebase_url)

#putting info we collected to DB
for user in allUsers:
    print(user.__dict__)
    db.post("/users", user.__dict__)

