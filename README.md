# 🏥 SOS Hospital Management System  
### Smart Emergency-Oriented Hospital Management Platform

> A Python-based desktop Hospital Management System integrated with an SOS emergency alert module for rapid response in critical situations.

---

## 🎯 Project Overview

**SO Hospital Management System** is a GUI-based desktop application developed using **Python and Tkinter** to manage hospital operations efficiently.

It includes:

- Patient record management  
- Staff and doctor management  
- Appointment scheduling  
- Treatment tracking  
- 🚨 Integrated SOS Emergency SMS Alert System  

This project demonstrates practical healthcare system design combined with API integration for emergency communication.

---

# 🚨 SOS Emergency Alert Feature

The system includes a built-in **SOS Module** that:

- Sends emergency SMS alerts
- Notifies predefined emergency contacts
- Uses Twilio API for communication
- Reduces response delay during critical medical situations

⚠️ This feature depends on proper API configuration and network availability.

---

# 🌟 Core Features

## 👤 Patient Management
- Add, update, delete patient records  
- Maintain medical history  
- Secure data storage  

## 👨‍⚕️ Doctor & Staff Management
- Manage doctor details  
- Assign departments  
- Track availability  

## 📅 Appointment Scheduling
- Book and manage appointments  
- Prevent scheduling conflicts  

## 💊 Treatment Records
- Diagnosis records  
- Prescription tracking  
- Visit history maintenance  

## 🚨 Emergency SMS Integration
- Twilio API-based alerts  
- Instant message dispatch  
- Configurable emergency contacts  

---

# 🛠️ Tech Stack

- **Language:** Python  
- **GUI Framework:** Tkinter  
- **API Integration:** Twilio SMS API  
- **Database:** (SQLite / MySQL – specify if applicable)  
- **Platform:** Windows Desktop  

---

# 🚀 Installation & Setup

## 1️⃣ Clone Repository

git clone https://github.com/your-username/sos-hospital-management-system.git

cd sos-hospital-management-system

## 2️⃣ Install Dependencies
pip install twilio

## 3️⃣ Configure Twilio Credentials

Add your credentials securely using environment variables:

export TWILIO_ACCOUNT_SID="your_sid"
export TWILIO_AUTH_TOKEN="your_token"

⚠️ Never upload credentials to public repositories.

## 4️⃣ Run Application
python main.py
