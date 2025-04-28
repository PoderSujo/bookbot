from stats import (
    word_counter, 
    char_counter, 
    sorted_char_counter)
import sys
# This function counts the number of words in a given text.
def get_book_text(path):
 with open(path) as f:
  text = f.read()
  return text
def main():
  book_path = ""
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    return sys.exit(1)
  book_path = sys.argv[1]
  try:
    book_text = get_book_text(book_path)
  except FileNotFoundError:
    print(f"File not found: {book_path}")
    return sys.exit(1)

  
  lista = sorted_char_counter(char_counter(book_text))
   
  print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...\n----------- Word Count ----------")
  print(f"Found {word_counter(book_text)} total words")
  print("----------- Character Count ------")
  for i in lista:
    print(f"{i['char']}: {i['num']}")
  print("============= END ===============")
main()