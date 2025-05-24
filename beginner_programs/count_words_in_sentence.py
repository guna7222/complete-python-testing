# Count words in a sentence

class CountWordsInASentence:

    def __init__(self, sentence):
        self.sentence = sentence

    def count_words_in_a_sentence(self):
        returns_list = self.sentence.split(" ")
        count_words = len(returns_list)
        return  count_words

    def display_message(self):
        print(f"total words in a sentence is: {self.count_words_in_a_sentence()}")


sentence_obj = CountWordsInASentence("Welcome to the python course")
sentence_obj.display_message()