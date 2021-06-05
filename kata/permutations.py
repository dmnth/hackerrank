#! /usr/bin/env python3

def permutations(strng):

    if len(strng) < 2:
        return strng

    all_perms = []
    for ind, char in enumerate(strng):
        sub_perms = permutations(strng[:ind] + strng[ind + 1:])
        for element in sub_perms:
            all_perms.append(element + char)

    return list(set(all_perms))



if __name__ == "__main__":
    print(permutations('aabb'))
