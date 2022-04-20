import pexpect

class StickyBit:

    def adding_and_removing_atribut(self, command):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline(f"chmod {command} /dtest/a1")
        child.expect_exact("#")
        child.sendline("getfacl /dtest/a1")
        child.expect_exact("~ #")
        if command == '-t' and '# flags: --t' != child.before.decode('utf-8').split('\r\n')[5]:
            return True
        elif command == '1777' and '# flags: --t' == child.before.decode('utf-8').split('\r\n')[5]:
            return True
        else:
            raise Exception("Error in adding Sticky Bit")

    def ivk3_commands(self, count):
        child = pexpect.spawn("su - ivk3")
        child.expect_exact("$")
        child.sendline("touch /dtest/a1/us")
        child.expect_exact("$")
        child.sendline("ls -la /dtest/a1")
        child.expect_exact("$")
        if int(child.before.decode('utf-8').split('\r\n')[1][6:]) > 10:
            child.sendline("rm /dtest/a1/us")
            child.expect_exact("?")
            child.sendline("yes")
            child.expect_exact("$")
            child.sendline("rm /dtest/a1/fb")
            child.expect_exact("?")
            child.sendline("yes")
            child.expect_exact("$")
            if 'Operation not permitted' in child.before.decode('utf-8').split('\r\n')[1] and count == 1:
                return True
            elif 'Operation not permitted' not in child.before.decode('utf-8').split('\r\n')[1] and count == 2:
                return True
            else:
                raise Exception("Permission error. Fb file was deleted.")
        else:
            raise Exception("View error")