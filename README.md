# CGPA-Calculator

---
This is a simple graphical CGPA (Cumulative Grade Point Average) calculator created using Python and the `Tkinter` library. It allows users to input their course names, credit hours, and grades, and calculates the CGPA based on the provided information.

## Features

- Input multiple courses with their credit hours and grades.
- Add more courses dynamically by clicking "Add Course".
- Calculates the CGPA based on the grades and credits provided.
- Displays the calculated CGPA instantly.

## How It Works

<!-- ### Formula -->

<!-- The formula for calculating the CGPA is:

\[
\text{CGPA} = \frac{\sum (\text{Credits of each course} \times \text{Grade Points of each course})}{\sum (\text{Credits of all courses})}
\]

Where the grade points are assigned based on the following grading system:

| Grade | Grade Points |
|-------|--------------|
| A+    | 10           |
| A     | 9            |
| B+    | 8            |
| B     | 7            |
| C     | 6            |
| D     | 5            |
| F     | 0            | -->

### Steps:

1. **Adding Courses**: 
   - You can add more courses by clicking the "Add Course" button.
   - Each course consists of the course name, the credit hours, and the grade received.
   
2. **Input Validation**:
   - The credit hours should be a numeric value.
   - Grades should be selected from a pre-defined dropdown (A+, A, B+, B, C, D, F).
   
3. **Calculate CGPA**:
   - The "Calculate CGPA" button computes the CGPA based on the provided information.
   - If there are any errors (e.g., invalid input, or total credits being zero), an error message will be displayed.

<!-- ### Example: -->


## Running the Application

### Prerequisites

- Python installed on your machine.
- `Tkinter` library (comes pre-installed with most Python distributions).

### How to Use:

1. Download the code.
2. Run the Python script (`python cgpa_calculator.py`).
3. The graphical window will open where you can start adding your course details.
4. After entering the course names, credits, and grades, click on the **Calculate CGPA** button to get the result.

## Code Structure

The application is built using the `Tkinter` library. The main components of the code are:

- **cpga_calculator()**: This function calculates the CGPA based on the total credits and grade points.
- **add_course_row()**: This function dynamically adds more rows to the form for additional courses.
- **Grade points dictionary**: It maps the letter grades (A+, A, B+, etc.) to numerical values (10, 9, 8, etc.).

<!-- ## Screenshots -->


---