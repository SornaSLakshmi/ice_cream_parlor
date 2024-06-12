import mysql.connector

conn = mysql.connector.connect(
host = "localhost",
user = "root",
password = None,
database = "ice_cream"
)

cursor = conn.cursor()

def add_seasonal_flavor(name, description, season):
    cursor.execute(f"INSERT INTO seasonal_flavors (name, description, season) VALUES ({name}, {description}, {season})")
    conn.commit()

def add_ingredient(name, quantity):
    cursor.execute(f"INSERT INTO ingredients (name, quantity) VALUES ({name}, {quantity})")
    conn.commit()

def add_customer_suggestion(flavor_name, customer_name, suggestion):
    cursor.execute(f"INSERT INTO customer_suggestions (flavor_name, customer_name, suggestion) VALUES ({flavor_name}, {customer_name}, {suggestion})")
    conn.commit()

def add_allergen(name):
    try:
        cursor.execute(f"INSERT INTO allergens (name) VALUES ({name})")
        conn.commit()
    except mysql.connector.errors.IntegrityError:
        print(f"Allergen '{name}' already exists.")

def add_to_cart(flavor_id, quantity):
    cursor.execute(f"INSERT INTO cart (flavor_id, quantity) VALUES ({flavor_id}, {quantity})")
    conn.commit()

def search_flavors(keyword):
    cursor.execute(f"SELECT * FROM seasonal_flavors WHERE name LIKE %{keyword}%")
    results = cursor.fetchall()
    return results

def filter_flavors(season):
    cursor.execute(f"SELECT * FROM seasonal_flavors WHERE season = {season}")
    results = cursor.fetchall()
    return results

def view_cart():
    cursor.execute('''SELECT cart.id, seasonal_flavors.name, cart.quantity 
                      FROM cart 
                      JOIN seasonal_flavors ON cart.flavor_id = seasonal_flavors.id''')
    results = cursor.fetchall()
    return results

while True:
    print("\nIce Cream Parlor Menu")
    print("1. Add Seasonal Flavor")
    print("2. Add Ingredient")
    print("3. Add Customer Suggestion")
    print("4. Add Allergen")
    print("5. Add to Cart")
    print("6. Search Flavors")
    print("7. Filter Flavors by Season")
    print("8. View Cart")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter flavor name: ")
        description = input("Enter description: ")
        season = input("Enter season: ")
        add_seasonal_flavor(name, description, season)
    elif choice == '2':
        name = input("Enter ingredient name: ")
        quantity = int(input("Enter quantity: "))
        add_ingredient(name, quantity)
    elif choice == '3':
        flavor_name = input("Enter flavor name: ")
        customer_name = input("Enter your name: ")
        suggestion = input("Enter your suggestion: ")
        add_customer_suggestion(flavor_name, customer_name, suggestion)
    elif choice == '4':
        name = input("Enter allergen name: ")
        add_allergen(name)
    elif choice == '5':
        flavor_id = int(input("Enter flavor ID: "))
        quantity = int(input("Enter quantity: "))
        add_to_cart(flavor_id, quantity)
    elif choice == '6':
        keyword = input("Enter search keyword: ")
        results = search_flavors(keyword)
        for row in results:
            print(row)
    elif choice == '7':
        season = input("Enter season: ")
        results = filter_flavors(season)
        for row in results:
            print(row)
    elif choice == '8':
        results = view_cart()
        for row in results:
            print(row)
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")