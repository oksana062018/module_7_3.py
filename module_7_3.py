import io

class WordsFinder:

    def __init__(self, *file_names):   # Сохраняем названия файлов в виде списка
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                # Читаем строки файла
                content = f.read().lower()
                for k in  [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    content = content.replace(k, '')   # замена знаков
                    words = content.split()
                    all_words[file_name] = words

        return all_words

    def find(self, word):
        res = {}
        for i, word_ in self.get_all_words().items():
            for j, w in enumerate(word_,1):
                if w == word.lower():
                    res[i]=j
                    break
        return res

    def count(self, word):
        results = {}
        for i , wd in self.get_all_words().items():
            results[i] = wd.count(word.lower())   # Считаем количество вхождений слова

        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего