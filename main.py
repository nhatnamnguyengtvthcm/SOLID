from single_responsibility.userHandle import UserHandler


def main():
    # Your code here
    valid_json_user = {"name": "John", "email": "john@gmail.com"}
    invalid_json_user = {"name": "Harry", "email": "harry@gmail"}

    user_handler = UserHandler()
    result = user_handler.create_user(valid_json_user)
    # result = user_handler.create_user(invalid_json_user)
    if result == "SUCCESS":
        print("User created successfully")  # User created successfully
    else:
        print("User creation failed")
    
if __name__ == "__main__":
    main()