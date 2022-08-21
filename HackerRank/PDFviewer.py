import string
import time
from turtle import title

start = time.time()
h = list('1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'.replace(' ', ''))
word = 'abc'
def designerPdfViewer(h, word):
    alphabet = list(string.ascii_lowercase)
    t_letter = []
    for i in word:
        for count, item in enumerate(alphabet):
            if i == item:
                t_letter.append(h[count])
    return(len(word) * int(max(t_letter)))

print(designerPdfViewer(h, word))
end = time.time()

print(end - start)