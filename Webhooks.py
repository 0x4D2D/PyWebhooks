import time
from discord_webhook import DiscordWebhook

print("Webhooks")
print("type help to show all commands")

url = "none"
text = "none"
username = "PyWebhooks"
ariurl = "https://cdn.discordapp.com/attachments/753041003945918547/844328074854006784/download.jpg"

while True:
    jerma = input("~")
    xset = jerma.split(" ")
    textafter = ""
    for i in range(len(xset)):
        if i > 0:
            textafter = textafter + xset[i] + " "

    if xset[0] == "url":
        print("Updated Bot Url target!")
        url = xset[1]

    if xset[0] == "text":
        text = textafter

    if xset[0] == "send":
        print("Sent Message " + "\"" + textafter + "\"")
        webhook = DiscordWebhook(url=url, content=textafter, username=username, avatar_url=ariurl)
        response = webhook.execute()

    if xset[0] == "once":
        print("Sent Message")
        webhook = DiscordWebhook(url=url, content=text, username=username, avatar_url=ariurl)
        response = webhook.execute()

    if xset[0] == "repeat":
        print("Sending " + xset[1] + " Messages")
        webhook = DiscordWebhook(url=url, content=text, username=username, avatar_url=ariurl)
        for i in range(int(xset[1])):
            print("Sent Message")
            response = webhook.execute()

    if xset[0] == "slow":
        print("Sending " + xset[1] + " Messages with delay " + xset[2])
        webhook = DiscordWebhook(url=url, content=text, username=username, avatar_url=ariurl)
        for i in range(int(xset[1])):
            print("Sent Message")
            response = webhook.execute()
            time.sleep(int(xset[2]))

    if xset[0] == "username":
        print("Set bot username")
        username = xset[1]

    if xset[0] == "liburl":
        print("Set bot profile picture")
        ariurl = xset[1]

    if xset[0] == "help":
        print("commands:")
        print("text: sets the text of the message")
        print("once: sends one message from text")
        print("send <message>: send one message that you have to put after the command")
        print("repeat <times>: sends the text x amount of times")
        print("slow <times> <delay>: repeat but with a delay")
        print("username <text>: sets the bots username")
        print("liburl <resource_url>: sets the bots profile picture")
        print("url <url>: Sets the url that the bot targets")

