import pexpect

class Immutable:

    def adding_atribut(self, key, file):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline(f'ls /dtest/a1 | grep {file}')
        child.expect_exact("#")
        if 'a' in child.before.decode('utf-8').split()[5:]:
            child.sendline(f'rm /dtest/a1/{file}')
            child.expect_exact("?")
            child.sendline('yes')
            child.expect_exact("#")
        child.sendline(f'touch /dtest/a1/{file}')
        child.expect_exact("#")
        child.sendline(f'chmod 777 /dtest/a1/{file}')
        child.expect_exact("#")
        child.sendline(f'ls -l /dtest/a1/{file}')
        child.expect_exact("#")
        if '-rwxrwxrwx' == child.before.decode('utf-8').split()[3]:
            child.sendline(f'chattr +{key} /dtest/a1/{file}')
            child.expect_exact("#")
            child.sendline(f'ls -l /dtest/a1/{file}')
            child.expect_exact("#")
            child.sendline(f'lsattr /dtest/a1/{file}')
            child.expect_exact("#")
            if '----i---------e-------' == child.before.decode('utf-8').split()[2] or \
                    '-----a--------e-------' == child.before.decode('utf-8').split()[2]:
                return True
            else:
                raise Exception("Chattr command error")
        else:
            raise Exception("Chmod command error")

    def ivk1_commands(self, count, file):
        child = pexpect.spawn("su - ivk1")
        child.expect_exact("$")
        child.sendline(f"echo '123' >> /dtest/a1/{file}")
        child.expect_exact("$")
        if count == 1:
            if ('Operation not permitted' not in child.before.decode('utf-8').split('\r\n')[1] and file == 'b') or \
                    ('Operation not permitted' in child.before.decode('utf-8').split('\r\n')[1] and file == 'a'):
                child.sendline(f"echo '123' > /dtest/a1/{file}")
                child.expect_exact("$")
                if 'Operation not permitted' in child.before.decode('utf-8').split('\r\n')[1]:
                    child.sendline(f"rm /dtest/a1/{file}")
                    if file == 'b':
                        child.expect_exact("?")
                        child.sendline("yes")
                    child.expect_exact("$")
                    if 'Operation not permitted' in child.before.decode('utf-8').split('\r\n')[1]:
                        child.sendline(f"cat /dtest/a1/{file}")
                        child.expect_exact("$")
                        if 'Operation not permitted' not in child.before.decode('utf-8').split('\r\n')[1]:
                            return True
                        else:
                            raise Exception("Error viewing file")
                    else:
                        raise Exception("Delete file error")
                else:
                    raise Exception("File modification error")
            else:
                raise Exception("File write error")
        elif count == 2:
            if 'Operation not permitted' not in child.before.decode('utf-8').split('\r\n')[1]:
                child.sendline(f"rm /dtest/a1/{file}")
                child.expect_exact("?")
                child.sendline("yes")
                child.expect_exact("$")
                if 'Operation not permitted' not in child.before.decode('utf-8').split('\r\n')[1]:
                    return True
                else:
                    raise Exception("Delete file error")
            else:
                raise Exception("File write error")

    def removing_atribut(self, key, file):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline(f'chattr -{key} /dtest/a1/{file}')
        child.expect_exact("#")
        child.sendline(f'ls -l /dtest/a1/{file}')
        child.expect_exact("#")
        child.sendline(f'lsattr /dtest/a1/{file}')
        child.expect_exact("#")
        if '--------------e-------' == child.before.decode('utf-8').split()[2]:
            return True
        else:
            raise Exception("Chattr command error")