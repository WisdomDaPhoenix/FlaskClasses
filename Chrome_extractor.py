#Extract Chrome Passwords
#-----------------------------------

import csv
import os
import sqlite3

# Specify the path to Chrome's SQLite database file
chrome_password_db_path = os.path.expanduser('~') + r"\AppData\Local\Google\Chrome\User Data\Default\Login Data"

def extract_passwords():
    # Connect to the database
    conn = sqlite3.connect(chrome_password_db_path)
    cursor = conn.cursor()

    try:
        # Execute the SQL query to fetch the saved passwords
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Create a new CSV file to store the passwords
        with open("chrome_passwords.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            
            # Write the header row to the CSV file
            writer.writerow(["Website", "Username", "Password"])
            
            # Write each password entry as a row in the CSV file
            for row in rows:
                url = row[0]
                username = row[1]
                # Decrypt the encrypted password using Chrome's secret key
                password = win32crypt.CryptUnprotectData(row[2])[1].decode('utf-8')
                writer.writerow([url, username, password])

        print("Passwords extracted successfully and saved to chrome_passwords.csv!")

    except sqlite3.OperationalError as e:
        # Handle any exceptions that occur during the process
        print("Error occurred:", str(e))

    # Close the database connection
    conn.close()

# Run the function to extract passwords
extract_passwords()

