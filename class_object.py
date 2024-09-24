def obj_func(obj, a):
   print('func1' + str(obj) + a)

    
def obj_func2(obj, a, b):
    print('func2:' + a + ',' + b + ',' + str(obj))
    
    
def obj_func3(obj, a):
    print('func3' + +str(obj) + str(a))

    
def class_func(a):
    print('class func1: ' + a)


def init_func1(obj, a):
    obj['object data'] = {'a':a}
    

def init_func2(obj, a, b):
    obj['object data'] = {'a':a, 'b':b}

    
def create_class(class_name, init_func, obj_func_lst, class_func_lst): 
    return {'class name':class_name, 'initialized function': init_func,
            'object functions':obj_func_lst, 'class function': class_func_lst}

  
def dot(all_objs, obj_name, func_name, *args):
    obj = all_objs[obj_name]
    return obj['class']['object functions'][func_name](obj, *args)


def dot_class(class_name, class_objs, class_func_name, *args):
    return class_objs[class_name]['class function'][class_func_name](*args)


def create_obj_by_class(class_name, class_objs, *args):
    new_obj = {}
    new_obj['class'] = class_objs[class_name]
    new_obj['class']['initialized function'](new_obj, *args)
    return new_obj


if __name__ == '__main__':
        
    print('run time, read class definition, read object create definition, and invoke the function')
    
    class_objs = {}    
    all_objs = {}
    
    class_objs['class1'] = create_class('class1', init_func1, {'obj_func':obj_func, 'obj_func2':obj_func2}, {})
    class_objs['class2'] = create_class('class2', init_func2, {'obj_func3': obj_func3 }, {'class_func': class_func})
    
    all_objs['new_obj'] = create_obj_by_class('class1', class_objs, 'first class');

    dot(all_objs, 'new_obj', 'obj_func2', 'hello', 'world')  
    dot_class('class2', class_objs, 'class_func', 'hello class ')
