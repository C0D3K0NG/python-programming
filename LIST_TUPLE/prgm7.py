# Write a Python program that scans an email address and forms a tuple of user
# name and domain.

email = input("Enter your email address: ")

user_name, domain = email.split('@')
email_tuple = (user_name, domain)

print(email_tuple)
