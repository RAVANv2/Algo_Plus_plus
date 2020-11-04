

def ways(friend):
	if friend < 0:
		return 0

	if friend == 0 or friend ==1:
		return 1

	ans = ways(friend-1) + (friend-1)*ways(friend-2)
	return ans



friend = 5
print(ways(friend))