import os
import glob

userID = '0'
file_list = glob.glob(os.path.join("src/files/poems","*.txt"))


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
#with open("src/files/poems/*.txt") as file:
#    messages = [line.strip() for line in file]
for file_path in file_list:
    messages.append(line.strip() for line in file_path)
picList = []
for file in os.listdir("src/pics"):
    if file.endswith(".png") or file.endswith(".jpg"):
        picList.append('src/pics/{}'.format(file))
ballReplies = []
with open("src/files/8ballReplies.txt") as file:
    ballReplies = [line.strip() for line in file]
