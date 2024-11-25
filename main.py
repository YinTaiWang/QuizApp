import os
import sys
import importlib
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

# Add the 'quizzes' folder to the system path for importing modules
if not os.path.exists('./quizzes'):
    os.makedirs('./quizzes')
    messagebox.showinfo("Info", "The 'quizzes' folder has been created. Add quiz files to start.")
sys.path.append('./quizzes')

def load_quiz(file_name):
    global quiz_data, current_question, score
    try:
        # Clear all widgets in the options_frame
        for widget in options_frame.winfo_children():
            widget.destroy()

        # Dynamically import the selected Python file
        module_name = file_name.replace('.py', '')
        quiz_module = importlib.import_module(module_name)
        importlib.reload(quiz_module)

        # Validate quiz data
        if not hasattr(quiz_module, 'quiz_data'):
            messagebox.showerror("Error", f"The selected quiz file '{file_name}' does not contain valid quiz data.")
            return

        # Load quiz data
        quiz_data = quiz_module.quiz_data
        current_question = 0
        score = 0

        # Reset feedback and score display
        feedback_label_correctness.config(text="")
        feedback_label_explanation.config(text="")
        score_label.config(text="Score: 0/{}".format(len(quiz_data)))
        score_label.pack(side="left", padx=10)
        next_btn.pack(side="left", padx=10)

        # Start the quiz
        show_question()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load quiz: {e}")

def show_file_selection():
    title_label.config(text="Select a Quiz File")
    qs_label.config(text="Choose a quiz file to start.")
    feedback_label_correctness.config(text="")
    feedback_label_explanation.config(text="")
    next_btn.pack_forget()
    score_label.pack_forget()

    for widget in options_frame.winfo_children():
        widget.destroy()

    files = [f for f in os.listdir('./quizzes') if f.endswith('.py')]
    if not files:
        qs_label.config(text="No quiz files found in the directory.")
        return
    
    for file in files:
        display_name = file.replace('.py', '')
        button = ttk.Button(options_frame, text=display_name, command=lambda f=file: load_quiz(f))
        button.pack(pady=5)

def show_question():
    global choice_btns
    if not quiz_data:
        qs_label.config(text="No quiz data loaded!")
        return

    question = quiz_data[current_question]
    title_label.config(text=f"Question {current_question + 1}")
    qs_label.config(text=question["question"])

    for btn in choice_btns:
        btn.destroy()

    choice_btns = []
    for i, option in enumerate(question["options"]):
        button = ttk.Button(options_frame, text=option, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    feedback_label_correctness.config(text="")
    feedback_label_explanation.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question = quiz_data[current_question]
    selected_button = choice_btns[choice]  # Get the selected button
    selected_choice = selected_button.cget("text")  # Get the button text

    if selected_choice.startswith(question["answer"]):
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label_correctness.config(text="Correct!", foreground="green")
        # Change the selected button's color to green
        selected_button.configure(bootstyle="success")
    else:
        feedback_label_correctness.config(text="Incorrect!", foreground="red")
        # Change the selected button's color to red
        selected_button.configure(bootstyle="danger")

    feedback_label_explanation.config(text=question.get("explanation", ""), foreground="black")

    # Disable all other buttons except the selected one
    for i, button in enumerate(choice_btns):
        if i != choice:
            button.config(state="disabled")

    # Enable the Next button
    next_btn.config(state="normal")


def next_question():
    global current_question
    current_question += 1
    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed", f"Final score: {score}/{len(quiz_data)}")
        root.destroy()

####################################################################################

# Screen customize
width = 1200
height = 800

### Main Window ###
root = tk.Tk()
root.title("Quiz App")
root.geometry(f"{width}x{height}")
style = Style(theme="flatly")
style.configure("success.TButton", background="green", foreground="white")
style.configure("danger.TButton", background="red", foreground="white")
style.configure("TLabel", font=("Helvetica", 15))
style.configure("TButton", font=("Helvetica", 13))
# title
title_label = ttk.Label(root, text="Quiz App", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

### Frames ###
# question
qs_label = ttk.Label(root, anchor="center", wraplength=width-100, padding=10)
qs_label.pack(pady=10)

# options
options_frame = ttk.Frame(root)
options_frame.pack(pady=10)

# feedback
feedback_label_correctness = ttk.Label(root, anchor="center", padding=10)
feedback_label_correctness.pack(pady=5)
feedback_label_explanation = ttk.Label(root, anchor="center", wraplength=width-100, padding=10)
feedback_label_explanation.pack(pady=5)
footer_frame = ttk.Frame(root)
footer_frame.pack(pady=10)

# score
score_label = ttk.Label(footer_frame, text="Score: 0/0", anchor="center", padding=10)
next_btn = ttk.Button(footer_frame, text="Next", command=next_question, state="disabled")

### Initialize dynamic components ###
choice_btns = []
quiz_data = []
current_question = 0
score = 0

show_file_selection()
root.mainloop()
