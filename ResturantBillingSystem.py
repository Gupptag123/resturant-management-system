import time
# -----------------------------
# Restaurant Billing System
# -----------------------------
menu = {
    1: {"name": "Burger", "price": 35},
    2: {"name": "Pizza 8 Inchs", "price": 199},
    3: {"name": "pizza 10 Inchs", "price": 249},
    4: {"name": "Vag Parcel", "price": 59},
    5: {"name": "Fries", "price": 60},
    6: {"name": "Soft Drink 250 ml", "price": 20},
    7: {"name": "Soft Drink 500 ml", "price":50},
    8: {"name": "Ice Cream Small", "price": 60},
    9: {"name": "Ice Cream Large", "price": 120},
    10: {"name": "Veg Thali", "price": 200},
    11: {"name": "Jain Thali", "price": 220},
    12: {"name": "Simpal Thali", "price": 150}
}

cart = {}


def show_menu():
    print("\n" + "=" * 45)
    print("          RESTAURANT MENU         ")
    print("=" * 45)

    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']:<15}   Rs. {item['price']}")

    print("=" * 45)


def add_to_cart():
    while True:
        try:
            item_id = int(input("\nEnter Item Number (0 to Finish): "))

            if item_id == 0:
                break

            if item_id not in menu:
                print("❌ Invalid Item!")
                continue

            qty = int(input("Enter Quantity: "))

            if qty <= 0:
                print("❌ Quantity must be greater than 0.")
                continue

            if item_id in cart:
                cart[item_id] += qty
            else:
                cart[item_id] = qty

            print("✅ Item Added Successfully!")

        except ValueError:
            print("❌ Please enter valid numbers.")


def generate_bill():
    if not cart:
        print("\nNo items ordered.")
        return

    print("\n")
    print("=" * 60)
    print("               RESTAURANT BILL: ")
    print("=" * 60)

    subtotal = 0

    print(f"{'Item':20}{'Qty':>8}{'Price':>10}{'Total':>15}")
    print("-" * 60)

    for item_id, qty in cart.items():
        item = menu[item_id]
        total = item["price"] * qty
        subtotal += total

        print(
            f"{item['name']:20}{qty:>8}{item['price']:>10}{total:>15}"
        )

    print("-" * 60)

    tax = subtotal * 0.10
    grand_total = subtotal + tax

    discount = 0

    if subtotal >= 5000:
        discount = grand_total * 0.05
        grand_total -= discount

    print(f"{'Subtotal:':40}   Rs. {subtotal:.2f}")
    print(f"{'GST (18%):':40}   Rs. {tax:.2f}")
    print(f"{'Discount:':40}   Rs. {discount:.2f}")
    print("-" * 60)
    print(f"{'Grand Total:':40}   Rs. {grand_total:.2f}")
    print("=" * 60)

    print("\nThank you for visiting! ❤️")


def main():
    print("=" * 45)
    print("       WELCOME TO MY RESTAURANT   ")
    print("=" * 45)

    input("\n Press ENTER to Start Ordering...  ")
    time.sleep(1)

    show_menu()
    add_to_cart()
    generate_bill()


if __name__ == "__main__":
    main()