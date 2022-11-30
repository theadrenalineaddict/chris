import json

# Load the inventory from the json file
with open('inventory.json') as f:
    inventory = json.load(f)


def add_items():
    while True:
        name = input('Item Name(X to Exit):')
        if name == 'X':
            return
        cost_price = input('Cost Price')
        retail_price = input('Retail Price')
        type = input('type')
        quantity = input('quantity')
        item = {'label': name, 'type': type, 'price': cost_price, 'quantity': quantity}
        inventory.append(item)
        with open('inventory.json', 'w') as f:
            json.dump(inventory, f, indent=4)

def remove_items():
    while True:
        for i in range(len(inventory)):
            print(i, inventory[i]['label'])
        number = input('Item # (X to Exit)')
        if number == 'X':
            return
        number = int(number)
        inventory[number] = {'label': 'Empty'}

def edit_items():
    while True:
        for i in range(len(inventory)):
            print(i, inventory[i]['label'])
        number = input('Item # (X to Exit)')
        if number == 'X':
            return
        number = int(number)
        print(inventory[number])
        inventory[number]['label'] = input('New Label')
        inventory[number]['type'] = input('New Type')
        inventory[number]['price'] = input('New Price')
        inventory[number]['quantity'] = input('New Quantity')


def admin_console():
    password: str = input('Passcode')
    # if password == '2345':
    if password != '2345':
        print('Wrong Password')
        return
    while True:
        print('Choose Action')
        print('1.Add Items')
        print('2.Remove Items')
        print('3.Edit Items')
        print('4.Sales')
        print('X to Exit')
        choice = input('> ')
        if choice == 'X':
            return
        if choice == '1':
            add_items()

            continue
        if choice == '2':
            remove_items()
            continue
        if choice == '3':
            edit_items()
            continue
        if choice == '4':
            sales()
            continue
        print('Invalid Choice')
        continue


def main():
    while True:
        print(chr(27) + "[2J")
        print('Welcome to the vending machine!')
        print('Please select and action:')
        print('1.Buy a product')
        print('2.Access the admin panel')

        choice = input('> ')

        if choice == '2':
            admin_console()
            continue



        print(chr(27) + "[2J")
        # Print the menu
        print("Welcome to the Vending Machine")
        for i, item in enumerate(
                inventory):  # enumerate() returns a tuple of the index and the item so we can use it to get the index in the loop
            print(
                f'{i + 1:02d}: {item["label"]}')  # The index is 0 based so we add 1 to it to make it 1 based. We also pad it with a 0 so it's always 2 digits long.

        # Get the user's choice
        choice = int(input(
            'Please select an item: ')) - 1  # We subtract 1 from the choice to get the index of the item in the list
        print(f'You selected {inventory[choice]["label"]}. That will be ${inventory[choice]["price"]}')

        # Get the user's payment
        change = float(input('Please insert money: '))
        if change < inventory[choice]['price']:
            print('You did not insert enough money')
            continue

        # Update the inventory
        inventory[choice]['quantity'] -= 1
        with open('inventory.json', 'w') as f:
            json.dump(inventory, f, indent=4)

        # Give the user their change
        print(f'Here is your {inventory[choice]["label"]} and ${change - inventory[choice]["price"]} in change')

        # Ask the user if they want to buy another item
        if input('Would you like to buy another item? (y/n) ') == 'n':
            print('Thank you for using the vending machine')
            break


if __name__ == '__main__':
    main()
