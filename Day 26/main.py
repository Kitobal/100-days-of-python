import pandas

# load data from csv to a pandas Data Frame
df = pandas.DataFrame(pandas.read_csv("nato_phonetic_alphabet.csv"))

# save the data in a dictionary using list comprehension
nato_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
# print(nato_alphabet)


def generate_phonetic():
    input_word = input("Enter a word: ")
    try:
        output_list = [nato_alphabet[letter] for letter in input_word.upper() if letter != " "]
    except KeyError:
        print("Only letters please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
