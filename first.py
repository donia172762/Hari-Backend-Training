print ("Hello, World!")
total = 0

for i in range(1, 21):
    if i % 2 == 0:
        total += i

print(total)

numbers = [4, 15, 8, 23, 42, 16]

for n in numbers:
    if n > 10:
        print(n)

numbers = [12, 45, 7, 89, 23, 56, 91, 34]

largest = numbers[0]

for n in numbers:
    if n>largest : 
        largest = n
        
print(largest)

scores = {
    "python": 85,   
    "SQL": 40,
    "Git": 70,
    "Docker": 30
}
total_score = 0
for subject, score in scores.items():
    if score < 50:
        print(f"{subject}: Needs Improvement")
    total_score += score
avg_score = total_score / len(scores)
print(f"Average Score: {avg_score}")

def calculate_avg(scores):
    total_score = 0

    for score in scores.values():
        total_score += score

    avg = total_score / len(scores)
    return avg
print(calculate_avg(scores))

user = {
    "username": "donia",
    "password": "12345"
}
def login(user):
    attempts = 0
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == user["username"] and password == user["password"]:
            print("Login successful!")
            break
        else:
            print("Invalid credentials.")
            attempts += 1

        if attempts == 3:
         print("Account locked!")
        
   
login(user)

def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False  
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    return True
print(validate_password("Donia123"))
