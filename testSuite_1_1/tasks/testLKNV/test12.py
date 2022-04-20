import pexpect

class Suid:


    def change_password(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline("passwd ivk1")
        child.expect_exact("password:")
        child.sendline("qwerty")
        child.expect_exact("password:")
        child.sendline("qwerty")
        child.expect_exact("#")
        if 'tokens updated successfully' in child.before.decode('utf-8').split('\r\n')[3]:
            return True
        else:
            return False

    def adding_atribut(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline("chmod a-s /usr/bin/passwd")
        child.expect_exact("#")
        child.sendline("chmod u+s /usr/bin/passwd")
        child.expect_exact("#")
        child.sendline("ls -l /usr/bin/passwd")
        child.expect_exact("#")
        if '-rws--x--x' == child.before.decode('utf-8').split()[3]:
            return True
        else:
            raise Exception("Permission error")

    def change_ivk1_passwd(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline("su - ivk1")
        child.expect_exact("$")
        child.sendline("passwd ivk1")
        i = child.expect_exact(["password:", "$"])
        if i == 1:
            if 'Authentication token manipulation error' in child.before.decode('utf-8').split("\r\n")[1]:
                return True
            else:
                raise Exception("Password change error")
        else:
            child.sendline("qwerty")
            child.expect_exact("password:")
            child.sendline("Orbit9death+colt")
            child.expect_exact("password:")
            child.sendline("Orbit9death+colt")
            child.expect_exact("$")
            if 'updated successfully' in child.before.decode('utf-8').split("\r\n")[2]:
                pwd = self.change_password()
                if pwd == True:
                    return True
                else:
                    return False
            else:
                raise Exception("Password change error")

    def rule_updates(self, command):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline(f"chmod {command} /usr/bin/passwd")
        child.expect_exact("#")
        child.sendline("ls -l /usr/bin/passwd")
        child.expect_exact("#")
        if command == 'u-s':
            if '-rwx--x--x' == child.before.decode('utf-8').split()[3]:
                return True
            else:
                raise Exception("Permission error")
        elif command == 'g+s':
            if '-rwx--s--x' == child.before.decode('utf-8').split()[3]:
                return True
            else:
                raise Exception("Permission error")
        elif command == 'a-s':
            if '-rwx--x--x' == child.before.decode('utf-8').split()[3]:
                return True
            else:
                raise Exception("Permission error")