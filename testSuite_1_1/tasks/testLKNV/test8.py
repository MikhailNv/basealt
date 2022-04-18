import pexpect

class ClassACL:

    def __init__(self):
        self.child = pexpect.spawn("su -")
        self.child.expect_exact("#")

    def getfacl(self):
        self.child.sendline("getfacl /dev/sdb1")
        self.child.expect_exact("~ #")
        if "Removing leading '/' from absolute path names" in self.child.before.decode('utf-8').split('\r\n')[1]:
            return True
        else:
            raise Exception('Getfacl error')

    def check_rights(self):
        self.child.sendline("su - ivk3")
        self.child.expect_exact("$")
        self.child.sendline("cat > /dev/sdb1")
        self.child.expect_exact("$")
        if 'Permission denied' in self.child.before.decode('utf-8').split('\r\n')[1] or \
                'Отказано в доступе' in self.child.before.decode('utf-8').split('\r\n')[1]:
            self.child.sendline("cat /dev/sdb1")
            self.child.expect_exact("$")
            return True
        else:
            raise Exception('Permission error')

    def add_rights(self):
        self.child.sendline("exit")
        self.child.expect_exact("#")
        self.child.sendline("setfacl -m u:ivk3:r /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("getfacl /dev/sdb1")
        self.child.expect_exact("~ #")
        if 'ivk3:r--' in self.child.before.decode('utf-8').split('\r\n')[6]:
            return True
        else:
            raise Exception("Add rights error")