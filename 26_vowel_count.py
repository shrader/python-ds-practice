from collections import Counter

def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    phrase = phrase.lower()
    vow_count = {}
    char_count = Counter(phrase)
    for vowel in vowels:
        if not char_count[vowel] == 0:
            vow_count[vowel] = char_count[vowel]

    return vow_count

print(vowel_count('HOW ARE YOU? i am great!'))