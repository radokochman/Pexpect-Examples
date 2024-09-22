import pexpect

username = "admin"
password = "admin"
ip = "10.0.1.2"
prompt = "Router#"

child = pexpect.spawn(f"ssh {username}@{ip}")
child.expect("Password:")
child.sendline(password)
child.expect(prompt)
child.sendline("show version")

index = 99
pages_counter = 1
command_output = ""
while index != 0:
    index = child.expect([prompt, '--More--'])
    if index == 0:
        command_output += child.before.decode()
    elif index == 1:
        command_output += child.before.decode()
        child.send(' ')
    
    pages_counter += 1

print(command_output)
print(f"Number of pages - {pages_counter}")
