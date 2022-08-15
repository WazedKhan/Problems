sentance = 'aWESOME is cODING'.swapcase()

sentance = sentance.split()[::-1]
reversed_sentence = ' '.join(sentance)

print(reversed_sentence.strip())