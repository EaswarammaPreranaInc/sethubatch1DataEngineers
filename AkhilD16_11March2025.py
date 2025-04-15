'''
1.Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character.
	Let input be  character  :  A
	Outut--->	Alpha  Numeric  Character
				Alphabet  Character
				Upper  case  Alphabet
'''

def charCheck():
	str=input("Enter a character:")
	if all([str.isalnum(),str.isalpha(),str.isupper()]):
		print("Alpha Numeric  Character")
		print("Alphabet Character")
		print("Upper case  Alphabet")
	elif all([str.isalnum(),str.isalpha(),str.islower()]):
		print("Alpha Numeric  Character")
		print("Alphabet Character")
		print("Lower case  Alphabet")
	elif all([str.isalnum(),str.isdigit()]):
		print("Alpha Numeric  Character")
		print("Digit Character")
	elif str.isspace():
		print("White Space")
	else:
		print("Special Character:")
charCheck()

'''
2.Write  a  program  to  reverse  a  string  without  slice.
	Let  input  be   Hyd
    Output ---> dyH
''' 

def stringReverse():
	try:
		str=input("Enter a string: ")
		res=''
		for i in range(1,len(str)+1):
			res+=str[-i]
		print(res)
	except (TypeError,SyntaxError,NameError):
		print("Input should be a String")

stringReverse()

'''
3.Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice
  Let  input  be  Hyd  is  green  city
  Output ---> city   green   is   Hyd
'''

def reverseOrderOfWords():
	str=input("Enter string sentence: ")
	list=str.split()
	res=''
	for i in range(1,len(list)+1):
		res+=list[-i]+" "
	print(res)

reverseOrderOfWords()

'''
4.Write  a  program  to  reverse  each  word  of  the  sentence.
  Let  input  be  Hyd  is  green  city
  Output ---> dyH si neerg ytic
'''

def reverseOfEachWord():
	str=input("Enter string sentence: ")
	list=str.split()
	res=''
	for i in range(len(list)):
		ex=list[i][::-1]
		res+=ex+" "
	print(res)
reverseOfEachWord()

'''
5.Write  a  program  to  sort  string  in  alphabetical  order
  Let  input  be  RAJESH
  Output --->  AEHJRS
'''

def alphabeticalStringSort():
	str=input("Enter a String: ")
	list=sorted(str)
	x=(res:='').join(list)
	print(x)
alphabeticalStringSort()
'''
6.Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
Output  ---> ADKPZ13579
'''

def alphaNumStringSort():
	str=input("Enter String: ")
	alphabets=[]
	digits=[]
	for i in str:
		if i.isalpha():
			alphabets.append(i)
		elif i.isdigit():
			digits.append(i)
	alphabets=sorted(alphabets)
	digits=sorted(digits)
	res="".join(alphabets+digits)
	print(res)
alphaNumStringSort() 
