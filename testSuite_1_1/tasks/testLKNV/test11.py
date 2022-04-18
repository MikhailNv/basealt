import pexpect

class RootRestriction:

    def __init__(self):
        self.child = pexpect.spawn("su -")
        self.child.expect_exact("#")

    def start_settings(self):
        self.child.sendline("setfacl -m o::0 /dtest/a1")
        self.child.expect_exact("#")
        self.child.sendline("chown ivk1:ivk2 /dtest/a1/fb")
        self.child.expect_exact("#")
        self.child.sendline("chmod o-rwx /dtest/a1/fb")
        self.child.expect_exact("#")
        self.child.sendline("chmod u-rwx /dtest/a1/fb")
        self.child.expect_exact("#")
        self.child.sendline("chmod g-rwx /dtest/a1/fb")
        self.child.expect_exact("#")
        self.child.sendline("chmod o-rwx /dev/sdb1")
        self.child.expect_exact("#")
        self.child.sendline("getfacl /dev/sdb1")
        self.child.expect_exact("~ #")
        if 'other::---' == self.child.before.decode('utf-8').split('\r\n')[8]:
            self.child.sendline("getfacl /dtest/a1/fb")
            self.child.expect_exact("~ #")
            if 'other::---' == self.child.before.decode('utf-8').split('\r\n')[7] and \
                'group::---' == self.child.before.decode('utf-8').split('\r\n')[6] and \
                'user::---' == self.child.before.decode('utf-8').split('\r\n')[5]:
                self.child.sendline("getfacl /dtest/a1")
                self.child.expect_exact("~ #")
                if 'other::---' == self.child.before.decode('utf-8').split('\r\n')[8]:
                    self.child.sendline("setfacl -m o::0 /dev/sdb1")
                    self.child.expect_exact("#")
                    self.child.sendline("setfacl -m g::0 /dev/sdb1")
                    self.child.expect_exact("#")
                    return True
                else:
                    raise Exception("Rights /dtest/a1 error")
            else:
                raise Exception("Rights /dtest/a1/fb error")
        else:
            raise Exception("Rights /dev/sdb1 error")

    def view_root_permissions(self):
        self.child.sendline("getfacl /dev/sdb1")
        self.child.expect_exact("~ #")
        if len(self.child.before.decode('utf-8').split('\r\n')) > 6:
            self.child.sendline("getfacl /dtest/a1/fb")
            self.child.expect_exact("~ #")
            if len(self.child.before.decode('utf-8').split('\r\n')) > 6:
                self.child.sendline("getfacl /dtest/a1")
                self.child.expect_exact("~ #")
                if len(self.child.before.decode('utf-8').split('\r\n')) > 6:
                    return True

    def restriction_of_root_rights(self):
        self.child.sendline('echo "3456" > /dtest/a1/fb')
        self.child.expect_exact("#")
        self.child.sendline('cat /dtest/a1/fb')
        self.child.expect_exact("#")
        if '3456' in self.child.before.decode('utf-8').split('\r\n'):
            self.child.sendline('/dtest/a1/fb')
            self.child.expect_exact("#")
            if 'Permission denied' in self.child.before.decode('utf-8').split('\r\n')[1]:
                self.child.sendline('touch /dtest/a1/b2')
                self.child.expect_exact("#")
                self.child.sendline('ls /dtest/a1')
                self.child.expect_exact("#")
                if 'b2' in self.child.before.decode('utf-8').split():
                    self.child.sendline('cd /dtest/a1')
                    self.child.expect_exact("#")
                    self.child.sendline('echo "777" > /dev/sdb1')
                    self.child.expect_exact("#")
                    self.child.sendline('cat /dev/sdb1')
                    self.child.expect_exact("#")
                    if '777' in self.child.before.decode('utf-8').split('\r\n'):
                        return True
                    else:
                        raise Exception("File recording error")
                else:
                    raise Exception("Touch directory error")
            else:
                raise Exception("Rights error")
        else:
            raise Exception("File recording error")

    def restoration_of_rights(self):
        self.child.sendline("su -")
        self.child.expect_exact("#")
        self.child.sendline('chmod o+x /dtest/a1/fb')
        self.child.expect_exact("#")
        self.child.sendline('getfacl /dtest/a1/fb')
        self.child.expect_exact("~ #")
        if 'other::--x' == self.child.before.decode('utf-8').split('\r\n')[7]:
            self.child.sendline('/dtest/a1/fb')
            self.child.expect_exact("#")
            if '3456: command not found' in self.child.before.decode('utf-8').split('\r\n')[1]:
                return True
            else:
                raise Exception("Permission error")
        else:
            raise Exception("Change rights other error")