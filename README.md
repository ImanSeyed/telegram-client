# telegram-client
A simple telegram client with some fun feature such as LMGTFY, Google Translate, Spam and so on.
## Installation
### Requirements
First of all, you have to install requirements. Easily run this command to install requirements in directory of repo:
```
$ pip3 -r requirements.txt
```
### Setup your client
You have to create `config.ini` in `client` directory to use `client.py`. For more detail, look at pyrogram documentation:
https://docs.pyrogram.org/topics/config-file

## Usage 
Enter to `client` directory in root of repository and simply run `client.py` with `python3`
```
$ cd client 
$ python3 client.py
```

## Commands
| Command | Description |
| --- | --- |
| !g search | LMGTFY |
| !kick | Kick the user that you replied to |
| !translate lang | Translate replied text to 'lang' language |
| !spam num text | Send text for num times |

## Add command and message
There is no obstacle for adding new command. Just edit `messages.json`. 
