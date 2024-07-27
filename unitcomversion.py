import os 
def LengthConversion():
    os.system('cls')
    print("Length Conversion")
    print("1. KM to M")
    print("2. M to KM")
    print("3. Feet to Inch")
    print("4. Inch to Feet")
    print("0. Back")
    select=int(input("Enter number for conversion"))
    if(select==1):
        km=float(input("enter length in km"))
        m=km*1000
        print(f"{km} KM to {m} M")


    elif(select==2):
        m=float(input("enter length in m"))
        km=m/1000
        print(f"{m} M to {km} KM")
    
    elif(select==3):
        feet=float(input("enter length in feet"))
        inch=12*feet
        print(f"{feet} feet to {inch} inch")

    elif(select==4):
        inch=float(input("enter length in inch"))
        feet=12/inch
        print(f"{inch} inch to {feet} feet")
    elif(select==0):
        main()
    else:
        print("********Invald choice********")
        LengthConversion()

def WeightConversion():
    os.system('cls')
    print("Weight Conversion")
    print("1. KG to G")
    print("2. G to KG")
    print("3. KG to Pounds")
    print("4. Pounds to KG")
    print("0. Back")

    select=int(input("Enter number for conversion"))
    if(select==1):
        kg=float(input("enter weight in kg"))
        g=kg*1000
        print(f"{kg} KG to {g} G")


    elif(select==2):
        g=float(input("enter weight in g"))
        kg=g/1000
        print(f"{g} G to {kg} KG")
    
    elif(select==3):
        kg=float(input("enter weight in KG"))
        pound=kg*(1/2.205)
        print(f"{kg} KG to {pound} pound")

    elif(select==4):
        pound=float(input("enter weight in pound"))
        kg=pound*2.205
        print(f"{pound} pound to {kg} pound")
    elif(select==0):
        main()
    else:
        print("********Invald choice********")
        WeightConversion()





def TempertureConversion():
    os.system('cls')
    print("Temperature Conversion")
    print("1. Fahrenheit to Celsius (F - C)")
    print("2. Celsius to Fahrenheit (C - F)")
    print("0. Back")
    select=int(input("Enter number for conversion"))

    if select==1:
        fahrenheit=float(input("enter temp in fahrenheit"))
        celsius=(fahrenheit-32)*5/9
        print(f"{fahrenheit} Fahrenheit to {celsius} Celsius.")
    elif select==2:
        celsius=float(input("enter temp in celsius"))
        fahrenheit=(celsius+9/5)+32
        print(f"{celsius} Celsius to {fahrenheit} Fahrenheit.")
    elif select==0:
        main()
    else:
        print("********Invald choice********")
        TempertureConversion()



def main():
    os.system('cls')
    print("Welcome to Unit Conversion")
    print("Select the desire unit conversion")
    print("1. LENGTH")
    print("2. Weight")
    print("3. Temperature")
    print("0. Quit")
    select=int(input("Enter number for conversion"))
    if(select==1):
        LengthConversion()
    elif(select==2):
        WeightConversion()
    elif(select==3):
        TempertureConversion()
    elif(select==0):
        quit()
    else:
        print("********Invald choice********")
        main()

if __name__ == "__main__":
   while(1):
       main()
       con_select=input("DO U want to continue?(y/n)")
       if con_select.lower() !='y':
           break
    

    
