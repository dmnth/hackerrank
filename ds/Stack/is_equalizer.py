#! /usr/bin/env python3

# Here we equalize stacks in mediocre-optimal way

def equalize_stack(s1, s2, s3):
	
	# Stack heights

	s1_h = sum(s1)
	s2_h = sum(s2)
	s3_h = sum(s3)

	while True:

		if s1_h == s2_h and s2_h == s3_h:
			break

		elif s1_h > s2_h and s1_h > s3_h:
			s1_h -= s1.pop()

		elif s2_h > s1_h and s2_h > s3_h:
			s2_h -= s2.pop()

		elif s3_h > s1_h and s3_h > s2_h:
			s3_h -= s3.pop()
	
	print(s1, '\n', s2, '\n', s3)
	return s3_h

if __name__ == "__main__":

	h1 = [1, 1, 1, 2, 3]
	h2 = [2, 3, 4]
	h3 = [1, 4, 1, 1]

	print(equalize_stack(h1, h2, h3))