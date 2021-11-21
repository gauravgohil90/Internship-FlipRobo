#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Q11. Factorial of a number

num = 3

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Error")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[18]:


# Q12. Prime or composite

num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")

else:
    print(num, "is NOT a prime number it is a COMPOSITE number")


# In[23]:


# 13. Check Palindrome

# Program to check if a string is palindrome or not

my_str = 'racecar'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




