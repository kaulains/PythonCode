"""
Translate a word or sentence into Pig Latin.
"""
def translate(text):
    """
    Rules:
    - If a word begins with a vowel, or starts with "xr" or "yt",
      add "ay" to the end.
    - If a word begins with one or more consonants, move the leading
      consonant cluster to the end and add "ay".
    - Treat "qu" as a single consonant sound.
    - Treat "y" as a vowel when it is not the first letter.
    - Works for single words and multi-word sentences.
    """

    vowels = "aeiou"
    words = text.split()
    result_words = []

    for inner_text in words:
        # Rule 1: vowel OR xr OR yt
        if (
            inner_text[0] in vowels
            or inner_text.startswith("xr")
            or inner_text.startswith("yt")
        ):
            result_words.append(inner_text + "ay")
            continue

        index = 0

        while index < len(inner_text):
            # handle "qu"
            if inner_text[index:index+2] == "qu":
                index += 2
                break

            # 'y' is vowel only if not first letter
            if index != 0 and inner_text[index] == "y":
                break

            if inner_text[index] in vowels:
                break

            index += 1

        result_words.append(inner_text[index:] + inner_text[:index] + "ay")

    return " ".join(result_words)