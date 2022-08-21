morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
code = []

for word in words:
    morse = ''
    for i in word:
        morse += morseCode[ord(i)-97]
    if morse not in code:
        code.append(morse)

print(len(code))