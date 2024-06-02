# Author: Shreyash Shriram Patil
# Date: 2nd June 2024

import sys

def na():
    print("NO")
    
def ha():
    print("YES")
    
def bol(boldiya):
    print(boldiya)

# def na():
#     print(f"{i} NO")
    
# def ha():
#     print(f"{i} YES")
    
# def bol(boldiya):
#     print(f"{i} {boldiya}")

# Function to append to output.txt
def append_to_file(content):
    with open("output.txt", "a") as f:
        f.write(content + "\n")
    

kyabola_usne = 'idk bro'

# Input handling
# input_string = input()
# rnd, res = input_string.split()
# rnd = int(rnd)

# rnd = int(input())
# res = input()

rnd = int(sys.argv[1])
res = sys.argv[2]

input_string = str(rnd) + " " + res

if(res != "YES" and res != "NO" and res != "NONE"):
    res = 'NO'

# Update kyabola_usne with res
kyabola_usne = res

# Append input to file
append_to_file(input_string)

# Process the input
if rnd == 1:
    ha()
elif rnd >= 199:
    na()
else:
    bol(kyabola_usne)


# Append final message to file after input is processed
append_to_file("<------------- This World Shall Know Pain ----------->\n")
