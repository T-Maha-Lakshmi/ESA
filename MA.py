import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

class MedicalAppointmentScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Appointment Scheduler")
        
        # Initialize variables
        self.patient_records = {}
        
        # Create tabs
        self.tabControl = ttk.Notebook(root)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text='Schedule Appointment')
        self.tabControl.add(self.tab2, text='Patient Records')
        self.tabControl.pack(expand=1, fill="both")
        
        # Tab 1: Schedule Appointment
        self.schedule_appointment_frame = ttk.LabelFrame(self.tab1, text="Schedule Appointment")
        self.schedule_appointment_frame.grid(row=0, column=0, padx=10, pady=10)
        
        # Appointment Date
        self.appointment_date_label = ttk.Label(self.schedule_appointment_frame, text="Appointment Date:")
        self.appointment_date_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.appointment_date_entry = ttk.Entry(self.schedule_appointment_frame)
        self.appointment_date_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Appointment Time
        self.appointment_time_label = ttk.Label(self.schedule_appointment_frame, text="Appointment Time:")
        self.appointment_time_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.appointment_time_entry = ttk.Entry(self.schedule_appointment_frame)
        self.appointment_time_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Patient Name
        self.patient_name_label = ttk.Label(self.schedule_appointment_frame, text="Patient Name:")
        self.patient_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.patient_name_entry = ttk.Entry(self.schedule_appointment_frame)
        self.patient_name_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Submit Button
        self.submit_button = ttk.Button(self.schedule_appointment_frame, text="Schedule Appointment", command=self.schedule_appointment)
        self.submit_button.grid(row=3, columnspan=2, padx=5, pady=10)
        
        # Tab 2: Patient Records
        self.patient_records_frame = ttk.LabelFrame(self.tab2, text="Patient Records")
        self.patient_records_frame.grid(row=0, column=0, padx=10, pady=10)
        
        # Patient Records Listbox
        self.patient_records_listbox = tk.Listbox(self.patient_records_frame, width=60, height=20)
        self.patient_records_listbox.grid(row=0, column=0, padx=5, pady=5)
        
        # Populate patient records initially
        self.populate_patient_records_listbox()
        
    def schedule_appointment(self):
        appointment_date = self.appointment_date_entry.get()
        appointment_time = self.appointment_time_entry.get()
        patient_name = self.patient_name_entry.get()
        
        if not appointment_date or not appointment_time or not patient_name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        appointment_datetime = f"{appointment_date} {appointment_time}"
        
        try:
            appointment_datetime = datetime.strptime(appointment_datetime, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Invalid date or time format. Please use YYYY-MM-DD HH:MM.")
            return
        
        self.patient_records_listbox.insert(tk.END, f"Appointment: {appointment_datetime} - Patient: {patient_name}")
        self.patient_records[appointment_datetime] = patient_name
        
        messagebox.showinfo("Success", "Appointment scheduled successfully.")
        
        # Clear input fields
        self.appointment_date_entry.delete(0, tk.END)
        self.appointment_time_entry.delete(0, tk.END)
        self.patient_name_entry.delete(0, tk.END)
    
    def populate_patient_records_listbox(self):
        for appointment_datetime, patient_name in self.patient_records.items():
            self.patient_records_listbox.insert(tk.END, f"Appointment: {appointment_datetime} - Patient: {patient_name}")

# Initialize Tkinter
root = tk.Tk()
app = MedicalAppointmentScheduler(root)
root.mainloop()
