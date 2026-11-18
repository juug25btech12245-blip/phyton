text = input("Enter a sentence: ").lower()

# Word frequency
word_freq = {}
for word in text.split():
    word = word.strip(".,!?;:")
    word_freq[word] = word_freq.get(word, 0) + 1

print("\nWord frequency:")
for w, c in word_freq.items():
    print(f"{w}: {c}")

# Character frequency
char_freq = {}
for ch in text:
    if ch.isalpha():
        char_freq[ch] = char_freq.get(ch, 0) + 1

print("\nCharacter frequency:")
for ch, c in sorted(char_freq.items()):
    print(f"{ch}: {c}")

most = max(word_freq, key=word_freq.get)
print("\nMost frequent word:", most, "->", word_freq[most])
