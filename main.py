from database import (  # Import your functions from the database module
    add_patient, add_doctors, add_nurses, add_staff, fetch_doctor_data, fetch_nurse_data, fetch_patient_data, fetch_staff_data
)
import re
import tkinter as tk
from tkinter import Button, Frame, Label, messagebox, Toplevel
from tkinter import ttk
from PIL import Image, ImageTk
import database
from tkinter import simpledialog
import os
from twilio.rest import Client
from csv_backend import CSVBackend
import pandas as pd
csv_backend = CSVBackend()
database.create_database()
def set_background(root, image_path):
    root.update()

    if not os.path.exists(image_path):
        print(f"Error: Image path does not exist - {image_path}")
        return

    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((root.winfo_width(), root.winfo_height()), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.lower()

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Hospital Management System")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)

        # Create and set the background image
        self.bg_image = Image.open(r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\asset\check.jpg")
        self.bg_label = tk.Label(self.root)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Centralize the login form (username, password, login button)
        self.frame = tk.Frame(self.root, bg="light blue", padx=20, pady=20)  # Create a frame to contain the form elements
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Label and Entry for Username
        self.label_username = tk.Label(self.frame, text="Username", font=("Arial", 16), width=15, anchor="w")
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username = tk.Entry(self.frame, font=("Arial", 14), width=25)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        # Label and Entry for Password
        self.label_password = tk.Label(self.frame, text="Password", font=("Arial", 16), width=15, anchor="w")
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password = tk.Entry(self.frame, show="*", font=("Arial", 14), width=25)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        # Login Button
        self.button_login = tk.Button(self.frame, text="Login", command=self.login, font=("Arial", 14), width=20, height=2)
        self.button_login.grid(row=2, columnspan=2, pady=20)

        self.update_background()  # Ensure the background is updated to the current window size

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode."""
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)

    def login(self):
        """Perform login."""
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        if database.verify_user(username, password):
            messagebox.showinfo("Success", "Login Successful!")
            self.root.withdraw()
            HospitalManagementApp(Toplevel(self.root))
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def update_background(self):
        """Update the background image to fit the window size."""
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        resized_image = self.bg_image.resize((window_width, window_height))
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo  # Keep a reference to the image
        self.root.after(100, self.update_background)


class HospitalManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)

        self.root.geometry("1920x1080")  # Increased size for better visibility
        self.root.after(100, lambda: set_background(self.root, r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\asset\hosp.jpg"))
        top_frame = tk.Frame(self.root, bg="#f0f0f0")
        top_frame.pack(side=tk.TOP, fill=tk.X)

        logout_button = tk.Button(top_frame, text="Logout", command=self.logout, font=("Arial", 10), bg="#ff4d4d", fg="white")
        logout_button.pack(side=tk.RIGHT, padx=10, pady=5)

        options_frame = tk.Frame(self.root)
        options_frame.pack(expand=True)
        tk.Button(options_frame, text="Manage Patients", command=self.open_patient_screen, width=30, font=("Arial", 16), bg="#4CAF50", fg="white").pack(pady=15)
        tk.Button(options_frame, text="Manage Doctors", command=self.open_doctor_screen, width=30, font=("Arial", 16), bg="#4CAF50", fg="white").pack(pady=15)
        tk.Button(options_frame, text="Manage Nurses", command=self.open_nurse_screen, width=30, font=("Arial", 16), bg="#4CAF50", fg="white").pack(pady=15)
        tk.Button(options_frame, text="Manage Staff", command=self.open_staff_screen, width=30, font=("Arial", 16), bg="#4CAF50", fg="white").pack(pady=15)
        # SOS button to send the message
        tk.Button(options_frame, text="SOS Alert", command=self.send_sos_message, width=30, font=("Arial", 16), bg="#4CAF50", fg="white").pack(pady=15)

    def send_sos_message(self):
        """Send an SOS message via Twilio."""
        # Fetch Twilio credentials from environment variables for security
        account_sid = os.getenv('TWILIO_ACCOUNT_SID','ACea05dc78f030d21387589815c8a9ee20')  # Replace with actual account SID
        auth_token = os.getenv('TWILIO_AUTH_TOKEN','132bf9639846d9ad8e4e285fdad5c00a')  # Replace with actual auth token
        messaging_service_sid = os.getenv('TWILIO_MESSAGING_SERVICE_SID','MG2fdb30db268992b5cbff75123db06543')  # Replace with actual SID
        to_phone_number = '+919354226150'  # Replace with the verified recipient's phone number

        if not all([account_sid, auth_token, messaging_service_sid]):
            messagebox.showerror("Error", "Twilio credentials are missing!")
            return

        try:
            # Initialize Twilio Client
            client = Client(account_sid, auth_token)

            # Sending the SOS message
            message = client.messages.create(
                messaging_service_sid=messaging_service_sid,
                body="Emergency! We are short of staff right now. Could you please help us.\n Please respond as soon as possible.",
                to=to_phone_number
            )

            messagebox.showinfo("Success", "SOS message sent successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send SOS message: {e}")

        

    def toggle_fullscreen(self, event=None):
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)

    def open_patient_screen(self):
        DataManagementApp(Toplevel(self.root), "Patient")

    def open_doctor_screen(self):
        DataManagementApp(Toplevel(self.root), "Doctor")

    def open_nurse_screen(self):
        DataManagementApp(Toplevel(self.root), "Nurse")

    def open_staff_screen(self):
        DataManagementApp(Toplevel(self.root), "Staff")

    def logout(self):
        self.root.withdraw()
        login_window = Toplevel(self.root)
        LoginApp(login_window)
        
class DataManagementApp:
    def __init__(self, root, data_type):
        self.root = root
        self.data_type = data_type
        self.root.title(f"{data_type} Management")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", self.toggle_fullscreen)

        self.root.geometry("1920x1080")  # Increased size for better visibility
        if self.data_type == "Patient":
            self.root.after(100, lambda: set_background(self.root, r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\asset\hos.jpg"))
        elif self.data_type == "Doctor":
            self.root.after(100, lambda: set_background(self.root, r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\asset\nur.jpg"))
        elif self.data_type == "Nurse":
            self.root.after(100, lambda: set_background(self.root, r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\asset\st.jpg"))
        elif self.data_type == "Staff":
            self.root.after(100, lambda: set_background(self.root, r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\asset\treatment.jpg"))

        fields = {
            "Patient": ["Name", "Age", "Gender", "Contact", "Health Issue"],
            "Doctor": ["Name", "Age", "Gender", "Contact", "Specialization", "Timing"],
            "Nurse": ["Name", "Age", "Gender", "Contact", "Floor", "Shift"],
            "Staff": ["Name", "Age", "Gender", "Contact", "Post", "Shift"]
        }

        self.entries = {}
        for idx, label in enumerate(fields[self.data_type]):
            tk.Label(self.root, text=label, font=("Arial", 16), anchor="center").grid(row=idx, column=0, padx=10, pady=10, sticky="ew")
            
            if label == "Gender":
                gender_combobox = ttk.Combobox(self.root, values=["Male", "Female", "Other"], font=("Arial", 16, "bold"))
                gender_combobox.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")
                self.entries[label] = gender_combobox
            elif label == "Shift" and self.data_type in ["Nurse", "Staff"]:
                shift_combobox = ttk.Combobox(self.root, values=["Morning Shift", "Evening Shift", "Night Shift"], font=("Arial", 16, "bold"))
                shift_combobox.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")
                self.entries[label] = shift_combobox
            elif label == "Specialization" and self.data_type == "Doctor":
                specialization_combobox = ttk.Combobox(self.root, values=["ENT", "Cardiology", "Orthopedics", "Neurology", "Pediatrics", "General Medicine"], font=("Arial", 16, "bold"))
                specialization_combobox.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")
                self.entries[label] = specialization_combobox
            elif label == "Timing" and self.data_type == "Doctor":
    # Add 24-hour shift slots with 4-hour intervals
                time_slots = [
                    "00:00 AM - 04:00 AM", "04:00 AM - 08:00 AM", "08:00 AM - 12:00 PM", "12:00 PM - 04:00 PM", 
                    "04:00 PM - 08:00 PM", "08:00 PM - 12:00 AM"
                ]
                timing_combobox = ttk.Combobox(self.root, values=time_slots, font=("Arial", 16, "bold"))
                timing_combobox.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")
                self.entries[label] = timing_combobox
            elif label == "Post" and self.data_type == "Staff":
    # Add post options for Staff
                post_combobox = ttk.Combobox(self.root, values=["Ambulance Driver", "Watchman", "Cleaner", "Receptionist"], font=("Arial", 16, "bold"))
                post_combobox.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")
                self.entries[label] = post_combobox
            elif label == "Floor" and self.data_type == "Nurse":
    # Add floor options for Nurse
                floor_combobox = ttk.Combobox(self.root, values=["1st Floor", "2nd Floor", "3rd Floor", "4th Floor"], font=("Arial", 16, "bold"))
                floor_combobox.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")
                self.entries[label] = floor_combobox
            else:
                entry = tk.Entry(self.root, font=("Arial", 16, "bold"))
                entry.grid(row=idx, column=1, padx=10, pady=10, sticky="ew")
                self.entries[label] = entry
        # Modified buttons for centralizing and increasing font size
        tk.Button(self.root, text="Add", command=self.add_data, font=("Arial", 16), bg="#4CAF50", fg="white").grid(row=len(fields[self.data_type]), column=0, columnspan=3, pady=15, padx=15, sticky="ew")
        tk.Button(self.root, text="View All", command=self.view_data, font=("Arial", 16), bg="#4CAF50", fg="white").grid(row=len(fields[self.data_type]) + 1, column=0, columnspan=3, pady=15, padx=15, sticky="ew")
        tk.Button(self.root, text="Search", command=self.search_data, font=("Arial", 16), bg="#4CAF50", fg="white").grid(row=len(fields[self.data_type]) + 2, column=0, columnspan=3, pady=15, padx=15, sticky="ew")
        tk.Button(self.root, text="Download Data", command=self.download_data, font=("Arial", 16), bg="#4CAF50", fg="white").grid(row=len(fields[self.data_type]) + 3, column=0, columnspan=3, pady=15, padx=15, sticky="ew")
        main_menu_button = tk.Button(self.root, text="Main Menu", command=self.open_main_menu, font=("Arial", 16), bg="#ff4d4d", fg="white")
        main_menu_button.grid(row=len(fields[self.data_type]) + 4, column=0, columnspan=3, pady=15, padx=15, sticky="ew")
        main_menu_button.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
  # Position the main menu button at the top-left corner

    def toggle_fullscreen(self, event=None):
        """Toggle fullscreen mode."""
        current_state = self.root.attributes('-fullscreen')
        self.root.attributes('-fullscreen', not current_state)

    def back_to_main_menu(self):
        """Navigate back to the main menu."""
        self.root.withdraw()
        main_menu_window = Toplevel(self.root)
        HospitalManagementApp(main_menu_window)

    def open_main_menu(self):
        """Opens the Main Menu"""
        self.root.withdraw()
        main_menu_window = Toplevel(self.root)
        HospitalManagementApp(main_menu_window)

    def add_data(self):
    # Retrieve the values from entry fields
        values = [entry.get().strip() for entry in self.entries.values()]

    # Check if any field is empty (i.e., contains a null or empty value)
        if any(not value for value in values):
            messagebox.showerror("Error", f"All fields for {self.data_type} must be filled!")
            return

    # Validate Name (No special characters allowed)
        name = values[0]  # Assuming name is the first field
        if not re.match("^[A-Za-z ]+$", name):
            messagebox.showerror("Error", "Name should only contain letters and spaces!")
            return
    
        contact = values[3]  # Assuming contact number is the fourth field
        if len(contact) != 10 or not contact.isdigit():
            messagebox.showerror("Error", "Contact number must be exactly 10 digits!")
            return
        if self.data_type == "Patient":
            self.add_patient_data(values)
        elif self.data_type == "Doctor":
            self.add_doctor_data(values)
        elif self.data_type == "Nurse":
            self.add_nurse_data(values)
        elif self.data_type == "Staff":
            self.add_staff_data(values)

    def add_patient_data(self, values):
        # Add patient data to the database
        name, age, gender, contact, health_issue = values
        add_patient(name, age, gender, contact, health_issue)  # Call the function from database module
        messagebox.showinfo("Success", "Patient added successfully")
        self.clear_all_fields()

    def add_doctor_data(self, values):
        # Add doctor data to the database
        name, age, gender, contact, sp, timing = values
        add_doctors(name, age, gender, contact, sp, timing)  # Call the function from database module
        messagebox.showinfo("Success", "Doctor added successfully")
        self.clear_all_fields()

    def add_nurse_data(self, values):
        # Add nurse data to the database
        name, age, gender, contact, floor, shift = values
        add_nurses(name, age, gender, contact, floor, shift)  # Call the function from database module
        messagebox.showinfo("Success", "Nurse added successfully")
        self.clear_all_fields()

    def add_staff_data(self, values):
        # Add staff data to the database
        name, age, gender, contact, post, shift = values
        add_staff(name, age, gender, contact, post, shift)  # Call the function from database module
        messagebox.showinfo("Success", "Staff added successfully")
        self.clear_all_fields()
        
    # Validate Age (3-digit number)
        age = values[1]  # Assuming age is the second field
        if not age.isdigit() or not (1 <= int(age) <= 999):
            messagebox.showerror("Error", "Age must be a valid 3-digit number!")
            return

        if self.data_type == "Doctor":
            shift_timing = values[5]
            if shift_timing not in ["00:00 AM - 04:00 AM", "04:00 AM - 08:00 AM", "08:00 AM - 12:00 PM", "12:00 PM - 04:00 PM", "04:00 PM - 08:00 PM", "08:00 PM - 12:00 AM"]:
                messagebox.showerror("Error", "Please select a valid shift timing for the doctor!")
                return
        
            specialization = values[4]
            if specialization not in ["ENT", "Cardiology", "Orthopedics", "Neurology", "Pediatrics", "General Medicine"]:
                messagebox.showerror("Error", "Please select a valid specialization for the doctor!")
                return

    # If the data type is "Nurse" or "Staff", validate the shift timing
        if self.data_type in ["Nurse", "Staff"]:
            shift = values[5]
            if shift not in ["Morning Shift", "Evening Shift", "Night Shift"]:
                messagebox.showerror("Error", "Please select a valid shift for the Nurse or Staff!")
                return
    
        print(f"Adding {self.data_type} data: {values}")

    # Check for duplicates based on unique fields (e.g., Patient ID, Doctor ID, etc.)
        if self.data_type == "Patient":
            if database.patient_exists(values[0]):  # Assuming Patient ID is the first field
                messagebox.showerror("Error", "Patient already exists in the database!")
                return
            database.add_patient(*values)
    
        elif self.data_type == "Doctor":
            if database.doctor_exists(values[0]):  # Assuming Doctor ID is the first field
                messagebox.showerror("Error", "Doctor already exists in the database!")
                return
            database.add_doctor(*values)  # Corrected from 'add_doctors' to 'add_doctor' (singular)
    
        elif self.data_type == "Nurse":
            if len(values) == 6:
                if database.nurse_exists(values[0]):  # Assuming Nurse ID is the first field
                    messagebox.showerror("Error", "Nurse already exists in the database!")
                    return
                database.add_nurse(*values)  # Corrected from 'add_nurses' to 'add_nurse' (singular)
            else:
                messagebox.showerror("Error", "Missing data for Nurse entry.")
                return
    

    # Success message after adding the data
        messagebox.showinfo("Success", f"{self.data_type} added successfully")
        self.clear_all_fields()

    def clear_all_fields(self):
    # Loop through all the entry widgets and clear their content
        for entry in self.entries.values():
            entry.delete(0, tk.END)  # Clear entry fields
    
    # Reset combo boxes, if present
        if hasattr(self, 'gender_combobox'):
            self.gender_combobox.set('')  # Reset gender combobox
        if hasattr(self, 'specialization_combobox'):
            self.specialization_combobox.set('')  # Reset specialization combobox
        if hasattr(self, 'shift_combobox'):
            self.shift_combobox.set('')  # Reset shift combobox

    # Reset any other widgets like checkboxes, if present
        if hasattr(self, 'morning_shift_var'):
            self.morning_shift_var.set(False)  # Example of a checkbox variable reset
        if hasattr(self, 'evening_shift_var'):
            self.evening_shift_var.set(False)  # Reset another checkbox, if present

    # Reset any other fields you might have
        if hasattr(self, 'name_entry'):
            self.name_entry.delete(0, tk.END)  # Reset any specific entry if needed
        if hasattr(self, 'age_entry'):
            self.age_entry.delete(0, tk.END)  # Reset any specific entry if needed
        if hasattr(self, 'shift_combobox'):
            self.shift_combobox.set('')  # Reset shift selection combobox
        if hasattr(self, 'date_entry'):
            self.date_entry.set('')  # Example for date fields or date pickers, reset the date
    
    # Optionally reset other form elements as per your requirements (e.g., radio buttons, text boxes)
        if hasattr(self, 'notes_textbox'):
            self.notes_textbox.delete(1.0, tk.END)  # Reset any text box

    def view_data(self):
        data = []
        if self.data_type == "Patient":
            data = database.get_all_patients()
        elif self.data_type == "Doctor":
            data = database.get_doctors()
        elif self.data_type == "Nurse":
            data = database.get_nurses()
        elif self.data_type == "Staff":
            data = database.get_staff()

        if not data:
            messagebox.showerror("Error", f"No data found for {self.data_type}.")
        else:
            self.show_table(data)
    def download_data(self):
        """Download all data from the selected table."""
        try:
            # Map the selected data type to the corresponding backend fetch function
            fetch_functions = {
                "Patient": fetch_patient_data,
                "Doctor": fetch_doctor_data,
                "Nurse": fetch_nurse_data,
                "Staff": fetch_staff_data
            }

            # Fetch the data using the appropriate function
            if self.data_type in fetch_functions:
                data = fetch_functions[self.data_type]()
            else:
                raise ValueError("Invalid data type selected.")

            # Save the data as a CSV file
            file_path = f"{self.data_type}_data.csv"
            data.to_csv(file_path, index=False)
            messagebox.showinfo("Success", f"{self.data_type} data downloaded successfully as {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download data: {e}")
    def search_data(self):
        search_id = simpledialog.askstring("Search", f"Enter {self.data_type} ID")
        if not search_id:
            return
        data = None
        if self.data_type == "Patient":
            data = database.search_patient(search_id)
        elif self.data_type == "Doctor":
            data = database.search_doctors(search_id)
        elif self.data_type == "Nurse":
            data = database.search_nurses(search_id)
        elif self.data_type == "Staff":
            data = database.search_staff(search_id)

        if data:
            messagebox.showinfo("Search Result", f"Data: {data}")
        else:
            messagebox.showerror("Error", "No data found")
    
    def show_table(self, data):
        table_window = Toplevel(self.root)
        table_window.title(f"{self.data_type} Data")

        # Create a Treeview widget
        table = ttk.Treeview(table_window, show="headings")
        table.pack(fill=tk.BOTH, expand=True)

        columns = []  # Define columns dynamically based on data type
        if self.data_type == "Patient":
            columns = ["id","Name", "Age", "Gender", "Contact", "Health Issue"]
        elif self.data_type == "Doctor":
            columns = ["id","Name", "Age", "Gender", "Contact", "Specialization", "Timing"]
        elif self.data_type == "Nurse":
            columns = ["id","Name", "Age", "Gender", "Contact", "Floor", "Shift"]
        elif self.data_type == "Staff":
            columns = ["id","Name", "Age", "Gender", "Contact", "Post", "Shift"]

        table["columns"] = columns
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=150, anchor="w")

        # Insert data into the table
        for row in data:
            table.insert("", tk.END, values=row)

        # Dynamically adjust the column widths based on the maximum length of the data
        for col in columns:
            max_len = max(len(col), max((len(str(item)) for item in [row[columns.index(col)] for row in data]), default=0))
            table.column(col, width=max_len * 10)

if __name__ == "__main__":
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()