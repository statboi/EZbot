# EZbot
EZbot is Python-based Discord bot maker, all you need to do is to host your bot, you don't even need to code, follow instructions, modify config.json file, and customize your bot! This is EZ!

# Remember that EZbot is still in early development, many features are unavailable and this is just a preview version.
# Documentation:
So, i bet you just wanted to make a bot, but you suck in coding and don't want to be lame using BotGhost? So you are in the right place.

# Quickstart
First (when you cloned/downloaded code) you'll need to "launch.py" file in app folder, it will install required packages if ran first time, and ask you for few things:
1. Bot token, you may know what it is, but if you don't - don't worry, i will explain:\
Bot token is just a pass used to login to bot Discord accounts, EZbot is open-source so you can see that it's not stealing your token.\
Where i can get this? Go to [Discord Developer Portal](https://discord.com/developers) and create new application, you should see something like this: \
![image](https://user-images.githubusercontent.com/80977526/112305664-40378080-8c9f-11eb-8be2-9c05504d31ab.png)
It's good, click "Bot" on the left, and click "Add bot" on the right, then click "Yes, do it!" \
![image](https://user-images.githubusercontent.com/80977526/112305835-6fe68880-8c9f-11eb-8f59-6f131bbe427f.png)
Then copy token, and paste it in EZbot.
2. Prefix, it is just string that needs to be placed before command to make it work, i'm sure you know what it is.
3. Author name, you can paste here your nickname, e.g. Maciejka, it will display it in help menu, and on command footers.\
![image](https://user-images.githubusercontent.com/80977526/112306165-ce136b80-8c9f-11eb-920f-a9c8698dcb2a.png)

So yeah, thats basically it, you can choose then do you want to run your bot now, or later
# Protips
1. If you want to add bot to your server, use [this](https://discordapi.com/permissions.html) tool.
2. If you want to change some values you added, or customize your bot, go to bot folder and enter 'config.json' file, there you can customize your bot **remember that this is early alpha version so some features may not work**
3. App will automatically get your bot's username and use it as bot name as on the screenshot above.
4. If you want to copy channel ID's (to enter it to config.json file as welcome/exit messages channels ***this feature is currently unavailable***) go to Discord settings > appearance > advanced > and turn on developer mode, then just right click on a channel and click "Copy ID"
5. To make sure that bot will work properly (welcome and leave messages), enable server members intent in your 'Bot' settings page of your app on Discord Developer Portal
![image](https://user-images.githubusercontent.com/80977526/112535925-1ff5e780-8dad-11eb-977f-13df40ad3e34.png)
