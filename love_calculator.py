def love_calculator():
    n1= input("enter your name: ")
    n2= input("enter your partner name: ")
    c= n1 + n2
    
    true = c.count('t')+c.count('r')+c.count('u')+c.count('e')
    love= c.count('l')+c.count('0')+c.count('v')+c.count('e')
    
    score= str(true)+ str(love)
    print(score)
    
love_calculator()    
