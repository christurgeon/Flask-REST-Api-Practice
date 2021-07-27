from flask.wrappers import Response
import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes":10, "views":10, "name":"bruh moment"},
    {"likes":100, "views":1000, "name":"how to code"},
    {"likes":1000, "views":100, "name":"how to make vid"}
]

for idx, d in enumerate(data):
    r = requests.put(BASE + "video/" + str(idx), d)
    print(r.json()) 

input()
r = requests.patch(BASE + "video/2", {"views" : 99, "likes" : 999})
print(r.json())

input()
r = requests.delete(BASE + "video/2")
print(r.json)

input()
r = requests.get(BASE + "video/2")
print(r.json())


# input()
# r = requests.get(BASE + "video/0")
# print(r.json())

# input()
# r = requests.get(BASE + "video/6")
# print(r.json())
