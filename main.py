from random import randint, random

'''Vowel Consonant Vowel Generator'''


class CVCGenerator:
    def __init__(self):
        self.vowels = "aeio"
        self.consonants = "bdfglpkz"
        self.num_consonants = len(self.consonants)
        self.num_vowels = len(self.vowels)
        pass

    def generate_id(self, seed):
        first_letter = (seed // (self.num_vowels * self.num_consonants)) % self.num_consonants
        second_letter = (seed // self.num_consonants) % self.num_vowels
        third_letter = seed % self.num_consonants
        return self.consonants[first_letter] + self.vowels[second_letter] + self.consonants[third_letter]

    def generate_a_sequence_of_ids(self, start, end):
        for x in range(start, end):
            print(self.generate_full_id(x))

    def generate_full_id(self, seed):
        # Moons 2.81E14 or 256^6 Currently does not work as intended
        # if seed > 2 ** 32:
        #     return "~" + \
        #            self.generate_id((seed // 2 ** 128) % 256) + self.generate_id((seed // 2 ** 64) % 256) \
        #            + "-" + \
        #            self.generate_id((seed // 2 ** 32) % 256) + self.generate_id((seed // 2 ** 16) % 256) \
        #            + "-" \
        #            + self.generate_id((seed // 2 ** 8) % 256) + self.generate_id(seed)
        # Planets 4.3 billion or 2^32
        if seed > 2 ** 16:
            return "~" + \
                   self.generate_id((seed // 2 ** 32) % 256) + self.generate_id((seed // 2 ** 16) % 256) \
                   + "-" \
                   + self.generate_id((seed // 2 ** 8) % 256) + self.generate_id(seed)
        # Stars 65_536 or 2^16
        elif seed > 2 ** 8:
            return self.generate_id((seed // 256) % 256) + self.generate_id(seed)
        # Galaxies 256 or 2^8
        else:
            return self.generate_id(seed)


class ChunkGenerator:
    def __init__(self, word_lists):
        self.word_lists = word_lists
        self.chunk_set = set()
        self.vowels = "aeiou"

    def process_word_lists(self):
        for list in self.word_lists:
            for word in list:
                chunk_list = self.new_chunk_up_word(word)
                for chunk in chunk_list:
                    if len(chunk) > 1:
                        self.chunk_set.add(chunk)

    def new_chunk_up_word(self, word):
        chunks = []
        temp_chunk = ""
        exhausted_vowel = False

        for letter in word:
            if len(temp_chunk) == 0:
                if letter in self.vowels:
                    temp_chunk += letter
                    continue
                continue

            if self.first_letter_is_vowel(temp_chunk):
                if letter in self.vowels and not exhausted_vowel:
                    temp_chunk += letter
                elif letter not in self.vowels:
                    temp_chunk += letter
                    exhausted_vowel = True
                else:
                    chunks.append(temp_chunk)
                    temp_chunk = letter

        chunks.append(temp_chunk)
        return chunks

    def chunk_up_word(self, word):
        chunks = []
        temp_chunk = ""
        for letter in word:
            if len(temp_chunk) == 0:
                temp_chunk += letter
                continue

            if self.first_letter_is_vowel(temp_chunk):
                if letter in self.vowels:
                    temp_chunk += letter
                else:
                    chunks.append(temp_chunk)
                    temp_chunk = letter
            else:
                if letter not in self.vowels:
                    temp_chunk += letter
                else:
                    chunks.append(temp_chunk)
                    temp_chunk = letter

        if temp_chunk != "":
            chunks.append(temp_chunk)
        return chunks

    def first_letter_is_vowel(self, word):
        return word[0] in self.vowels

    def get_consonant_chunks_list(self):
        chunks_list = []
        for chunk in self.chunk_set:
            if not self.first_letter_is_vowel(chunk):
                chunks_list.append(chunk)

        return chunks_list

    def get_vowel_chunks_list(self):
        chunks_list = []
        for chunk in self.chunk_set:
            if self.first_letter_is_vowel(chunk):
                chunks_list.append(chunk)

        return chunks_list


class IdGenerator:
    def __init__(self, consonant_chunk_list, vowel_chunk_list, chunk_list):
        self.consonant_chunk_list = consonant_chunk_list
        self.vowel_chunk_list = vowel_chunk_list
        self.chunk_list = chunk_list

    def get_new_id(self):
        new_id_list = [self.new_get_random_word() for x in range(4)]
        new_id = self.squash_list_to_string(new_id_list)

        return new_id

    def squash_list_to_string(self, list):
        new_string = ""
        for x in list:
            new_string += x
            new_string += "-"
        return new_string[0:-1]

    def get_random_word(self):
        prefix = self.vowel_chunk_list[randint(0, len(self.vowel_chunk_list) - 1)]
        middle = self.consonant_chunk_list[randint(0, len(self.consonant_chunk_list) - 1)]
        return prefix + middle

    def new_get_random_word(self):
        prefix = self.chunk_list[randint(0, len(self.chunk_list) - 1)]
        suffix = self.chunk_list[randint(0, len(self.chunk_list) - 1)]
        return prefix + suffix


def main():
    # for x in range(10):
    #     print(id_generator.get_new_id())
    # word_lists = []
    # for i in range(1, 6):
    #     with open(f"word_files/{i}-syllable-words.txt", "r") as file:
    #         word_lists.append([line.strip() for line in file.readlines()])
    #
    # chunker = ChunkGenerator(word_lists)
    # chunker.process_word_lists()
    #
    # id_generator = IdGenerator(chunker.get_consonant_chunks_list(), chunker.get_vowel_chunks_list(),
    #                            [x for x in chunker.chunk_set])
    # for x in range(10):
    #     print(id_generator.get_new_id())

    gen = CVCGenerator()
    gen.generate_a_sequence_of_ids(2 ** 32-16, 2 ** 32 + 2 ** 4)


if __name__ == "__main__":
    main()
