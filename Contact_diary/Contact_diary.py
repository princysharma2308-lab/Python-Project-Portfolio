# Project:Contact Diary
# Author:Princy Sharma
# Date:24/10/2026
contacts={}
while True:
    print("contact diary")
    print("enter 1 to add contact")
    print("enter 2 to search for a contact")
    print("enter 3 to update a contACT")
    print("enter 4 to delete a contact")
    print("enter 5 to view all contact")
    print("enter 6 to exit")

    user_choice=int(input("enter your choice"))

    if(user_choice)==6:
        break
    elif(user_choice)==1:
        name=input("enter name: ")
        phone=input("enter phone:")
        contacts[name]=phone
    elif(user_choice)==2:
        user_search=input("enter conatct name:")
        if user_search in contacts:
            print("contact found")
            print(contacts[user_search])
        else:
            print("not found") 
    elif(user_choice)==3:
        update_contact=input("enter contact to update; " )
        if update_contact in contacts:
            update_no = input("enter updated phone no ;")
            contacts[update_contact]=update_no
        else:
            print("cotact not found")
    elif(user_choice)==4:
        contact_deleted=input("enter contact to delete;" )
        if contact_deleted in contacts:
            del contacts[contact_deleted]
        else:
            print("contact not found")
    elif(user_choice)==5:
        print(contacts)