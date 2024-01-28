import codecs

def add_user(username, real_name, password):
    try:
        with open("passwd.txt", "a") as file:  # Encrypt the password using ROT-13 encoding
            encrypted_password = codecs.encode(password, 'rot_13')
            file.write(f"{username}:{real_name}:{encrypted_password}\n")
        print("User Created.")
    except IOError:
        print("Error: Unable to add user.")

if __name__ == "__main__":
    # Input new user details
    new_username = input("Enter new username: ")
    new_real_name = input("Enter real name: ")
    new_password = input("Enter password: ")
    
    # Check if the username already exists
    with open("passwd.txt", "r") as file:
        for line in file:
            if new_username == line.split(":")[0]:
                print("Cannot add. Most likely username already exists.")
                break
        else:
            add_user(new_username, new_real_name, new_password)



# Function to change the password of an existing user
def change_password(username, current_password, new_password):
    try:
        with open("passwd.txt", "r") as file:
            lines = file.readlines()
        with open("passwd.txt", "w") as file:
            for line in lines:
                parts = line.split(":")
                if parts[0] == username:
                    # Encrypt the current password and compare with the stored encrypted password
                    encrypted_current_password = codecs.encode(current_password, 'rot_13')
                    if parts[2].strip() == encrypted_current_password:
                        # If current password matches, encrypt and write the new password to the file
                        encrypted_new_password = codecs.encode(new_password, 'rot_13')
                        file.write(f"{parts[0]}:{parts[1]}:{encrypted_new_password}\n")
                        print("Password changed.")
                    else:
                        print("Current password is invalid. No change made.")
                else:
                    file.write(line)
    except IOError:
        print("Error: Unable to change password.")

if __name__ == "__main__":
    # Input username and passwords
    target_username = input("User:             ")
    current_password = input("Current Password: ")
    new_password = input("New Password:     ")
    confirm_password = input("Confirm:          ")
    
    if new_password == confirm_password:
        change_password(target_username, current_password, new_password)
    else:
        print("Passwords do not match. No change made.")
        
        


# Function to check if a user can login
def check_login(username, password):
    try:
        with open("passwd.txt", "r") as file:
            for line in file:
                parts = line.split(":")
                if parts[0] == username:
                    # Encrypt the input password and compare with the stored encrypted password
                    encrypted_password = codecs.encode(password, 'rot_13')
                    if parts[2].strip() == encrypted_password:
                        return True
                    else:
                        return False
        return False
    except IOError:
        print("Error: Unable to check login.")

if __name__ == "__main__":
     # Input login credentials
    login_username = input("User:     ")
    login_password = input("Password: ")
    
    if check_login(login_username, login_password):
        print("Access granted.")
    else:
        print("Access denied.")
        
# Function to delete a user from the passwd.txt file       
def delete_user(username):
    try:
        with open("passwd.txt", "r") as file:
            lines = file.readlines()
        with open("passwd.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ":"):
                    file.write(line)
        print("User Deleted.")
    except IOError:
        print("Error: Unable to delete user.")

if __name__ == "__main__":
    # Input username to be deleted
    target_username = input("Enter username: ")
    delete_user(target_username)
