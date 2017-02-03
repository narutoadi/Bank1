from luhn import luhn 
def generateDebitCards(lott_no):
	dcNo = list("2200000000000000")
	print(dcNo)
	dcNoArr = [dcNo] * 10000
	list1 = [4,8,12,5,9,13,3,7,11]
	for j in xrange(0,10000):
		for i in list1:
			dcNoArr[j][i] = str(lott_no%10)
			lott_no = lott_no/10
	list2 = [2,6,10,14]
	for j in xrange(0,10000):
		k=j
		for i in list2:
			dcNoArr[j][i] = str(k%10)
			k=k/10
		dcNoArr[j][15] = luhn(dcNoArr[j])
		print (dcNoArr[j])

generateDebitCards(1)