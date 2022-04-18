import pexpect

class ClassGID:

    def __init__(self):
        self.child = pexpect.spawn("su -")
        self.child.expect_exact("#")

    def first_rights_change(self):
        self.child.sendline("chmod u-rw /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("chmod o-rw /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("chmod g-rw /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("setfacl -m g::0 /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("setfacl -m g:ivk3:rw /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("getfacl /dev/sdb1")
        self.child.expect_exact("~ #")
        if 'ivk3:rw-' in self.child.before.decode('utf-8').split('\r\n')[7]:
            return True
        else:
            raise Exception("Rights change error")

    def check_rights(self, user):
        self.child.sendline(f"su - {user}")
        self.child.expect_exact("$")
        self.child.sendline('echo "456" > /dev/sdb1')
        self.child.expect_exact("$")
        if user == 'ivk2':
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

    def second_rights_change(self):
        self.child.sendline(f"exit")
        self.child.expect_exact("#")
        self.child.sendline("setfacl -x g:ivk3 /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("setfacl -m o::rw /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("setfacl -m g::0 /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("getfacl /dev/sdb1")
        self.child.expect_exact("~ #")
        if 'other::rw-' == self.child.before.decode('utf-8').split('\r\n')[8] and 'group:ivk3:rw-' not in self.child.before.decode('utf-8').split('\r\n'):
            return True
        else:
            raise Exception("Rights change error")
