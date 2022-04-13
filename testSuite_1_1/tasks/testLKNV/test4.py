import pexpect

class CheckingSecondGID:

    def add_ivk3(self):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
        child.sendline("useradd ivk3")
        child.expect_exact("#")
        child.sendline("passwd ivk3")
        child.expect_exact("password")
        child.sendline("qwerty")
        child.expect_exact("password")
        child.sendline("qwerty")
        child.expect_exact("#")
        return True

    def viewing_rights(self, command):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
            child.expect_exact('#')
        child.sendline("ls -l /dtest/file1")
        child.expect_exact("#")
        child.sendline(f"setfacl -m g:ivk3:{command} /dtest/file1")
        child.expect_exact("#")
        child.sendline("ls -l /dtest/file1")
        child.expect_exact("#")
        child.sendline("getfacl /dtest/file1")
        child.expect_exact("~ #")
        if 'ivk3:rwx' not in child.before.decode().split('\r\n')[7] and 'ivk3:r-x' not in child.before.decode().split('\r\n')[7]:
            return child.before.decode().split('\r\n')[1:8]
        else:
            return True

    def check_rights(self, user):
        child = pexpect.spawn(f"su - {user}")
        i = child.expect_exact(["$", "Password:"])
        if i == 1:
            child.sendline('qwerty')
            child.expect_exact('$')
        child.sendline('cat /dtest/file1')
        if child.expect_exact(['$', pexpect.EOF]) == 0:
            child.sendline('echo 123 > /dtest/file1')
            if child.expect_exact(['$', 'Permission denied']) == 0:
                child.sendline('/dtest/file1')
                if child.expect_exact(['$', pexpect.EOF]) == 0:
                    return child.before.decode().split('\r\n')[1]
                else:
                    return pexpect.EOF
            else:
                return child.before.decode().split('\r\n')[1]
        else:
            return pexpect.EOF

