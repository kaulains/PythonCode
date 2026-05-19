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

    for text in words:
        # Rule 1: vowel OR xr OR yt
        if (
            text[0] in vowels
            or text.startswith("xr")
            or text.startswith("yt")
        ):
            result_words.append(text + "ay")
            continue

        i = 0

        while i < len(text):
            # handle "qu"
            if text[i:i+2] == "qu":
                i += 2
                break

            # 'y' is vowel only if not first letter
            if i != 0 and text[i] == "y":
                break

            if text[i] in vowels:
                break

            i += 1

        result_words.append(text[i:] + text[:i] + "ay")

    return " ".join(result_words)