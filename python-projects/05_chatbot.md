# Project 5: Simple Chatbot

**Difficulty:** ⭐⭐⭐ Medium  
**Real-world Use:** Customer service, FAQ automation, conversation practice

## Project Overview

Build a **Simple Chatbot** that can have conversations:
- Respond to user queries with predefined responses
- Learn and remember user information
- Context-aware conversations
- Small talk capabilities
- Task automation (set reminders, notes)
- Sentiment analysis (detect mood)

## Features to Implement

1. **Basic Conversation**:
   - Greet user
   - Respond to greetings
   - Respond to goodbyes
   - Small talk (weather, time, etc.)

2. **Information Retrieval**:
   - Store user information (name, age, preferences)
   - Recall information in conversations
   - Ask clarifying questions

3. **Intent Recognition**:
   - Identify what user wants to do
   - Greet, Ask Question, Set Reminder, Get Time, Get Weather

4. **Keyword Matching**:
   - Match user input against known patterns
   - Find best matching response
   - Handle variations in user input

5. **Learning & Memory**:
   - Remember conversation history
   - Improve responses based on feedback
   - Learn new patterns

6. **Personality**:
   - Give the chatbot a personality (friendly, professional)
   - Use varied responses (not always the same)

7. **Task Integration**:
   - Set reminders
   - Create to-do items
   - Get current time/date
   - Perform simple calculations

8. **Data Persistence**:
   - Save conversation history
   - Save learned patterns
   - Load on startup

## Technologies/Concepts Needed
- String matching and pattern recognition
- Dictionary-based responses
- Natural language processing basics
- Data structures (lists, dictionaries)
- File I/O
- Time/date operations
- Regular expressions (optional)

## Step-by-Step Guidance

### Step 1: Design Response Database
```python
responses = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "greetings"],
        "responses": [
            "Hello! How can I help you?",
            "Hi there! What can I do for you?",
            "Hey! What's up?"
        ]
    },
    "time": {
        "patterns": ["what time", "what's the time", "current time"],
        "responses": ["It's currently {}"]
    },
    "name": {
        "patterns": ["my name is", "i'm", "call me"],
        "responses": ["Nice to meet you, {}!"]
    }
}
```

### Step 2: Create Core Functions
- `extract_intent(user_input)` - Identify what user wants
- `extract_entities(user_input)` - Extract info (name, time, etc.)
- `get_response(intent)` - Get appropriate response
- `match_pattern(user_input, patterns)` - Pattern matching
- `learn_from_feedback(user_feedback)`
- `save_conversation()`
- `load_conversation()`

### Step 3: Build Pattern Matching
```python
def match_pattern(user_input, patterns):
    user_input = user_input.lower()
    for pattern in patterns:
        if pattern in user_input:
            return True
    return False
```

### Step 4: Create Intent Mapping
```python
intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "weather": ["weather", "is it raining"],
    "time": ["what time", "current time"],
    "help": ["help", "assist", "support"]
}
```

## Example Usage

```
=== Simple Chatbot ===
Type 'quit' to exit

Chatbot: Hello! I'm your assistant. What's your name?
You: My name is Alice

Chatbot: Nice to meet you, Alice! How can I help you today?
You: What time is it?

Chatbot: It's currently 14:35 on February 9, 2025
You: Can you remind me to buy milk?

Chatbot: I'll remind you to buy milk at what time?
You: At 5 PM

Chatbot: Reminder set for 5:00 PM to buy milk
You: Thank you!

Chatbot: You're welcome, Alice! Anything else?
You: bye

Chatbot: Goodbye, Alice! Have a great day!
```

## Conversation Example 2

```
You: Hello

Chatbot: Hi there! How can I help you?
You: I need help with Python

Chatbot: I can help with Python questions! What do you want to know?
You: How do I read a file?

Chatbot: To read a file in Python:
    with open('filename.txt', 'r') as file:
        content = file.read()

You: That's helpful thanks

Chatbot: You're welcome! Do you have more questions?
You: No, I'm good

Chatbot: Great! See you next time!
```

## Real-World Enhancement Ideas
1. **Natural Language Processing**: Use NLTK or spaCy
2. **Machine Learning**: Train on real conversations
3. **API Integration**: Connect to real services (weather, news)
4. **Voice Interface**: Add speech recognition
5. **Multi-language Support**: Support different languages
6. **Sentiment Analysis**: Detect user emotion
7. **FAQ Integration**: Link to knowledge base
8. **User Feedback**: Learn from corrections
9. **Personality Profiles**: Different bot personalities
10. **Context Awareness**: Remember conversation context

## Grading Criteria
- ✅ Can understand basic intents
- ✅ Responses are appropriate and varied
- ✅ Can remember user information
- ✅ Can handle different user input variations
- ✅ Conversation flows naturally
- ✅ Can set reminders or tasks
- ✅ Data persists between sessions
- ✅ Has personality and friendliness
- ✅ Gracefully handles unknown inputs

## Tips for Better Chatbot
- Add variety to responses (don't repeat same response)
- Always validate user input
- Be friendly and helpful
- Explain when you don't understand
- Ask clarifying questions
- Remember context from conversation
- Use user's name in responses (personalization)
