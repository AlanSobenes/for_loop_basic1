my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
for count in range(0,5):
    print("looping =", count)
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")
for val in "string":
    if val == "i":
        break
    print(val)
for val in "string":
    if val == "i":
        continue
    print(val)
y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")