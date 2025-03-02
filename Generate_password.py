import random
import string
def generate_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters
    elif complexity == 'high':
        characters == string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for _ in range(length))
    return password
def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password:"))
            if length < 8:
                print("Password length should be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Invalid input.Please enter a number.")
    while True:
        complexity = input("Enter the desired complexity of the password(low, medium, high): ")
        if complexity.lower() in['low', 'medium', 'high']:
            break
        else:
            print("Invalid input.Please enter low, medium, or high.")
    password = generate_password(length, complexity.lower())
    print(f"Generated Password:{password}")
if __name__ == "__main__":
    main()