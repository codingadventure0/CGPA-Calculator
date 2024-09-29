import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("CGPA Calculator")
root.geometry("600x400")

frame = ttk.Frame(root, padding="10")
frame.pack(expand=1, fill="both")

course_rows = []

def cpga_calculator():
    total_credits = total_grade_points = 0
    grade_points_dict = {"A+":10, "A":9, "B+":8, "B":7, "C":6, "D":5, "F":0}

    labels = ["Course Name", "Credit", "Grade"]
    for i, text in enumerate(labels):
        ttk.Label(frame, text=text, background="yellow", font=("Arial", 12, "bold"))
        Label.grid(row=0, column=i, padx=10, pady=5, sticky="ew")
    
    cgpa = total_grade_points / total_credits
    result.config(text=f"CGPA: {cgpa:.2f}")
    
    
labels = ["Course Name", "Credit", "Grade"]
for i, text in enumerate(labels):
    ttk.Label(frame, text=text, background="yellow", font=("Arial", 12, "bold")).grid(row=0, column=i, padx=10, pady=5, sticky="ew")






root.mainloop()