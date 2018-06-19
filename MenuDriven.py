import cmath
def prime(num):
  for i in range(2,num):
      if num%i==0:
          print(num," is not a Prime Number")
          break
      else:
          print(num," is a Prime Number")
          break
def fact(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    #print(fac)
    print("The Factorial of a Given Number:")
    print(fac)
def factorial(num):
  if num==1:
    return num
  else:
    return num*factorial(num-1)
def pal(num):
  rev=str(num)[::-1]
  print(rev)
  if(num==int(rev)):
    print("The Given Number",num," is a Palindrome")
  else:
    print("The Given Number",num," is not a Palindrome")
def fibo(num):
  if num==0:
    return 0
  elif num==1:
    return 1
  else:
    return fibo(num-1)+fibo(num-2)
print("1.Prime Number\n2.Factorial\n3.Factorial using Recursion\n4.Palindrome\n5.Add Complex Number\n6.Fibonacci\n")
dict={'PrimeNumber':1,'Factorial':2,'Factorial using recursion':3,'Palindrome Number':4,'Complex Number':5,'Fibonacci':6,'Exit':7}

option=0
    
while(option!=dict['Exit']):
      print("Enter Your Choice")
      option=int(input())
      #print(dict)
      if option == dict['PrimeNumber']:
        print("To Find Whether the Given Number is Prime or Not")
        num=int(input())
        prime(num)
      elif option==dict["Factorial"]:
          print("To find The  Factorial")
          num=int(input())
          fact(num)
      elif option==dict["Factorial using recursion"]:
          print("To find The  Factorial")
          num=int(input())
          if num<0:
            print("Factorial doesn't exist for negative numbers")
          elif num==0:
            print("The Factorial of number 0 is 1")
          else:
           print("The factorial of",num,"is",factorial(num))
      elif option==dict["Palindrome Number"]:
       print("Enter the Number To check to find Palindrome")
       num=int(input())      
       pal(num)
      elif option==dict["Complex Number"]:
        print("Enter the Complex Number 1")
        num1=int(input())
        num2=int(input())
        cnum1=complex(num1,num2)
        print("Enter the Complex Number 2")
        num3=int(input())
        num4=int(input())
        cnum2=complex(num3,num4)
        cnum=cnum1+cnum2
        print("Addition of Two Complex Number is:",cnum)
      elif option==dict["Fibonacci"]:
        num=int(input("Enter The Number To find The Fibonacci Series"))
        fibo(num)
        print("Fibonacci Series for",num,"nth term is",fibo(num))
        
      else:
         print("Invalid Entry")
      
          
