class Logger:
    debug_mode = False
    verbose_mode = False

    def __init__(self, debug_mode = False, verbose_mode = False ):
        self.debug_mode = debug_mode
        self.verbose_mode = verbose_mode

    def value(self, message:str = ""):
        self.message = message
        return self

    def debug(self):
        if self.debug_mode:
            print(f"DEBUG:{self.message}")
        return self

    def info(self, flag:bool = True):
        if self.verbose_mode and flag:
            print(f"INFO:{self.message}")
        return self
