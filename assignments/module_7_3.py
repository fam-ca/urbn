class WordFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                line_result = ''
                for line in file:
                    line_lowered = line.lower()
                    
                    punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for char in line_lowered:
                        if char not in punc:
                            line_result += char
                all_words[file_name] = line_result.split()
        return all_words
    
    def find(self, word):
        word_found = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            for i in range(len(value)):
                if word.lower()==value[i]:
                    word_found[key] = i+1
                    return word_found
    
    def count(self, word):
        count = 0
        word_count = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            for i in range(len(value)):
                if word.lower()==value[i]:
                    count += 1
        word_count[key] = count
        return word_count



finder2 = WordFinder('assignments/files/file1.txt', 'assignments/files/file2.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

finder1 = WordFinder('assignments/files/MotherGoose.txt')
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordFinder('assignments/files/RudyardKiplingIf.txt',)
print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))