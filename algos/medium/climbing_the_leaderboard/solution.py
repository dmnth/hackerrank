

def climbingTheLeaderboard(ranked, player):
	
	
	for stat in player:

		ranked.append(stat)
		
		current = ranked[0]

		for i in range(0, len(ranked)):

			k = ranked[i]
			j = i - 1
			
			while j >= 0 and k > ranked[j]:
				print(ranked[i], ranked[j], ranked[j+1])
				ranked[j + 1] = ranked[j]
				j -= 1

			ranked[j + 1] = k

		
	return


if __name__ == "__main__":

	ranked = [100, 90, 90, 80]
	player = [70, 80, 105]

	result = climbingTheLeaderboard(ranked, player)
	print(result)