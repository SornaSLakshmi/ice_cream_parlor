# Ice Cream Parlor Cafe

This is a simple Python application to manage an ice cream parlor's offerings, inventory, and customer suggestions.

## Prerequisites

- Python 3.x installed
- MySQL installed and running

## Setup Instructions

1. **Install Python Package:**

   Open a terminal or command prompt and run:

   pip install mysql-connector-python


2. **Setup MySQL Database:**

- Create a database named `ice_cream`.
- Run the following SQL commands in your MySQL client to create the necessary tables:

  ```sql
  CREATE TABLE seasonal_flavors (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      description TEXT,
      season VARCHAR(255)
  );

  CREATE TABLE ingredients (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      quantity INT
  );

  CREATE TABLE customer_suggestions (
      id INT AUTO_INCREMENT PRIMARY KEY,
      flavor_name VARCHAR(255),
      customer_name VARCHAR(255),
      suggestion TEXT
  );

  CREATE TABLE allergens (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) UNIQUE
  );

  CREATE TABLE cart (
      id INT AUTO_INCREMENT PRIMARY KEY,
      flavor_id INT,
      quantity INT,
      FOREIGN KEY (flavor_id) REFERENCES seasonal_flavors(id)
  );
  ```

3. **Update Database Connection:**

In the `ice_cream_parlor.py` file, update the MySQL connection settings:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=None,
    database="ice_cream"
)
```

4. **Run the Application**:

In the terminal or command prompt, navigate to the directory containing the `ice_cream_parlor.py` file and run:

```bash
python ice_cream_parlor.py
```

5. **Interact with the Menu**:

Follow the on-screen instructions to add flavors, ingredients, suggestions, allergens, and manage the cart.
