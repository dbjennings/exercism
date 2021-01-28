import random
import string

class Robot:
    def __init__(self):
        self.reset()
    
    def reset(self):
        random.seed()
        
        self.name = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
        self.name += ''.join(random.choice(string.digits) for i in range(3))

    #def __init__(self):
    #    self.reset()