import os
import glob

userID = '0'
file_list = glob.glob(os.path.join(os.getcwd(),"src/files/prompts","*.txt"))


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
for path in file_list:
    with open(path) as file:
        lines = file.readlines()
        for line in lines:
            messages.append(line)

picList = []
for file in os.listdir("src/pics"):
    if file.endswith(".png") or file.endswith(".jpg"):
        picList.append('src/pics/{}'.format(file))

cardList = []
for file in os.listdir("src/cards"):
    if file.endswith(".png") or file.endswith(".jpg"):
        cardList.append('src/cards/{}'.format(file))
cardMap = [x.replace("src/cards/", "").replace(".png", "").replace(".jpg", "").lower() for x in cardList]

ballReplies = []
with open("src/files/8ballReplies.txt") as file:
    ballReplies = [line.strip() for line in file]
