import random


#2.5 עליך לחשב ממוצע טמפרטורה של 5 ערים בעולם
#רוץ בלולאה מ- 1 עד 5 ובכל פעם קלוט את הטמפרטורה
#אם הטמפרטורה קטנה ממינוס 50 או גדולה מפלוס 45 קלוט שוב ושוב, עד אשר הטמפרטורה
#תהיה בטווח.
#בתום הקלט של 5 הערים , חשב את ממוצע הטמפרטורה. רמז: ראה קוד של השיעור


the_sum: int = 0
number: int = 0
for i in range(1, 6):
    number = int(input('enter number: '))
    if number - 50 <= number <= 40:
        print(number, end=" ")

    the_sum += number
else:

    print('all 5 numbers were inserted')
    avg: float = the_sum / 5
    print(f"the avg is: {avg: .2f}")

# jump point
print('finish')









# in random form
#the_sum: int = 0
#number: int = 0
#for i in range(1, 5):
#    random_number: int = random.randint(-50, 40)
#    if random_number -50 <= random_number <= 40:
#        print(random_number, end=" ")

#    the_sum += random_number
#else:

#    print('all 5 numbers were inserted')
#    avg: float = the_sum / 5
#    print(f"the avg is: {avg: .2f}")

#print('finish')