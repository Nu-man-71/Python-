import random


lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789" 
symbols = "!@#$%^&*(){}][?/\<-_>"

	all = lower + upper + num + symbols
	length = 13
		password ="".join(random.sample(all, length))
			print(password)