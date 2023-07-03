import random

num_agreements = 0

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
            word = self.__generate_new_word()
            self.vocabulary.append(word)
            
        # if listener knows the same word, consensus is reached
        if word in listener.vocabulary:
            self.vocabulary = [word]
            listener.vocabulary = [word]
            # track agreement
            return 1
            
        # if the listener does not know the word, add it to their vocabulary
        else:
            listener.vocabulary.append(word)
            # no agreement
            return 0
    
    def __generate_new_word(self, max_syllables = 3):
        
        #num_syllables = random.randint(1, max_syllables)
        
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        nasals = "nm"
        
        word = ''
        for _ in range(max_syllables):
            pattern = random.choice(['CV', 'V', 'CVN', 'VN'])
            for char in pattern:
                if char == 'C':
                    word += random.choice(consonants)
                elif char == 'V':
                    word += random.choice(vowels)
                elif char == 'N':
                    word += random.choice(nasals)
                    
        return word