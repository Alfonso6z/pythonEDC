def fib(n):
    
    if(n>1):
        return fib(n-1) + fib(n-2)
    elif(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        print("Error")

def main():
    print ("hola")
    n = int(input("ingresa un número"))
    print(fib(n))
    
    for i in range(n+1):
        print(f"{fib(i)}",end=', ')

main()