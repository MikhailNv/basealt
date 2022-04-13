import pexpect

class CatalogGID:

    def create_file_and_dir(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('mkdir /dtest/dir1')
        child.expect_exact("#")
        child.sendline('ls /dtest')
        child.expect_exact("#")
        if 'dir1' in child.before.decode('utf-8').split()[2]:
            child.sendline('touch /dtest/dir1/file')
            child.expect_exact("#")
            child.sendline('ls /dtest/dir1')
            child.expect_exact("#")
            if 'file' in child.before.decode('utf-8').split():
                child.close()
                return True
            else:
                child.close()
                raise Exception('Touch file error')
        else:
            child.close()
            raise Exception('Touch dir error')

    def change_rights(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('chown ivk1:ivk2 /dtest/dir1')
        child.expect_exact("#")
        child.sendline('ls -l /dtest')
        child.expect_exact("#")
        if 'ivk1' in child.before.decode('utf-8').split()[5:14] and 'ivk2' in child.before.decode('utf-8').split()[5:14]:
            child.sendline('chmod u+rwx /dtest/dir1')
            child.expect_exact("#")
            child.sendline('chmod g-w /dtest/dir1')
            child.expect_exact("#")
            child.sendline('chmod o-w /dtest/dir1')
            child.expect_exact("#")
            child.sendline('ls -l /dtest')
            child.expect_exact("#")
            if 'drwxr-xr-x' == child.before.decode('utf-8').split()[5:14][0]:
                return True
            else:
                raise Exception('Change rights error')
        else:
            raise Exception('Change rights error')

    def check_users_rights(self, user, file):
        child = pexpect.spawn(f"su - {user}")
        child.expect_exact("$")
        child.sendline('ls /dtest/dir1')
        child.expect_exact("$")
        if 'Permission denied' not in child.before.decode('utf-8').split():
            child.sendline(f'touch /dtest/dir1/{file}')
            child.expect_exact("$")
            child.sendline('ls -l /dtest/dir1')
            child.expect_exact("$")
            if file in child.before.decode('utf-8').split()[14:23]:
                return True
            else:
                raise Exception(f'Touch file error ({user})')
        else:
            raise Exception('Permission error')

    def new_owner_rights(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('chmod u-w /dtest/dir1')
        child.expect_exact("#")
        child.sendline('ls -l /dtest/')
        child.expect_exact("#")
        if 'dr-xr-xr-x' == child.before.decode('utf-8').split()[5:14][0]:
            return True
        else:
            raise Exception('Change rights error')

