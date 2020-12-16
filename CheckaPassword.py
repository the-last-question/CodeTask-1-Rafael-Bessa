import re
def checkpasswort(password):
    if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$",password):
        return True
    else:
        return False




def __main__():
    passw = input("informe a senha\n")

    if checkpasswort(passw):
        print("senha valida")

    else:
        print("senha invalida")
__main__()




