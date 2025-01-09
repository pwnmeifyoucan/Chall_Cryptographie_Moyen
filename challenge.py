import random as rd

charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_-!@#$()[]<>/"

def f(a,b,n,x):
	return (a*x+b)%n

def encrypt(message,a,b,n):
	encrypted = ""
	for char in message:
		x = charset.index(char)
		x = f(a,b,n,x)
		encrypted += charset[x]

	return encrypted

n = len(charset)
a = rd.randint(2,n-1)
b = rd.randint(1,n-1)

print(encrypt(FLAG,a,b,n))

# ENCRYPTED FLAG: #$F-7-V-6L->S>dr$qgNz-g4-Np[-4>)}dRL-L<