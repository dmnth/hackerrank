
def designerPdfViewer(heights, str):

	l = len(str)
	letters = [chr(i) for i in range(97, 123)]
	tallest = 0
	for i in range(len(letters)):
		if letters[i] in str.lower() and heights[i] > tallest:
			tallest = heights[i]

	area = l * 1 * tallest

	return area

if __name__ == "__main__":

	file = open("./input/input00.txt", 'r')
	file_2 = open("./input/input06.txt", 'r')
	out_1 = file.readlines()
	out_2 = file.readlines()

	heights = [int(x) for x in out_1[0].rstrip('\n').split()]
	word = out_1[1]

	result = designerPdfViewer(heights, word)
	print(result)

