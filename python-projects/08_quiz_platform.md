# Project 8: Online Quiz Platform

**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Real-world Use:** Education, employee training, certifications

## Project Overview

Build an **Online Quiz Platform**:
- Create and manage quizzes
- Multiple question types
- Automatic grading
- User accounts and results tracking
- Leaderboard
- Performance analytics
- Timed quizzes
- Question pools and randomization

## Features to Implement

1. **Quiz Management**:
   - Create quizzes
   - Edit quizzes
   - Delete quizzes
   - Set difficulty level
   - Set time limit
   - Set pass score (60%, 70%, etc.)

2. **Question Types**:
   - Multiple choice
   - True/False
   - Short answer (keyword matching)
   - Fill in the blank
   - Multiple select

3. **Question Bank**:
   - Store questions
   - Organize by category
   - Difficulty levels
   - Reuse questions across quizzes
   - Question tags

4. **User Management**:
   - User registration/login
   - User profiles
   - Track quiz history
   - View past results

5. **Quiz Taking**:
   - One question at a time
   - Progress indicator
   - Time remaining display
   - Review answers before submit
   - Save progress (optional)

6. **Automatic Grading**:
   - Score calculation
   - Show correct answers
   - Provide explanations
   - Identify weak areas

7. **Results Tracking**:
   - Store quiz results
   - Show score breakdown
   - Performance over time
   - Compare with previous attempts

8. **Leaderboard**:
   - Top scorers
   - Filters by quiz/category
   - See rankings

9. **Analytics**:
   - Question difficulty analysis
   - Most missed questions
   - Student performance reports
   - Class average (for teachers)

## Technologies/Concepts Needed
- User authentication
- Complex data structures
- File I/O
- Timer functionality
- Mathematical calculations
- String comparison for answers
- Data analysis

## Step-by-Step Guidance

### Step 1: Design Data Structures
```python
users = [
    {
        "id": 1,
        "username": "alice",
        "password": "hashed",
        "email": "alice@example.com",
        "role": "student",  # student, teacher, admin
        "created_date": "2025-01-01"
    }
]

quizzes = [
    {
        "id": 1,
        "title": "Python Basics",
        "description": "Test your Python knowledge",
        "category": "Programming",
        "difficulty": "Easy",
        "time_limit": 30,  # minutes
        "pass_score": 70,
        "total_questions": 10,
        "questions": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # question IDs
        "created_by": 1,
        "created_date": "2025-01-15"
    }
]

questions = [
    {
        "id": 1,
        "quiz_id": 1,
        "type": "multiple_choice",  # multiple_choice, true_false, short_answer
        "question_text": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "correct_answer": "4",  # or index 1 for multiple choice
        "explanation": "2 + 2 = 4",
        "difficulty": "Easy",
        "category": "Math"
    }
]

results = [
    {
        "id": 1,
        "quiz_id": 1,
        "user_id": 1,
        "score": 85,
        "max_score": 100,
        "percentage": 85,
        "passed": True,
        "time_taken": 22,  # minutes
        "answers": [
            {
                "question_id": 1,
                "user_answer": "4",
                "correct": True
            }
        ],
        "submitted_date": "2025-02-09 14:30:00"
    }
]
```

### Step 2: Create Core Functions
- `create_quiz(title, description, category, time_limit, pass_score)`
- `add_question(quiz_id, question_data)`
- `get_quiz_questions(quiz_id)`
- `start_quiz(user_id, quiz_id)`
- `submit_answer(quiz_id, question_id, user_answer)`
- `calculate_score(quiz_id, user_answers)`
- `save_result(user_id, quiz_id, score, answers)`
- `get_leaderboard(quiz_id)`
- `get_user_performance(user_id)`
- `get_quiz_analytics(quiz_id)`

### Step 3: Build Menu System
```
=== Online Quiz Platform ===
1. Login
2. Register
3. Browse Quizzes
4. Take Quiz
5. View Results
6. Leaderboard
7. My Statistics
8. Admin Panel (Create Quiz)
9. Exit
```

### Step 4: Quiz Taking Flow
```
Start Quiz → Timer Starts → Question 1 of 10
↓
Display Question + Options
↓
User Selects Answer
↓
Next/Previous Navigation
↓
Submit Quiz
↓
Auto-Grade
↓
Show Results (Score, Percentage, Pass/Fail)
↓
Show Detailed Review (Each Question)
↓
Compare with Previous Attempts
```

## Example Usage

```
Choose option: 4
Available Quizzes:
1. Python Basics (Easy) - 10 questions
2. Data Structures (Medium) - 15 questions
3. Web Development (Hard) - 20 questions

Choose quiz: 1
Quiz: Python Basics
Time limit: 30 minutes
Pass score: 70%

Ready to start? (yes/no): yes
Starting quiz...

=== Question 1 of 10 ===
Time remaining: 29:45

Question: What is the correct way to create a list?
A) [1, 2, 3]
B) (1, 2, 3)
C) {1, 2, 3}
D) list(1, 2, 3)

Your answer: A
Next question? (yes): yes

[... 9 more questions ...]

=== Quiz Complete ===
Submitting answers...

Score: 85/100
Percentage: 85%
Status: PASSED ✓
Time taken: 22 minutes

Results Breakdown:
Correct: 8/10
Incorrect: 2/10
Skipped: 0/10

Question Review:
[1] What is...? ✓ Correct
[2] How to...? ✗ Incorrect (You: B, Correct: A)
    Explanation: The correct way is A because...

Compare with previous attempts:
Attempt 1: 75% (2025-02-01)
Attempt 2: 85% (2025-02-09) ← Latest

Your ranking: 5/120 students
```

## Real-World Enhancement Ideas
1. **Scheduled Exams**: Set specific dates/times for quizzes
2. **Question Pool**: Random questions from a large pool
3. **Question Banks**: Different versions of quizzes
4. **Partial Credit**: Points for partially correct answers
5. **Essay Questions**: Manually graded questions
6. **Discussion Forums**: Discuss questions with peers
7. **Certificates**: Generate certificates for passing
8. **Progress Tracking**: See learning progress over time
9. **Mobile App**: Access from phones/tablets
10. **Question Analytics**: Statistics about question difficulty
11. **Custom Feedback**: Detailed feedback per question
12. **API Integration**: Connect to learning management systems

## Grading Criteria
- ✅ Can create and manage quizzes
- ✅ Multiple question types work correctly
- ✅ Automatic grading is accurate
- ✅ Timer functionality works
- ✅ Results are saved properly
- ✅ User authentication works
- ✅ Leaderboard shows correct rankings
- ✅ Analytics provide useful insights
- ✅ UI is intuitive and user-friendly
- ✅ Data persists between sessions

## Tips for Implementation
- Use a simple hashing for passwords (don't store plain text)
- Implement a timer using time module
- Show progress bar for quiz completion
- Allow users to review before submitting
- Store all answers to provide feedback
- Consider question randomization (don't show in same order)
