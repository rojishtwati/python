def main():
    print("Welcome to Tarkari Bazar")
    print("Select the desire unit")
    print("1. ALU       100/Kg")
    print("2. Tomato    75/kg")
    print("3. chilli    30/kg")
    print("0. Quit")
    select=int(input("Enter number for product"))
    money=int(input("enter amount you have"))
    if(select==1):
        Qnt=float(money/100)
        print(f"you can have= {Qnt}")
    elif(select==2):
        Qnt=float(money/75)
        print(f"you can have= {Qnt}")
    elif(select==3):
        Qnt=float(money/30)
        print(f"you can have= {Qnt}")
    elif(select==0):
        quit()
    else:
        print("********Invald choice********")
        main()

if __name__ == "__main__":
   while(1):
       main()
       print("Thank you for visiting")
       con_select=input("DO U want to continue?(y/n)")
       if con_select.lower() !='y':
           break
    