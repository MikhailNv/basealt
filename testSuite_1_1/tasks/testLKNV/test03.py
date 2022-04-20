import pexpect

class CheckingFirstGID:

    def access(self):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
            child.expect_exact('#')
        child.sendline("mkdir /dtest")
        child.expect_exact("#")
        child.sendline("chmod g+rwx /dtest")
        child.expect_exact("#")
        child.sendline("chmod o+rwx /dtest")
        child.expect_exact("#")
        child.sendline("sudo -u ivk1 touch /dtest/file1")
        child.expect_exact("#")
        return True

    def create_file(self):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
            child.expect_exact('#')
        child.sendline('chmod u-rw /dtest/file1')
        child.expect_exact('#')
        child.sendline('chmod o-rw /dtest/file1')
        child.expect_exact('#')
        child.sendline('chmod g-rwx /dtest/file1')
        child.expect_exact('#')
        child.sendline('chown :ivk2 /dtest/file1')
        child.expect_exact('#')
        child.sendline('ls -l /dtest/file1')
        child.expect_exact('#')
        if 'ivk2' not in child.before.decode().split('\r\n')[1]:
            return child.before.decode().split('\r\n')[1]
        else:
            return True

    def setting_new_rights(self, command):
        child = pexpect.spawn("su -")
        i = child.expect_exact(["#", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
            child.expect_exact('#')
        child.sendline(f'setfacl -m g::{command} /dtest/file1')
        child.expect_exact('#')
        child.sendline('getfacl /dtest/file1')
        child.expect_exact('~ #')
        if command == 'rx':
            if 'r-x' not in child.before.decode().split('\r\n')[6]:
                return child.before.decode().split('\r\n')[1:8]
            else:
                return True
        else:
            if '-w-' not in child.before.decode().split('\r\n')[6]:
                return child.before.decode().split('\r\n')[1:8]
            else:
                return True

    def operations_on_files(self):
        child = pexpect.spawn("su - ivk2")
        i = child.expect_exact(["$", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
            child.expect_exact('$')
        child.sendline('cat /dtest/file1')
        child.expect_exact('$')
        print(child.before.decode().split('\r\n'))
        child.sendline('echo 123 > /dtest/file1')
        child.expect_exact('$')
        if 'Permission denied' not in child.before.decode().split('\r\n')[1]:
            return child.before.decode().split('\r\n')
        else:
            child.sendline('/dtest/file1')
            child.expect_exact('$')
            child.sendline('whoami')
            child.expect_exact('$')
            if 'ivk2' not in child.before.decode().split('\r\n')[1]:
                return child.before.decode().split('\r\n')
            else:
                return True

    def check_rights_for_ivk2(self):
        child = pexpect.spawn("su - ivk2")
        i = child.expect_exact(["$", "Password:"])
        if i == 1:
            child.sendline('Wels082017')
            child.expect_exact('$')
        child.sendline('cat /dtest/file1')
        child.expect_exact('$')
        if 'Permission denied' not in child.before.decode().split('\r\n')[1]:
            return child.before.decode().split('\r\n')
        else:
            child.sendline('echo 123 > /dtest/file1')
            child.expect_exact('$')
            return True