# email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

#This will split the email into 2 halfs, first half contains the characters before @ and other half contains characters after the @
#The first half we naed it username and other half we named it domain
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

#re.search(pattern, string, flags=0)

# apilneupane123@gmail.com

import re

email = input("What's your email? ").strip()

if re.search(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
