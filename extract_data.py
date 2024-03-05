import re
name = input("Enter file name:")
total = 0
if  len(name) < 1:
    name = "extra.txt"
handle = open(name)
for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for number in numbers:
        total = total + int(number)
    
print(total)




    