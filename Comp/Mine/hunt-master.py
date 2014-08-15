# 00: start
# 01: next
# 02: killer koalas
# 03: upenn levine hall
# 04: saast
# 05: betrayal
# 06: Sunday night
# { More TBA }

from random import randint

CH_BASE = ord('a')

def char_to_val(ch):
    return ord(ch) - CH_BASE

def val_to_char(val):
    return chr(CH_BASE + val)

def shift_ch(ch, n):
    return val_to_char((char_to_val(ch) + n) % 26)

def shift(ciphertext, n):
    return ''.join([shift_ch(ch, n) for ch in ciphertext])

def caeser(ciphertext):
    if ciphertext.isalpha() and ciphertext.islower():
        for i in range(0, 26):
            candidate = shift(ciphertext, -i)
            print 'n = {}: {}'.format(i, candidate)
            resp = raw_input('Is this the correct decryption? ').lower()
            while resp != 'y' and resp != 'n':
                resp = raw_input('Is this the correct decryption [y/n] ').lower()
            if resp == 'y':
                print 'Message decrypted!'
                return candidate
        print 'Message not decrypted!'
        return None
    else:
        print 'Invalid input.  Ciphertext should only contain lower-cased letters.'
        return None

def caeser_enc(infilename, outfilename):
    with open(infilename, 'r') as f:
        pt = [l.strip().lower() for l in f.readlines()]
        ct = [''.join([shift_ch(ch, n)
                       for ch in l.strip().lower() if ch.isalpha()])
              for l,n in zip(pt, [randint(0, 25) for x in [0] * len(pt)])]
    print '\n'.join(pt)
    print '====='
    print '\n'.join(ct)
    with open(outfilename, 'w') as f:
        f.writelines([l + '\n' for l in ct])

#####

class LetterInventory(object):
    def __init__(self, s):
        s = s.lower().strip()
        self.inv = { val_to_char(i) : s.count(val_to_char(i))
                     for i in range(0, 26) }

    def __len__(self):
        return sum(self.inv.values())

    def __contains__(self, li):
        return not len([ c for c in
                         [ self.inv[ch] - li.inv[ch] for ch in self.inv.keys() ]
                       if c < 0 ]) > 0

    def __sub__(self, li):
        ret = LetterInventory('')
        ret.inv = { ch : self.inv[ch] - li.inv[ch] for ch in self.inv.keys() }
        return ret;

    def __str__(self):
        return ''.join([ ch * self.inv[ch] for ch in sorted(self.inv.keys()) ])

    def __repr__(self):
        return self.__str__()

def load_dictionary(filename):
    with open(filename) as f:
        return { word : LetterInventory(word)
                 for word in [l.strip() for l in f.readlines()] }

def prune_dictionary(dic, li):
    return { word : dic[word] for word in dic.keys()
             if LetterInventory(word) in li }

def prune_dictionary_by_size(dic, n):
    return { word : dic[word] for word in dic.keys()
             if len(word) >= n }

def prune_dictionary_by_prefix(dic, prefix):
    return { word : dic[word] for word in dic.keys()
             if word.startswith(prefix) }

def find_anagrams(dic, li, match):
    if len(li) <= 0:
        return [match] if len(match) > 0 else []
    res = []
    for word in dic.keys():
        if dic[word] in li:
            li1 = li - dic[word]
            res = res + find_anagrams(prune_dictionary(dic, li), li1, match + [word])
    return res

def anagrams_do_it():
    dic = load_dictionary('twl_2006_wordlist.txt')
    li = LetterInventory('widespreadwigwaggingwrinkliestwildebeest')
    print 'Finding: {0}'.format(li)
    dic = prune_dictionary(dic, li)
    print 'Length after word prune: {0}'.format(len(dic))
    dic = prune_dictionary_by_size(dic, 10)
    print 'Length after size prune: {0}'.format(len(dic))
    dic = prune_dictionary_by_prefix(dic, 'w')
    print 'Length after prefix prune: {0}'.format(len(dic))
    print find_anagrams(dic, li, [])

def freqs(filename):
    lines = [l.strip() for l in open(filename) if len(l) > 0]
    counts = { ch : 0 for ch in [chr(ord('a') + i) for i in range(0, 26)] }
    for line in lines:
        for ch in line:
            counts[ch] = counts[ch] + 1
    total = float(sum([len(l) for l in lines]))
    return { ch : round(counts[ch] / total, 5) for ch in counts }

def test_freqs():
    f_enc = freqs('pg8800-enc.txt')
    f_raw = freqs('pg8800-raw-treated.txt')
    results = zip(sorted(f_enc.items(), key=lambda p:p[1]), sorted(f_raw.items(), key=lambda p:p[1]))
    keys = { q[0] : p[0] for p,q in results }
    open('09-test-key.txt', 'w').writelines([v + '\n' for k,v in sorted(keys.items(), key=lambda p:p[0])])
