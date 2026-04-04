"""
Executive Movie Rating & Recommendation System
Pylint-friendly (E501 fixed)
"""

import json
import os
from statistics import mean


class Movie:
    """Movie class."""

    def __init__(self, title, year, genres, director):
        self.title = title
        self.year = year
        self.genres = genres
        self.director = director
        self.ratings = []

    def add_rating(self, rating):
        """Add rating."""
        if 1 <= rating <= 10:
            self.ratings.append(rating)

    def avg_rating(self):
        """Average rating."""
        return round(mean(self.ratings), 2) if self.ratings else 0

    def to_dict(self):
        """Convert to dict."""
        return self.__dict__


class User:
    """User class."""

    def __init__(self, name):
        self.name = name
        self.history = []

    def watch(self, movie):
        """Add to history."""
        if movie not in self.history:
            self.history.append(movie)

    def to_dict(self):
        """Convert to dict."""
        return self.__dict__


class MovieSystem:
    """Main system."""

    def __init__(self, file_name="data.json"):
        self.file_name = file_name
        self.movies = {}
        self.users = {}
        self.load()

    # ---------- DATA ----------

    def save(self):
        """Save data."""
        data = {
            "movies": {
                k: v.to_dict()
                for k, v in self.movies.items()
            },
            "users": {
                k: v.to_dict()
                for k, v in self.users.items()
            },
        }

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load(self):
        """Load data."""
        if not os.path.exists(self.file_name):
            return

        with open(self.file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        for title, info in data.get("movies", {}).items():
            movie = Movie(
                info["title"],
                info["year"],
                info["genres"],
                info["director"],
            )
            movie.ratings = info.get("ratings", [])
            self.movies[title] = movie

        for name, info in data.get("users", {}).items():
            user = User(name)
            user.history = info.get("history", [])
            self.users[name] = user

    # ---------- MOVIES ----------

    def add_movie(self):
        """Add movie."""
        title = input("Title: ")
        year = int(input("Year: "))
        genres = input("Genres (comma): ").split(",")
        director = input("Director: ")

        self.movies[title] = Movie(
            title,
            year,
            genres,
            director
        )
        print("Movie added!")

    def show_movies(self):
        """Display movies."""
        if not self.movies:
            print("No movies available")
            return

        for movie in self.movies.values():
            print(
                f"{movie.title} ({movie.year}) - "
                f"Rating: {movie.avg_rating()}"
            )

    # ---------- USERS ----------

    def add_user(self):
        """Add user."""
        name = input("Enter username: ")

        if name not in self.users:
            self.users[name] = User(name)
            print("User created!")
        else:
            print("User already exists")

    # ---------- RATING ----------

    def rate_movie(self):
        """Rate movie."""
        user = input("Username: ")
        title = input("Movie title: ")
        rating = int(input("Rating (1-10): "))

        if user in self.users and title in self.movies:
            self.users[user].watch(title)
            self.movies[title].add_rating(rating)
            print("Rating added!")
        else:
            print("Invalid user or movie")

    # ---------- SEARCH ----------

    def search(self):
        """Search movie."""
        keyword = input("Search title: ").lower()

        results = [
            movie
            for movie in self.movies.values()
            if keyword in movie.title.lower()
        ]

        if not results:
            print("No results")
            return

        for movie in results:
            print(movie.title)

    # ---------- RECOMMEND ----------

    def recommend(self):
        """Recommend movies."""
        user = input("Username: ")

        if user not in self.users:
            print("User not found")
            return

        history = self.users[user].history
        recommendations = []

        for movie in self.movies.values():
            if movie.title not in history:
                recommendations.append(movie)

        if not recommendations:
            print("No recommendations")
            return

        print("Recommended Movies:")
        for movie in recommendations[:5]:
            print(movie.title)

    # ---------- MENU ----------

    def menu(self):
        """Main menu."""
        while True:
            print("\n==== MOVIE SYSTEM ====")
            print("1. Add Movie")
            print("2. Show Movies")
            print("3. Add User")
            print("4. Rate Movie")
            print("5. Search Movie")
            print("6. Recommend Movies")
            print("7. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_movie()
            elif choice == "2":
                self.show_movies()
            elif choice == "3":
                self.add_user()
            elif choice == "4":
                self.rate_movie()
            elif choice == "5":
                self.search()
            elif choice == "6":
                self.recommend()
            elif choice == "7":
                self.save()
                print("Data saved. Exiting...")
                break
            else:
                print("Invalid choice")


# ---------- RUN ----------

if __name__ == "__main__":
    app = MovieSystem()
    app.menu()
