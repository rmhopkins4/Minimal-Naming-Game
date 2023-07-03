import random

class Agent():
    def __init__(self, name):
        self.name = name
        self.vocabulary = []
        
    def communicate(self, listener):
        # pick random word 
        if len(self.vocabulary) > 0:
            word = random.choice(tuple(self.vocabulary))
        # or generate one at random if one does not exist
        else:
            word = generate_new_word()
            
        # if listener knows the same word, consensus is reached
        if word in listener.vocabulary:
            self.vocabulary = [word]
            listener.vocabulary = [word]
        # if the listener does not know the word, add it to their vocabulary
        else:
            listener.vocabulary.append(word)
            
            
def generate_new_word(num_syllables = 3):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    nasals = "nm"
    
    word = ''
    for _ in range(num_syllables):
        pattern = random.choice(['CV', 'V', 'CVN', 'VN'])
        for char in pattern:
            if char == 'C':
                word += random.choice(consonants)
            elif char == 'V':
                word += random.choice(vowels)
            elif char == 'N':
                word += random.choice(nasals)
                
    return word

print(generate_new_word())