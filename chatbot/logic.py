def get_bot_response(user_input):
    user_input = user_input.lower()

    if "balance" in user_input:
        return "You can check your account balance via net banking or ATM."
    elif "loan" in user_input:
        return "We offer home loans, car loans, and personal loans."
    elif "interest" in user_input:
        return "Interest rates depend on the account type."
    elif "account" in user_input:
        return "You can open savings or current accounts online."
    elif "help" in user_input:
        return "Ask me about balance, loans, interest, or accounts."
    else:
        return "Sorry, I didn’t understand your query."
