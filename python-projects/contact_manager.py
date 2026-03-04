"""
Contact Manager Application

A complete command-line Contact Manager that allows users to:
- Add, edit, delete contacts
- Search contacts
- Group by category
- Mark favorites
- Save to JSON
- Import from JSON
- Export to CSV

Author: Shweta Borganve
"""

import json
import csv
import re
from datetime import datetime
from typing import List, Dict, Optional


class Contact:
    """Represents a single contact."""

    def __init__(
        self,
        contact_id: int,
        name: str,
        phone: str,
        email: str,
        address: str,
        birthday: str,
        category: str,
        favorite: bool = False,
        created: Optional[str] = None
    ) -> None:
        """Initialize contact object."""
        self.id = contact_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.birthday = birthday
        self.category = category
        self.favorite = favorite
        self.created = created or datetime.now().strftime("%Y-%m-%d")

    def to_dict(self) -> Dict:
        """Convert contact object to dictionary."""
        return self.__dict__

    @staticmethod
    def from_dict(data: Dict) -> "Contact":
        """Create Contact object from dictionary."""
        return Contact(**data)


class ContactManager:
    """Main Contact Manager class."""

    FILE_NAME = "contacts.json"

    def __init__(self) -> None:
        """Initialize ContactManager."""
        self.contacts: List[Contact] = []
        self.load_contacts()

    # ---------------- Validation Methods ---------------- #

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone format."""
        pattern = r"^\+?\d[\d\-]{7,14}\d$"
        return bool(re.match(pattern, phone))

    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Validate date format YYYY-MM-DD."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    # ---------------- Core Functions ---------------- #

    def generate_id(self) -> int:
        """Generate unique ID."""
        if not self.contacts:
            return 1
        return max(contact.id for contact in self.contacts) + 1

    def add_contact(
        self,
        name: str,
        phone: str,
        email: str,
        address: str,
        birthday: str,
        category: str
    ) -> None:
        """Add new contact."""
        if not name.strip():
            raise ValueError("Name is required.")
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone format.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        if not self.validate_date(birthday):
            raise ValueError("Invalid birthday format (YYYY-MM-DD).")

        new_contact = Contact(
            contact_id=self.generate_id(),
            name=name.strip(),
            phone=phone.strip(),
            email=email.strip(),
            address=address.strip(),
            birthday=birthday.strip(),
            category=category.strip()
        )

        self.contacts.append(new_contact)
        self.save_contacts()

    def search_contact(self, query: str) -> List[Contact]:
        """Search contacts by name, phone, email, or category."""
        query = query.lower()
        return [
            contact for contact in self.contacts
            if query in contact.name.lower()
            or query in contact.phone.lower()
            or query in contact.email.lower()
            or query in contact.category.lower()
        ]

    def edit_contact(self, contact_id: int, field: str, new_value: str) -> None:
        """Edit contact field."""
        contact = self.get_contact_by_id(contact_id)
        if not contact:
            raise ValueError("Contact not found.")

        if field == "phone" and not self.validate_phone(new_value):
            raise ValueError("Invalid phone format.")
        if field == "email" and not self.validate_email(new_value):
            raise ValueError("Invalid email format.")
        if field == "birthday" and not self.validate_date(new_value):
            raise ValueError("Invalid birthday format.")

        if hasattr(contact, field):
            setattr(contact, field, new_value)
            self.save_contacts()
        else:
            raise ValueError("Invalid field name.")

    def delete_contact(self, contact_id: int) -> None:
        """Delete contact by ID."""
        contact = self.get_contact_by_id(contact_id)
        if not contact:
            raise ValueError("Contact not found.")

        self.contacts.remove(contact)
        self.save_contacts()

    def get_contact_by_id(self, contact_id: int) -> Optional[Contact]:
        """Get contact by ID."""
        for contact in self.contacts:
            if contact.id == contact_id:
                return contact
        return None

    def mark_favorite(self, contact_id: int) -> None:
        """Mark contact as favorite."""
        contact = self.get_contact_by_id(contact_id)
        if not contact:
            raise ValueError("Contact not found.")

        contact.favorite = True
        self.save_contacts()

    # ---------------- File Handling ---------------- #

    def save_contacts(self) -> None:
        """Save contacts to JSON."""
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([c.to_dict() for c in self.contacts], file, indent=4)

    def load_contacts(self) -> None:
        """Load contacts from JSON."""
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [Contact.from_dict(d) for d in data]
        except FileNotFoundError:
            self.contacts = []

    def export_to_csv(self, file_name: str = "contacts.csv") -> None:
        """Export contacts to CSV."""
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id", "name", "phone", "email",
                    "address", "birthday",
                    "category", "favorite", "created"
                ]
            )
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())


# ---------------- Menu System ---------------- #

def main() -> None:
    """Main menu function."""
    manager = ContactManager()

    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. View All Contacts")
        print("4. Mark Favorite")
        print("5. Delete Contact")
        print("6. Export to CSV")
        print("7. Exit")

        choice = input("Choose option: ").strip()

        try:
            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                address = input("Address: ")
                birthday = input("Birthday (YYYY-MM-DD): ")
                category = input("Category: ")

                manager.add_contact(
                    name, phone, email, address, birthday, category
                )
                print("✓ Contact added successfully!")

            elif choice == "2":
                query = input("Search: ")
                results = manager.search_contact(query)
                for contact in results:
                    print(contact.to_dict())

            elif choice == "3":
                for contact in manager.contacts:
                    print(contact.to_dict())

            elif choice == "4":
                contact_id = int(input("Contact ID: "))
                manager.mark_favorite(contact_id)
                print("✓ Marked as favorite!")

            elif choice == "5":
                contact_id = int(input("Contact ID: "))
                manager.delete_contact(contact_id)
                print("✓ Contact deleted!")

            elif choice == "6":
                manager.export_to_csv()
                print("✓ Exported to CSV!")

            elif choice == "7":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
