def favorite_books():
    return [
        {"title": "LOTR", "author": "J. R. R. Tolkien"},
        {"title": "The Hobbit", "author": "J. R. R. Tolkien"},
        {"title": "Peanutbutter", "author": "Ming"},
    ]


def first_three_books():
    books = favorite_books()
    return books[:3]

def student_database():
    return {
        "Bob": "1109",
        "Rob": "1110",
        "Job": "1111",
    }
