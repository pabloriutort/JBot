from decorators import reply, text


def to_text(a_list):
    """Returns list as string
    """
    return " ".join(a_list)
    
@text
def hello(bot, args):
    """Salute function
    Without decorator to see what happens...
    
    Returns a string as a salute message
    """
    return "Hello sir, welcome"


@text
def send_text(bot, args):
    return "Text without citing. You said: {0}".format(to_text(args))


@reply
def reply_text(bot, args):
    return "Example of citing (only visible with more people in chat)"

