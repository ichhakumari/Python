state=['delhi','mumbai','kota','gaya']
fruit=['mango','apple','lichi']

# function 1 : length of a list
def len_cities(list):
    print(len(list))
    
# function 2  : print item of list in single line
def print_item(list):
    for item in list:
        print(item , end=" ")
   
   
#print factoriAL  ofn 
def cal_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(fact)

# convert usd into inr 
def converter(usd_value):
    inr_value = usd_value*83
    print(usd_value ,'usd=', inr_value ,"inr")


# Funtion call
converter(2000)       # 166000
cal_fact(4)           # 24
print_item(state)     # delhi mumbai kota gaya
len_cities(fruit)     # 3

