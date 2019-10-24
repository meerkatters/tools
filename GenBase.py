"""
Written by Nicolette Lewis
at University of Washington
for CESG 505: Engineering Computing
Date: October 15, 2019
Homework 2
Problem 1 - baseconverter.py
Program Description:
class GeneralBase()

"""
import re
import p2functions as p

class GenBase(object):

    def __init__(self, b=2,v=0):

        v=p.to_base(10,str(v))        ## values are stored in base ten regardless of b....
        v=int(v)
        self.val = { 'base' : b , 'value' : v}
        self.CheckBase()

    def __str__(self):
        s='{} base {}'.format(self.val['value'],self.val['base'])
        return s

    def __repr__(self):
        __repr__=p.to_base(self.val['base'],self.val['value'])
        return __repr__(self)

    def __add__(self,other):
        int1 = (self.val['value'])
        int2 = (other.val['value'])
        ans=p.to_base(self.val['base'],int1+int2)
        return GenBase(self.val['base'],ans)

    def __sub__(self,other):
        int1 = (self.val['value'])
        int2 = (other.val['value'])
        ans = p.to_base(self.val['base'], int1 - int2)
        return GenBase(self.val['base'], ans)

    def __mul__(self,other):
        int1 = (self.val['value'])
        int2 = (other.val['value'])
        ans = p.to_base(self.val['base'], int1 * int2)
        return GenBase(self.val['base'], ans)

    def __floordiv__(self,other):
        int1 = (self.val['value'])
        int2 = (other.val['value'])
        ans = p.to_base(self.val['base'], int1 // int2)
        return GenBase(self.val['base'], ans)


    def __mod__(self,other):
        int1 = (self.val['value'])
        int2 = (other.val['value'])
        ans = p.to_base(self.val['base'], int1 % int2)
        return GenBase(self.val['base'], ans)

    def __eq__(self,other):
        if not isinstance(other,GenBase):
            return NotImplemented
        return (self.val['value']==other.val['value'])

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    @classmethod
    def value(self):
            return (self.val['value'])

    def base(self):
            return (self.val['base'])


    def ChangeBase(self,x):
            v=str(self.val['value'])

            self.val['base']=x

    def CheckBase(self):
        SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        inval=str(self.val['value'])
        base=self.val['base']
        digits = re.findall(r'\d', str(inval))
        empty = []
        if digits != empty:
            minbase = max(digits)
            if base < (int(minbase) + 1):
                if inval.index(minbase) > 0:
                    outval1 = inval.replace(inval[inval.index(minbase) - 1],
                                            str(int(inval[inval.index(minbase) - 1]) + 1))
                    outval = outval1.replace(str(minbase), '0')
                else:
                    outval = inval.replace(str(minbase), '10')

                p = 'converting {}{} to a number that can be represented in base {}, {}'
                print(p.format(inval, str(base).translate(SUB), str(base), outval))
                self.val['value'] = outval

