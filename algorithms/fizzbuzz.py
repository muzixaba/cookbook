# if number is a multiple of 3, print 'Fizz'
# if multiple of 5 return 'buzz'
# else return the number

def fb1(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
        

def fb2(n):
    for i in range(1, n+1):
        output = ""
        if i%3==0:
            output += "Fizz"
        if i%5==0:
            output += "Buzz"
        print(output or i)


def fb3(n):
    """Uses tenery operators"""
    for i in range(1, n+1):
        output="Fizz" if i%3==0 else ""
        output+="Buzz" if i%5==0 else ""
        print(i) if output=="" else print(output)

def fb4(n):
    print("fb4 output")
    for i in range(1, n+1):
        print("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i)

fb4(15)