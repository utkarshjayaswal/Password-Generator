import random
import string
import sys

def load_wordlist():
    """Returns a list of common words for generating passphrases"""
    words = [
        "apple", "banana", "orange", "grape", "lemon", "peach", "mango",
        "house", "table", "chair", "light", "phone", "book", "desk",
        "happy", "sunny", "green", "blue", "quick", "calm", "bright",
        "tiger", "eagle", "panda", "whale", "horse", "koala", "zebra",
        "river", "ocean", "cloud", "storm", "moon", "star", "wind",
        "music", "dance", "dream", "smile", "laugh", "heart", "peace"
    ]
    return words

def generate_passphrase(num_words=3, add_number=True, add_special=True):
    """
    Generate a memorable passphrase using common words and optional numbers/special characters
    
    Parameters:
    - num_words: Number of words to include in the passphrase (default: 3)
    - add_number: Whether to add a random number (default: True)
    - add_special: Whether to add a special character (default: True)
    """
    words = load_wordlist()
    selected_words = random.sample(words, num_words)
    
    # Capitalize the first letter of each word
    selected_words = [word.capitalize() for word in selected_words]
    
    # Add a random number if requested
    if add_number:
        selected_words.append(str(random.randint(100, 999)))
    
    # Add a special character if requested
    if add_special:
        special_chars = "!@#$%^&*"
        selected_words.append(random.choice(special_chars))
    
    # Join the words with hyphens
    passphrase = "-".join(selected_words)
    return passphrase

def main():
    print("\n=== Friendly Password Generator ===\n")
    
    try:
        num_words = int(input("How many words would you like in your passphrase? (2-5, default: 3): ") or 3)
        num_words = max(2, min(5, num_words))  # Ensure number is between 2 and 5
        
        add_number = input("Would you like to add a number? (y/n, default: y): ").lower() != 'n'
        add_special = input("Would you like to add a special character? (y/n, default: y): ").lower() != 'n'
        
        passphrase = generate_passphrase(num_words, add_number, add_special)
        
        print("\nYour generated passphrase is:")
        print(f"\n\t{passphrase}\n")
        print("This passphrase is both memorable and secure!")
        print("Remember to store it safely and never share it with anyone.")
        
    except KeyboardInterrupt:
        print("\nPassword generation cancelled.")
        sys.exit(0)
    except ValueError:
        print("\nPlease enter a valid number.")
        sys.exit(1)

if __name__ == "__main__":
    main()
