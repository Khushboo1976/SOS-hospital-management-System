import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Create the Welcome App Class
class WelcomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to SOS Hospital Management System")
        
        # Full-Screen Mode
        self.root.state('zoomed')
        self.root.configure(bg="#f0f0f0")

        # Load Background Image
        self.bg_image = Image.open(r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\asset\hosp.jpg")
        self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create Background Label
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for Content
        content_frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief="ridge")
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=800, height=500)

        # Welcome Title
        title_label = tk.Label(content_frame, text="WELCOME to\nSOS Hospital management system", font=("Arial", 30, "bold"), fg="#333333", bg="#ffffff")
        title_label.pack(pady=20)

        # About Hospital Section
        about_text = (
            "Our advanced Hospital Management System is designed to sustain and securely manage all patient\n" 
            "and administrative data with utmost precision. Built on a foundation of trust and reliability,\n"
            "it ensures seamless operations, from patient registrations to critical data handling,\n"
            "maintaining the highest standards of confidentiality. This system provides a comprehensive\n"
            "and user-friendly platform for healthcare professionals, delivering an unparalleled level \n"
            "of care and efficiency. Whether it's managing patient records, scheduling appointments, or \n"
            "generating reports, our solution is crafted to meet the dynamic needs of modern healthcare \n"
            "facilities, making it a trusted partner in delivering quality healthcare services.\n"
        )
        about_label = tk.Label(content_frame, text=about_text, font=("Arial", 12), fg="#555555", bg="#ffffff", justify="center")
        about_label.pack(pady=10)

        # About Foundation Section
        foundation_text = (
            "We focus on innovative healthcare solutions, patient care, and community outreach programs."
        )
        foundation_label = tk.Label(content_frame, text=foundation_text, font=("Arial", 12), fg="#555555", bg="#ffffff", justify="center")
        foundation_label.pack(pady=10)

        # Login Button
        login_button = tk.Button(content_frame, text="Login to Your Account", font=("Arial", 14, "bold"), bg="#007BFF", fg="#ffffff", command=self.goto_login)
        login_button.pack(pady=10)

        # New Patient Login Button
        patient_login_button = tk.Button(content_frame, text="Patient Login", font=("Arial", 14, "bold"), bg="#28A745", fg="#ffffff", command=self.goto_patient_login)
        patient_login_button.pack(pady=10)

    # Function to go to the login page (Admin/Staff)
    def goto_login(self):
        try:
            # Destroy the welcome window
            self.root.destroy()
            
            # Define the correct path to the main.py file
            main_file_path = r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\main.py"
            
            # Check if the file exists
            if os.path.exists(main_file_path):
                os.system(f'python "{main_file_path}"')
            else:
                print(f"Error: {main_file_path} not found.")
        except Exception as e:
            print(f"Error opening login page: {e}")

    # Function to go to the patient login page
    def goto_patient_login(self):
        try:
            # Destroy the welcome window
            self.root.destroy()
            
            # Define the correct path to the patient login page (patient_login.py)
            patient_login_file_path = r"C:\Users\HP\OneDrive\Learning Path kg\python\SOS Hospital management system\patient_login.py"
            
            # Check if the file exists
            if os.path.exists(patient_login_file_path):
                os.system(f'python "{patient_login_file_path}"')
            else:
                print(f"Error: {patient_login_file_path} not found.")
        except Exception as e:
            print(f"Error opening patient login page: {e}")

# Main entry point of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WelcomeApp(root)  # Properly instantiate the WelcomeApp class
    root.mainloop()

