

def get_params(args, only_args=False):
    """Returns bot and params separately
    
    Gets the message text and splits it into command and text.
    """
    update_msg = args[1].message
    command_parms = update_msg.text.split(' ')[1:]
    if only_args:
        return_val = command_parms
    else:
        # returns bot (args[0]) and whatever params for the command
        return_val = (args[0], update_msg, command_parms)
    return return_val


def reply(func):
    """Command decorator function for text replies
    
    Uses the reply_text function to return the value of wrapped function
    """
    def command_parms(*args, **kwargs):
        bot, update_msg, command_args = get_params(args)
        update_msg.reply_text(func(bot, command_args))
    return command_parms


def text(func):
    """Command decorator function for text replies
    
    Uses the reply_text function to return the value of wrapped function
    """
    def command_parms(*args, **kwargs):
        bot, update_msg, command_args = get_params(args)
        bot.send_message(update_msg.chat_id, func(bot, command_args))
    return command_parms

