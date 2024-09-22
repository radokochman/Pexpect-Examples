import pexpect
import time

user_exec_prompt = "Router>"
privileged_exec_prompt = "Router#"

def reboot_with_sleep():
    start_time = time.time()
    child = pexpect.spawn(f"virsh console vm1")
    child.sendline("\r")
    
    index = child.expect([user_exec_prompt, privileged_exec_prompt])
    if index == 0:
        child.sendline("en")
        child.expect(privileged_exec_prompt)
    
    child.sendline("reload")
    child.expect("Proceed with reload\? \[confirm\]")
    child.sendline("\r")
    
    time.sleep(200)

    child.sendline("\r")
    child.expect(user_exec_prompt)
    print("--- Execution time: {} seconds ---".format(time.time() - start_time))


def reboot_with_expect():
    start_time = time.time()
    child = pexpect.spawn(f"virsh console vm1")
    child.sendline("\r")
    
    index = child.expect([user_exec_prompt, privileged_exec_prompt])
    if index == 0:
        child.sendline("en")
        child.expect(privileged_exec_prompt)
    
    child.sendline("reload")
    child.expect("Proceed with reload\? \[confirm\]")
    child.sendline("\r")
    
    child.expect("Press RETURN to get started\!", timeout=300)

    child.sendline("\r")
    child.expect(user_exec_prompt)
    print("--- Execution time: {} seconds ---".format(time.time() - start_time))


reboot_with_sleep()
reboot_with_expect()
