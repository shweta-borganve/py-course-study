# Project 3: Contact Management System

**Difficulty:** ⭐⭐⭐ Medium  
**Real-world Use:** Store and manage personal contacts

## Project Overview

Build a **Contact Manager** application that acts like a digital address book:
- Add, edit, delete contacts
- Search contacts by name, phone, email
- Store contact details: name, phone, email, address, birthday
- Group contacts into categories
- Export/Import contacts
- Quick dialer (show phone number for quick calling)

## Features to Implement

1. **Add Contact**:
   - Name (required)
   - Phone number (validate format)
   - Email (validate format)
   - Address
   - Birthday
   - Category (Friends, Family, Work, etc.)

2. **Search Contacts**:
   - By name (partial match)
   - By phone number
   - By email
   - By category

3. **Edit Contact**:
   - Modify any field
   - Keep creation date

4. **Delete Contact**:
   - Confirm before deletion
   - Move to deleted contacts

5. **View Contacts**:
   - List all contacts
   - Grouped by category
   - Sorted alphabetically or by category

6. **Contact Groups**:
   - Create custom groups
   - Assign contacts to groups
   - Quick actions on group (send email list, etc.)

7. **Favorites**:
   - Mark important contacts as favorite
   - Quick access to favorites

8. **Data Persistence**:
   - Save to JSON
   - Import from JSON
   - Export to CSV

## Technologies/Concepts Needed
- Data structures (dictionaries, lists)
- File I/O (JSON, CSV)
- Input validation (email, phone)
- String searching and matching
- Date handling
- Object-oriented programming (optional)

## Step-by-Step Guidance

### Step 1: Design Data Structure
```python
contacts = [
    {
        "id": 1,
        "name": "John Doe",
        "phone": "+1-234-567-8900",
        "email": "john@example.com",
        "address": "123 Main St",
        "birthday": "1990-05-15",
        "category": "Friends",
        "favorite": False,
        "created": "2025-02-09"
    }
]
```

### Step 2: Create Validation Functions
- `validate_phone(phone)` - Check format
- `validate_email(email)` - Check format
- `validate_date(date)` - Check date format

### Step 3: Create Core Functions
- `add_contact(name, phone, email, address, birthday, category)`
- `search_contact(query)`
- `edit_contact(contact_id, field, new_value)`
- `delete_contact(contact_id)`
- `get_contacts_by_category(category)`
- `mark_favorite(contact_id)`
- `export_to_csv()`
- `import_from_json()`

### Step 4: Build Menu System
```
=== Contact Manager ===
1. Add Contact
2. Search Contact
3. View All Contacts
4. View by Category
5. View Favorites
6. Edit Contact
7. Delete Contact
8. Export to CSV
9. Import from JSON
10. Exit
```

## Example Usage

```
Choose option: 1
Enter name: Alice Smith
Enter phone: +1-555-123-4567
Enter email: alice@example.com
Enter address: 456 Oak Ave
Enter birthday (YYYY-MM-DD): 1992-03-22
Choose category:
1. Friends
2. Family
3. Work
4. Other
Choice: 1
✓ Contact added successfully!

Choose option: 2
Search query: Alice
Results:
[1] Alice Smith
    Phone: +1-555-123-4567
    Email: alice@example.com
    Category: Friends
    Birthday: March 22

Choose option: 3
=== All Contacts (5 total) ===

Friends (2):
- Alice Smith (555-123-4567)
- Bob Johnson (555-987-6543)

Family (2):
- Mom (555-111-2222)
- Sister (555-333-4444)

Work (1):
- Boss (555-999-0000)
```

## Real-World Enhancement Ideas
1. **Birthday Reminders**: Alert when birthday is coming
2. **Contact Photos**: Store profile pictures
3. **Notes**: Add personal notes about contacts
4. **Call/Message History**: Track interactions
5. **Social Media**: Store social media profiles
6. **Emergency Contacts**: Mark priority contacts
7. **Duplicate Detection**: Find similar contacts
8. **Backup**: Automatic backup to cloud/email
9. **Password Protection**: Encrypt sensitive data
10. **Relationship Tracking**: How you know the person
11. **Communication Preferences**: Email vs phone
12. **Last Contact Date**: Track when you last contacted them

## Grading Criteria
- ✅ Can add, edit, delete contacts
- ✅ Validation works (email, phone format)
- ✅ Search is accurate and fast
- ✅ Categorization works properly
- ✅ Data persists between sessions
- ✅ User interface is intuitive
- ✅ Export/Import functions work
- ✅ Handles edge cases (duplicate names, etc.)
