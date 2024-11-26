MAIN_CATEGORIES = {
    'General': 9,
    'Entertainment': {
        'Books': 10,
        'Film': 11,
        'Music': 12,
        'Musicals & Theatres': 13,
        'Television': 14,
        'Video Games': 15,
        'Board Games': 16,
        'Comics': 29,
        'Japanese Anime & Manga': 31,
        'Cartoon & Animations': 32,
    },
    'Science': {
        'Nature': 17,
        'Computers': 18,
        'Mathematics': 19,
        'Gadgets': 30,
    },
    'Mythology': 20,
    'Sports': 21,
    'Geography': 22,
    'History': 23,
    'Politics': 24,
    'Art': 25,
    'Celebrities': 26,
    'Animals': 27,
    'Vehicles': 28,
}

def get_main_categories():
    '''
    Tagastab peamiste kategooriate nimekirja.
    '''
    return list(MAIN_CATEGORIES.keys())

def get_subcategories(category_name):
    '''
    Tagastab alamkategooriate loendi antud peakategooria jaoks.
    '''
    return MAIN_CATEGORIES.get(category_name, {})
