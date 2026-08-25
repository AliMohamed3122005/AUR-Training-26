
stock = {}
def read_handle_file():
    try:
        with open("stock.txt","r") as file:
            id = 1
            for line in file:
                if "," in line:
                    key,value=line.split(",",1)
                    stock[id]=(key,int(value))
                    id+=1
    except FileNotFoundError:
        print("File Not found.")
    except ValueError:
        print("Value Error.")
    return stock

def add(stock):
    print("1-Add New Fruit\n" \
    "2-Edit quantity")
    choice = input("Enter Choice: ")
    if choice == "2":
        edited_item=input("Enter the fruit id or name: ").lower()
        if edited_item.isdigit():
            edited_item = int(edited_item)
            if edited_item in stock:
                key,value=stock[edited_item]
                new_quantity=int(input("Enter your new quantity: "))
                stock[edited_item]=(key,new_quantity)
                print("Updated Successfully")
            else:
                print("Id is not found!")
        else:
            for id,(key,value) in stock.items():
                if key == edited_item:
                    new_quantity=int(input("Enter your new quantity: "))
                    stock[id]=(key,new_quantity)
                    print("Updated Successfully")
                    break
            else:
                    print("Fruit is not Found")
    elif choice == "1":
        new_id = len(stock)+1
        key=input("Enter The Fruit you want to add: ").lower()
        value=input("Enter the quantity:")
        stock[new_id]=(key,int(value))
        print("Added Successfully\n")
    save_file(stock)
    show_stock(stock)



def remove(stock):
    dt=input("Enter The Fruit Or Id you want to remove: ").lower()
    if dt.isdigit():
        dt=int(dt)  
        if dt in stock:
            del stock[dt]
            print("Removed Successfully")
        else:
            print("Not Found!")
    else:
        for id,(key,value) in stock.items():
            if key == dt:
                del stock[id]
                print("Removed Successfully")
                break
        else:
                print("Not Found!")
    save_file(stock)
    show_stock(stock)


def show_stock(stock):
    for id, (key, value) in stock.items():
        print(f"{id} {key}: {value}")


def save_file(stock):
    with open("stock.txt","w") as file:
        for id,(key,value) in stock.items():
            file.write(f"{key},{value}\n")


def menu(stock):
    print("Welcome to our program-Choose what you are want to do\n" \
    "1-Add stock\n" \
    "2-Remove stock\n" \
    "3-Show stock's content\n" \
    "4-to exit the program")
    choice=input()
    if choice == "1":
        show_stock(stock)
        add(stock)
    elif choice == "2":
        show_stock(stock)
        remove(stock)
    elif choice == "3":
        show_stock(stock)
    elif choice == "4":
        return False
    else:
        raise ValueError("Unknown")
    return True


#Main

stock = read_handle_file()
while menu(stock):
    pass
