def discountPrices(sentence, discount):
    words = sentence.split(" ")
    for index, value in enumerate(words):
        if value.startswith("$", 0, len(value)) and value.replace("$","", 1).isnumeric():
            price = int(value.replace("$","", 1))
            discount_price = "%.2f" %(price*(100-discount)/100)
            words[index] = "$"+str(discount_price)

    return " ".join(words)

sentence = "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
discount = 50
print(discountPrices(sentence, discount))