# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10B-Tpl6mAeyDZhQXJ3a2iGtw4XZwvyBT
"""

#predictive text-driven Haiku 

import json,requests

repeat = "yes"
print ("Hello, welcome to the predictive text Haiku generator! ")

try:

   while repeat.strip() == "yes":

     response = requests.get("https://www.datamuse.com/api/")
     base_url = "https://api.datamuse.com/words?md=s&rel_trg="
     second_base = "https://api.datamuse.com/words?md=s&lc=&rel_rhy="
     
     search = input("What word do you want to search? ")
     full_url = base_url + search
     response = requests.get(full_url)
#initilising arrays 
     words=[]
     two=[]
     second =[]
     third = []
     fourth =[]
     fifth=[]
     sixth=[]
     sixthh=[]
     seven=[]
#First line
     if response:
    
       data = json.loads(response.text)
       #print(json.dumps(data, indent = 4))
       for i in data :
         if i["numSyllables"] == 3:
           words.append(i["word"])
       for j in data :
         if j["numSyllables"] == 2:
           two.append(j["word"])
           #printing first line 
       print(words[1],two[2])
     a = words[1]
     b = two[2]
#Second line
     f_line = "https://api.datamuse.com/words?md=s&lc="
     s_line="https://api.datamuse.com/words?md=s&rel_rhy="
     one= f_line+a
     lc=f_line+b
     rhy=s_line+b
     response = requests.get(one)
    #first word
     if response:
       data = json.loads(response.text)
       #print(json.dumps(data, indent = 4))
    
       for i in data :
         if i["numSyllables"] == 3:
           words.append(i["word"])
    #second word

     response = requests.get(lc) 
     if response:
       data = json.loads(response.text)
       #print(json.dumps(data, indent = 4))
     
       for j in data :
         if j["numSyllables"] == 2:
           third.append(j["word"])
#third word
     response1 = requests.get(lc)
     if response1:
       dataa = json.loads(response1.text)
       #print(json.dumps(dataa, indent = 4))
       for k in dataa :
         if k["numSyllables"] == 2:
           fourth.append(k["word"])

     response2 = requests.get(rhy)

     if response2:
       dataaa = json.loads(response2.text)
       #print(json.dumps(dataaa, indent = 4))

       for m in dataaa :
         if m["numSyllables"] == 2:
           fifth.append(m["word"])
  #printing second line
       print(words[3],third[3],fifth[2])

#third line
     c = fifth[0]
     t_line = "https://api.datamuse.com/words?md=s&lc="
     t1_line="https://api.datamuse.com/words?md=s&rel_rhy="
     lc1 = t_line+a
     rhy1= t1_line+b
     response = requests.get(full_url)
     if response:
       data = json.loads(response.text)
    #print(json.dumps(data, indent = 4))
       for i in data :
         if i["numSyllables"] == 3:
           sixth.append(i["word"])
    #print (sixth[0])
    #second word
     response = requests.get(lc)

     if response:
       data = json.loads(response.text)
       for k in data :
         if k["numSyllables"] == 2:
           sixthh.append(k["word"])

     response = requests.get(rhy1)
     if response:
       data = json.loads(response.text)
       # print(json.dumps(data, indent = 4))
       for m in data :
         if m["numSyllables"] == 2:
           seven.append(m["word"])
      #printing third line
       print(sixth[0],seven[1])

     repeat = input("Would you like to run another analysis (yes/no)? ")

#exception 
except ValueError:
    print("Sorry, you entered an invalid number.")

except Exception as e:
    print("Sorry, an unexpected error occurred.")
    print(e)
