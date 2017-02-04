def luhn( s ):
	l = len(s)-1
	sum = 0
	for i in range(0,l):
		if i%2:
			sum = sum + int(s[i])
		else:
			sq = int(s[i]) * int(s[i])
			sum = sum + int(sq%10) + int(sq/10)

	if sum%10 == 0:
		return '0'
	else:
		return str(10-(sum%10))

