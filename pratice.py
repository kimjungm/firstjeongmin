from random import *
numbers = range(1, 21)
numbers = list(numbers)
shuffle(numbers)

winner = sample(numbers,4)
print("---당첨자 발표---")
print("치킨당첨자: ", format(winner[0]))
print("커피당첨자: ",format(winner[1:]))
print("---축하합니다---")









