import sys
import os
from clinput import get_user_input
from logger import Logger

debug_mode = False
verbose_mode = False
logger = None

def show_menus():
    print("NOTE: all lowercase input is allowed.")
    print("1. put my commit in uatDeployment branch")
    print("type 'stop' to exit!")



def event_loop():
    user_entered = 'start';
    while user_entered != "stop":
        show_menus()

        logger.value(str(get_user_input)).debug()

        user_entered = get_user_input(
            valid_inputs = ["stop","start","deploy"], 
            prompt = "$ ",
            logger = logger)



def app():
    global debug_mode
    global verbose_mode
    global logger

    flags = ''
    for elem in [elem[1:] for elem in sys.argv if elem.startswith('-')]:
        flags+=elem

    if 'd' in flags:
        debug_mode = True
    if 'v' in flags:
        verbose_mode = True

    logger = Logger(debug_mode = debug_mode,
                    verbose_mode = verbose_mode)

    logger.value("app" + str(logger)).debug()

    event_loop()

if __name__ == "__main__":
    app()
