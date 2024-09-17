#תרגיל בלולאה מקוננת
#קלוט מהמשתמש ממספר חיובי גדול מ -0 והדפס את הצורה הבאה, לדוגמא אם נקלט 5הדפס -




num = int(input("Enter a positive number greater than 0: "))

for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# one eternity later, after mistakes and some screams under my bad I figured out the reversed loop


for i in range(num - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
