email = input("Enter the email address: ")
index_at = email.index("@")

username = email[:index_at]
domain = email[index_at+1:]

print(f"The Username is: {username}")
print(f"The Domain is: {domain}")
