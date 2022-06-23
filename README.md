# TextMotes
A software for making you express your emotions without any trouble. You can use pre-configured emote codes anywhere you want. Just put configured phrase beneath `;` characters and magic will happen.

# Example
`;smile;` will produce 🙂

`;heart;` will produce ❤

`;like;` will produce 👍

# Configuration
You can configure each phrase for each emote, add and remove them simply in configuration file.
Default configuration:
```
updown = 🙃
heart = ❤
smile = 🙂
proud = 😁
wink = 😉
angel = 😇
think = 🤔
throw = 🤮
cowboy = 🤠
like = 👍
sleep = 😴
fright = 😬
shh = 🤫
faceless = 😶
swag = 😎
susp = 🧐
tear = 😢
sad = 😕
angry = 😡
skull = 💀
love = 😍
tong = 😛
cry = 😭
party = 🥳
```

# Controlling the software
Since all is working in background, here is how you can controll the program for your needs.<br />
`;quit;` - shutdown the software<br />
`;restart;` - restart the software<br />
`;emotes;` - list all loaded emotes<br />

# Running TextMotes on system startup
You can make TextMotes launching itself after every reboot to not bother to do it later.
First solution is:
> Press WIN + r and type shell:startup. When the directory will appear, paste here shortcut to the program.

Second solution is:
> Launch "Registry Editor" and go to "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run", then create new entry containing path to TextMotes executable as value.
