#! /usr/bin/env python3

# 1. Get highest stack
# 2. Pop top element from it
# 3. Repeat until all stacks are same height

def stack_equalizer(stack_1, stack_2, stack_3):

    s1_height = sum(stack_1)
    s2_height = sum(stack_2)
    s3_height = sum(stack_3)

#    hash_map = {stack_1_height: stack_1, stack_2_height: stack_2, \
#            stack_3_height: stack_3}
    
    hash_map = {'stack_1': s1_height, 'stack_2': s2_height, 'stack_3': s3_height}

    
    
    print(hash_map)
    print(hash_map.keys())
    print(hash_map.values())

if __name__ == "__main__":

    h1 = [3, 2, 1, 1, 1]
    h2 = [4, 3, 2]
    h3 = [1, 1, 4, 1]

    stack_equalizer(h1, h2, h3)
