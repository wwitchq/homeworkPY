"""
Создайте базу данных фильмов состоящая из столбцов: id,название, год выпуска, жанр, рейтинг.
Создайте функции для добавления фильма в базу, получения всех фильмов, получение фильма по определенному году, обновления рейтинга, удаления фильма.
"""
import sqlite3

# Создаем базу данных и таблицу для фильмов
def create_movie_database():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS movies 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      title TEXT, 
                      year INTEGER, 
                      genre TEXT, 
                      rating REAL)''')
    connection.commit()
    connection.close()

# Добавление фильма в базу
def add_movie(title, year, genre, rating):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies (title, year, genre, rating) VALUES (?, ?, ?, ?)", (title, year, genre, rating))
    connection.commit()
    connection.close()

# Получение всех фильмов
def get_all_movies():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    connection.close()
    return movies

# Получение фильма по определенному году
def get_movie_by_year(year):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies WHERE year=?", (year,))
    movies = cursor.fetchall()
    connection.close()
    return movies

# Обновление рейтинга фильма
def update_rating(movie_id, new_rating):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE movies SET rating=? WHERE id=?", (new_rating, movie_id))
    connection.commit()
    connection.close()

# Удаление фильма
def delete_movie(movie_id):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
    connection.commit()
    connection.close()
