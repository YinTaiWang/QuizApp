import os
import re
import sys
import random
import importlib
import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style

# Add the 'quizzes' folder to the system path for importing modules
if not os.path.exists('./quizzes'):
    os.makedirs('./quizzes')
    messagebox.showinfo("Info", "The 'quizzes' folder has been created. Add quiz files to start.")
sys.path.append('./quizzes')

# Scrolling
def on_frame_configure(event):
    # Update scrollable region dynamically
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))
    
def on_mouse_wheel(event):
    # Enable mouse wheel scrolling
    main_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Quiz
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
        # random.shuffle(quiz_data)  # Randomize the order of questions
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
    global choice_btns, selected_answers
    selected_answers = []  # Reset selected answers for the new question

    if not quiz_data:
        qs_label.config(text="No quiz data loaded!")
        return

    question = quiz_data[current_question]
    title_label.config(text=f"Question {current_question + 1}")
    qs_label.config(text=question["question"])

    # Update the hint label
    num_answers = len(question["answer"]) if isinstance(question["answer"], list) else 1
    answers_hint_label.config(text=f"Select {num_answers} answer{'s' if num_answers > 1 else ''}.")

    # Clear existing buttons
    for btn in choice_btns:
        btn.destroy()

    # Create buttons for options
    choice_btns = []
    for i, option in enumerate(question["options"]):
        button = ttk.Button(options_frame, text=option, command=lambda i=i: check_answer(i))
        button.pack(pady=5)
        choice_btns.append(button)

    feedback_label_correctness.config(text="")
    feedback_label_explanation.config(text="")
    next_btn.config(state="disabled")


def check_answer(choice):
    global selected_answers, score  # Track selected answers
    question = quiz_data[current_question]
    selected_button = choice_btns[choice]
    selected_choice = selected_button.cget("text")  # Get full button text

    # Check if the answer is a list or a single string
    if isinstance(question["answer"], list):
        # If the answer is a list, handle prefixes (e.g., "A. Option")
        if re.match(r"^[A-Z]\.\s", selected_choice):
            selected_prefix = selected_choice.split(".")[0]  # Extract prefix (e.g., "A")
        else:
            selected_prefix = selected_choice  # Use the whole text if no prefix

        # Add selected prefix to the list of selected answers
        if selected_prefix not in selected_answers:
            selected_answers.append(selected_prefix)

        # Check if the selected prefix is correct
        if selected_prefix in question["answer"]:
            feedback_label_correctness.config(text="Correct!", foreground="green")
            selected_button.configure(bootstyle="success")
        else:
            feedback_label_correctness.config(text="Incorrect!", foreground="red")
            selected_button.configure(bootstyle="danger")

        # Check if the user has clicked the same number of options as there are correct answers
        if len(selected_answers) == len(question["answer"]):
            # Evaluate if all selected answers are correct
            if set(selected_answers) == set(question["answer"]):
                score += 1  # Increment the score if all answers are correct
                score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
                feedback_label_correctness.config(text="All answers are correct!", foreground="green")
            else:
                feedback_label_correctness.config(text="Some answers are incorrect.", foreground="red")

            # Show the explanation
            feedback_label_explanation.config(text=question.get("explanation", ""), foreground="black")

            # Disable buttons that are not in selected_answers
            for button in choice_btns:
                if button.cget("text").split(".")[0] not in selected_answers:
                    button.config(state="disabled")
            
            # Enable the Next button
            next_btn.config(state="normal")

    else:
        # If the answer is a single string, compare directly with the full choice text
        if selected_choice.startswith(question["answer"]):
            score += 1
            score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
            feedback_label_correctness.config(text="Correct!", foreground="green")
            selected_button.configure(bootstyle="success")
        else:
            feedback_label_correctness.config(text="Incorrect!", foreground="red")
            selected_button.configure(bootstyle="danger")

        # Disable all buttons after a single choice
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
height = 900

###################
### Main Window ###
###################
# root = tk.Tk()
# root.title("Quiz App")
# root.geometry(f"{width}x{height}")

