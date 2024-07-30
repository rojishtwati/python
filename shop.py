import os
marketdict={'vegName':'PRICE per KG',
            'alu':100,
            'tomato':60,
            'chilli':120,
            'carrot':120,
            'onion':90,
            'radish':80,
            'cabbage':80,
            'peas':60,
            'mushroom':500} # vegName=['null','alu','tomato','carrot','chilli','onion','radish','cabbage','peas','mushroom'] #add more if needed
cartdict={0:0}#'listNum':'Quantity'
vegName=list(marketdict.keys())
def item(i):
    print("################### Welcome to Tarkari Bazar ####################")
    print("Select the desire unit and quantity in KG")
    for loop in vegName:
         print(f"{i}.{vegName[i].upper()}       ................      {marketdict.get(vegName[i])}/Kg")
         i=i+1
    print("0. Quit")
    buy(i)

def buy(i):
    i=i
    select=int(input("Select number for product:::"))
    if(select<i and select>0):
        cartdict[select]=float(input("enter Quantity in KG"))
    elif(select==0):
        quit()
    else:
        print("********Invald choice********")
        buy(i)

def bill():
    n=1 
    GTotal=0
    listNum=list(cartdict.keys())
    print("########################## Tarkari Bazar Invoice #############################")
    print("S.n         Particular       Rate      QNT       Total")
    cartdict.pop(0)
    marketdict.pop("vegName")
    for x in list(cartdict.keys()):
         total=marketdict.get(vegName[x])*cartdict.get(x)
         GTotal=GTotal+total
         print(f"{n}            {vegName[x].upper()}           {marketdict.get(vegName[x])}          {cartdict.get(x)}      {total}       ")
         n=n+1
         

    print(f"            GRAND TOAL ===    {GTotal}")
    return GTotal
if __name__ == "__main__":
    while(1):
       i=0
       os.system('cls')
       item(i)
       con_select=input("DO U want to add more product?(y/n)")
       if con_select.lower() !='y':
           break
    os.system('cls')
    amt=bill()
    money=int(input("enter amount you have"))
    print(f"Return amt == {money-amt}")
    print("Thank you for visiting")
    
      
    