"""Classical Bobs function """ 

def response(hey_bob):
    """
    Generate Bob's response based on the user's message.

    Rules:
    - Silence -> "Fine. Be that way!"
    - Yelled question -> "Calm down, I know what I'm doing!"
    - Question -> "Sure."
    - Yelling -> "Whoa, chill out!"
    - Anything else -> "Whatever."
    """

    # Remove leading and trailing whitespace
    hey_bob = hey_bob.strip()

    # Handle empty or whitespace-only input
    if hey_bob == "":
        return "Fine. Be that way!"

    # Determine whether the hey_bob is a question
    is_question = hey_bob.endswith("?")

    # Determine whether the hey_bob is being yelled
    # A valid yell must contain alphabetic characters
    has_letters = any(char.isalpha() for char in hey_bob)
    is_yelling = has_letters and hey_bob.isupper()

    # Handle yelled questions
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"

    # Handle normal questions
    if is_question:
        return "Sure."

    # Handle yelling
    if is_yelling:
        return "Whoa, chill out!"

    # Default response
    return "Whatever."
        
        
