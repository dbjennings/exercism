from __future__ import division
from math import gcd

class Rational:
    def __init__(self, numer, denom):
        n = -numer if denom<0 else numer
        d = -denom if denom<0 else denom
        g = gcd(n,d)
        self.numer = int(n/g)
        self.denom = int(d/g)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        n = (self.numer*other.denom)+(other.numer*self.denom)
        d = self.denom*other.denom
        return Rational(n,d)

    def __sub__(self, other):
        n = (self.numer*other.denom)-(other.numer*self.denom)
        d = self.denom*other.denom
        return Rational(n,d)

    def __mul__(self, other):
        return Rational(self.numer*other.numer,self.denom*other.denom)

    def __truediv__(self, other):
        return Rational(self.numer*other.denom,self.denom*other.numer)

    def __abs__(self):
        return Rational(abs(self.numer),abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer**power,self.denom**power)

    def __rpow__(self, base):
        return base**(self.numer/self.denom)