import pexpect

class Suid:

    def __init__(self):
        self.child = pexpect.spawn("su -")
        self.child.expect_exact("#")

    def adding_atribut(self):
        self.child.sendline("chmod a-s /usr/bin/passwd")
        self.child.expect_exact("#")
        self.child.sendline("chmod u+s /usr/bin/passwd")
        self.child.expect_exact("#")
        self.child.sendline("ls -l /usr/bin/passwd")
        self.child.expect_exact("#")
        if '-rws--x--x' == self.child.before.decode('utf-8').split()[3]:
            return True
        else:
            raise Exception("Permission error")

    def change_ivk1_passwd(self):
        self.child.sendline("su - ivk1")
        self.child.expect_exact("$")
        self.child.sendline("passwd")
        self.child.expect_exact("password:")
        self.child.sendline("qwerty")
        self.child.expect_exact("password:")
        self.child.sendline("qwerty1")
        self.child.expect_exact("password:")
        self.child.sendline("qwerty1")
        self.child.expect_exact("$")

cr = Suid()
#print(cr.adding_atribut())
print(cr.change_ivk1_passwd())