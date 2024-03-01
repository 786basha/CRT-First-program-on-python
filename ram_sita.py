import time
print("\n Wellcome Sir!...\n Please Fill the details....\n")
name_cust = input(" Name :")
phone_cust = int(input(" Mobile :"))

frt_bag = []
veg_bag = []
soft_bag = []
rice_bag = []
Bag = []
itm_price = {
    "Apple":230,
    "Banana":60,
    "DragonFruite":250,
    "Tomato":30,
    "Brinjal":40,
    "Capsicam":70,
    "Coke":120,
    "7-up":60,
    "Maaza":45,
    "Rice":50
}


def check_out():
    while True:
        print("\t\t ================  Check Out Menu ================\n \t\t*************  Select an Option Below ***********")
        print("\t\t________________________________________________________")
        cval = int(input("\n 1.Display All items on Bag\n 2.Add Items\n 3.Remove Items\n 4.Place Order \n____________________________________\n Select An Option ..... "))
        if cval == 1:
            print(Bag)
            time.sleep(2)
        elif cval == 2:
            Main_Menu()
        elif cval == 3:
            remove_bag()
        elif cval == 4:
            prcc = 0
            btot = len(Bag)
            for i in Bag:
                print("Price of ",i," = ",itm_price[i])
                prcc += itm_price[i]
            print("Total Elements on Bag:",btot)
            print("Total Amount to Pay is ",prcc," Rupees only...\n \t\t Select Payment Method....")
            print(" 1.Cash \t 2.UPI \t 3.Card \t 4.Check Out Menu")
            

            mode = int(input("Type of payment Mode ..."))
            if mode == 4:
                check_out()
            
            print("Payment Initiated ....")
            time.sleep(2)

            print("Payment Successfull ........")

            print("\n\n \t\t    THANKS YOU MR.",name_cust,"\n\t\t Payment Invoice copy sent to ",phone_cust)

            Bag.clear()
            Main_Menu()

            
            



def Main_Menu():
    print("\n\t\t ***** Main Menu ****** \n \t\t Mr.",name_cust,"You can fill your bag hear...\n")
    print("_______________________")
    val_1 = int(input(" 1.Fruites\n 2.Vegetables\n 3.Soft Drinks\n 4.Rice\n 5.Bag Value..\n 9.Check-Out... \n_______________________\n Select Item : "))
    if val_1 == 5:
        print("\n\t ************** Displaying Cart *************\n")
        print("\t",Bag)
        print("\t ___________________________________________________")
        Main_Menu()
    if val_1 == 9:
        check_out()
    if val_1 == 1:
        while True:
            print("\n\t********** Fruite Mart *********\t\t (' To exit enter 0') ")
            print("______________________________")
            frt_sel = int(input(" 1.Apple\t230/kg\n 2.Banana\t60/kg\n 3.DragonFruite\t250/kg\n______________________________\n\t\t Item : "))
            if frt_sel == 1:
                frt_bag.append("Apple")
                Bag.extend(frt_bag)
                frt_bag.clear()
                print(Bag)
                time.sleep(1) 
            elif frt_sel==2:
                frt_bag.append("Banana")
                Bag.extend(frt_bag)
                frt_bag.clear()
                print(Bag)
                time.sleep(1)
            elif frt_sel == 3:
                frt_bag.append("DragonFruite")                
                Bag.extend(frt_bag)
                frt_bag.clear()
                print(Bag)
                time.sleep(1)
            elif frt_sel == 0:
                Main_Menu()
            else:
                print("Make Correct Selection....")
    elif val_1 == 2:
        while True:
            print("\n\t****** Vegetable Mart *******\n Fill your bag...\t\t 0 to exit") 
            print("______________________________")
            veg_sel = int(input(" 1.Tomato\t30/kg\n 2.Brinjal\t40/kg\n 3.Capsicam\t70/kg\n ______________________________\n Select one... : "))
            if veg_sel == 1:
                veg_bag.append("Tomato")
                Bag.extend(veg_bag)
                veg_bag.clear()
                print(Bag)
                time.sleep(1)
            elif veg_sel==2:
                veg_bag.append("Brinjal")
                Bag.extend(veg_bag)
                veg_bag.clear()
                print(Bag)
                time.sleep(1)
            elif veg_sel == 3:
                veg_bag.append("Capsicam")    
                Bag.extend(veg_bag)
                veg_bag.clear()
                print(Bag)
                time.sleep(1)
            elif veg_sel == 0:
                Main_Menu()
            else:
                print("Make Correct Selection....")
    elif val_1 == 3:
        while True:
            print("\n\t ****************** Soft Drink's Mart ****************\n Fill your bag...")
            print("______________________________")
            soft_sel = int(input(" 1.Coke \t 120/1200ml\n 2.7-up \t 60/600ml\n 3.Maaza\t 45/600ml\n______________________________\n\t  Select an Option :"))
            if soft_sel == 1:
                soft_bag.append("Coke")
                Bag.extend(soft_bag)
                soft_bag.clear()
                print(Bag)
                time.sleep(1)
            elif soft_sel==2:
                soft_bag.append("7-Up")
                Bag.extend(soft_bag)
                soft_bag.clear()
                print(Bag)
                time.sleep(1)
            elif soft_sel == 3:
                soft_bag.append("Maaza")   
                Bag.extend(soft_bag)
                soft_bag.clear()
                print(Bag)
                time.sleep(1)
            elif soft_sel == 0:
                Main_Menu()          
            else:
                print("Make Correct Selection....")
    elif val_1 == 4:
        print("\n ")
        print("Rice Mart Having Single Brand \n Continue With your own risk....")
        val = int(input("Enter No.of Kilo Grams of Rice :"))
        for i in range(val):
            rice_bag.append("Rice")
        Bag.extend(rice_bag)
        rice_bag.clear()
        print(Bag)
        Main_Menu()


def remove_bag():
    print("\t +++++++++ Removing From Cart +++++++++++ ")
    print(Bag)
    val = input("Remove value :")
    Bag.remove(val)
    print(val," is Successfully Removed From the cart")
    x = int(input("\t\t If Wnat to Delete Another one... press 1 to continue or 0 for exit :"))
    if x == 1:
        remove_bag()
    elif x == 0:
        check_out()
    else:
        print("Check it out ....")


Main_Menu();

