import random

tile_distribution = {'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6, 'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2, 'K': 1, 'J': 1, 'X': 1, 'Q': 1, 'Z': 1}
tile_points = {'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10, 'E': 1, 'A': 1, 'I': 1, 'O': 1, 'U': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1}

dictionary_txt = open('dictionary.txt', 'r').read()

def generate_bag(letters):
    bag_tiles = []
    for letter in letters:
        for i in range(letters[letter]):
            bag_tiles.append(letter)
    
    return bag_tiles

def generate_points(letters):
    total_points = sum(tile_points[letter] for letter in letters)
    return total_points

def tile_drawn(letter):
    return letter.pop(0)

def find_word_from_dic(rack, dict):
    validated_words = []
    dict = dict.split('\n')
    created_word = []
    for word in dict:
        word_array = word.upper()
        for letter in word_array:
            if letter in rack:
                created_word.append(rack.pop(rack.index(letter)))
        if len(created_word) == len(word):
            validated_words.append(word)
        rack += created_word
        created_word = []
    return validated_words

# function to find word with the most points 

def play_scrabble():
    new_bag = generate_bag(tile_distribution)
    random.shuffle(new_bag)
    assigned_tiles = []
    for i in range(7):
        assigned_tiles.append(tile_drawn(new_bag))
    print(f'The tiles generated are...\n{assigned_tiles}')
    generate_word = find_word_from_dic(assigned_tiles, dictionary_txt)
    
    

play_scrabble()
