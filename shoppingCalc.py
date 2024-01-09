'''  Name: LAVANYA SASIKALA
     Student ID: 156621211
     Assignment
    This program implements a simple shopping calculator.Some items such as candy,eggs, and flour will have special promotional discounts
    applied to them.Users will enter the name of an item found at the grocery store, along with number of items purchased, and price per item.
    If the item name is found in a list of discounts, each additional item purchased will lead to the price being discounted by 5%, 
    up to a maximum of 20%.Once the user has finished entering items and their prices, you program will print a receipt.Each item will be 
    printed along with item number and the price. The program will print a total on a new line, and on another new line, the total discount applied to all purchases.
'''

itemList=[]         #A list to store the items purchased.
discntitemList=["candy","eggs","flour","hummus","ice cream","chicken soup","diapers"]   #The list of items having discounts

def askItemName():
    '''This function prompts the user to enter the name of the items to be purchased. The item name should be a valid string of characters.
     If numbers are entered,error message will be printed and the user is prompted again to enter the correct input. If enter key is the input then 
     the function to print the receipt will be called. If the input is valid, the item is appended to a list and the function to prompt the price of the item is called'''
    iscorrect =True
    while iscorrect:

        itemName = input("Please enter an item of food , or press Enter to exit: ")   #Prompts user to enter the item name.
        if itemName.isalpha():      # Checking for the validity of the user input.If valid, askiTEMpRICE FUNCTION IS CALLED.
            
            askItemPrice(itemName)
            itemList.append(itemName)  # itemList is appended.
            #iscorrect = False
            #print(itemList)
        elif itemName=="" :         #If input is enter key, printreceipt() is called.
            
            printreceipt(itemList)
            iscorrect = False
            
        else :                      #For invalid input, the function is called again.
            print("Please enter a valid item")
            askItemName()



def askItemPrice(itemName):
    ''' This function prompts the user to enter the priceof the item selected. This takes item Name as the parameter. If the input entered is valid
    the function to ask item quantity is called. if not valid, the function is again called after displaying error message.'''
    
    #print("Item is"+itemName)
    itemPrice = input("Item is: "+ itemName+ ".Please enter the price for this item: ")        #Prompts the user for the price of he item
    #print(itemPrice)
    iscorrect = itemPrice.isalpha()             #Checking the validity of the price entered.
   # print(iscorrect)
    if(itemPrice.isalpha()): 
        print("Error: price must be a number.Example: 1, or 1.99.")           #If characters are entered, display error message
        askItemPrice(itemName)
    elif itemPrice=="":                     #If enter key, dispaly error message.
        print("Error: price must be a number.Example: 1, or 1.99.")
        askItemPrice(itemName)


    else:
        itemPriceCheck = itemPrice.replace(".","")          # If the price is a floating point number, to compare, the decimal point neds to be replaced.
        if(itemPriceCheck.isnumeric and float(itemPrice) >0):
            askItemQuantity(itemName,itemPrice)             #If the input is valid, call the function to input the no:of items purchased.
    
       

def askItemQuantity(itemName,itemPrice):
    '''The function is for asking the quantity of each item purchasing. The validity of the input is checked and, if valid the function
    to calcuate the price is called. If not valid, error message is printed and the function will becalled again'''

    itemQuantity = input("Item is: "+ itemName+ ".How many will you purchase? ")  #Prompting the user to enter the quantity.

    if itemQuantity.isdigit() and int(itemQuantity) > 0:   #Checking the validity of the input.
        itemQuantity = int(itemQuantity)
        calcPrice(itemName,itemPrice,itemQuantity)       #If valid, calcPrice() is caled for calculating the price of the item purchased.
    else:
         print("Not a valid quantity")                  #If not valid, error message is displayed and the function is called again for he valid input.
         askItemQuantity(itemName,itemPrice)

def calcPrice(itemName, itemPrice,itemQuantity):
    '''This function checks whether the item is in the list of discounted items, checks for the quantities bought and then apply the discounts as per conditions..
    The savings of each item is calculated and is maintained as a list. The lists for itemQuantity, itemPrice, itemNewPrice anf total is also maintained'''
   
   
    
    if itemName in discntitemList:              #Checking whether the item is in discounted list. If yes, checking the quantities and applyingthe discounts appropriately. 
        
        if itemQuantity ==1:                    #If itemQuantity is 1, discount is not applicable.
            itemNewPrice = float(itemPrice)
           
        elif itemQuantity ==2:                  #If itemQuantity is 2, 5% discount 
           
            itemNewPrice = float(itemPrice)*0.95
            

        elif itemQuantity ==3:                  #If itemQuantity is 3, 10% discount 
            
            itemNewPrice = float(itemPrice)*0.90
           
        elif itemQuantity ==4:                  #If itemQuantity is 4, 15% discount 
            
            itemNewPrice = float(itemPrice)*0.85
           
        else:                                       #For any quantities of 5 and above, discount is 20%
           
            itemNewPrice = float(itemPrice)*0.80
            
    else:                                       #If the item is not in the discounted list, there is no discount.
        itemNewPrice =float(itemPrice)
    

    savings = float(itemPrice)-itemNewPrice                 #The amount saved for each item per quantity  is calculated.
    #print("Item New Price "+ str(itemNewPrice))
    itemQuantityList.append(itemQuantity)                   # The list of item quantities purchased.
    #print("itemQuantityList =", itemQuantityList)
    itemNewPrice = round(itemNewPrice,2)
    priceList.append(itemNewPrice)                          #The list of price after discount of each item.
    #print("priceList is" ,priceList)                       
    savingList.append(savings*itemQuantity)                 #The list of total savings under each item.
    #print("Savins listis:",savingList)
    
    totalPrice = round(itemNewPrice*itemQuantity,2)                #Calculating the totalof each item
    #print("totalPrice = :" +str(totalPrice))
    totalPriceList.append(totalPrice)                       #The list of total of each item
    #print("totalPriceList" ,totalPriceList)


def printreceipt(itemList):
    '''This function prints the receipt in the desired format. For each item in the itemList, the name , quantity purchased, 
    price per quantity after discount and total is calculated. The total amount of shopping and the savings is also calculated and displayed.'''
    total = 0
    savings = 0
    print ("RECEIPT")
    for item in range(len(itemList)):         
        itemName = str(itemList[item])
        total += sum([totalPriceList[item]])   #Total of amount of each item
        #print("total: "+str(total))
        savings+= sum([savingList[item]])       #Calculating savings.
        
        #savingList[item]
        

        print(f"{item+1:}. {itemName:<15} {itemQuantityList[item]:<3} *  $ {priceList[item]:.02f}  =  $  {totalPriceList[item]:.02f}")
    print(f"Total: { ' ' *30} ${total:.02f}" )
    print(f"Your Savings:{ ' ' *25} ${savings:.02f}")


if __name__ == "__main__":
    '''Main function having some global variable lists initialized and calling the function askItemName.'''
    priceList = []
    totalPriceList = []
    itemQuantityList =[]
    savingList = []
    #Total = 0
    askItemName()               #Calling the function askItemName()
    


    
