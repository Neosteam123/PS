import random as rd
from random import *
import string
import datetime
import os

current_time = datetime.datetime.now().strftime("%H-%M-%S")
current_date = datetime.datetime.today().strftime ('%d-%b-%Y')
if os.path.exists("EMAIL_DUMMY.txt"):
      os.rename("EMAIL_DUMMY.txt","ID_"+str(current_date)+"_"+str(current_time)+".txt")
      print("Old File Name Was Changed")
id_text_file = open("EMAIL_DUMMY.txt", "x")
number_id = input("Enter Number Of Gmail For Run:  ")
for i in range(0, int(number_id)):
      first_name = str(rd.choice(open("name.txt").readlines()).lower()).rstrip('\n')
      family_name = str(rd.choice(open("family_name.txt").readlines()).lower()).rstrip('\n')
      nick_name = str(rd.choice(open("nickname.txt").readlines()).lower()).rstrip('\n')   #rstrip remove newline character in string
      number = "".join(choice(string.digits) for j in range(rd.randint(1,3)))
      id_format = str(first_name + family_name +nick_name+str(number)).rstrip('\n')
      # print (id_format)
      characters = string.ascii_letters + string.digits
      password = "".join(choice(characters) for x in range(rd.randint(9, 12)))
      id_text = str(id_format + "@gmail.com" + "," + password)
      #id_text= str(password+ "@gmail.com" + "," + password)        # RANDOM ALL
      id_text_file.write("%s\n" % id_text)
print(str(number_id)+ " Random Gmail Was Created")


