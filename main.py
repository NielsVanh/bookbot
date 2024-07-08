def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        # print(file_contents)
        return file_contents
        
def count_words():
    file_contents = main()
    
    file_words = file_contents.split()
    
    # print(len(file_words))
    return len(file_words)
    
def count_characters():
    file_contents = main().lower()
    characters = {}
    
    for i in range(len(file_contents)):
        if file_contents[i] not in characters:
            characters[file_contents[i]] = 1
        else:
            characters[file_contents[i]] += 1
    
    return characters

def sort_characters():
    dict_characters = count_characters()
    characters = []
    
    for character, character_count in dict_characters.items():
        if character.isalpha():
            characters.append({
                "character": character,
                "character_count": character_count
            })
            
    def sort_on(dict):
        return dict["character_count"]
    
    characters.sort(reverse=True, key=sort_on)
    return characters
    
    
def make_report():
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document")
    print("")
    
    for character_dict in sort_characters():
        print(f"The {character_dict['character']} was found {character_dict['character_count']} times")
    
    print("--- End report ---")
        
make_report()