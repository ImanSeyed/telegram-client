# telegram-client
## Installation
### Requirements
First of all, you have to install requirements. Easily run this command to install requirements in directory of repo:
```
$ pip -r requirements.txt
```
### Setup your client
You have to create `config.ini` in `client` directory to use `client.py`. For more detail, look at pyrogram documentation:
https://docs.pyrogram.org/topics/config-file

## Usage 
Just run `client.py`! 
```
$ cd client && python client.py
```

## Commands
| Command | Description |
| --- | --- |
| !g search | LMGTFY |
| !smart | Show ubuntu wiki for asking smart question |
| !ask | Show **DON'T ask to ask** text |
| !flood | Warn to stop flooding |
| !paste | Ask for using CentOS pastebin instead of picture or long text |
| !farsi | Ask for send message in persian |
| !spam num text | Send text for num times |

## Add command and message
There is no obstacle for adding new command. Just edit `messages.json`. 
