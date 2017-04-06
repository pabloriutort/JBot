JBot
===

It is now a dummy bot but it can be so much more.

## Run JBot
Based on Docker as you can see in the Dockerfile.  
For running it you have to do something like:
```
docker build -t j_bot .
docker run -d --env-file <your envs> --name j_bot j_bot
```

[Env file](https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file) it's a file for the Docker container where you can put env variables. The bot token should be named `BOT_TOKEN` and lives in this file.

## Commands
The funny part of this bot is how its commands are defined.  
For now* we have decorators for:
* __@reply__  Uses `udpdate.message.reply_text()`
* __@text__  Uses [bot.send_message()](https://core.telegram.org/bots/api#sendmessage)

_*more will come_

We can use the decorators like this
```
from decorators import text

@text
def send_text(args):
    return "This message will be sent when `/send_text` is called"
```

* `args` contain a list of whatever comes after the command `/command <args>`
* This is a well defined command, the decorator takes care of returning the response with the bot
* All commands must return something