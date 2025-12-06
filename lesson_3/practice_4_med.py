#Question 1
#Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the days before computers had video screens.

#For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it.

phrase = 'The Flintstones Rock!'

for count in range(1,11):
    print(('-' * count) + phrase)


#Question 2
#Alan wrote the following function, which was intended to return all of the factors of number:

#Reprompt solution
def factors(number):
    divisor = number
    result = []
    while divisor <= 0:
        print('Cannot divide by negative numebrs or zero. Please input a number greater than 0.')
        number = int(input())
        divisor = number
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(0))

#Graceful handling of edge cases and small change.

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(10))

#Alyssa noticed that this code would fail when the input is a negative number, and asked Alan to change the loop.
#How can he make this work? Note that we're not looking to find the factors for negative numbers,
#but we want to handle it gracefully instead of going into an infinite loop.

#Bonus Question: What is the purpose of number % divisor == 0 in that code?
#To ensure clean division so the only returns are factors of the number input.