print("Welcome to our Vending Machine and get your drinks!")

class VendingMachine:
    items = {
        "apple": 3,
        "orange": 3,
        "water": 2,
        "coffee": 5
    }

    #displaying items with prices
    def display_items(drink):
        print("Available items:")
        for item, price in drink.items.items():
            print(f"{item}: RM{price}")


    def buy_item(drink, item, amount):
        if item not in drink.items:
            print("Item not available.") #if the item entered is not in the list
            return

        item_price = drink.items[item]
        if amount < item_price:
            print("Insufficient amount. Please insert more money.")  #if the amount entered by customer less than the price
            return

        change = amount - item_price
        RM_note = [100, 50, 20, 10, 5, 1]  #type of RM note available for the changes
        returned_notes = {}

        #formula to release the least amount of notes
        for note in RM_note:
            if change >= note:
                count = change // note
                returned_notes[note] = count
                change -= count * note

        print(f"Please take your {item}.")
        print("Returning changes:")
        for num_note, count in returned_notes.items():
            print(f"{count} x RM{num_note}")

vending_machine = VendingMachine()
vending_machine.display_items()

item_choice = input("Enter the drink you want (apple, orange, water, or coffee): ")
amount = int(input("Insert the amount in RM"))

vending_machine.buy_item(item_choice, amount)
