import random

num = random.randrange(1, 9, 1)

guess = input("guess a number between 1 and 9:")
nextTryLess = input('your guess was lower than my number, try a number bigger than', guess)
nextTryMore = input('your guess was higher than my number, try a number smaller than', guess)
print (guess)

if (guess<num):
    print(nextTryLess)
elif (guess>num):
    print(nextTryMore)
else:
    print('Great!your right!!')
