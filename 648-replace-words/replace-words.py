class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_set = set(dictionary)
        splitted_sentence = sentence.split(' ')
        for i, word in enumerate(splitted_sentence):
            result = ''
            for char in word:
                result += char
                if result in dict_set:
                    splitted_sentence[i] = result
                    break
        return ' '.join(splitted_sentence)
            
