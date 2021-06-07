#! /usr/bin/env python3 

# A game of two stacks 
# one pops from two stacks of non-negative ints
# Keeps track of his sum !> maxSum

# Find the maximum possible score, that can be achieved

def two_chairs(maxSum, s1, s2):

	maxScore = maxSum
	current_score = 0
	difference = 0
	moves_made = 0
	current_stack = s1

	while current_score <= maxScore:
		
		if current_score == 0:
			current_score += s1.pop(0)
			moves_made += 1

		peeked_top_s1 = s1[0]
		peeked_top_s2 = s2[0]

		if current_score + peeked_top_s1 < maxScore:
			current_score += s1.pop(0)
			moves_made += 1
			peeked_top_s1 = s1[0]

		elif current_score + peeked_top_s1 == maxScore:
			current_score += s1.pop(0)
			moves_made += 1
			break

		elif current_score + peeked_top_s1 >= maxScore and current_score + peeked_top_s2 < maxScore:
			current_score += s2.pop()
			moves_made += 1
			peeked_top_s2 = s2[0]
			

		print(' max score: ', maxScore, '\n', \
			'current score: ', current_score, '\n', \
			'difference: ', difference, '\n',
			'moves: ', moves_made, '\n', \
			's1 top: ', s1[0], '\n', \
			's2 top: ', s2[0], '\n')


if __name__ == "__main__":

	s1 = [1, 2, 3, 4, 5]
	s2 = [6, 7, 8, 9]

	s3 = [4, 2, 4, 6, 1]
	s4 = [2, 1, 8, 5]

	two_chairs(10, s3, s4)