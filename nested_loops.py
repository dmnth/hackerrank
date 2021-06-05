#! /usr/bin/env python3

ll_1 = [4, 33, 12, 99, -1, 32, 9, 9, 0]
ll_2 = [9]



def get_merge_point(ll_1, ll_2):

    index = 0 
    while index != len(ll_1):
        ll_2_index = 0
        while ll_2_index != len(ll_2):
            if ll_1[index] == ll_2[ll_2_index]:
                return ll_1[index]
                break
            ll_2_index += 1
        index += 1
    return 0

result = get_merge_point(ll_1, ll_2)
print(result)


