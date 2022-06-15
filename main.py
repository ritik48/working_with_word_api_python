import requests

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def search(text):
    content = requests.get(URL+text)
    if content.status_code == 404:
        print(f"{text} is not valid.")
        return
    content = content.json()
    contents = content[0]

    print("Word : ",contents["word"])
    phonetics = contents["phonetics"][0]["audio"]
    print("Audio : ",phonetics)

    meanings = contents["meanings"]

    for meaning in meanings:
        print(meaning["partOfSpeech"],": ")

        definitions = meaning["definitions"]

        for definion in definitions:
            print("Definition : ",definion["definition"])

        synonyms = meaning["synonyms"]
        antonyms = meaning["antonyms"]
        print("Synonyms  : ",','.join(synonyms))
        print("Antonyms  : ",','.join(antonyms))

        print("\n")


while True:
    word = input("Enter a word : ")
    search(word)
