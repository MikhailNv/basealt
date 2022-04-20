import pexpect

class Immutable:

    def adding_atribut(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('ls /dtest/a1 | grep a')
        child.expect_exact("#")
        if 'a' in child.before.decode('utf-8').split()[5:]:
            child.sendline('rm /dtest/a1/a')
            child.expect_exact("?")
            child.sendline('yes')
            child.expect_exact("#")
        child.sendline('touch /dtest/a1/a')
        child.expect_exact("#")
        child.sendline('chmod 777 /dtest/a1/a')
        child.expect_exact("#")
        child.sendline('ls -l /dtest/a1/a')
        child.expect_exact("#")
        if '-rwxrwxrwx' == child.before.decode('utf-8').split()[3]:
            child.sendline('chattr +i /dtest/a1/a')
            child.expect_exact("#")
            child.sendline('ls -l /dtest/a1/a')
            child.expect_exact("#")
            child.sendline('lsattr /dtest/a1/a')
            child.expect_exact("#")
            if '----i---------e-------' == child.before.decode('utf-8').split()[2]:
                return True
            else:
                raise Exception("Chattr command error")
        else:
            raise Exception("Chmod command error")

    def ivk1_commands(self, count):
        child = pexpect.spawn("su - ivk1")
        child.expect_exact("$")
        child.sendline("echo '123' > /dtest/a1/a")
        child.expect_exact("$")
        if count == 1:
            if 'Operation not permitted' in child.before.decode('utf-8').split('\r\n')[1]:
                child.sendline("rm /dtest/a1/a")
                child.expect_exact("$")
                if 'Operation not permitted' in child.before.decode('utf-8').split('\r\n')[1]:
                    return True
                else:
                    raise Exception("Delete file error")
            else:
                raise Exception("File write error")
        elif count == 2:
            if 'Operation not permitted' not in child.before.decode('utf-8').split('\r\n')[1]:
                child.sendline("rm /dtest/a1/a")
                child.expect_exact("?")
                child.sendline("yes")
                child.expect_exact("$")
                if 'Operation not permitted' not in child.before.decode('utf-8').split('\r\n')[1]:
                    return True
                else:
                    raise Exception("Delete file error")
            else:
                raise Exception("File write error")

    def removing_atribut(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('chattr -i /dtest/a1/a')
        child.expect_exact("#")
        child.sendline('ls -l /dtest/a1/a')
        child.expect_exact("#")
        child.sendline('lsattr /dtest/a1/a')
        child.expect_exact("#")
        if '--------------e-------' == child.before.decode('utf-8').split()[2]:
            return True
        else:
            raise Exception("Chattr command error")


cr = Immutable()
#print(cr.adding_atribut())
#print(cr.delete_atribut())
print(cr.ivk1_commands(2))