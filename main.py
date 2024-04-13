def letterCounter(string):

    dict = {}
    for l in string.lower():
        if not l.isalpha():
            continue

        if l in dict:
            dict[l] += 1
        else:
            dict[l] = 1

    return dict

def letterDictToList(dict):

    list = []
    for key in dict.keys():

        new_dict = {
            "letter": key,
            "count": dict[key]
        }
        list.append(new_dict)
    
    return list

def sort_on(dict):
    return dict["count"]

if __name__ == '__main__':

    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()

    word_count = len(file_contents.split())
    letter_dict = letterCounter(file_contents)
    letter_list = letterDictToList(letter_dict)
    letter_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt --")
    print(f"{word_count} words found in the document")

    for dict in letter_list:
        
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")

    print("--- End report ---")