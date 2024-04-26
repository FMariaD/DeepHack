# MIPTHack

### Hello :wave:

This is the repo with our solution for DEEPHACK.AGENTS :space_invader: 

Using **GigaChat** :moyai: and **GigaChain** :link: for **Scientific Applications** :rocket: 

Link to our [Google Drive](https://drive.google.com/drive/folders/1fNpjzK7XUh54LPNTFT7cmecvHg-BtKiQ).

UI is presented in the form of a Telegram bot - [@GigaBrainChatbot](https://t.me/GigaBrainChatbot) (not uploaded to the server yet :pensive:). \
Bot can search for articles in the scientific fields of user's interest and answer questions about the articles found. All articles are taken from the https://arxiv.org.

Sorry last minute we changed repo due to some issues :(
If you want to see commit history, please check [old_repo](https://github.com/Maximilean/MIPTHack)

### Installation
To install dependencies run
```
pip install -r requirements.txt
```
or if you encounter a conflict with versions, run:
```
pip install -r requirements_with_versions.txt
```

### Usage

1. create file .env with API key and Telegram token with names `GIGACHAT_TOKEN` and `BOT_TOKEN` respectfully
2. start redis server
3. run `bot.py` file
