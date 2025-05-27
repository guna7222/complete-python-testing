# Longest Word in a sentence

class LongestWord:

    def __init__(self, sentence):
        self.sentence = sentence

    def longest_word(self):
        initial_count = ""
        words = self.sentence.split()
        for i in words:
            if len(i) > len(initial_count):
                initial_count = i
        print(initial_count)



user_input_for_longest_word = str(input("Enter a word"))

# object
obj = LongestWord(user_input_for_longest_word)
obj.longest_word()