import random
import string
s = ""
for i in range(5):
#char = random. choice("0123456789abcdefgh")
#print(char)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.digits)
#char = random. choice("0123456789abcdefghABCDEFG")
    all_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_char =  random.choice(all_chars)
    print("random_char:",random_char)
#s = ""
#for i in range(5):
    s += random_char
print(s)