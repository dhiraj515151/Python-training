def checkPrimeNumber(n):
    if n>2:
        print(n,"Number is not a prime number")
    else:    
        for i in range(2,int(n/2)+1):
            if n % i == 0:
                print("{} is not a prime number".format(n))
                break
        else:
            print("{} is a prime number".format(n))

checkPrimeNumber(2)
