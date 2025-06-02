choice = ""
while choice != "q":
    print("Menu:")
    print("(I)nstructions")
    print("(C)alculate")
    print("(Q)uit")
    choice = input("Choice: ").lower()

    if choice == "i":

        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
    elif choice == "c":

        while True:
            try:
                num_products = int(input("Number of products: "))
                if num_products < 0:
                    print("Invalid input")
                else:
                    break
            except ValueError:
                print("Invalid input")

        while True:
            try:
                price_per_product = float(input("Price: "))
                if price_per_product <= 0:
                    print("Invalid input")
                else:
                    break
            except ValueError:
                print("Invalid input")

        if num_products > 5:
            total_price = num_products * price_per_product * 0.9
        else:
            total_price = num_products * price_per_product
        print(f"{num_products} x ${price_per_product:.2f} products = ${total_price:.2f}")
    elif choice == "q":
        print("Farewell")
    else:
        print("Invalid choice")