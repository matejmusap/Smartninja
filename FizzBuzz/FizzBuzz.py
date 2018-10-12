print "Hello to fizz buzz app"
print "Curious what it is?"
input = raw_input("Enter number from 1 to 100: ")
try:
    number = int(input)
    if 0 <= number > 100:
        print "Write number between 0 and 100"
    else:
        for x in range(1, number + 1):
            if x % 3 != 0 and x % 5 != 0:
                print int(x)
            elif x % 3 == 0 and x % 5 != 0:
                print "fizz"
            elif x % 3 != 0 and x % 5 == 0:
                print "buzz"
            elif x % 3 == 0 and x % 5 == 0:
                print "fizzbuzz"
        print "It funny, isn't it!"
except Exception as e:
    print "Please enter a whole number."