# # set style
# style = Style(theme="flatly")
# style.configure("success.TButton", background="green", foreground="white")
# style.configure("danger.TButton", background="red", foreground="white")
# style.configure("TLabel", font=("Helvetica", 14))
# style.configure("TButton", font=("Helvetica", 13))
# # title label
# title_label = ttk.Label(root, font=("Helvetica", 16, "bold"))
# title_label.pack(expand=True)

# ##############
# ### Frames ###
# ##############
# # question
# qs_label = ttk.Label(root, anchor="center", wraplength=width-100, padding=10)
# qs_label.pack(pady=10)

# # hint: number of answers
# answers_hint_label = ttk.Label(root, text="", anchor="center", padding=10)
# answers_hint_label.pack(pady=5)

# # options
# options_frame = ttk.Frame(root)
# options_frame.pack(pady=10)

# # feedback
# feedback_label_correctness = ttk.Label(root, anchor="center", padding=10)
# feedback_label_correctness.pack(pady=5)
# feedback_label_explanation = ttk.Label(root, anchor="center", wraplength=width-100, padding=10)
# feedback_label_explanation.pack(pady=5)

# # footer
# footer_frame = ttk.Frame(root)
# footer_frame.pack(pady=10)
# # score
# score_label = ttk.Label(footer_frame, text="Score: 0/0", anchor="center", padding=10)
# # next button
# next_btn = ttk.Button(footer_frame, text="Next", command=next_question, state="disabled")

# ### Initialize dynamic components ###
# choice_btns = []
# quiz_data = []
# current_question = 0
# score = 0

# show_file_selection()
# root.mainloop()


###################
### Main Window ###
###################
root = tk.Tk()
root.title("Quiz App")
root.geometry(f"{width}x{height}")

# set style
style = Style(theme="flatly")
style.configure("success.TButton", background="green", foreground="white")
style.configure("danger.TButton", background="red", foreground="white")
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 13))

### Full-page scrollable canvas ###
main_canvas = tk.Canvas(root)
main_canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
scrollbar.pack(side="right", fill="y")

# Frame inside the canvas
main_frame = ttk.Frame(main_canvas)
main_frame_id = main_canvas.create_window((0, 0), window=main_frame, anchor="n", width=width)

# Configure canvas scrolling
main_canvas.configure(yscrollcommand=scrollbar.set)
main_frame.bind("<Configure>", on_frame_configure)



main_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

#######################
### Widgets in Main ###
#######################
# Title label
title_label = ttk.Label(main_frame, text="Quiz App", font=("Helvetica", 16, "bold"))
title_label.pack(pady=20, anchor="center")

# Question label
qs_label = ttk.Label(main_frame, text="Your question will appear here.", font=("Helvetica", 14), anchor="center", justify="center", wraplength=width - 50)
qs_label.pack(pady=10)

# Hint: Number of answers
answers_hint_label = ttk.Label(main_frame, text="", font=("Helvetica", 12), anchor="center", justify="center")
answers_hint_label.pack(pady=5)

# Options frame
options_frame = ttk.Frame(main_frame)
options_frame.pack(pady=10)

# Feedback labels
feedback_label_correctness = ttk.Label(main_frame, font=("Helvetica", 12), anchor="center", justify="center")
feedback_label_correctness.pack(pady=5)

feedback_label_explanation = ttk.Label(main_frame, font=("Helvetica", 12), wraplength=width - 50, anchor="center", justify="center")
feedback_label_explanation.pack(pady=5)

# Footer frame
footer_frame = ttk.Frame(main_frame)
footer_frame.pack(pady=10)

# Score and next button
score_label = ttk.Label(footer_frame, text="Score: 0/0", font=("Helvetica", 12), anchor="center", justify="center")
next_btn = ttk.Button(footer_frame, text="Next", command=next_question, state="disabled")

# Pack footer widgets
score_label.pack(side="left", padx=10)
next_btn.pack(side="left", padx=10)



#########################
### Initialize Widgets ##
#########################
choice_btns = []
quiz_data = []
current_question = 0
score = 0

# Start with file selection
show_file_selection()
root.mainloop()
