import pexpect

class ClassGID:

    def __init__(self):
        self.child = pexpect.spawn("su -")
        self.child.expect_exact("#")

    def delete_rights(self):
        self.child.sendline("setfacl -x u:ivk3 /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("chmod u-rw /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("getfacl /dev/sdb1")
        self.child.expect_exact("~ #")
        if 'ivk3' not in self.child.before.decode('utf-8').split('\r\n')[6] and 'user::---' == self.child.before.decode('utf-8').split('\r\n')[5]:
            return True
        else:
            raise Exception("Delete rights error")

    def check_rights(self, user):
        self.child.sendline(f"su - {user}")
        self.child.expect_exact("$")
        self.child.sendline("cat > /dev/sdb1")
        self.child.expect_exact("$")
        if user == 'ivk1':
            if 'Permission denied' in self.child.before.decode('utf-8').split('\r\n')[1] or \
                    'Отказано в доступе' in self.child.before.decode('utf-8').split('\r\n')[1]:
                self.child.sendline("cat /dev/sdb1")
                self.child.expect_exact("$")
                if 'Permission denied' in self.child.before.decode('utf-8').split('\r\n')[1] or \
                        'Отказано в доступе' in self.child.before.decode('utf-8').split('\r\n')[1]:
                    return True
                else:
                    raise Exception("Read error")
            else:
                raise Exception("Data recording error")
        else:
            if 'Permission denied' not in self.child.before.decode('utf-8').split('\r\n')[1] or \
                    'Отказано в доступе' not in self.child.before.decode('utf-8').split('\r\n')[1]:
                self.child.sendline("cat /dev/sdb1")
                self.child.expect_exact("$")
                if 'Permission denied' not in self.child.before.decode('utf-8').split('\r\n')[1] or \
                        'Отказано в доступе' not in self.child.before.decode('utf-8').split('\r\n')[1]:
                    return True
                else:
                    raise Exception("Read error")
            else:
                raise Exception("Data recording error")