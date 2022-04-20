import pexpect

class CheckingUID:

    def add_ivk1(self):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
        child.sendline("useradd ivk1")
        child.expect_exact("#")
        child.sendline("passwd ivk1")
        child.expect_exact("password")
        child.sendline("qwerty")
        child.expect_exact("password")
        child.sendline("qwerty")
        child.expect_exact("#")
        child.sendline("su - ivk1")
        child.expect_exact("$")
        child.sendline("whoami")
        child.expect_exact("$")
        print(child.before.decode().split('\r\n'))
        return True

    def check_input_for_ivk1(self):
        child = pexpect.spawn('su - ivk1')
        child.expect_exact("$")
        child.sendline("touch tfile")
        child.expect_exact("$")
        child.sendline("ls -l tfile")
        child.expect_exact("$")
        child.sendline("echo 123 > tfile")
        child.expect_exact("$")
        child.sendline("cat tfile")
        child.expect_exact("$")
        return True

    def change_chmod(self):
        try:
            child = pexpect.spawn("su -")
            i = child.expect_exact(["#", "Password:"])
            if i == 1:
                child.sendline('Wels082017')
            child.sendline("chmod u-rw /home/ivk1/tfile")
            child.expect_exact("#")
            child.sendline("ls -l /home/ivk1/tfile")
            child.expect_exact("#")
            return True
        except pexpect.EOF:
            return False

    def read_file_with_ivk1(self):
        child = pexpect.spawn("su - ivk1")
        i = child.expect_exact(["$", "Password:"])
        if i == 1:
            child.sendline('qwerty')
        child.sendline("cat tfile")
        child.expect_exact("$")
        if 'Permission denied' not in child.before.decode('utf-8').split('\r\n')[1]:
            return child.before.decode()
        child.sendline("echo 456 >> tfile")
        child.expect_exact("$")
        if 'Permission denied' not in child.before.decode('utf-8').split('\r\n')[1]:
            return child.before.decode()
        return True