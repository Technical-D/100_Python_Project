# Word Count program
def word_count(words, word_count_dict):
    for word in words:
        word = word.lower()
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1

print("Welcome to a Word Count Program!")
while True:
    file_path = input("Enter a file path for word count: ")
    try:
        word_count_dict = {}
        with open(file_path, 'r') as f:
            for lines in f:
                words = lines.split()
                word_count(words, word_count_dict)
        
        sorted_word_by_count = sorted(word_count_dict.items(), key=lambda x:x[1], reverse=True)
        print("Top 10 most repeated words!")
        print("Word |", "Count")
        for i, (word , count) in enumerate(sorted_word_by_count[:10]):
            print(word, ":",count)
        
        break
    except FileNotFoundError:
        print("File not found! Enter a valid file path.")




