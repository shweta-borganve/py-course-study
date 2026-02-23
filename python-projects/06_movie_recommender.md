# Project 6: Movie Rating & Recommendation System

**Difficulty:** ⭐⭐⭐⭐ Medium-Hard  
**Real-world Use:** Movie database, recommendation engine

## Project Overview

Build a **Movie Database & Recommendation System**:
- Store and manage movie information
- Users can rate and review movies
- Get movie recommendations based on ratings
- Search by genre, actor, director
- Calculate average ratings
- Track watch history
- Get statistics on viewing patterns

## Features to Implement

1. **Movie Database**:
   - Store movies with: title, year, genre(s), director, actors, plot, rating(s)
   - Add new movies
   - Edit movie information
   - Delete movies

2. **User Management**:
   - Create user profiles
   - Track viewing history
   - Store user preferences
   - Keep user ratings and reviews

3. **Rating System**:
   - Users rate movies (1-10 or 1-5 stars)
   - Calculate average rating
   - Show review count
   - Sort by rating

4. **Search & Filter**:
   - Search by title
   - Filter by genre
   - Filter by actor/director
   - Filter by year range
   - Filter by rating threshold

5. **Recommendation Engine**:
   - Recommend based on user's past ratings
   - Find movies similar to liked movies (same genre/actor)
   - Collaborative filtering (if user liked X, they might like Y)
   - Trending movies (highest rated recently)

6. **User Reviews**:
   - Users can write reviews
   - Show review highlights
   - Helpful votes on reviews
   - Spoiler warnings

7. **Statistics**:
   - Most watched movies
   - Highest rated movies
   - User's watch statistics
   - Genre preferences

8. **Data Persistence**:
   - Save movies, users, ratings to JSON/CSV
   - Load on startup

## Technologies/Concepts Needed
- Complex data structures
- File I/O (JSON)
- Sorting and filtering
- List comprehensions
- Algorithm design (recommendations)
- Statistical calculations
- User authentication basics

## Step-by-Step Guidance

### Step 1: Design Data Structures
```python
movies = [
    {
        "id": 1,
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Drama", "Crime"],
        "director": "Frank Darabont",
        "actors": ["Tim Robbins", "Morgan Freeman"],
        "plot": "...",
        "average_rating": 9.3,
        "review_count": 2500000,
        "ratings": []  # [{"user_id": 1, "rating": 10, "review": "..."}, ...]
    }
]

users = [
    {
        "id": 1,
        "username": "alice",
        "password": "hashed",
        "rated_movies": [
            {"movie_id": 1, "rating": 10, "date": "2025-02-09"}
        ],
        "watch_history": [
            {"movie_id": 1, "date": "2025-02-09", "duration_watched": 142}
        ],
        "favorite_genres": ["Drama", "Thriller"]
    }
]
```

### Step 2: Create Core Functions
- `add_movie(title, year, genres, director, actors, plot)`
- `rate_movie(user_id, movie_id, rating)`
- `add_review(user_id, movie_id, review_text)`
- `search_movies(query)`
- `filter_by_genre(genre)`
- `filter_by_year(start_year, end_year)`
- `get_top_rated_movies(limit=10)`
- `recommend_movies(user_id)` - **KEY FUNCTION**
- `get_similar_movies(movie_id)`
- `get_user_statistics(user_id)`

### Step 3: Implement Recommendation Algorithm
```python
def recommend_movies(user_id):
    # Get user's favorite genres
    user = get_user(user_id)
    favorite_genres = user["favorite_genres"]
    
    # Find movies with those genres that user hasn't rated
    recommendations = []
    for movie in movies:
        if movie["id"] not in user["rated_movies"]:
            # Check if movie has favorite genres
            for genre in favorite_genres:
                if genre in movie["genres"]:
                    recommendations.append(movie)
                    break
    
    # Sort by rating
    recommendations.sort(key=lambda m: m["average_rating"], reverse=True)
    return recommendations[:5]
```

### Step 4: Build Menu System
```
=== Movie Recommendation System ===
1. Add Movie
2. Search Movies
3. Rate Movie
4. Write Review
5. View Recommendations
6. View Top Rated
7. Filter by Genre
8. User Statistics
9. View Watch History
10. Exit
```

## Example Usage

```
Choose option: 2
Search movie: The Matrix
Found 1 movie:
[1] The Matrix (1999)
    Director: Lana Wachowski, Lilly Wachowski
    Genres: Sci-Fi, Action
    Rating: 8.7/10 (1.2M reviews)
    Cast: Keanu Reeves, Laurence Fishburne

Choose option: 3
Which movie to rate? (enter ID): 1
Your rating (1-10): 9
Add review? (yes/no): yes
Your review: Mind-bending masterpiece! The action scenes are incredible.

✓ Rating submitted! (9/10)
✓ Review posted!

Choose option: 5
=== Recommendations for Alice ===
Based on your ratings and preferences (Sci-Fi, Action)

1. Inception (2010) - 8.8/10
   Director: Christopher Nolan
   "Mind-bending like The Matrix, you'll love this!"

2. Interstellar (2014) - 8.6/10
   Director: Christopher Nolan
   "Epic sci-fi adventure from the same director as Inception"

3. The Dark Knight (2008) - 9.0/10
   Director: Christopher Nolan
   "If you like great action and storytelling"

Choose option: 8
=== Alice's Statistics ===
Movies Rated: 45
Average Rating Given: 7.8/10
Most Watched Genre: Sci-Fi (32 movies)
Total Watch Time: 156 hours
Most Watched Director: Christopher Nolan (7 movies)
```

## Real-World Enhancement Ideas
1. **Social Features**: Follow friends, see their ratings
2. **Advanced Recommendations**: Machine learning algorithms
3. **Watch List**: Movies to watch later
4. **Notifications**: New releases in favorite genres
5. **Discussion Forums**: Discuss movies with other users
6. **Spoiler Detection**: Hide spoilers in reviews
7. **Multiple Ratings**: Different rating scales (visual, story, acting)
8. **API Integration**: Get real movie data from TMDB/OMDb
9. **Mobile App**: Convert to mobile application
10. **User Profiles**: Public profiles with favorites
11. **Awards Tracking**: Track movie awards
12. **Streaming Services**: Show which service has the movie

## Grading Criteria
- ✅ Movie management works (add, edit, delete)
- ✅ User authentication basic implementation
- ✅ Rating and review system works
- ✅ Search and filtering is accurate
- ✅ Recommendation engine produces relevant suggestions
- ✅ Statistics are calculated correctly
- ✅ Data persists between sessions
- ✅ UI is user-friendly
- ✅ Code is well-organized with clear functions
