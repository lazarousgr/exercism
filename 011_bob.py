def response(hey_bob):
    bob_response = "Whatever."
    
    if hey_bob.isupper() and hey_bob.strip().endswith("?"):
        bob_response = "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        bob_response =  "Whoa, chill out!"
    elif hey_bob.strip().endswith("?"):
        bob_response = "Sure."
    elif hey_bob.isspace() or  not hey_bob:
        bob_response = "Fine. Be that way!"
        
    return bob_response

print("Whatever?     ".strip(), 2)