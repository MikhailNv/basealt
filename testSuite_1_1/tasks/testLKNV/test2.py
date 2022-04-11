import pexpect

class CheckingACL:

    def add_ivk2(self):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
        child.sendline("useradd ivk2")
        child.expect_exact("#")
        child.sendline("passwd ivk2")
        child.expect_exact("password")
        child.sendline("qwerty")
        child.expect_exact("password")
        child.sendline("qwerty")
        child.expect_exact("#")
        child.sendline("su - ivk2")
        child.expect_exact("$")
        child.sendline("whoami")
        child.expect_exact("$")
        print(child.before.decode().split('\r\n'))
        return True

    def add_rights(self, command):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
        child.sendline(f'setfacl {command} /home/ivk1/tfile')
        child.expect_exact("#")
        child.sendline('getfacl /home/ivk1/tfile')
        child.expect_exact("~ #")
        if command == '-m user:ivk2:rw':
            if 'user:ivk2:rw' not in child.before.decode().split('\r\n')[6]:
                return child.before.decode().split('\r\n')
            else:
                return True
        else:
            if 'user:ivk2:rw' in child.before.decode().split('\r\n')[6]:
                return child.before.decode().split('\r\n')
            else:
                return True

    def check_rights_ivk2(self, flag):
        child = pexpect.spawn("su - ivk2")
        i = child.expect_exact(["$", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
        child.sendline('echo 456 >> /home/ivk1/tfile')
        child.expect_exact("$")
        if flag == 'after':
            if 'Permission denied' not in child.before.decode().split('\r\n')[1]:
                return child.before.decode().split('\r\n')
            else:
                return True
        else:
            child.sendline('cat /home/ivk1/tfile')
            child.expect_exact("$")
            if '456' not in child.before.decode().split('\r\n'):
                return child.before.decode().split('\r\n')
            else:
                return True


ch = CheckingACL()
#print(ch.add_ivk2())
#print(ch.add_rights('-x u:ivk2'))
print(ch.check_rights_ivk2('before'))

