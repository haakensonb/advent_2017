from itertools import permutations

with open('./day_4/input.txt') as f:
    passphrases = f.readlines()
passphrases = [line.strip() for line in passphrases]

def is_valid_1(p_input):
    phrase = p_input.split(' ')
    # Checks for duplicate words
    return len(phrase) == len(set(phrase))

def is_valid_2(p_input):
    all_anagrams = []
    words = p_input.split(' ')
    valid = False
    if len(words) == len(set(words)):
        valid = True

    for word in words:
        anagrams = set([''.join(p) for p in permutations(word)])
        # Remove the original word from the set
        if word in anagrams:
            anagrams.remove(word)
        all_anagrams.append(anagrams)
    
    for word in words:
        for anagrams in all_anagrams:
            if word in anagrams:
                valid = False

    return valid

def count_valid_passphrases(passphrases, validation_type):
    counter = 0
    for passphrase in passphrases:
        if validation_type(passphrase):
            counter += 1
    return counter

print(count_valid_passphrases(passphrases, is_valid_1))
print(count_valid_passphrases(passphrases, is_valid_2))