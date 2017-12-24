passphrases = [line.strip() for line in open('./day_4/input.txt').readlines()]

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

    for i, word in enumerate(words):
        for other_word in words[i+1:]:
            # Words are anagrams if both end up the same when sorted
            if sorted(word) == sorted(other_word):
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