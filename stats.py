def word_counter(text):
  return len(text.split())
# This function counts the number of words in a given text.
def char_counter(text):
    char_dict = {}
    text = text.lower()
    for char in text:
            if char.isalpha():
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
    return char_dict
# This function counts the number of characters in a given text.

def sorted_char_counter(dicts):
    lista = [{"char": k, "num": v} for k, v in dicts.items()]
    lista.sort(key=lambda x: x["num"], reverse=True)
    return lista

