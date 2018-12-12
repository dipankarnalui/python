x = "AbduLLAH iSt eiN KeKs!"
for i in x:
	if i.isupper():
		i.replace("A","+")
	elif i.islower():
		i.replace("i","-")
	elif i.isspace():
		i.replace(" ","?")
	else:
		print(x)