from cocos.euclid import *
from cocos.actions import *
from cocos.director import director
from pyglet.window import key
import math

class CustomJump(IntervalAction):

    def init(self, thief_type=None):

        if thief_type == 'fat':
            self.position = (500, 0)
            self.height = 100
            self.duration = 10
            self.jumps = 7

        elif thief_type == 'small':
            self.position = (500, 0)
            self.height = 100
            self.duration = 10
            self.jumps = 7

        elif thief_type == 'tall':
            self.position = (500, 0)
            self.height = 100
            self.duration = 10
            self.jumps = 7

    def start( self ):
        self.start_position = self.target.position
        self.delta = Vector2(*self.position)

    def update(self, t):
        y = self.height * abs( math.sin( t * math.pi * self.jumps ) )
        y = int(y+self.delta[1] * t)
        x = self.delta[0] * t
        self.target.position = self.start_position + Point2(x,y)
        print self.target.position, ':', director.scene.catcher.position

    def __reversed__(self):
        return CustomJump( (-self.position[0],-self.position[1]), self.height, self.jumps, self.duration)

    def step(self, dt):
        self._elapsed += dt
        try:
            self.update( min(1, self._elapsed/self.duration ) )
        except ZeroDivisionError:
            self.update(1.0)

    def done(self):
        return self._elapsed >= self.duration

class CustomMove(Move):

    def step(self, dt):
        keys = director.scene.keys
        catcher = director.scene.catcher
        if keys[key.LEFT] and catcher.position[0] > 300: 
            catcher.position = (catcher.position[0] - catcher.mov_rate, \
                                    catcher.position[1])

        elif keys[key.RIGHT] and catcher.position[0] < 500:
            catcher.position = (catcher.position[0] + catcher.mov_rate, \
                                    catcher.position[1])
