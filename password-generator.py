import random
import string
import sys

def generate_password(length=12):
    """
    Generate a random password of specified length using letters, numbers, and special characters
    
    Parameters:
    - length: Length of the password (default: 12)
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password
    remaining_length = length - len(password)
    all_chars = lowercase + uppercase + digits + special
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password characters
    random.shuffle(password)
    return ''.join(password)

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
    print("1. Generate a memorable passphrase")
    print("2. Generate a random password")
    
    try:
        choice = int(input("\nEnter your choice (1 or 2): "))
        
        if choice == 1:
            num_words = int(input("\nHow many words would you like in your passphrase? (2-5, default: 3): ") or 3)
            num_words = max(2, min(5, num_words))  # Ensure number is between 2 and 5
            
            add_number = input("Would you like to add a number? (y/n, default: y): ").lower() != 'n'
            add_special = input("Would you like to add a special character? (y/n, default: y): ").lower() != 'n'
            
            result = generate_passphrase(num_words, add_number, add_special)
            print("\nYour generated passphrase is:")
        
        elif choice == 2:
            length = int(input("\nEnter desired password length (8-32, default: 12): ") or 12)
            length = max(8, min(32, length))  # Ensure length is between 8 and 32
            
            result = generate_password(length)
            print("\nYour generated password is:")
        
        else:
            print("\nInvalid choice. Please choose 1 or 2.")
            sys.exit(1)
            
        print(f"\n\t{result}\n")
        print("This password is secure!")
        print("Remember to store it safely and never share it with anyone.")
        
    except KeyboardInterrupt:
        print("\nPassword generation cancelled.")
        sys.exit(0)
    except ValueError:
        print("\nPlease enter a valid number.")
        sys.exit(1)

if __name__ == "__main__":
    main()
