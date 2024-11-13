import psycopg2

db = psycopg2.connect(
    database='4-uy ishi',
    user='postgres',
    password='1',
    host='localhost',
    port='2008'
)
cursor = db.cursor()
# cursor.execute('''
#     --1.1
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id SERIAL PRIMARY KEY,
#     nomi VARCHAR(100) NOT NULL,
#     model TEXT NOT NULL,
#     year INTEGER ,
#     price NUMERIC(12, 2),
#     mavjud BOOL DEFAULT TRUE
#     );
#     INSERT INTO cars (nomi, model, year, price, mavjud) VALUES
#     ('Toyota Camry', 'Sedan', 2023, 35000.00, TRUE),
#     ('BMW X5', 'SUV', 2022, 55000.00, TRUE),
#     ('Audi A4', 'Sedan', 2021, 40000.00, FALSE),
#     ('Tesla Model S', 'Sedan', 2024, 75000.00, TRUE);
#     -----------------------------------------------------------------------
#     --1.2
#     CREATE TABLE IF NOT EXISTS customers(
#     customer_id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     soname VARCHAR(50),
#     phone_number CHAR(13) ,
#     address TEXT
#      );
#
#      INSERT INTO customers (name, soname, phone_number, address) VALUES
#     ('Toxir ', 'Toxirov', '+998901234567', 'Toshkent, Yunusobod'),
#     ('Sobir', 'Sobirov', '+998971234567', 'Samarkand, Buxoro ko''chasi 12'),
#     ('Jalil', 'Jalilov', '+998941234567', 'Farg''ona, Shohruhbek ko''chasi 5'),
#     ('Bakir', 'Bakirov', '+998931234567', 'Buxoro, Oqtepa ko''chasi 8');
#     ----------------------------------------------------------------------------
#     --1.3
#     CREATE TABLE IF NOT EXISTS orders(
#     id SERIAL PRIMARY KEY ,
#     car_id INTEGER  ,
#     customer_id INTEGER ,
#     sana DATE NOT NULL ,
#     total_price NUMERIC(12, 2),
#     FOREIGN KEY (car_id) REFERENCES cars(car_id),
#     FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
#
#     );
#
#     INSERT INTO orders (car_id, customer_id, sana, total_price) VALUES
#     (1, 2, '2024-12-31', 35000.00),
#     (3, 1, '2024-5-12', 40000.00),
#     (2, 4, '2024-1-15', 55000.00),
#     (4, 3, '2024-10-14', 75000.00);
#     -------------------------------------------------------------------
#     --1.4
#     CREATE TABLE IF NOT EXISTS employees(
#     id SERIAL PRIMARY KEY ,
#     employe_name VARCHAR(50) NOT NULL,
#     position VARCHAR(50),
#     salary NUMERIC(10, 2)
#     );
#
#     INSERT INTO employees (employe_name, position, salary) VALUES
#     ('Ali', 'Dizayner', 2500.50),
#     ('Vali', 'Marketing Manager', 3200.00),
#     ('Jahongir', 'Texnik Xodim', 1500.75),
#     ('Dilshod', 'HR Menejeri', 2800.00);
#     -------------------------------------------
# ''')
# 2.1
# cursor.execute('''
# ALTER TABLE customers
# ADD COLUMN email VARCHAR(100) DEFAULT 'toxirToxirov@gamil.com';
# ''')
# -------------------------
# 2.2
# cursor.execute('''
# ALTER TABLE customers RENAME COLUMN name TO names;
# ''')
# ------------
# 2.3
# cursor.execute('''
# ALTER TABLE customers
# RENAME TO mijozlar
# ''')
# -----------
# 3
# domla 3 chini biryola qilib ketdim
# ---------------
# 4
# cursor.execute('''
# UPDATE employees SET employe_name = 'Toxir' WHERE id = 3
# ''')
# cursor.execute('''
# UPDATE employees SET employe_name = 'Sobir' WHERE id = 1
# ''')
# ---------------
# 5
# cursor.execute('''
# DELETE FROM employees WHERE id = 2;
# ''')
# ---------------
# 6
# cursor.execute('''
# SELECT * FROM cars
# ''')
# a=cursor.fetchall()
# for a in a:
#     print(a)
# -----------------------------
# cursor.execute('''
# SELECT * FROM mijozlar
# ''')
# b=cursor.fetchall()
# for b in b:
#     print(b)
# ------------------------
# cursor.execute('''
# SELECT id, nomi,names,sana , total_price FROM orders
# JOIN cars ON orders.car_id = cars.car_id
# JOIN mijozlar ON orders.customer_id = mijozlar.customer_id;
# ''')
# c=cursor.fetchall()
# for c in c:
#     print(c)
# ---------------------
# cursor.execute('''
# SELECT * FROM employees
# ''')
# d=cursor.fetchall()
# for d in d:
#     print(d)
db.commit()
db.close()