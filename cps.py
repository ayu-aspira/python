'''
Created on May 29, 2022

@author: allenyu
'''

'''

(+  *(3 4 ) 5 )

(+  *(3 4 ) 5 )   k: lambda x : x 
*(3 4 )  k: lambda x : +(x 5)
3  k: lambda x: +( *(x 4) 5)
4  k: lambda x: +( *(4 *) 5)
5  k: lambda x: +( *(3 4) x)
'''


'''

(+  *(3 4 ) 5 )

(+  *(3 4 ) 5 )   k: lambda x : x 
*(3 4 )  k: lambda x : +(x 5)
3  k: lambda x: +( *(x 4) 5)
4  k: lambda x: +( *(4 *) 5)
5  k: lambda x: +( *(3 4) x)
'''

def map_lst(lst, f):
    rls = []
    def inner_map(lst,f):
        if len(lst) == 0:
            return rls
        else:
            rls.append(f(lst[0]))
            return inner_map(lst[1:],f)
    return inner_map(lst,f)        


def cons(r, ls):
    rls = []
    rls.append(r)
    rls.append(ls)
    return rls

def map_lst_cps(lst,f):
    def map_inner(lst, accum):
        if len(lst) == 0:
            return accum(lst) 
        else:
            return map_inner(lst[1:], lambda x: accum(cons(f(lst[0]), x)))
    return map_inner(lst,lambda x: x)             
    
if __name__ == '__main__':
    lst = map_lst([1,2,3,4], lambda x: x + 1)
    rlst = map_lst_cps([1,2,3,4], lambda x: x + 1)   
    print(rlst)
    print(([1,2,4,6])[0])
    print(([1,2,4,6])[1:-1])