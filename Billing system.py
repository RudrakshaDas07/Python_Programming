while True:                                                #Billing system
    name=input("Enter customer's name:")
    ph_no=int(input("Enter customer's ph no.:"))
    total=0
    while True:
        print("Enter the amount and quantity")
        amount=float(input("Enter amount:"))
        quantity=float(input("Enter quantity:"))
        total+=(amount*quantity)
        repeat=input("Do you want to add more items?(yes/no)")
        if repeat=="no" or repeat=="No":
            break
    print("-"*40)
    print("Name:",name)
    print("Ph no.:",ph_no)
    print("Amount to be paid:",total)
    print("-"*40)
    print("**************Happy Shopping**************")
    repeat1=input("Do you want to go to next customer?(yes/no)")
    if repeat1=="no" or repeat1=="No":
       break

