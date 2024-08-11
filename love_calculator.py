# /** q2. Love Calculator
#  This is a difficult challenge! 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 

# R occurs 1 time 

# U occurs 2 times 

# E occurs 2 times 

# Total = 5 

# L occurs 1 time 

# O occurs 0 times 

# V occurs 0 times 

# E occurs 2 times 

# Total = 3 



# Love Score = 53

# These functions will help you: 

# You can use the count() function to count the number of times a character occurs in a string. Docs: https://www.w3schools.com/python/ref_list_count.asp  
# */



You can use the lower() function to change all the inputs to lower case. Docs: https://www.w3schools.com/python/ref_string_lower.asp
def love_calculator():
    n1= input("enter your name: ")
    n2= input("enter your partner name: ")
    c= n1 + n2
    
    true = c.count('t')+c.count('r')+c.count('u')+c.count('e')
    love= c.count('l')+c.count('0')+c.count('v')+c.count('e')
    
    score= str(true)+ str(love)
    print(score)
    
love_calculator()    
