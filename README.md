<h1 align="center">Инструкция по запуску тестов</h1>

* Перед дальнейшими действиями проверьте, установлены ли gimp, vlc, vim в системе. Если нет, то их необходимо заинсталлировать.
* Шаг 1
    ```bash
    # Установка дополнительного пакета
    su - 
    echo "rpm [p8] http://ftp.altlinux.org/pub/distributions/ALTLinux/ p8/branch/x86_64 classic" >> /etc/apt/sources.list.d/altsp.list
    apt-get update
    apt-get install xorg-xvfb
    exit (or) su - officer
    ```
* Шаг 2
    * Переходим по [ссылке]:https://bootstrap.pypa.io/get-pip.py и сохраняем файл.
    * Открываем терминал и переходим при помощи команды cd в раздел с сохраненным файлом get-pip.py
    ```bash
    python3 get-pip.py
    # После успешной установки удаляем файл
    sudo rm get-pip.py
    ```
