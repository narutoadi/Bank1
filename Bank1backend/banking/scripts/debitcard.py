from luhn import luhn 
from random import randint
import sys
sys.path.append('/home/aditi/Bank1/Bank1backend/')
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bank1.settings')
django.setup()
from banking.models import DebitCard

def generateDebitCards(lott_num, vfm, vfy):
	dcNo = list("2200000000000000")
	vtm = vfm
	vty = vfy + 5
#	print(dcNo)
	lott=int(lott_num)
	lot=lott
	dcNoArr = [dcNo] * 10000
	list1 = [4,8,12,5,9,13,3,7,11]
	for j in range(0,10000):
		for i in list1:
			dcNoArr[j][i] = str(lot%10)
			lot = int(lot/10)
	list2 = [2,6,10,14]
	for j in range(0,10000):
		k=j
		for i in list2:
			dcNoArr[j][i] = str(k%10)
			k=int(k/10)
		dcNoArr[j][15] = luhn(dcNoArr[j])
		cardNo = ("".join(dcNoArr[j]))
		cvv = str(randint(100, 999))
		pin = str(randint(1000, 9999))
		print(cardNo,vfm, vfy,vtm, vty,lott,cvv,pin)
		modelInstace = DebitCard(debitCardNumber=cardNo, validFromMonth=vfm, validFromYear=vfy, validThruMonth=vtm, validThruYear=vty, lottNo=lott, cvv=cvv, pin=pin)
		modelInstace.save()


generateDebitCards(1,2,11)