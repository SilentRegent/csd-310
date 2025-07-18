"""
Zachary Anderson, Tevyah Hanley, Angela Vargas
7/16/25
-3 Report Queries for the Outland Adventure Case Study in one script
Milestone #3 Module 11.1
"""
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Starship12!',
    database='outland_adventures'
)
cursor = conn.cursor()


print("Equipment Sales vs Rentals")
#formatting output
print("="*55)

#query 1
Equipment_rental_vs_sale = """
SELECT 
    CONCAT(UPPER(LEFT(transaction_type, 1)), LOWER(SUBSTRING(transaction_type, 2))) AS transaction_type, 
    COUNT(*) AS total_transactions,
    SUM(e.price) AS total_revenue
FROM Transaction_Details t
JOIN Equipment e ON t.equipment_id = e.equipment_id
GROUP BY transaction_type;
""" # used concat and lower to capitalize data in transaction_type table

cursor.execute(Equipment_rental_vs_sale)
results1 = cursor.fetchall()

print("Transaction Type | Total Transactions | Total Revenue")
#formatting output
print("-"*55)

for row in results1:
    print(f"{row[0]:<16} | {row[1]:<18} | ${row[2]:.2f}")

print("-"*55)
print("Booking Trends by Region")
print("="*55)

#query 2
booking_trends = """
SELECT 
    t.region,
    YEAR(b.booking_date) AS year,
    COUNT(*) AS total_bookings
FROM Booking b
JOIN Trip t ON b.trip_id = t.trip_id
GROUP BY t.region, year
ORDER BY t.region, year;
"""

cursor.execute(booking_trends)
results2 = cursor.fetchall()

#formatting for table character size
print("Region            | Year | Total Bookings")
print("-"*55)

for row in results2:
    print(f"{row[0]:<16} | {row[1]}  | {row[2]}")


print("-"*55)
print("Equipment Older Than 5 Years")
print("="*55)

#query 3
equipment_age= """
SELECT 
    name,
    purchase_date,
    TIMESTAMPDIFF(YEAR, purchase_date, CURDATE()) AS age_years
FROM Equipment
WHERE TIMESTAMPDIFF(YEAR, purchase_date, CURDATE()) > 5;
"""

cursor.execute(equipment_age)
results3 = cursor.fetchall()

print("Equipment Name       | Purchase Date| Age (Years)")
print("-"*55)

for row in results3:
    print(f"{row[0]:<20} | {row[1]}   | {row[2]}")
print("-"*55)

cursor.close()
conn.close()
