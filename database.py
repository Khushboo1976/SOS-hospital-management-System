import sqlite3
import pandas as pd
# Create a database connection and tables
def create_database():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    # Create patients table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age TEXT NOT NULL,
            gender TEXT NOT NULL,
            contact INTEGER NOT NULL,
            health_issue TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact INTEGER NOT NULL,
            sp TEXT NOT NULL,
            timing TEXT NOT NULL
        )
    ''')
    
    #nurse table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nurses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact INTEGER NOT NULL,
            floor TEXT ,
            shift TEXT 
        )
    ''')

    #other staff details
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS staff (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact INTEGER NOT NULL,
            post TEXT NOT NULL,
            shift TEXT
        )
    ''')
    # Create users table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Insert admin user if it doesn't exist
    cursor.execute(
        "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)",
        ("sos123", "ram@123")
    )

    conn.commit()
    conn.close()

# User login verification
def verify_user(username, password):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Add new patient
def add_patient(name, age, gender, contact, health_issue):
    try:
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO patients (name, age, gender, contact, health_issue) VALUES (?, ?, ?, ?, ?)",
            (name, age, gender, contact, health_issue)
        )
        conn.commit()
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

# Get all patients
def get_all_patients():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.close()
    return patients

# Search for a patient by ID
def search_patient(patient_id):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    patient = cursor.fetchone()
    conn.close()
    return patient

#doctors details....    
def add_doctors(name, age, gender, contact,sp,timing):
    try:
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO doctors (name, age, gender, contact, sp,timing) VALUES (?, ?, ?, ?, ?, ?)",
            (name, age, gender, contact, sp, timing)
        )
        conn.commit()
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def get_doctors():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.close()
    return doctors


def search_doctors(doctors_id):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors WHERE id=?", (doctors_id,))
    doctors = cursor.fetchone()
    conn.close()
    return doctors
#nurses details....    
def add_nurses(name, age, gender, contact,floor,shift):
    try:
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO nurses (name, age, gender, contact, floor ,shift) VALUES (?, ?, ?, ?, ?, ?)",
            (name, age, gender, contact, floor , shift) # type: ignore
        )
        conn.commit()
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def get_nurses():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nurses")
    nurses = cursor.fetchall()
    conn.close()
    return nurses


def search_nurses(nurses_id):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM nurses WHERE id=?", (nurses_id,))
    nurses = cursor.fetchone()
    conn.close()
    return nurses
#staff details....    
def add_staff(name, age, gender, contact,post,shift):
    try:
        conn = sqlite3.connect("hospital.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO staff (name, age, gender, contact, post ,shift) VALUES (?, ?, ?, ?, ?, ?)",
            (name, age, gender, contact, post , shift) # type: ignore
        )
        conn.commit()
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()

def get_staff():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff")
    staff = cursor.fetchall()
    conn.close()
    return staff


def search_staff(staff_id):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff WHERE id=?", (staff_id,))
    staff = cursor.fetchone()
    conn.close()
    return staff
def patient_exists(self, patient_id):
        # Query the database to check if a patient with the given ID exists
        query = "SELECT * FROM patients WHERE patient_id = ?"
        result = self.execute_query(query, (patient_id,))
        return bool(result)  # Returns True if the patient exists, otherwise False
    
def doctor_exists(self, doctor_id):
        # Similar query for doctors
    query = "SELECT * FROM doctors WHERE doctor_id = ?"
    result = self.execute_query(query, (doctor_id,))
    return bool(result)
    
def nurse_exists(self, nurse_id):
        # Similar query for nurses
    query = "SELECT * FROM nurses WHERE nurse_id = ?"
    result = self.execute_query(query, (nurse_id,))
    return bool(result)
    
def staff_exists(self, contact):
    # Check for staff existence using the contact field
    query = "SELECT * FROM staff WHERE contact = ?"
    result = self.execute_query(query, (contact,))
    return bool(result)
def execute_query(self, query, params):
        # Execute the query and return the result
        # Implement database query execution logic here
     pass
def fetch_patient_data():
    """Fetch all patient data from the database."""
    try:
        conn = sqlite3.connect("hospital.db")
        query = "SELECT * FROM patients"
        patient_data = pd.read_sql(query, conn)
        conn.close()
        return patient_data
    except Exception as e:
        print(f"Error fetching patient data: {e}")
        return pd.DataFrame()

def fetch_doctor_data():
    """Fetch all doctor data from the database."""
    try:
        conn = sqlite3.connect("hospital.db")
        query = "SELECT * FROM doctors"
        doctor_data = pd.read_sql(query, conn)
        conn.close()
        return doctor_data
    except Exception as e:
        print(f"Error fetching doctor data: {e}")
        return pd.DataFrame()

def fetch_nurse_data():
    """Fetch all nurse data from the database."""
    try:
        conn = sqlite3.connect("hospital.db")
        query = "SELECT * FROM nurses"
        nurse_data = pd.read_sql(query, conn)
        conn.close()
        return nurse_data
    except Exception as e:
        print(f"Error fetching nurse data: {e}")
        return pd.DataFrame()

def fetch_staff_data():
    """Fetch all staff data from the database."""
    try:
        conn = sqlite3.connect("hospital.db")
        query = "SELECT * FROM staff"
        staff_data = pd.read_sql(query, conn)
        conn.close()
        return staff_data
    except Exception as e:
        print(f"Error fetching staff data: {e}")
        return pd.DataFrame()