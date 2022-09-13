sentence1 = "My name is Haley"
sentence2 = "My cook Haley"
def areSentencesSimilar( sentence1, sentence2):
    if len(sentence1) < len(sentence2):
        return False

    sentence1 = list(sentence1.split(' '))
    sentence2 = list(sentence2.split(' '))

    while sentence2:
        
        if sentence1[0] == sentence2[0]:
            sentence2.pop(0)
        elif sentence1[-1] == sentence2[-1]:
            sentence2.pop[-1]
        else:
            return False

        return True



print(areSentencesSimilar(sentence1, sentence2))