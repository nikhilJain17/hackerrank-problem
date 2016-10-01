# Test Cases
a = "aabcd"
b = "abcde"

# list holding count of occurences (is 26 values long for each letter of alphabet)
occurences = []

# final answer
ans = 0

# main function
def main():
	# initialize occurences with 26 zero's
	for i in range(0, 26):
		occurences.append(0)
	
	# iterate through a, increment occurences for each letter that appears
	for letter in a:
		# get the ascii value of the letter
		ascii_value = ord(letter)

		# subtract 97 to go from ascii number to actual number
		# EX: ascii value of a is 97, but index in occurences should be 0
		# b is 98, c is 99, and so on
		index = ascii_value - 97
		occurences[index] += 1

	print(occurences)

	# do the same thing for b, except decrement this time
	for letter in b:
		# get the ascii value of the letter
		ascii_value = ord(letter)

		# subtract 97 to go from ascii number to actual number
		# EX: ascii value of a is 97, but index in occurences should be 0
		# b is 98, c is 99, and so on
		index = ascii_value - 97
		occurences[index] -= 1

	print(occurences)

	# iterate through occurences (which now holds the differences in the two strings PER LETTER)
	for i in occurences:

		global ans

		# abs() is the absolute value function
		ans += abs(i)

	print("\n\nThe final answer is: ") 
	print(ans)




# execute main function
if __name__ == "__main__":
	main()
