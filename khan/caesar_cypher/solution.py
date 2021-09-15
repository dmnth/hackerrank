
chars = [chr(i) for i in range(97, 123)]

def caesarCypher(str, key):

	new_string = ""

	if key > len(chars):
		print("key value should be less or equal to number of letters in alphabet")
		return

	for char in str:

		if char != " " and char in chars:
			char_idx = chars.index(char)
			cyphered_char_idx = (char_idx+key) % len(chars)
			new_char = chars[cyphered_char_idx]
			new_string += new_char
		else:
			new_string += char
			
	
	return new_string

def caesarDeCypher(str, key):

	result = ''

	for char in str:

		if char != " " and char in chars:
			idx = chars.index(char)
			old_idx = (idx-key) % len(chars)
			old_char = chars[old_idx]
			result += old_char
		else:
			result += char
	
	return result

def uncypherCypher(str):
	
	results = []

	for i in range(len(chars)):
		possible_string = caesarDeCypher(str, i)
		results.append(possible_string)

	
	return results

if __name__ == "__main__":
	str = "i am afraid of horses"
	key = 19

	cypheredString = caesarCypher(str, key)
	decypheredString = caesarDeCypher(cypheredString, key)
	print(cypheredString)
	print(decypheredString)
	result = uncypherCypher(cypheredString)
	for str in result:
		print(str)