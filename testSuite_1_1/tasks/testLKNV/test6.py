import pexpect

class CatalogACL:


    def change_dir_rights(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('mkdir /dtest/a1')
        child.expect_exact("#")
        child.sendline('ls -l /dtest/')
        child.expect_exact("#")
        if 'a1' in child.before.decode('utf-8').split()[5:14][8]:
            child.sendline('chown ivk1:ivk2 /dtest/a1')
            child.expect_exact("#")
            child.sendline('ls -l /dtest')
            child.expect_exact("#")
            if 'ivk1' in child.before.decode('utf-8').split()[5:14] and 'ivk2' in child.before.decode('utf-8').split()[
                                                                                  5:14]:
                child.sendline('chmod g-rx /dtest/a1')
                child.expect_exact("#")
                child.sendline('chmod o-rx /dtest/a1')
                child.expect_exact("#")
                child.sendline('ls -l /dtest')
                child.expect_exact("#")
                child.sendline('chmod u-rwx /dtest/a1')
                child.expect_exact("#")
                child.sendline('ls -l /dtest')
                child.expect_exact("#")
                if 'd---------' == child.before.decode('utf-8').split()[5:14][0]:
                    return True
                else:
                    raise Exception('Change rights error')
            else:
                raise Exception('Read rights error')
        else:
            raise Exception('Folder creation error')

    def additional_rule(self, command):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline(f'setfacl -m u:ivk3:{command} /dtest/a1')
        child.expect_exact("#")
        child.sendline('getfacl /dtest/a1')
        child.expect_exact("~ #")
        if command in child.before.decode('utf-8').split()[20]:
            return True
        else:
            raise Exception('Change rights error')

    def check_users_rights(self, user, file):
        child = pexpect.spawn(f"su - {user}")
        child.expect_exact("$")
        child.sendline('ls /dtest/a1')
        child.expect_exact("$")
        list_of_rights = []
        if 'Permission denied' in child.before.decode('utf-8').split('\r\n')[1] and 'fb' not in child.before.decode('utf-8').split('\r\n'):
            list_of_rights.append(False)
        else:
            list_of_rights.append(True)
        child.sendline(f'touch /dtest/a1/{file}')
        child.expect_exact("$")
        if 'Permission denied' in child.before.decode('utf-8').split('\r\n')[1]:
            list_of_rights.append(False)
        else:
            list_of_rights.append(True)
        child.sendline('cd /dtest/a1')
        child.expect_exact("$")
        if 'Permission denied' in child.before.decode('utf-8').split('\r\n')[1]:
            list_of_rights.append(False)
        else:
            list_of_rights.append(True)
        return list_of_rights

    def change_first_rights(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('chmod g+rwx /dtest/a1')
        child.expect_exact("#")
        child.sendline('setfacl -x u:ivk3 /dtest/a1')
        child.expect_exact("#")
        child.sendline('setfacl -m g::rx /dtest/a1')
        child.expect_exact("#")
        child.sendline('getfacl /dtest/a1')
        child.expect_exact("~ #")
        if 'r-x' in child.before.decode('utf-8').split('\r\n')[6]:
            return True
        else:
            raise Exception('Change rights error')

    def change_second_rights(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('setfacl -m g::0 /dtest/a1')
        child.expect_exact("#")
        child.sendline('chmod g-rwx /dtest/a1')
        child.expect_exact("#")
        child.sendline('setfacl -m g:ivk3:r /dtest/a1')
        child.expect_exact("#")
        child.sendline('getfacl /dtest/a1')
        child.expect_exact("~ #")
        if 'r--' in child.before.decode('utf-8').split('\r\n')[7]:
            return True
        else:
            raise Exception('Change rights error')

    def change_third_rights(self):
        child = pexpect.spawn("su -")
        child.expect_exact("#")
        child.sendline('chmod g-rwx /dtest/a1')
        child.expect_exact("#")
        child.sendline('setfacl -x g:ivk3 /dtest/a1')
        child.expect_exact("#")
        child.sendline('setfacl -m o::wx /dtest/a1')
        child.expect_exact("#")
        child.sendline('getfacl /dtest/a1')
        child.expect_exact("~ #")
        if '-wx' in child.before.decode('utf-8').split('\r\n')[8]:
            return True
        else:
            raise Exception('Change rights error')
