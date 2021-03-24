import os
import time
import json
os.chdir("bot")

if "first_launch.txt" in os.listdir():
    os.remove("first_launch.txt")
    with open("config.json", "r") as r:
        data = json.load(r)
        print("Hello! I detected this is first launch, great! Configuration process will start in few seconds\nIn the meantime, go to https://github.com/statboi/EZbot readme.md file will be your guide, if you won't know what to insert.")
        time.sleep(5)
        print("Ok, first i will install required pip packages, please wait...")
        time.sleep(2)
        os.system(r"pip install -r requirements.txt")
        print("")
        print("Please insert your bot token below (Go to docs mentioned above for more info)")
        token = input()
        print("Cool, now enter prefix you want your bot to use.")
        prefix = input()
        print("OK, who is the creator of the bot? This will be used as creator name for example in help menu, or in message footers (e.g. Created by [name], powered by EZbot).")
        name = input()
        print("Fine! This is kinda it, token will be used as a key to make this app log in to your bot account, prefix will be prefix, and name will be creator name used in message footers.")
        print("Give me a moment now, i will append your things to config,json file, by the way you can change them and customize bot later by going into this file.")
        for p in data["botSettings"]:
            datatowrite = {'config':[{'token': f'{token}', 'prefix': f'{prefix}', 'authorName': f'{name}', 'readReadmeTxt': 'forMoreInfo'}], 'botSettings':[{"botStatus": f'{p["botStatus"]}', 'welcomeMessageOn': f'{p["welcomeMessageOn"]}', 'welcomeMessage': f'{p["welcomeMessage"]}', 'welcomeMessageChannelId': f'{p["welcomeMessageChannelId"]}', 'welcomeDmOn': f'{p["welcomeDmOn"]}', 'welcomeDm': f'{p["welcomeDm"]}', 'leaveMessageOn': f'{p["leaveMessageOn"]}', 'leaveMessage': f'{p["leaveMessage"]}', 'leaveMessageChannelId': f'{p["leaveMessageChannelId"]}'}]}
            w = open(r"config.json", "w")
            json.dump(datatowrite, w, indent=4)
            yorn = input("Do you want to start your bot now? Enter 'y' or 'n' ")
            if yorn.lower()=="y":
                print("OK, i will launch it in 3 seconds...")
                time.sleep(3)
                os.system("python main.py")
            else:
                print("OK, run this file when you will want to run your bot. Bye!")
                exit()
else: os.system("python main.py")
