"""
Professional Contact Manager Application.

Features:
- Add, search, delete contacts
- Mark favorite contacts
- JSON persistence
- CSV export
- Input validation
- Clean architecture (No pylint warnings)

Author: Shweta Borganve
"""

import json
import csv
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional


# ---------------- Data Models ---------------- #

@dataclass
class ContactInfo:
    """Stores personal contact details."""
    name: str
    phone: str
    email: str
    address: str
    birthday: str
    category: str


@dataclass
class ContactMeta:
    """Stores metadata about contact."""
    contact_id: int
    favorite: bool = False
    created: str = datetime.now().strftime("%Y-%m-%d")


@dataclass
class Contact:
    """Represents a complete contact."""
    info: ContactInfo
    meta: ContactMeta


# ---------------- Manager Class ---------------- #

class ContactManager:
    """Main class responsible for managing contacts."""

    FILE_NAME = "contacts.json"

    def __init__(self) -> None:
        """Initialize contact manager and load data."""
        self.contacts: List[Contact] = []
        self.load_contacts()

    # ---------- Validation Methods ---------- #

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        """Validate phone number format."""
        pattern = r"^\+?\d[\d\-]{7,14}\d$"
        return bool(re.match(pattern, phone))

    @staticmethod
    def validate_date(date_str: str) -> bool:
        """Validate date in YYYY-MM-DD format."""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    # ---------- Core Methods ---------- #

    def generate_id(self) -> int:
        """Generate a unique contact ID."""
        if not self.contacts:
            return 1
        return max(c.meta.contact_id for c in self.contacts) + 1

    def add_contact(self, data: dict) -> None:
        """
        Add a new contact.

        Args:
            data (dict): Dictionary containing contact fields.
        """
        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()
        email = data.get("email", "").strip()
        address = data.get("address", "").strip()
        birthday = data.get("birthday", "").strip()
        category = data.get("category", "").strip()

        if not name:
            raise ValueError("Name required.")
        if not self.validate_phone(phone):
            raise ValueError("Invalid phone.")
        if not self.validate_email(email):
            raise ValueError("Invalid email.")
        if not self.validate_date(birthday):
            raise ValueError("Invalid date.")

        info = ContactInfo(
            name=name,
            phone=phone,
            email=email,
            address=address,
            birthday=birthday,
            category=category,
        )

        meta = ContactMeta(contact_id=self.generate_id())

        self.contacts.append(Contact(info=info, meta=meta))
        self.save_contacts()

    def search_contact(self, query: str) -> List[Contact]:
        """
        Search contacts by name, phone, email, or category.

        Args:
            query (str): Search keyword.

        Returns:
            List[Contact]: Matching contacts.
        """
        query = query.lower()
        return [
            contact for contact in self.contacts
            if query in contact.info.name.lower()
            or query in contact.info.phone.lower()
            or query in contact.info.email.lower()
            or query in contact.info.category.lower()
        ]

    def get_contact_by_id(self, contact_id: int) -> Optional[Contact]:
        """
        Retrieve contact by ID.

        Args:
            contact_id (int): Contact ID.

        Returns:
            Optional[Contact]: Found contact or None.
        """
        for contact in self.contacts:
            if contact.meta.contact_id == contact_id:
                return contact
        return None

    def delete_contact(self, contact_id: int) -> None:
        """
        Delete contact by ID.

        Args:
            contact_id (int): Contact ID.
        """
        contact = self.get_contact_by_id(contact_id)
        if not contact:
            raise ValueError("Contact not found.")
        self.contacts.remove(contact)
        self.save_contacts()

    def mark_favorite(self, contact_id: int) -> None:
        """
        Mark contact as favorite.

        Args:
            contact_id (int): Contact ID.
        """
        contact = self.get_contact_by_id(contact_id)
        if not contact:
            raise ValueError("Contact not found.")
        contact.meta.favorite = True
        self.save_contacts()

    # ---------- File Handling ---------- #

    def save_contacts(self) -> None:
        """Save all contacts to JSON file."""
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(
                [asdict(contact) for contact in self.contacts],
                file,
                indent=4
            )

    def load_contacts(self) -> None:
        """Load contacts from JSON file."""
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.contacts = [
                    Contact(
                        info=ContactInfo(**item["info"]),
                        meta=ContactMeta(**item["meta"]),
                    )
                    for item in data
                ]
        except FileNotFoundError:
            self.contacts = []

    def export_to_csv(self) -> None:
        """Export contacts to CSV file."""
        with open("contacts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID", "Name", "Phone", "Email",
                "Address", "Birthday", "Category",
                "Favorite", "Created"
            ])
            for contact in self.contacts:
                writer.writerow([
                    contact.meta.contact_id,
                    contact.info.name,
                    contact.info.phone,
                    contact.info.email,
                    contact.info.address,
                    contact.info.birthday,
                    contact.info.category,
                    contact.meta.favorite,
                    contact.meta.created,
                ])


# ---------------- Main Function ---------------- #

def main() -> None:
    """Run command-line interface for Contact Manager."""
    manager = ContactManager()

    while True:
        print("\n1. Add")
        print("2. Search")
        print("3. View All")
        print("4. Delete")
        print("5. Favorite")
        print("6. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                data = {
                    "name": input("Name: "),
                    "phone": input("Phone: "),
                    "email": input("Email: "),
                    "address": input("Address: "),
                    "birthday": input("Birthday YYYY-MM-DD: "),
                    "category": input("Category: "),
                }
                manager.add_contact(data)
                print("Added successfully!")

            elif choice == "2":
                results = manager.search_contact(input("Search: "))
                for contact in results:
                    print(contact.meta.contact_id, "-", contact.info.name)

            elif choice == "3":
                for contact in manager.contacts:
                    print(contact.meta.contact_id, "-", contact.info.name)

            elif choice == "4":
                manager.delete_contact(int(input("ID: ")))

            elif choice == "5":
                manager.mark_favorite(int(input("ID: ")))

            elif choice == "6":
                break

        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
