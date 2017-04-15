from JBot import JBot
import commands as co
import logging
from os import environ


# set logging
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

if 'DEBUG' in environ and environ['DEBUG'] == '1':
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)


# initialize JB
jb = JBot()

jb.add_command('hello', co.hello)
jb.add_command('reply', co.reply_text)
jb.add_command('send', co.send_text)

jb.listen()

