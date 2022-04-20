import pexpect

class Sgid:

    def __init__(self):
        child = pexpect.spawn("su - ivk1")
        child.expect_exact("$")
        child.sendline("touch /dtest/test1")
        child.expect_exact("$")

    def adding_atribut(self, command):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline(f"setfacl -m {command} /dtest/test1")
        child.expect_exact("#")
        child.sendline("getfacl /dtest/test1")
        child.expect_exact("~ #")
        if command == 'u:ivk3:rwx':
            if 'user:ivk3:rwx' == child.before.decode('utf-8').split('\r\n')[6]:
                return True
            else:
                raise Exception("Change rights error")
        elif command == 'm::r':
            if 'mask::r--' == child.before.decode('utf-8').split('\r\n')[8]:
                return True
            else:
                raise Exception("Change rights error")

    def ivk3_commands(self):
        check_list = []
        child = pexpect.spawn("su - ivk3")
        child.expect_exact("$")
        child.sendline('echo "aaa" > /dtest/test1')
        child.expect_exact("$")
        if 'Permission denied' in child.before.decode('utf-8').split('\r\n')[1]:
            check_list.append(False)
        else:
            check_list.append(True)
        child.sendline("cat /dtest/test1")
        child.expect_exact("$")
        if 'aaa' == child.before.decode('utf-8').split('\r\n')[1]:
            check_list.append(True)
        else:
            check_list.append(False)
        child.sendline("/dtest/test1")
        child.expect_exact("$")
        if 'aaa: command not found' in child.before.decode('utf-8').split('\r\n')[1]:
            check_list.append(True)
        else:
            check_list.append(False)
        return check_list