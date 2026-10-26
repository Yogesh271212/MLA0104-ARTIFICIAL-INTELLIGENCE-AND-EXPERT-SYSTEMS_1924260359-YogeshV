def is_vowel(ch):
    return ch.lower() in {'a', 'e', 'i', 'o', 'u'}

def analyze_sentence(sentence):
    vowels_found = [ch for ch in sentence if is_vowel(ch)]
    return vowels_found, len(vowels_found)

text = "Artificial Intelligence and Expert Systems Laboratory"
vowels, count = analyze_sentence(text)
print("Input Sentence:", text)
print("Identified Vowels:", vowels)
print("Total Vowel Count:", count)
