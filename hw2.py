import random
from operator import truediv

# הגרל מספר בין 1-100

# קלוט מספר מהמשתמש עד אשר המשתמש ינחש את המספר שהוגרל ע"י המחשב
# IF: ROLL_NUM > PRINTED_NUM
# print ('your number is too big')


# IF: ROLL_NUM < PRINTED_NUM
# print ('your number is too small')

# IF: ROLL_NUM == PRINTED_NUM
# print('BINGO')


# המספר לא מוגרל מחדש = הגרלה 1 קבועה בהתחלה שזה נחשב ל NESTED LOOP
# והמשתמש מנסה לנחש שוב עד שפוגע
# בתום המשחק הדפס כמה נסיונות היו





random_number: int = random.randint(1, 100)
print(random_number, end=" ")
counter: int = 1
while True:
    user_guess: int = int(input('guess the number'))
    if user_guess < random_number:
        print('too low')
        counter += 1
    elif user_guess > random_number:
        print('too high')
        counter += 1
    else:
        print('bingo')
        print(counter)
        break











#counter: int = 1

#for i in range(1):
#    random_number: int = random.randint(1, 100)
#    print(random_number, end=" ")

#    random_bool: bool = random.choice([True, False])

#    random_number = random.randint(1, 100)
#    counter += 10000000000
#    while True:
#        user_answer: int = int(input("What's the number?"))

#        if user_answer < random_number:







