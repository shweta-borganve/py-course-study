# Problem 10: Advanced Challenge - Quiz Game with Scoring

**Difficulty:** ⭐⭐⭐⭐⭐ Hard

## Problem Description

Create an **interactive quiz game** that:

1. Stores questions in a data structure (nested dict/list)
2. Asks users multiple-choice questions
3. Tracks the user's score
4. Provides feedback (correct/incorrect)
5. Shows the final score and percentage
6. Allows users to **retake the quiz** or **see their score history**
7. **Saves** quiz attempts to a file with timestamp

The quiz should have at least 10 questions about Python programming.

## Learning Goals
- Combine multiple concepts: functions, dictionaries, lists, file I/O, loops
- Real-world application
- User input validation
- Data persistence
- Complex logic flow

## Hints to Get Started

1. **Define questions as a nested structure:**
```python
questions = [
    {
        "question": "What is Python?",
        "options": ["A programming language", "A snake", "A company", "None"],
        "correct": 0  # Index of correct answer
    },
    # ... more questions
]
```

2. **Create functions for:**
   - `ask_question(q)` - displays a question, gets answer, checks correctness
   - `calculate_score(correct, total)` - returns score and percentage
   - `save_score(name, score, percentage)` - saves to file with timestamp
   - `show_history()` - reads and displays all previous attempts
   - `main()` - runs the entire quiz flow

3. **Main flow:**
   - Ask for user's name
   - Loop through questions
   - Keep track of correct answers
   - After each question, show if correct/incorrect
   - Show final score
   - Ask if they want to try again
   - Save results

## Example

**Program Output:**
```
=== Python Quiz Game ===
Enter your name: Alice

Question 1: What is the correct way to create a list in Python?
A) [1, 2, 3]
B) (1, 2, 3)
C) {1, 2, 3}
D) list(1, 2, 3)

Your answer: A
✓ Correct!

Question 2: What is the output of print(5 / 2)?
A) 2
B) 2.0
C) 2.5
D) Error

Your answer: C
✓ Correct!

... (more questions)

=== Quiz Complete ===
Name: Alice
Score: 8/10
Percentage: 80%

Great job! Keep practicing!

Do you want to try again? (yes/no): no

=== Score History ===
Alice: 80% (2025-02-09 14:30:15)
Alice: 75% (2025-02-09 14:25:00)
```

## Tips
- Use `input()` with validation - check if the answer is A, B, C, or D
- Use `input().upper()` to convert to uppercase for consistency
- Use `datetime.datetime.now()` to get timestamp (you may need to import)
- When saving scores, append to file (use mode `'a'` for append)
- Keep the menu simple with clear options

## Challenge (Optional)
1. Add difficulty levels - easy, medium, hard questions
2. Add a timer - give user only 30 seconds per question
3. Add hints - user can request a hint (removes one wrong option)
4. Add a leaderboard - show top 5 scores
5. Add categories - user chooses quiz topic (Python basics, Functions, Lists, etc.)
6. Add explanations - after wrong answer, show why the correct answer is right

**This is a comprehensive problem - combining everything you've learned!**
