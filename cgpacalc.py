# ===============================================
#  SGPA / CGPA Calculator (Updated for Custom Credits)
# PRATAP KHANDELWAL
# Template for University Students
# ===============================================

def grade_and_point(marks):
    """Calculates the letter grade and grade point based on marks."""
    if marks >= 90:
        return "A+", 10
    elif marks >= 80:
        return "A", 9
    elif marks >= 70:
        return "B+", 8
    elif marks >= 60:
        return "B", 7
    elif marks >= 50:
        return "C", 6
    elif marks >= 40:
        return "D", 4
    else:
        return "F", 0

def safe_float_input(prompt, max_value=None):
    """Handles invalid input (non-numeric or negative) and optional max value check."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Value cannot be negative. Please try again.")
                continue
            if max_value is not None and value > max_value:
                print(f"Error: Value cannot exceed {max_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

# Updated subject list - credit values removed from tuples to be asked via input
subjects = [
    ("Subject 1", "theory"),
    ("Subject 2", "theory"),
    ("Subject 3", "practical"),
    ("Subject 4", "theory"),
    ("Subject 5", "theory"),
    ("Subject 6", "theory"),
    ("Subject 7", "practical"),
    ("SPECIALIZATION", "theory")
]

OPTIONAL_SUBJECT_NAME = "SPECIALIZATION"

print("\n===== SGPA CALCULATOR =====")
print(" Class: CSE DEPARTMENT\n")

# ---- COMMON INTERNAL ASSESSMENT INPUT ----
internal_assessment = safe_float_input(
    "Enter your Common Internal Assessment marks (out of 30): ", max_value=30
)

total_credit_points = 0
total_credits = 0

for subject_name, category in subjects:
    print(f"\n--- Subject: **{subject_name}** | Category: {category.upper()} ---")

    # --- OPTIONAL SUBJECT CHECK ---
    if subject_name == OPTIONAL_SUBJECT_NAME:
        is_taken = input(f"Did you take {subject_name}? (y/n): ").strip().lower()
        if is_taken not in ['yes', 'y']:
            print(f"--> Skipping optional subject: {subject_name}.")
            continue 

    # --- NEW: ASK FOR SUBJECT CREDITS ---
    credit = safe_float_input(f"Enter credits for {subject_name}: ")

    if category == "theory":
        mid = safe_float_input("Mid Term Marks (out of 50): ", max_value=50)
        end = safe_float_input("End Sem Marks (out of 100): ", max_value=100)

        mid_scaled = (mid / 50) * 20
        end_scaled = (end / 100) * 50
        final_marks = internal_assessment + mid_scaled + end_scaled

    else:  # practical
        final_marks = safe_float_input("Final Practical Marks (out of 100): ", max_value=100)
        
    grade, point = grade_and_point(final_marks)

    total_credit_points += (credit * point)
    total_credits += credit 

    print(f"Final Marks: {final_marks:.2f}/100")
    print(f"Grade: {grade} | Grade Point: {point}")

# ---- SGPA & Percentage ----
if total_credits > 0:
    sgpa = total_credit_points / total_credits
    percentage = sgpa * 10 
else:
    sgpa = 0.0
    percentage = 0.0

print("\n =============================================================")
print(f"Total Credits: {total_credits}")
print(f"SGPA         : {sgpa:.2f}")
print(f"Percentage   : {percentage:.2f}%")
print("==============================================================")
