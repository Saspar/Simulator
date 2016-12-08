screen_w, screen_h = 800, 600
fps = 60
TILESIZE = 50
score = [0]

class State_switcher(Exception):
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value
    def ___str___(self):
        return repr(self.value)