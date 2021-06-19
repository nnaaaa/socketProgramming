import validation
import authentication

user = {}
while True:
    chose = input()
    if not chose:
        continue
    if chose == "quit":
        break
    if chose.split(" ")[0] == "login":
        chose = chose.split(" ")
        if len(chose) == 2:
            user["account"] = chose[1]
            if validation.validate(user):
                authentication.auth(user)
        else:
            validation.validate("")