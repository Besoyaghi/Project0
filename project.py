import tkinter as tk
from tkinter import filedialog, messagebox

# Mock data
schools = [{"name": "Dubai School A", "rating": "Outstanding", "fees": "AED 40,000"},
           {"name": "Dubai School B", "rating": "Good", "fees": "AED 30,000"}]
universities = [{"name": "UAE University", "deadline": "March 2025", "scholarships": "Available"},
                {"name": "Dubai University", "deadline": "April 2025", "scholarships": "Limited"}]

def upload_documents():
    file = filedialog.askopenfilename()
    if file:
        messagebox.showinfo("Upload Successful", f"Document {file} uploaded for attestation.")

def search_schools():
    school_list = "\n".join([f"{s['name']} - {s['rating']} - {s['fees']}" for s in schools])
    messagebox.showinfo("Schools", school_list)

def search_universities():
    uni_list = "\n".join([f"{u['name']} - Deadline: {u['deadline']} - Scholarships: {u['scholarships']}" for u in universities])
    messagebox.showinfo("Universities", uni_list)

def parent_teacher_communication():
    messagebox.showinfo("Feature", "Interactive Parent-Teacher Communication is under development.")

# Main Window
root = tk.Tk()
root.title("Dubai Schools App")
root.geometry("500x400")

# Title
title = tk.Label(root, text="Dubai Schools App", font=("Arial", 20))
title.pack(pady=20)

# Buttons
btn_attestation = tk.Button(root, text="Online Attestation", font=("Arial", 14), command=upload_documents)
btn_attestation.pack(pady=10)

btn_search_schools = tk.Button(root, text="Search Schools", font=("Arial", 14), command=search_schools)
btn_search_schools.pack(pady=10)

btn_search_universities = tk.Button(root, text="Search Universities", font=("Arial", 14), command=search_universities)
btn_search_universities.pack(pady=10)

btn_communication = tk.Button(root, text="Parent-Teacher Communication", font=("Arial", 14), command=parent_teacher_communication)
btn_communication.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", font=("Arial", 14), command=root.destroy)
btn_exit.pack(pady=20)

# Run App
root.mainloop()
