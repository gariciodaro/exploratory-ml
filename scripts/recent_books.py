"""
Module to find recent coding books

Autor: Gari
Date: June 2022
"""


def find_recent_coding_books(recent_books_pth, coding_books_pth):
    """Take two path, sent them to list, find the intersection
    Arg:
        recent_books_pth: (str) path to file, which contains the recent
        books.
        coding_books_pth: (str) path to file, coding books.
    Returns:
        recent_coding_books: (set) recent coding books.
    """
    with open(recent_books_pth, encoding='utf-8') as file_path_one:
        recent_books = file_path_one.read().split('\n')
    with open(coding_books_pth, encoding='utf-8') as file_path_two:
        coding_books = file_path_two.read().split('\n')
    # Intersection
    recent_coding_books = set(recent_books).intersection(coding_books)
    return recent_coding_books


if __name__ == '__main__':
    RECENT_CODING_BOOKS = find_recent_coding_books(
        '../data/books_published_last_two_years.txt',
        '../data/all_coding_books.txt')
    print(RECENT_CODING_BOOKS)
