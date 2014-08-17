def generator(grammar, tok):
    if tok not in grammar:
        return tok
    else:
        rule = grammar[tok]
        alt = random.choice(rules)
        toks = alt.split()
        return " ".join([generate(grammar,tok) for tok in toks])


def sum(i):
    if i == 0:
        return i
    else:
        return i + sum(i-1)

print sum(3)