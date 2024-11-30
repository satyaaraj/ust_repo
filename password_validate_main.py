from password_validate_fun import password_validate
def main():
    input_passwords = "asqwr1234@1,aF145#,2w3E*,2We3345"
    ip_split = input_passwords.split(",")
    for ip in ip_split:
        print(password_validate(ip))
if __name__ == "__main__":
    main()
