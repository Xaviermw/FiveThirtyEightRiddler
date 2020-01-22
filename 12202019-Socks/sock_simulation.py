import random

class Sock:
	def __init__(self, color):
		self.color = color

def one_sock_round(pairs):

	remaining_socks = []
	picked_socks = []

	for i in range(pairs):
		remaining_socks.append(Sock(i))
		remaining_socks.append(Sock(i))

	over = False
	sock_round = 0

	while(over == False):
		sock_round = sock_round + 1
		picked_sock = remaining_socks[random.randint(0, len(remaining_socks)-1)]
		for sock in picked_socks:
			if (picked_sock.color == sock.color):
				over = True
		picked_socks.append(picked_sock)
		remaining_socks.remove(picked_sock)

	return sock_round

SIMULATIONS = 1000000
PAIRS = 10

total_rounds = 0

for sim in range(SIMULATIONS):
	total_rounds = total_rounds + one_sock_round(PAIRS)

print(total_rounds/SIMULATIONS)


