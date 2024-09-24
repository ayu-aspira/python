'''
Created on Nov 14, 2021

@author: Allen Yu
'''

islogging = True

'''
class version
'''

class LoggingBase:

    def __getattribute__(self, item):
        attr = super(LoggingBase, self).__getattribute__(item)

        def decorate_func(*args):
            print('-----------log input parameter')
            print('class :' + str(self) + ';method:' + str(attr.__func__))
            for arg in args:
                print('parameter: ' + arg)
            print('----------end log input parameter')
            rval = attr.__func__(self, *args)
            print('----------the result log:' + str(rval))
            return rval

        return decorate_func if islogging is True else attr

    
class MyClass2(LoggingBase):

    def __init__(self, a):
        self.a = a
        
    def print_me(self, b, x):
        print('myClass2' + b + ',' + x)


class MyClass1(LoggingBase):

    def print_some_thing(self, a):
        print('myClass1' + a)
        return MyClass2('app')     

'''

Simple version
with no class involved

'''    

  
def log(func, *args): 

    def inner_no_log():
        return func(*args)
    
    def inner_with_log():
        print('----- logging function name----' + str(func))
        for arg in args:
            print('parameter:' + arg)
        print('----- end logging parameter')
        rvalue = func(*args)
        print('-----log result:' + str(rvalue))
        return rvalue

    return inner_with_log() if islogging is True else inner_no_log()


def do_something_func(a, b):
    print('print:' + a + b)

    
def do_something_func2(a):
    print('print me' + a)
    
    
if __name__ == '__main__':
    MyClass1().print_some_thing('hello').print_me('world', '!')
    MyClass2('test2').a
    
    print('-----------------')
    
    log(do_something_func, 'hello', 'world')
    log(do_something_func2, 'world2')
    
