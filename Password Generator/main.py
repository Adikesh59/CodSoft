import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    password_length = int(input("Enter your Password Length : "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    if( password_length <=4):
        print("Please make some Strong Password ")
        print("Weak Password : "+"".join(random.sample(s,password_length)))
    else:
        print("Strong Password : "+"".join(random.sample(s,password_length)))    