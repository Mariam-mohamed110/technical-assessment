import random
import readline
import itertools

tile_distribution = {'E': 12, 'A': 9, 'I': 9, 'O': 8, 'N': 6, 'R': 6, 'T': 6, 'L': 4, 'S': 4, 'U': 4, 'D': 4, 'G': 3, 'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2, 'H': 2, 'V': 2, 'W': 2, 'Y': 2}

def open_dictionary():
    with open('dictionary.txt') as f:
        dictionaryTxt = readline(f)
    return dictionaryTxt

def generate_bag(letters):
    bag_tiles = []
    for letter in letters:
        for i in range(letters[letter]):
            bag_tiles.append(letter)
    
    return bag_tiles

def generate_points(letters):
    sum = 0
    for i in str(letters):
            if type(i) == str:
                if i == 'D' or i == 'G':
                    sum += 2
                elif i == 'B' or i == 'C' or i == 'M' or i == 'P':
                    sum += 3
                elif i == 'F' or i == 'H' or i == 'V' or i == 'W' or i == 'Y':
                    sum += 4
                elif i == 'K':
                    sum += 5
                elif i == 'J' or i == 'X':
                    sum += 8
                elif i == 'Q' or i == 'Z':
                    sum += 10
                else:
                    sum += 1
    return sum

# print(generatePoints('D, A'))
# print(generatePoints('GUARDIAN')) 

def tile_drawn(letter):
    return letter.pop(0)

def check_word(word):
    checked_word = []
    if word in open_dictionary():
        checked_word.append(word)
    
    return checked_word

def find_word(word_from_player):
# try to make the longest word possible first
# move on to make shorter words if not available
    player_hand = len(word_from_player)
# How do I do that?
# is there a method in built?
# arrange letters in an object?
# searched online = permutation
#  idea using permutation,
#  = different ways in which a given set of objects can be arranged
# using the letters given, it finds the most amount of word combinations
# maybe cross referencing using xt file?
# ran out of time 
# will look into this later, seems interesting :)
        


def play_scrabble():
    new_bag = generate_bag(tile_distribution)
    random.shuffle(new_bag)
    assigned_tiles = [tile_drawn(new_bag), tile_drawn(new_bag), tile_drawn(new_bag), tile_drawn(new_bag), tile_drawn(new_bag), tile_drawn(new_bag), tile_drawn(new_bag)]
    return assigned_tiles

print(play_scrabble())
# prints out an array of letters