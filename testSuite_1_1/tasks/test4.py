import subprocess
import sys
from passlib.hash import sha512_crypt
import pexpect

class CheckingRules1419:

    # Конструктор класса, создающий при запуске вспомогательный файл.
    def __init__(self, passwd):
        with open('cat.txt', 'w') as f:
            f.write(passwd)
            f.close()

    # Вспомогательный метод
    def call_new_window(self, command):
        input = open('cat.txt')
        f = subprocess.run(command, stdin=input, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, encoding='utf-8')
        input.close()
        return f

    # Проверка прав
    def check_rights(self, user, passwd):
        child = pexpect.spawn(f"su - {user}")
        i = child.expect_exact(["$", "Password:"])
        if i == 1:
            child.sendline(passwd)
            child.expect_exact("$")
        child.sendline('echo "456" >> /tmp/share')
        child.expect_exact("$")
        if '~' in child.before.decode().split('\r\n')[1]:
            child.sendline('cat /tmp/share')
            child.expect_exact("$")
            if child.before.decode().split('\r\n')[1].isdigit() == True:
                return True
            else:
                return False
        else:
            return False

    # Проверка добавления пользователей и группы.
    def check_add_users_and_groups(self):
        print(sys.path)
        passwd_test1 = sha512_crypt.hash('q1w2e3r4')
        passwd_test2 = sha512_crypt.hash('1q2w3e4r')
        afu = self.call_new_window(f'sudo -S -u root useradd test1 -p {passwd_test1}'.split())
        asu = self.call_new_window(f'sudo -S -u root useradd test2 -p {passwd_test2}'.split())
        ag = self.call_new_window('sudo -S -u root groupadd testgroup'.split())
        user_list = [afu, asu]
        for i in user_list:
            if i.returncode != 0:
                return i.stderr
        if ag.returncode != 0:
            return ag.stderr
        gpasswd = self.call_new_window(f'sudo -S -u root gpasswd -M test1 testgroup'.split())
        if gpasswd.returncode != 0:
            return gpasswd.stderr
        touch_file = self.call_new_window('sudo -S -u root touch /tmp/share'.split())
        if touch_file.returncode != 0:
            return touch_file.stderr
        chgrp = self.call_new_window('sudo -S -u root chgrp testgroup /tmp/share'.split())
        if chgrp.returncode != 0:
            return chgrp.stderr
        chmod = self.call_new_window('sudo -S -u root chmod g+w /tmp/share'.split())
        if chmod.returncode != 0:
            return chmod.stderr
        if self.check_rights('test1', 'q1w2e3r4') == True and self.check_rights('test2', '1q2w3e4r') == False:
            return True

    # Проверка смены пароля у тестового пользователя.
    def check_change_password_testuser(self, password):
        child = pexpect.spawn("su - test1")
        i = child.expect_exact(["$", "Password:"])
        if i == 1:
            child.sendline(password)
            child.expect_exact("$")
        child.sendline("passwd test1")
        child.expect_exact("password:")
        child.sendline(password)
        i = child.expect_exact(["password:", "$"])
        if i == 1:
            error_mg = child.before.decode().split('\r\n')[2]
            if 'passwd: Authentication token manipulation error' in error_mg:
                return True
            else:
                return error_mg
        else:
            child.sendline("ivk1419!")
            child.expect_exact("password:")
            child.sendline("ivk1419!")
            child.expect_exact("$")
            if 'updated successfully' in child.before.decode().split('\r\n')[2]:
                return True
            else:
                return child.before.decode().split('\r\n')

    # Запрет измения собственного пароля у тестового пользователя.
    def prohibition_of_change(self):
        chage = self.call_new_window('sudo -S -u root chage -m 36500 test1'.split())
        if chage.returncode != 0:
            return chage.stderr
        return self.check_change_password_testuser('ivk1419!')

    # Проверка изменения пароля root-пользователем.
    def check_change_passwd_with_root(self):
        child = pexpect.spawn('sudo -i')
        i = child.expect_exact(["#", "password"])
        if i == 1:
            child.sendline('qwerty')
            child.expect_exact("#")
        child.sendline('passwd test1')
        child.expect_exact("password:")
        child.sendline('q1w2e3r4')
        child.expect_exact("password:")
        child.sendline('q1w2e3r4')
        child.expect_exact("#")
        if 'successfully' in child.before.decode().split('\r\n')[3]:
            return True
        else:
            return child.before.decode().split('\r\n')

    # Удаление созданных пользователей, файлов и группы.
    def delete_data(self):
        del_test1 = self.call_new_window('sudo -S userdel test1'.split())
        del_test2 = self.call_new_window('sudo -S userdel test2'.split())
        del_group = self.call_new_window('sudo -S groupdel testgroup'.split())
        rmdir = self.call_new_window('sudo -S rm /tmp/share'.split())
        exit_list = [del_test1, del_test2, del_group, rmdir]
        for i in exit_list:
            if i.returncode != 0:
                return i.stderr
        return True


