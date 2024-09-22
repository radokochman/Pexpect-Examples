import pexpect

username = "admin"
password = "admin"
ip = "10.0.1.2"
prompt = "Router#"

child = pexpect.spawn(f"ssh {username}@{ip}")
child.expect("Password:")
child.sendline(password)
child.expect(prompt)
child.sendline("show platform")
child.expect(prompt)
output = child.before.decode()
print(output)
