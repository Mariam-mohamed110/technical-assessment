import random
from itertools import permutations

tile_distribution = {'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6, 'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2, 'K': 1, 'J': 1, 'X': 1, 'Q': 1, 'Z': 1}
tile_points = {'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10, 'E': 1, 'A': 1, 'I': 1, 'O': 1, 'U': 1, 'N': 1, 'R': 1, 'T': 1, 'L': 1, 'S': 1}

def open_dictionary():
    dictionary_txt = open('scrabble/dictionary.txt', 'r').read()
    return dictionary_txt

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

def check_word(word):
    if word in open_dictionary():
        return True
    else:
        False
    

def find_word(word_from_player):
    for permutation in permutations(word_from_player):
        new_word = "".join(permutation)
        new_word = new_word.lower()
        validated_word = []
        print(new_word)
        if check_word(new_word):
            print(validated_word)
            return validated_word.append(new_word)

print(find_word("HWEN"))

def play_scrabble():
    new_bag = generate_bag(tile_distribution)
    random.shuffle(new_bag)
    assigned_tiles = []
    for i in range(7):
        assigned_tiles.append(tile_drawn(new_bag))
    print(f'The tiles generated are...\n{assigned_tiles}')
    play_game = find_word(assigned_tiles)
    
    return play_game

# print(play_scrabble())
