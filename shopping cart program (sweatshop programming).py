import math

def print_menu(foods:list[str], prices:list[int]):
    """prints a table with 2 lists. Assumes list1 is string list2 is a list of ints"""
    


# def print_menu(foods, prices):
#     """assumes 2 parallel arrays are passed in"""
#     for i in range(len(foods)):
#         print(f"{foods[i]}: {prices[i]}")
def main():
    foods = []
    prices = []

    total = 0.0

    print_menu(foods, prices)
    while True:
        userinput = input("What would you like to buy? Or press Q to quit -> ").strip()
        if userinput.lower() == 'q':
            break
        
        while True:
            priceinput = input(f"Enter the price for '{userinput}': ").strip()
            
            try:
                priceinput = float(priceinput)
                break
            except ValueError:
                print("Invalid Input, try again.")
                continue
        foods.append(userinput)
        prices.append(priceinput)
        total += priceinput
    
    print (f"           YOUR CART")        
    print("*" * 29)
    print(f"*  Food:           | Price: *")
    print("*" * 29)
    for idx in range(len(foods)):
        #note this assumes the parallel lists have the same number of elements. 
        print (f"*  {str(foods[idx]).ljust(15)} | ${str(prices[idx]).ljust(7)}*")
    print("*" * 29)


    print(f"Total Cost:  ${total:.2f}\n")



if __name__ == "__main__":
    main()
