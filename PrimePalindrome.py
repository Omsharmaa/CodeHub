def isprime(n):
	for i in range(2,n):
		if n%i==0:
			return 0
			break
	else:
		return 1
def ispalindrome(n):
	a=str(n)
	if a[::-1]==a:
		return 1
	else:
		return 0
n=int(input('Enter a number you want to check:-  '))
p1=isprime(n)
p2=ispalindrome(n)
if p1==1 and p2==1:
	print('\nYes !',n,'is a prime palindrome number')
else:
	print('\nNo,',n,'is not a prime palindrome number')
