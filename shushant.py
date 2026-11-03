# def Anime(name):
#     print(name, "is the best anime of all time")
    
# name = input("enter the name:")
# name2 = input("enter the name :")
    
# Anime(name)
# Anime(name2)

# def greet(everyone, noon):
#     return(everyone, noon)

# print(greet("Adarsh, Nayan"))

# def good(*students):
#     return f"{students[0:2]}"
# print(good("Adarsh","Baluni"))


# def add(a , b):
#     result = a + b
#     return(result)

# add(20,21)
# print(add(20,21))

# Question 1

# def even(num):
#     if num % 2 == 0:
#         return(True)
#     else:
#         return(False)
# num = int(input("enter the number :"))
# print(even(num))

# Question 2

# def same_type(First):
#     first = type(First[0])
#     for item in First:
#         if first != type(item):
#             return(False)
#     return(True)
# print(same_type([1,2,3,4,5,8]))

# class Animal:
#     def dog(self,name):
#         print(name)
#     def cat(self,name):
#         print(name)
# object = Animal()
# object.dog("nayan")
# object.cat("Oggy")


# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def get_details(self):
#         print(f'student name is{self.name}and his age is {self.age}')
# o = student(" john snow ",29)
# o.get_details()

# class Animal:
#     def __init__(self,Name,age,gender):
#         self.name = Name
#         self.age = age
#         self.gender = gender
#     def dog(self):
#         return(self.name,self.age,self.gender)
#     def get_details(self):
#         print(f'her name is {self.name} her age is {self.age} and her gender is {self.gender}')
# object = Animal("Nayan",19, "female")
# object.get_details()
# print(object.dog())

# try:
# print("A")
# except:
# print("B")
# else:
# print("C")

# def square(n):
#     return n ** 2
# print(square(10))


# def Even(n):
#     return n % 2 == 0
# print(Even(10))


# try:
#     n = int(input("Enter the number :"))
#     print(n)
# except:
#     print("Pls enter the valid number :")


# def safe_divide(a,b):
#     if b == 0:
#         print("Cannot divide by Zero")
#         return None
#     return a / b
# print(safe_divide(10,0))

# def find_max(a,b,c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(find_max(10,20,13))


# class Grandfather:
#     def __init__(self,Name):
#         self.Name = Name
#         self.surname = "Baluni"
        
# class Father(Grandfather):
#     def __init__(self, Name,job):
#         super().__init__(Name)
#         self.job = job


# class Child(Father):
#     def __init__(self, Name, job,school):
#         super().__init__(Name, job)
#         self.school = school
        
        
#     def output(self):
#         print(f"{self.Name} {self.job} {self.school}")
        
# c = Child("Name","JOb","SCHOOL")
# c.output()
# print(c.surname)

# class Bank_account:
#     def __init__(self,account_number,holder_name,initial_balance-0):
#         self.__account_number = account_number
#         self.__holder_name = holder_name
#         self.__initial_balance = initial_balance
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance +- amount
#             print(f"deposited rupees{amount: 2f}.new balanceis rupees {self.__balance:.2f}.")
#         else:
#             print("Deposite amount must be positive")
#     def withdrawl(self,amount):
#         if 0 < amount <= 5


# class Father:
#     def __init__(self):
#         self.__salary = 100000
    
#     def __upi(self,amount):
#         self.__salary -= amount
    
#     def __send_recipt(self):
#         print(f"Current balance is {self.__salary}")
        
#     def main(self):
#         amount = int(input("Enter the amount: "))
#         self.__upi(amount)
#         self.__send_recipt()   
        
# object = Father()
# object.main()    

# import requests
# web_url = 'https://aimicrodegree.org/'
# response = requests.get(web_url)
# response.headers

# print( response.headers)


# import requests
# from bs4 import BeautifulSoup

# def scrape_example():
#     url = 'https://edunetfoundation.org/'
#     response = response.get(url)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text,'html.parser')
#         title = soup.title.get_text()
#         print(f"Title of the page:{title}")
#     else:
#         print(f'Failed tp retrieve the page.Status code:{response.status_code}')
        
#     if __name__ == "__main__":
#         scrape_example()
    
import requests
from bs4 import BeautifulSoup

url = "https://books.torscape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')

# h3= (soup.find("h3"))
# print(h3.a['title'])    

print(response)
        
        
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




        
    




               













        
    



    




