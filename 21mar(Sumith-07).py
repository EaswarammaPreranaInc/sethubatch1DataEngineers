'''def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b)     #[50 , 60 , 70 , 80]-------------->2nd
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) #[10 , 20 , 30 , 40] -------> 1st 
change(a) 
print(a) #[10 , 20 , 30 , 40] -------> 3rd
'''
'''quiz scoring
def check_gu(guess,answer):
	global score
	still_guess=True
	attempt=0
	while still_guess and attempt<3:
		if guess.lower()== answer.lower():
			print("correct")
			score+=1
			still_guess=False
		else:
			if attempt<2:
				guess=("wrong ans,try again")
			attempt+=1
		if attempt==3:
			print("correct ans is",answer)

score=0
print("Are you a introvert?")
guess1=input("Do you talk to girls ")
check_gu(guess1, "NO")
guess2 = input("Can you walk with a stranger? ")
check_gu(guess2, "No")
guess3 = input("Can you sleep entire day? ")
check_gu(guess3, "yes")
print("Your Score is "+ str(score))
'''
'''
def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = input("ip_address")
print(ipaddress)
'''
lst=69
for i in range (6):
	str=""
	for j in range(65,lst+1):
		str+=chr(j)
	print(str,end='')
	print(' '*(2*i-1),end='')
	if i == 0:
		revstr=str[::-1]
		print(revstr[1:])
	else:
		print(str[::-1])
	lst-=1













