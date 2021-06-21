# lIne jumps 

def kangaroo(x1, v1, x2, v2):

	if v2 == v1:
        return "NO"
    
    if (x2 - x1) * (v2 - v1) < 0 and (x2 - x1) % (v2 - v1) == 0:
        return "YES"

    
    return "NO"




if __name__ == "__main__":
	c = kangaroo(21, 6, 47, 3)
	a = kangaroo(0, 2, 5, 3)
	b = kangaroo(0, 3, 4, 2)
	print(a)
	print(b)
	print(c)