"""
Email Validator & Newsletter System
Pylint 10/10 version
"""

import re
import csv
import random
from datetime import datetime
from typing import List, Dict, Optional, Callable


class EmailValidator:
    """Handles email validation and typo detection."""

    COMMON_DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com"]

    @staticmethod
    def validate(email: str) -> bool:
        """Validate email format."""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def suggest_typo(email: str) -> Optional[str]:
        """Suggest correction for common domain typos."""
        domain = email.split("@")[-1]

        for correct_domain in EmailValidator.COMMON_DOMAINS:
            if (
                domain.startswith(correct_domain[:3])
                and domain != correct_domain
            ):
                return f"Did you mean {correct_domain}?"
        return None


class SubscriberManager:
    """Manages subscriber operations."""

    def __init__(self) -> None:
        self.subscribers: List[Dict] = []

    def add(self, email: str, category: str = "Regular") -> bool:
        """Add a new subscriber."""
        if not EmailValidator.validate(email):
            return False

        subscriber = {
            "email": email,
            "category": category,
            "date": datetime.now().isoformat(),
            "status": "Active",
        }
        self.subscribers.append(subscriber)
        return True

    def remove(self, email: str) -> None:
        """Remove subscriber."""
        self.subscribers = [
            sub for sub in self.subscribers
            if sub["email"] != email
        ]

    def unsubscribe(self, email: str) -> bool:
        """Unsubscribe user."""
        for sub in self.subscribers:
            if sub["email"] == email:
                sub["status"] = "Unsubscribed"
                return True
        return False

    def export_csv(self, filename: str) -> None:
        """Export CSV."""
        if not self.subscribers:
            return

        keys = self.subscribers[0].keys()

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.subscribers)

    def import_csv(self, filename: str) -> None:
        """Import CSV."""
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.subscribers.append(dict(row))


class TemplateManager:
    """Handles templates."""

    def __init__(self) -> None:
        self.templates: Dict[str, str] = {}

    def create(self, name: str, content: str) -> None:
        """Create template."""
        self.templates[name] = content

    def preview(self, name: str) -> str:
        """Preview template."""
        if name not in self.templates:
            return "Template not found"
        return self.templates[name].replace("{name}", "User")


class CampaignManager:
    """Handles campaigns."""

    def __init__(self) -> None:
        self.campaigns: List[Dict] = []

    def create(self, name: str, template: str) -> None:
        """Create campaign."""
        self.campaigns.append({
            "name": name,
            "template": template,
            "sent": False,
            "open_rate": 0,
            "click_rate": 0,
        })

    def send(self, name: str) -> bool:
        """Send campaign."""
        for campaign in self.campaigns:
            if campaign["name"] == name:
                campaign["sent"] = True
                campaign["open_rate"] = random.randint(40, 90)
                campaign["click_rate"] = random.randint(10, 50)
                return True
        return False

    def stats(self) -> List[Dict]:
        """Return stats."""
        return self.campaigns


# -------- MENU HANDLERS -------- #


def handle_add(subs: SubscriberManager) -> None:
    """Handle adding subscriber."""
    email = input("Enter email: ").strip()
    if subs.add(email):
        print("Added successfully")
    else:
        print("Invalid email")


def handle_remove(subs: SubscriberManager) -> None:
    """Handle removing subscriber."""
    email = input("Enter email: ").strip()
    subs.remove(email)
    print("Removed")


def handle_export(subs: SubscriberManager) -> None:
    """Handle export to CSV."""
    subs.export_csv("subscribers.csv")
    print("Exported")


def handle_import(subs: SubscriberManager) -> None:
    """Handle import from CSV."""
    subs.import_csv("subscribers.csv")
    print("Imported")


def handle_template(templates: TemplateManager) -> None:
    """Handle template creation."""
    name = input("Template name: ")
    content = input("Content: ")
    templates.create(name, content)


def handle_preview(templates: TemplateManager) -> None:
    """Handle template preview."""
    name = input("Template name: ")
    print(templates.preview(name))


def handle_campaign(campaigns: CampaignManager) -> None:
    """Handle campaign creation."""
    name = input("Campaign name: ")
    template = input("Template name: ")
    campaigns.create(name, template)


def handle_send(campaigns: CampaignManager) -> None:
    """Handle sending campaign."""
    name = input("Campaign name: ")
    print("Campaign sent" if campaigns.send(name) else "Not found")


def handle_stats(campaigns: CampaignManager) -> None:
    """Handle viewing stats."""
    for campaign in campaigns.stats():
        print(campaign)


def handle_unsubscribe(subs: SubscriberManager) -> None:
    """Handle unsubscribe."""
    email = input("Enter email: ").strip()
    print("Unsubscribed" if subs.unsubscribe(email) else "Not found")


# -------- MAIN -------- #


def main() -> None:
    """Main function."""
    subs = SubscriberManager()
    templates = TemplateManager()
    campaigns = CampaignManager()

    actions: Dict[str, Callable[[], None]] = {
        "1": lambda: handle_add(subs),
        "2": lambda: handle_remove(subs),
        "3": lambda: handle_export(subs),
        "4": lambda: handle_import(subs),
        "5": lambda: handle_template(templates),
        "6": lambda: handle_preview(templates),
        "7": lambda: handle_campaign(campaigns),
        "8": lambda: handle_send(campaigns),
        "9": lambda: handle_stats(campaigns),
        "10": lambda: handle_unsubscribe(subs),
    }

    while True:
        print("\n===== MENU =====")
        print("1. Add Subscriber")
        print("2. Remove Subscriber")
        print("3. Export CSV")
        print("4. Import CSV")
        print("5. Create Template")
        print("6. Preview Template")
        print("7. Create Campaign")
        print("8. Send Campaign")
        print("9. View Stats")
        print("10. Unsubscribe")
        print("0. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "0":
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
