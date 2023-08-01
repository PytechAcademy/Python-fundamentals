# Storing User Details in NoSQL Databases
users_db = {
    'user1': {
    'name': 'John Doe',
    'age': 30,
    'email': 'john@example.com',
    'city': 'New York',
},
"user2": {
    'name': 'Jane Smith',
    'age': 25,
    'email': 'jane@example.com',
    'city': 'Los Angeles',
}
}
# Accessing user details
user_id = 'user1'
user_details = users_db[user_id]
if user_details:
    print(f"User: {user_id}")
    print(f"Name: {user_details['name']}")
    print(f"Age: {user_details['age']}")
    print(f"Email: {user_details['email']}")
    print(f"City: {user_details['city']}")
else:
    print("User not found.")