import simplecrypt

# Считываем бинарный код(зашифрованное сообщение методом simplecrypt.encrypt)
with open("encrypted.bin", "rb") as inp:
    ciphertext = inp.read()

# Считываем файл с паролями
with open("passwords.txt", "r") as passwords:
    for password in passwords:
        try:
            # Подбираем пароль для расшифровки сообщения
            plaintext = simplecrypt.decrypt(password.rstrip(), ciphertext)

        # Игнорируем ошибки при неверно подобранном пароле
        except simplecrypt.DecryptionException:
            continue

        # Пароль найден
        else:
            print(plaintext.decode('utf8'))
            break
