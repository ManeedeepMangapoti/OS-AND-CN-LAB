# Indexed file organization example with index file

# Function to add a product with an index
def add_product(filename, index_filename, product_id, name):
    with open(filename, 'a') as file:
        pos = file.tell()  # Record the position
        file.write(f"{product_id},{name}\n")
    with open(index_filename, 'a') as index_file:
        index_file.write(f"{product_id},{pos}\n")

# Function to retrieve a product by ID using the index
def find_product(filename, index_filename, product_id):
    with open(index_filename, 'r') as index_file:
        for line in index_file:
            idx_id, pos = line.strip().split(',')
            if idx_id == product_id:
                with open(filename, 'r') as file:
                    file.seek(int(pos))
                    record = file.readline().strip()
                    print(f"Product Found: {record}")
                    return
    print("Product not found.")

# Adding products
add_product("products_indexed.txt", "products_index.txt", "P001", "Laptop")
add_product("products_indexed.txt", "products_index.txt", "P002", "Smartphone")
add_product("products_indexed.txt", "products_index.txt", "P003", "Tablet")

# Retrieving a specific product
print("Searching for Product ID P002:")
find_product("products_indexed.txt", "products_index.txt", "P002")
