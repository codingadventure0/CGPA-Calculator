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

    for course_name, course_credit, grade_list in course_rows:
        try:
            credits = float(course_credit.get())
            grade = grade_list.get()
            
            if grade not in grade_points_dict:
                raise ValueError("Invalid grade selected")
            
            total_credits += credits
            total_grade_points += credits * grade_points_dict[grade]
            
        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid input:{ve}")
            return
    
    if total_credits == 0:
        messagebox.showerror("Error", "Total credits cannot be zero")
        return
    
    cgpa = total_grade_points / total_credits
    result.config(text=f"CGPA: {cgpa:.2f}")
    

def add_course_row(frame):
    row = len(course_rows) + 1
    course_name = tk.Entry(frame, font=("Arial", 10), relief="solid", borderwidth=2)
    course_name.grid(row=row, column=0, padx=10, pady=5, sticky="ew")
    
    course_credit = tk.Entry(frame, font=("Arial", 10), relief="solid", borderwidth=2)
    course_credit.grid(row=row, column=1, padx=10, pady=5, sticky="ew")

    grade_var = tk.StringVar(value="Select Grade")
    grade_list = ttk.Combobox(frame, textvariable=grade_var, values=["A+", "A", "B+", "B", "C", "D", "F"], font=("Arial", 10), state="readonly")
    grade_list.grid(row=row, column=2, padx=10, pady=5, sticky="ew")

    course_rows.append((course_name, course_credit, grade_list))
    
    
labels = ["Course Name", "Credit", "Grade"]
for i, text in enumerate(labels):
    ttk.Label(frame, text=text, background="yellow", font=("Arial", 12, "bold")).grid(row=0, column=i, padx=10, pady=5, sticky="ew")


add_course_row(frame)

ttk.Button(frame, text="Add Course", command=lambda: add_course_row(frame)).grid(row=20, column=0, padx=10, pady=10, sticky="ew")
ttk.Button(frame, text="Calculate CGPA", command=cpga_calculator).grid(row=20, column=1, padx=10, pady=10, sticky="ew")


cgpa_result = ttk.Label(frame, text="CGPA: ", font=("Arial", 12))
cgpa_result.grid(row=21, column=0, columnspan=3, pady=20)

root.mainloop()
