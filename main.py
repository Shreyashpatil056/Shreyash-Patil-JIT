# Author: Shreyash Shriram Patil
# Date: 2nd June 2024

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
    
# Number of rounds
n = 200

kyabola_usne = 'idk bro'
i = 0

# Loop through the rounds
while i < n:
    # Input handling
    input_string = input()
    rnd, res = input_string.split()
    rnd = int(rnd)
    i += 1

    kyabola_usne = res
    # Append input to file
    append_to_file(input_string)
    
    if i == 1:
        ha()
    elif i >= n - 1:
        na()
    else:
        bol(kyabola_usne)
        
    

# Append final message to file after all inputs are taken
append_to_file("<------------- This World Shall Know Pain ---------->\n")
