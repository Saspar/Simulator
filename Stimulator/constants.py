    #CONSTANTS
screen_w, screen_h = 800, 600
fps = 60
TILESIZE = 50

    #VARIABLES
score = [0]
keraspeed = [1]
keraspeed2 = [4]
keratimer = [100]
countdown = [0] #0 = False, 1 = True

class State_switcher(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value
    def ___str___(self):
        return repr(self.value)