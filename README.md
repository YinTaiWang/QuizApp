# QuizApp

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Steps](#steps)
3. [Quiz Format](#quiz-format)
4. [Screenshots](#screenshots)

---

## Overview
QuizApp is an easy-to-use application for creating and taking quizzes. Users can build their own quizzes by defining questions, options, and answers in a structured format. The app supports single-answer and multiple-answer questions, and it provides explanations for answers to enhance learning.

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Conda or Pip for managing dependencies

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/quizapp.git
   cd quizapp
   ```

2. Install dependencies using Pip:
    ```
    pip install -r requirements.txt
    ```

3. Run the app
    ```
    python main.py
    ```

---

## Quiz Format

Quizzes are stored in the `quizzes` folder and should be Python `.py` files. Each quiz defines its questions in a variable called `quiz_data`, which is a list of dictionaries. Each dictionary represents a question and contains the following fields:

1. **`question`** (string): The question text.

2. **`options`** (list): Possible answers, optionally prefixed (e.g., `"A. Option1"`) or as plain text (e.g., `"Option1"`).

3. **`answer`** (string or list): The correct answer(s):
   - Single-answer questions use a string.
   - Multiple-answer questions use a list.
   - Answers can be the full text (e.g., `"Option1"`) or prefixes (e.g., `"A"`).

4. **`explanation`** (optional, string): Additional information explaining the correct answer.

An example quiz can be found in the `quizzes` folder under `example.py`. It provides a template for creating your own quizzes with the correct structure.

---

## Screenshots

**Main Menu:**  
![Main Menu](https://raw.githubusercontent.com/YinTaiWang/QuizApp/main/screenshots/main_menu.png)

**Quiz Question:**  
![Quiz Question](https://raw.githubusercontent.com/YinTaiWang/QuizApp/main/screenshots/quiz_example.png)