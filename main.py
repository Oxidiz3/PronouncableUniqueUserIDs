from random import randint, random


class IdGenerator:
    def __init__(self, wordList):
        self.wordList = wordList
        self.seed = randint(0, 2^31)
    
    def get_new_id(self):
        new_id_list = [self.get_random_word() for x in range(4)]
        new_id = self.squash_list_to_string(new_id_list)

        return new_id

    def squash_list_to_string(self, list):
        new_string = ""
        for x in list:
            new_string += x.strip() 
            new_string += "-"
        return new_string[0:-1]
        
    def get_random_word(self):
        word_position = randint(0, len(self.wordList)-1)
        return self.wordList[word_position]

def main():
    wordList = []
    with open("1-syllable-words.txt", "r") as file:
        wordList = file.readlines()
    
    id_generator = IdGenerator(wordList)
    for x in range(10):
        print(id_generator.get_new_id())


if __name__=="__main__":
    main()