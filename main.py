def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        return file_contents
        
def count_words():
    file_contents = main()
    file_words = file_contents.split()
    print(len(file_words))
    
def count_characters():
    file_contents = main().lower()
    characters = {}
    for i in range(len(file_contents)):
        if file_contents[i] not in characters:
            characters[file_contents[i]] = 1
        else:
            characters[file_contents[i]] += 1
    
    return characters
     
        
# main()
# count_words()
print(count_characters())