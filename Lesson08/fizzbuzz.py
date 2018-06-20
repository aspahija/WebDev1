print "Welcome to the fizzbuzz game!"

x = int(raw_input("Please enter a number between 1 and 100: "))

print x
print
for i in range(1, x+1):

    if i % 15 == 0:
        print "fizzbuzz"

    elif i % 3 == 0:
        print "fizz"

    elif i % 5 == 0:
        print "buzz"

    else:
        print i