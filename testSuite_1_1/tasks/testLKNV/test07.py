import pexpect

class ClassUID:

    def __init__(self):
        self.child = pexpect.spawn("su -")
        self.child.expect_exact("#")
        self.child.sendline('setenforce 0')
        self.child.expect_exact("#")

    def change_rights(self):
        self.child.sendline('ls /dev | grep sdb1')
        self.child.expect_exact("#")
        if 'sdb1' in self.child.before.decode('utf-8').split():
            self.child.sendline('rm /dev/sdb1')
            self.child.expect_exact("?")
            self.child.sendline('yes')
            self.child.expect_exact("#")
        self.child.sendline('touch /dev/sdb1')
        self.child.expect_exact("#")
        self.child.sendline('ls -l /dev/sdb1')
        self.child.expect_exact("#")
        self.child.sendline('chown ivk1:ivk2 /dev/sdb1')
        self.child.expect_exact("#")
        self.child.sendline('chmod u-w /dev/sdb1')
        self.child.expect_exact("#")
        self.child.sendline('ls -l /dev/sdb1')
        self.child.expect_exact("#")
        print(self.child.before.decode('utf-8').split())
        if '-r--r--r--' in self.child.before.decode('utf-8').split() and \
                'ivk1' == self.child.before.decode('utf-8').split()[5] and \
                'ivk2' == self.child.before.decode('utf-8').split()[6]:
            return True
        else:
            raise Exception('Changing access rights error')

    def check_rights(self):
        self.child.sendline('su - ivk1')
        self.child.expect_exact("$")
        self.child.sendline('cat test > /dev/sdb1')
        self.child.expect_exact("$")
        list_of_rights = []
        if 'Permission denied' in self.child.before.decode('utf-8').split('\r\n')[1]:
            list_of_rights.append(False)
        else:
            list_of_rights.append(True)
        self.child.sendline('cat /dev/sdb1')
        self.child.expect_exact("$")
        if 'Permission denied' in self.child.before.decode('utf-8').split('\r\n')[1]:
            list_of_rights.append(False)
        else:
            list_of_rights.append(True)
        return list_of_rights

    def add_the_right_to_write(self):
        self.child.sendline('su - ivk1')
        self.child.expect_exact("$")
        self.child.sendline('chmod u+w /dev/sdb1')
        self.child.expect_exact("$")
        self.child.sendline('ls -l /dev/sdb1')
        self.child.expect_exact("$")
        if '-rw-r--r--' == self.child.before.decode('utf-8').split()[3]:
            return True
        else:
            raise Exception('Changing access rights error')