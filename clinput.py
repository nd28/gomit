from logger import Logger

def get_user_input(prompt:str = "> ", valid_inputs:list = ["stop","help"], logger = None):
    __doc__ = """why this function
        to discard "enter", "tab", such invalid inputs and ask again til it's valid
        """

    if not isinstance(logger, Logger):
        logger = Logger(False, False)

    logger.value("get_user_input" + str(logger)).debug()

    the_input = ""
    while the_input not in valid_inputs:
        logger.value(f" '{the_input}' is not valid command").info(the_input != "")

        the_input = input(prompt).strip()
    else:
        return the_input

