'''
Created on Nov 19, 2021

@author: allenyu
'''
    
def of(value):
    return Option(value)

class Option:
    is_none = 0
    is_not_none = 1
    
    def __init__(self,x):
        if x is None:
            self.type = Option.is_none
        else:
            self.type = Option.is_not_none
            self.value = x
        
    
    def flat(self):
        def inner_flat(x):
            if isinstance(x, Option):
                return inner_flat(x.get_value())
            else:
                return x
        return inner_flat(self)
        
    
    def get_value(self):
        if self.type == Option.is_none:
            return None
        else:
            return self.value
        
    def __getattribute__(self, item):
        if item in ['type','value','to_string' ,'map','flat','get_value']:
            return super(Option, self).__getattribute__(item)
        elif self.type == Option.is_not_none:            
            return decorate_func(self.value.__getattribute__(item))
        else:
            return lambda : self
            

class test:
    def __init__(self,a):
        self.a = a
        
    def print_myself(self):
        return test(self.a + 1)
    
def get_value(a):
    if a == 0:
        return None
    else:
        return test(a + 1)
    
def my_app(a):
    get_value(a).print_myself()
    

def decorate_func(func):
    def inner_func(*args):
        rst= func(*args)
        return of(rst)
    return inner_func
    
if __name__ == '__main__':
    x = decorate_func(get_value)(0).print_myself().print_myself().print_myself()
    print(x.flat())
    

    
    
    
    
    