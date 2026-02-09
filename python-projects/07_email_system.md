# Project 7: Email Validator & Newsletter System

**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Real-world Use:** Email validation, mailing list management, bulk email

## Project Overview

Build an **Email Management System**:
- Validate email addresses
- Manage email subscriber lists
- Send bulk emails (simulated)
- Categorize subscribers
- Track email campaigns
- Unsubscribe management
- Email templates

## Features to Implement

1. **Email Validation**:
   - Check email format is valid
   - Check domain exists (DNS lookup - optional)
   - Detect disposable emails
   - Check for common typos

2. **Subscriber Management**:
   - Add/remove subscribers
   - Import email lists from CSV/JSON
   - Export subscriber lists
   - Categorize subscribers (VIP, Regular, Inactive)
   - Track subscription date

3. **List Segmentation**:
   - Divide subscribers into groups
   - Create filtered lists based on criteria
   - Manage multiple mailing lists

4. **Email Templates**:
   - Create reusable templates
   - Add variables (name, date, etc.)
   - Preview templates
   - Store templates

5. **Campaign Management**:
   - Create email campaigns
   - Set send time
   - Track open rates (simulated)
   - Track click rates (simulated)
   - View campaign statistics

6. **Unsubscribe Management**:
   - Add unsubscribe option
   - Track unsubscribes
   - Handle bounce-backs
   - Manage blacklist

7. **Email Preview & Testing**:
   - Preview email before sending
   - Test email rendering
   - Send test emails

8. **Analytics**:
   - Track open rates
   - Track click rates
   - Delivery statistics
   - Best send times

## Technologies/Concepts Needed
- Regular expressions (email validation)
- File I/O (CSV, JSON)
- String manipulation
- Data structures
- Email libraries (optional: smtplib)
- CSV handling
- Statistical calculations

## Step-by-Step Guidance

### Step 1: Email Validation with Regex
```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Test
print(validate_email("alice@example.com"))  # True
print(validate_email("invalid.email"))       # False
```

### Step 2: Design Data Structures
```python
subscribers = [
    {
        "id": 1,
        "email": "alice@example.com",
        "name": "Alice",
        "list": "VIP",
        "status": "active",  # active, unsubscribed, bounced
        "subscribed_date": "2025-01-15",
        "last_email_open": "2025-02-09",
        "email_opens": 45,
        "email_clicks": 12
    }
]

campaigns = [
    {
        "id": 1,
        "name": "Valentine's Day Sale",
        "template_id": 1,
        "recipient_list": "all",
        "scheduled_date": "2025-02-14",
        "status": "draft",  # draft, scheduled, sent
        "open_count": 0,
        "click_count": 0,
        "unsubscribe_count": 0
    }
]

templates = [
    {
        "id": 1,
        "name": "Weekly Newsletter",
        "subject": "This Week's Updates - {{date}}",
        "body": "Hello {{name}},\n\nHere are this week's updates...",
        "created_date": "2025-01-01"
    }
]
```

### Step 3: Create Core Functions
- `validate_email(email)` - Validate email format
- `add_subscriber(email, name, list_name)`
- `import_subscribers(csv_file)`
- `export_subscribers(csv_file)`
- `create_campaign(name, template_id, recipient_list)`
- `preview_email(template_id, subscriber_data)`
- `send_campaign(campaign_id)` - Simulate sending
- `track_open(campaign_id, subscriber_id)`
- `get_campaign_stats(campaign_id)`
- `unsubscribe(email)`

### Step 4: Build Menu System
```
=== Email Newsletter System ===
1. Add Subscriber
2. View All Subscribers
3. Import Subscribers (CSV)
4. Export Subscribers
5. Manage Lists
6. Create Email Template
7. Create Campaign
8. Preview Campaign
9. Send Campaign
10. View Campaign Stats
11. Unsubscribe
12. Exit
```

## Example Usage

```
Choose option: 1
Enter email: alice@example.com
Enter name: Alice Smith
Enter list (VIP/Regular): VIP
✓ Subscriber added!

Choose option: 3
Import from CSV file: subscribers.csv
Processing...
✓ Imported 150 subscribers

Choose option: 6
Create new template:
Template name: Weekly Newsletter
Subject: This Week's Updates
Body (press Ctrl+D when done):
Hello {{name}},
Here are the latest updates...
✓ Template created!

Choose option: 7
Campaign name: February Newsletter
Select template: 1 (Weekly Newsletter)
Select recipient list: All subscribers
Schedule date (YYYY-MM-DD): 2025-02-10
✓ Campaign created and scheduled!

Choose option: 8
Preview for: alice@example.com
Subject: This Week's Updates
Body:
Hello Alice,
Here are the latest updates...
[Preview looks good!]

Choose option: 9
Campaign: February Newsletter
Recipients: 500 emails
Sending...
✓ Campaign sent to 500 subscribers
(Simulated sending)

Choose option: 10
Campaign Stats: February Newsletter
Total Sent: 500
Delivered: 498
Open Rate: 35% (175 opens)
Click Rate: 8% (40 clicks)
Bounce Rate: 0.4% (2 bounces)
Unsubscribe Rate: 0.2% (1 unsubscribe)
```

## Real-World Enhancement Ideas
1. **Actual Email Sending**: Use SMTP to send real emails
2. **A/B Testing**: Test different subject lines
3. **Advanced Analytics**: Heat maps, engagement scoring
4. **Personalization**: Dynamic content based on user data
5. **Automation**: Triggered emails based on user actions
6. **List Cleaning**: Detect and remove invalid emails
7. **GDPR Compliance**: Privacy and consent tracking
8. **Spam Detection**: Check if email looks like spam
9. **API Integration**: Connect to email service (SendGrid, Mailchimp)
10. **Mobile Preview**: Show how email looks on mobile
11. **Drag-and-Drop Builder**: Visual email editor
12. **Timezone Support**: Send emails at optimal times

## Grading Criteria
- ✅ Email validation works correctly
- ✅ Can add and manage subscribers
- ✅ Bulk import/export works
- ✅ Templates can be created and reused
- ✅ Campaigns track statistics
- ✅ Preview shows correct data
- ✅ Unsubscribe management works
- ✅ Data persists between sessions
- ✅ User interface is clear

## Important Notes
- Regex for email is complex - feel free to use a simpler version
- Don't actually send emails (use simulation)
- Store email addresses securely
- Follow email best practices (unsubscribe option, etc.)
