import random
import string


def create_pw(pw_length=12):
   letters = string.ascii_letters
   digits = string.digits
   special_chars = string.punctuation

   alphabet = letters + digits + special_chars
   pwd = ''
   pw_strong = False
   print(alphabet)
   while not pw_strong and len(pwd)<12:
       print(pwd)
       char = random.choice(alphabet)
       pwd += char

       if ((char in special_chars and char in pwd) and (char in digits and char in pwd) ):
           pw_strong = True

   return pwd


print(create_pw())