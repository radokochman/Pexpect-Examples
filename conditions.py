import pexpect

username = "admin"
password = "admin"
prompt = "Router#"

child = pexpect.spawn("telnet 10.0.1.3 2233")
child.sendline("\r")

index = 99
while index != 0:
    index = child.expect([prompt, "Username:", "Password:"])
    if index == 0:
        print("Found prompt!")
    elif index == 1:
        print(f"Found Username in the console, sending {username}")
        child.sendline(username)
    elif index == 2:
        print(f"Found Password in the console, sending {password}")
        child.sendline(password)
