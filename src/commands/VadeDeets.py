import os
userID = '0'


def boboTag(mess):
    if mess == "BOBO MO":
        mess = 'BOBO MO <@{!s}>'.format(userID)
        return mess
    return mess


def findBobo(words):
    for word in words:
        if word == "bobo":
            return True
    return False


messages = []
with open("src/files/curse.txt") as file:
    messages = [line.strip() for line in file]
picList = []
for file in os.listdir("src/pics"):
    if file.endswith(".png") or file.endswith(".jpg"):
        picList.append('src/pics/{}'.format(file))
ballReplies = []
with open("src/files/8ballReplies.txt") as file:
    ballReplies = [line.strip() for line in file]
