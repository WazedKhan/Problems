def time_in_words(hour: int, minute: int) -> str:
    # black: ignore
    num_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "quarter",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        21: "twenty one",
        22: "twenty two",
        23: "twenty three",
        24: "twenty four",
        25: "twenty five",
        26: "twenty six",
        27: "twenty seven",
        28: "twenty eight",
        29: "twenty nine",
        30: "half",
    }
    hour_in_word = num_words.get(hour)

    if minute == 0:
        return f"{hour_in_word} o' clock"

    elif minute == 15:
        return f"quarter past {hour_in_word}"
    elif minute == 45:
        return f"quarter to {num_words.get(hour % 12 + 1)}"

    elif minute == 30:
        return f"half past {hour_in_word}"

    elif minute < 30:
        if minute == 1:
            return f"one minute past {hour_in_word}"
        return f"{num_words.get(minute)} minutes past {hour_in_word}"
    else:
        if 60 - minute == 1:
            return f"one minute to {num_words.get(hour % 12 + 1)}"
        return f"{num_words.get(60 - minute)} minutes to {num_words.get(hour % 12 + 1)}"
