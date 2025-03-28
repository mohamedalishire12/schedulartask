
import csv
import os
import sqlite3
from datetime import datetime

CSV_FILENAME = "sample_data.csv"
DB_FILENAME = "example.db"

def create_sample_csv_if_not_exists(csv_filename):
    """
    Checks if 'sample_data.csv' exists.
    If not, creates a small CSV file with sample headers and data.
    """
    if not os.path.isfile(csv_filename):
        print(f"[{datetime.now()}] - '{csv_filename}' not found. Creating a sample CSV file...")
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            # Write header row
            writer.writerow(["id", "name", "value"])
            # Write some sample rows
            writer.writerow([1, "Alpha", 10.2])
            writer.writerow([2, "Beta", 20.5])
            writer.writerow([3, "Gamma", 30.7])
    else:
        print(f"[{datetime.now()}] - Found existing '{csv_filename}'. Will read it directly.")

def read_csv_data(csv_filename):
    """
    Reads CSV and returns a list of tuples containing the data.
    Assumes the CSV has columns: id, name, value.
    """
    rows = []
    with open(csv_filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)  # Skip header
        if header and len(header) < 3:
            print("Error: The CSV header doesn't match expected columns (id, name, value).")
            return rows
        for line in reader:
            if len(line) == 3:
                rows.append((line[0], line[1], line[2]))
    return rows

def initialize_database(db_filename):
    """
    Creates a local SQLite database file (if it doesn't exist) and a table 'my_table'.
    """
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT,
            value REAL
        )
    """)
    conn.commit()
    conn.close()

def update_sql_table(db_filename, rows):
    """
    Inserts or replaces rows into 'my_table'.
    :param rows: list of tuples [(id, name, value), ...]
    """
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()

    for row in rows:
        if len(row) == 3:
            id_val, name_val, value_val = row
            try:
                id_val = int(id_val)
                value_val = float(value_val)
            except ValueError:
                print(f"Skipping row due to invalid numeric data: {row}")
                continue
            cursor.execute("""
                INSERT OR REPLACE INTO my_table (id, name, value)
                VALUES (?, ?, ?)
            """, (id_val, name_val, value_val))

    conn.commit()
    conn.close()

def main():
    start_time = datetime.now()
    print(f"[{start_time}] - Script started.")

    # Step 1: Check or create the CSV file
    create_sample_csv_if_not_exists(CSV_FILENAME)

    # Step 2: Initialize the database and table
    initialize_database(DB_FILENAME)

    # Step 3: Read data from CSV
    data_rows = read_csv_data(CSV_FILENAME)
    if not data_rows:
        print(f"[{datetime.now()}] - No valid data to update. Exiting.")
        return

    # Step 4: Update/Insert rows in the SQL table
    update_sql_table(DB_FILENAME, data_rows)

    end_time = datetime.now()
    print(f"[{end_time}] - Finished updating the database.")
    print(f"Script run duration: {end_time - start_time}")

    # Pause so you can see the output in the console
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
