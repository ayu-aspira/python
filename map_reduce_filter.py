'''
generated 10.28

@author: Allen Yu

'''



def map_list(lst, func):
    rlst = []
    for l in lst:
        rlst.append(func(l)) 
    return rlst


def filter_list(lst, predict):
    rlst = []
    for l in lst:
        if predict(l):
            rlst.append(l)
    return rlst


def reduce_lst(lst, default, reduce_func):
    rst = default;
    for l in lst:
        rst = reduce_func(rst, l)
    return rst;


class CustomizedList:
    m = 'map'
    f = 'filter'

    def __init__(self, lst):
        self.lst = lst
        self.func_lst = []

    def map(self, func):
        new_lst = []
        new_lst.extend(self.lst)
        new_cust_lst = CustomizedList(new_lst)
        
        new_func_lst = []
        new_func_lst.extend(self.func_lst)
        new_func_lst.append((CustomizedList.m, func))
        
        new_cust_lst.func_lst = new_func_lst
        
        return new_cust_lst
    
    def filter(self, func):
        new_lst = []
        new_lst.extend(self.lst)
        new_cust_lst = CustomizedList(new_lst)
        
        new_func_lst = []
        new_func_lst.extend(self.func_lst)
        new_func_lst.append((CustomizedList.f, func))
        new_cust_lst.func_lst = new_func_lst
        
        return new_cust_lst 
    
    def flat(self):
        rlst = []
        def inner(e, rlst):
            if not isinstance(e, CustomizedList):
                rlst.append(e)
            else:
                [inner(x, rlst) for x in  e.execute() ] 
        inner(self, rlst)
        return rlst
    
    def recursive_execute(self):
        rlst = []
        def inner(e):
            inner_lst = []
            if not isinstance(e, CustomizedList):
                inner_lst.append(e)
                return inner_lst
            else:
                inner_lst.extend(   inner(x) for x in  e.execute()   )
                return inner_lst 
        rlst.extend(inner(self))
        return rlst
        
    def execute(self): 
        rlst = []
        rlst.extend(self.lst)
        for each in self.func_lst:
            rlst = (map_list if each[0] == CustomizedList.m else filter_list)(rlst, each[1])
        return rlst


def flat(e, rlst):
    if isinstance(e, CustomizedList):
        [flat(x, rlst) for x in  e.execute() ] 
    else:
        rlst.append(e)

                
def reduce_recursive(lst, default, reduce_func): 
    if len(lst) == 0:
        return default
    elif len(lst) == 1:
        return reduce_func(default, lst[0])
    else:
        return reduce_func(lst[0], reduce_recursive(lst[1:], default, reduce_func))


# tail recursive equals iteration
def reduce_tail_recursive(lst, default, reduce_func):
    
    def inner(lst, last_value):
        return last_value if len(lst) == 0 else inner(lst[1:], reduce_func(last_value, lst[0]))
        
    return default if len(lst) == 0 else inner(lst, default)    

            
def group_by_lst(lst, group_by_key_func):
    rlst = map_list(lst, lambda x: (group_by_key_func(x), x))
    rdict = {}
    for key, i in rlst:
        value = rdict.get(key, [])
        value.append(i)
        rdict[key] = value   
    return rdict   


def get_key(x, group_by_condition):
        for cond, key in group_by_condition.items():
            if cond(x):
                return key


def test_map_reduce_filter():
    lst = [1, 3, 4, 6]  
    print(lst[0])   
    print(lst[1:])
    print(map_list(lst, lambda x: x + 1))
    print(filter_list(lst, lambda x: x > 3))  
    print(reduce_lst(lst, 10, lambda x, y: x + y)) 
    print(reduce_recursive(lst, 10, lambda x, y: x + y)) 
    print('tail recursive:' + str(reduce_tail_recursive(lst, 10, lambda x, y: x + y))) 
    
    group_by_condition = {lambda x: x < 18: 'under age', lambda x: x >= 18 and x < 30: 'young adult',
          lambda x: x >= 30 and x < 70: 'adult', lambda x: x >= 70: 'senior'}
    print(group_by_lst([('a', 12), ('b', 56), ('c', 34), ('c', 24), ('d', 70)], lambda x: get_key(x[1], group_by_condition)))


# tail recursive equals iteration
def check_list(lst, category_func):
    newLst = []

    def inner_check(lst, last_key, last_category):
        if len(lst) == 0:
            return newLst
        else: 
            ele = lst[0]   
            current_category = category_func(ele) 
            current_key = last_key if  current_category == last_category else last_key + 1         
            newLst.append((current_key, ele))
            return inner_check(lst[1:], current_key, current_category)
    
    return newLst if len(lst) == 0 else inner_check(lst, -1, category_func(lst[0]))

   
if __name__ == '__main__':

    print(CustomizedList([1, 2, 6, 4]).map(lambda x: x + 1).map(lambda x: x * 2).execute())
    test_map_reduce_filter()
    test_str = 'ab123b23cdd432a'
    
    grp_lst = group_by_lst(check_list(test_str, lambda x: x.isalpha()), lambda x:x[0])
    rlst = []
    for key, value in grp_lst.items():
        mapped_lst = map_list(value, lambda x: x[1])
        reduce_value = reduce_lst(mapped_lst, '', lambda x , y: x + y)
        rlst.append(reduce_value)
    print(rlst)

