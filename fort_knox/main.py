import cryptonash

print("""
====================================================================================================
                                            Welcome to Fort Knox
====================================================================================================
      1=> Register
      2=> Login
      """)

choice = input("Choose an option: ")
if choice == '1':
    email = input("Email address: ")
    password = input("Password: ")
    password_hash = cryptonash.calculate_sha256(password)
    with open('database.txt','a') as file:
        file.write(f"{email}:{password_hash}\n")
elif(choice == 2):
    #TODO
    pass
else:
    print("Invalid choice, see you next time")