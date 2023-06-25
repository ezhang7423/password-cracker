from collections import Counter
import itertools

import tqdm
from pyrage import passphrase
from math import comb

with open("secret.age", 'rb') as f:        
    bFileText = f.read()
        

options_1 = ['war', 'whose', 'water', 'whatever', 'drawn', 'who', 'what', 'was']
options_2 = ['given', 'encreased', 'seven', 'net', 'ten', 'chosen']
lasts = ['do', 'tender', 'nine', 'reason', 'granting', 'no', 'consent', 'redress', 'seats', 'in', 'derived', 'it', 'ever', 'had', 'state', 'event', 'denied', 'are', 'one', 'sign', 'iv', 'and', 'consist', 'intents', 'signed', 'vi', 'as', 'grants', 'i', 'giving', 'arising', 'greatest', 'vested', 'created', 'charged', 'entered', 'grant', 's', 'sent', 'congress', 'granted', 'its', 'at', 'enter', 'end', 'd', 'ended', 'vest', 'raise', 'grand', 'retained', 'desire', 'an', 'v', 'has', 'seat', 'senate', 'is', 'done', 'so', 'states', 'standard', 'danger', 'test', 'stated', 'a', 'raising', 'seas', 'give', 'on', 'date', 're']


# constraint 1
validLetterCounts = {
   'a': 3, 'n': 4, 'd': 2, 'i': 2, 'o': 1, 't': 2, 'e': 3, 'r': 2, 's':3, 'v': 1, 'g': 2, 'w': 1, 'c': 1, 'h': 1
} 

def gen_combinations(length, max_lasts=3):
    # Combining one element from options_1, one from options_2, and up to three from lasts
    results = []
    for last_count in range(1, max_lasts + 1):
        gen = itertools.product(options_1, options_2, itertools.combinations(lasts, last_count))
        for option_1, option_2, last_options in tqdm.tqdm(gen, total=48*comb(len(lasts), last_count)):
            combination = ''.join([option_1, option_2, *last_options])
            # Filter combinations based on the number of characters
            if len(combination) == length:
                results.append([option_1, option_2, *last_options])
    return results

    
    



def decrypt(word):
    try:
        return passphrase.decrypt(bFileText, word)
    except pyrage.DecryptError:
        return False


if __name__ == '__main__':
    # Example usage:
    max_length = sum(validLetterCounts.values())  # specify max length of the combination string
    all_combinations = gen_combinations(max_length, max_lasts=5)
    ftd_combinations = []
    for c in tqdm.tqdm(all_combinations):
        if dict(Counter(''.join(c))) == validLetterCounts:
            ftd_combinations.append(c)
    print(ftd_combinations)
    