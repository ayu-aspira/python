'''
Created on Nov 22, 2021

@author: allenyu
'''
from map_reduce_filter import filter_list, map_list


def select_sort(lst):
    rlst = []    
    def sort_inner(rlst, current_lst):
        if len(rlst) == len(lst):
            return rlst
        else:
            small = find_the_smallest(current_lst)
            rlst.append(small[1])
            return sort_inner(rlst, filter_list(current_lst, lambda x : x[0] != small[0]))
    
    return sort_inner(rlst,convert_lst(lst))

def find_the_smallest(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        left = lst[0]
        right = find_the_smallest(lst[1:])
        return left  if left[1] <=right[1] else right   
    
 
def convert_lst(lst):
    l = [-1]
    def func(a):
        l[0] = l[0] + 1
        return (l[0], a)
    return map_list(lst, func )    


def merge_lst(left, right):
    rlst = []
    
    def inner(rlst, current_left, current_right):
        if len(rlst) == len(left) + len(right):
            return rlst
        else:
            if len(current_left) == 0:
                rlst.extend(current_right)
            elif len(current_right) == 0:
                rlst.extend(current_left)
            else:
                left_first = current_left[0]
                right_first= current_right[0]
                if left_first <= right_first:
                    rlst.append(left_first)
                    inner(rlst, current_left[1:], current_right)
                else:
                    rlst.append(right_first)
                    inner(rlst, current_left, current_right[1:])
            return rlst
                    
    
    return inner(rlst,left,right)


def merge_sort(lst):
    if len(lst)<2:
        return lst[:]
    else:
        middle = len(lst)//2
        left = merge_sort(lst[:middle])
        right = merge_sort(lst[middle:]) 
        return merge_lst(left, right)
    
if __name__ == '__main__':
        
    print(select_sort([4,6,1,1,8,3,5,9,2,7])) 
    print('----------------------------')  
    print(merge_sort([4,6,1,1,8,3,5,9,2,7]))