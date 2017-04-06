from JBot import JBot
import commands as co


jb = JBot()

jb.add_command('hello', co.hello)
jb.add_command('reply', co.reply_text)
jb.add_command('send', co.send_text)
jb.listen()

