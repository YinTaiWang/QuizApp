'''
Example quiz_data
-----------------
Each question is represented as a dictionary.

Fields:
1. "question": A string containing the question text.
2. "options": A list of possible answers. Each option can:
   - Start with a prefix (e.g., "A. ", "B. ") or
   - Contain only the answer text itself (e.g., "Amsterdam", "Taiwan").
3. "answer": Specifies the correct answer(s). It can be:
   - A single string for single-answer questions:
     * If prefixed (e.g., "A"), the answer is the prefix.
     * If unprefixed (e.g., "Amsterdam"), the answer is the full text.
   - A list of strings for multiple-answer questions:
     * Use prefixes (e.g., ["A", "C"]) if the options are prefixed.
     * Use full text (e.g., ["Python", "Java"]) if the options are unprefixed.
4. "explanation": A string explaining the correct answer(s) for feedback.

Notes:
- Single-answer questions can use a string for "answer".
- Multiple-answer questions must use a list for "answer".
'''

quiz_data = [
    {
        "question": "What is the capital of the Netherlands?",
        "options": ["Amsterdam", "Rotterdam", "The Hague", "Utrecht"],
        "answer": "Amsterdam",  # Single answer with full text
        "explanation": "Amsterdam is the capital city of the Netherlands, known for its canals, museums, and historic architecture."
    },
    {
        "question": "Where is bubble tea originally from?",
        "options": ["A. Japan", "B. Taiwan", "C. China", "D. South Korea"],
        "answer": "B",  # Single answer with prefix
        "explanation": "Bubble tea originated in Taiwan in the 1980s and has since gained global popularity."
    },
    {
        "question": "Select all prime numbers:",
        "options": ["A. 2", "B. 3", "C. 4", "D. 5"],
        "answer": ["A", "B", "D"],  # Multiple answers with prefixes
        "explanation": "Prime numbers are greater than 1 and divisible only by 1 and themselves. 2, 3, and 5 are prime, but 4 is not."
    },
    {
        "question": "Which of the following are programming languages?",
        "options": ["Python", "HTML", "Java", "CSS"],
        "answer": ["Python", "Java"],  # Multiple answers with full text
        "explanation": "Python and Java are programming languages, while HTML and CSS are markup and styling languages."
    }
    # Add more questions
]
