# 1. Basic
for x in range(150):
    print(x)
# 2. Multiples of Five
for x in range(5, 1000, 5):
    print(x)
# 3. Counting the Dojo way
for x in range(1, 101):
    if x % 10 == 0:
        x = "Coding Dojo"
    elif x % 5 == 0:
        x =  "Coding"
    print(x)    
# 4. Whoa. That sucker's Huge
sum = 0    
for x in range(0, 500001):
    if x % 2 == 1:
        sum += x
print(sum)
# 5. Countdown by Fours
for x in range(2018,0,-4):
    print(x)
# 6. Flexible Counter
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x) 