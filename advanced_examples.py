import pexpect
import time

username = "admin"
password = "admin"
ip = "10.0.0.2"
prompt = "Router#"
clear_buffer = ".+"

child = pexpect.spawn(f"ssh {username}@{ip}")
child.expect("Password:")
child.sendline(password)
child.expect(prompt)
child.sendline("show clock")
child.expect(prompt)
print(f"Printing output for the first time:\n{child.before.decode()}")

child.sendline("\r")
child.sendline("\r")
child.sendline("\r")
child.sendline("show clock")
time.sleep(2)
child.expect(prompt)
print(f"Printing output for the second time:\n{child.before.decode()}")
print(f"Reamining content of the buffer:\n{child.buffer.decode()}")

child.expect(clear_buffer)
print(f"Buffer content after cleaning:\n{child.buffer.decode()}")
child.sendline("show clock")
child.expect(prompt)
print(f"Printing output after clearing the buffer:\n{child.before.decode()}")
child.close()

child = pexpect.spawn(f"ssh {username}@{ip}")
child.expect("Password:")
child.sendline(password)
child.expect(prompt)
child.sendline("\r")
child.sendline("\r")
child.sendline("\r")
child.sendline("show clock")
time.sleep(2)
child.expect(pexpect.TIMEOUT, timeout=0)
print(f"Buffer content after refresh:\n{child.buffer.decode()}")
