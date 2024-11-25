import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Function to display the current question and choices
def show_question():
    global choice_btns
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]

    # Update the title with the current question number
    title_label.config(text=f"Question {current_question + 1}")

    # Update the question text
    qs_label.config(text=question["question"])

    # Clear existing buttons
    for btn in choice_btns:
        btn.destroy()

    # Create buttons dynamically based on the number of options
    choice_btns = []
    choices = question["options"]
    for i in range(len(choices)):
        button = ttk.Button(
            options_frame,
            text=choices[i],
            command=lambda i=i: check_answer(i)
        )
        button.pack(pady=5)
        choice_btns.append(button)

    # Clear the feedback label and disable the next button
    feedback_label_correctness.config(text="")
    feedback_label_explanation.config(text="")
    next_btn.config(state="disabled")

# Function to check the selected answer and provide feedback
def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice.startswith(question["answer"]):
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label_correctness.config(text="Correct!", foreground="green")
    else:
        feedback_label_correctness.config(text="Incorrect!", foreground="red")
    feedback_label_explanation.config(text=question["explanation"], foreground="black")
    
    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()



# Create the main window
width = 1200
height = 900
root = tk.Tk()
root.title("Quiz App")
root.geometry(f"{width}x{height}")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 15))
style.configure("TButton", font=("Helvetica", 12))

# Create the title label for the question number
title_label = ttk.Label(
    root,
    text="Question",
    anchor="center",
    font=("Helvetica", 16, "bold"),
    padding=10
)
title_label.pack(pady=10)

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=width-100,
    padding=10
)
qs_label.pack(pady=10)

# Create a frame for the options
options_frame = ttk.Frame(root)
options_frame.pack(pady=10)

# Create the feedback label
# for correctness (Correct/Incorrect)
feedback_label_correctness = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label_correctness.pack(pady=5)

# for explanation (Detailed explanation)
feedback_label_explanation = ttk.Label(
    root,
    anchor="center",
    wraplength=width-100,
    padding=10
)
feedback_label_explanation.pack(pady=5)

# Create a frame for the score and next button
footer_frame = ttk.Frame(root)
footer_frame.pack(pady=10)

# Create the score label
score_label = ttk.Label(
    footer_frame,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(side="left", padx=10)

# Create the next button
next_btn = ttk.Button(
    footer_frame,
    text="Next",
    command=next_question,
    state="disabled"  # Initially disabled
)
next_btn.pack(side="left", padx=10)

# Initialize dynamic components
choice_btns = []  # Initialize the choice buttons as an empty list
current_question = 0  # Initialize the current question index
score = 0  # Initialize the score

# Show the first question
show_question()

# Start the main event loop
root.mainloop()

