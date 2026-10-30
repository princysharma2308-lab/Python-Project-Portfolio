# Project=Grocery list Manager
# Author= Princy Sharma
# Date=23-08-2026

grocery=[]

while True:
    print("Grocery List Manager")
    print("Choose 1 to add item in grocery list")
    print("Choose 2 to remove item in grocery list")
    print("Choose 3 to see the grocery list")
    print("Choose 4 to search item in grocery list")
    print("Choose 5 to exit the grocery list")

    Choice= int(input("Enter your choice: ", ))

    if(Choice==1):
      item=input("enter the item: ", )
      grocery.append(item)
      print("item added to the list")

    elif(Choice==2):
       item=input("enter the item to remove: ", )

       if item in grocery:
         grocery.remove(item)
         print("item removed")
       else:
         print("item not found")

    elif(Choice==3):
        print(grocery)
    
    elif(Choice==4):
      item=input("enter the item to search:",  )   

      if item in grocery:
        print("item is found in the list")
      else:
        print("item not found")

    elif(Choice==5):
       print("Thankyou for the list")
     

    else:
      print("inavalid input! please enter number between 1 to 5")
    
