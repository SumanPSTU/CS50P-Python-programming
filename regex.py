import  re
email = str(input("enter your email: ")).strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$",email,flags=re.DOTALL):
    print("valid")
else:
    print("Invalid")