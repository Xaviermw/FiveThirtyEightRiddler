def choice_probability(socks_minus_one, round):
	probability = 1
	total = socks_minus_one
	unmatch = total-1

	for i in range(0, round-2):
		probability = probability*(unmatch/total)
		unmatch = unmatch - 2
		total = total - 1

	probability = probability*((total-unmatch)/total)

	return probability


PAIRS = 10

total_expected_value = 0

for i in range(2, PAIRS+2):
	total_expected_value = total_expected_value + i * (choice_probability((PAIRS*2)-1, i))

print(total_expected_value)

