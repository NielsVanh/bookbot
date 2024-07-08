def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        
def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_words = file_contents.split()
        print(len(file_words))
        
main()
count_words()