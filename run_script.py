import main_hash as mh


def hashing_bases():
    sample = mh.Hash()

    sample.import_bases()
    sample.hash_bases()

    """
    Создание баз для Яндекса
    Структура: hash - .CSV (+ название столбца "phone")
    Лимит площадки: 1048576000 Bytes (in binary) -> (1000 MB)
    Установленный лимит: 1027604480 Bytes (in binary) -> (980MB)
    """
    sample.save_for_yandex()

    """
    Создание баз для Фейсбука/IG
    Структура: msisdn - .TXT (без названия столбца)
    Лимит площадки: нет
    Установленный лимит: нет
    """
    sample.save_for_facebook()

    """
    Создание баз для ВК
    Структура: hash - .TXT (без названия столбца)
    Лимит площадки: 20971520 Bytes (in binary) -> (20MB)
    Установленный лимит: 19922944 Bytes (in binary) -> (19MB)
    """
    sample.save_for_vkontakte()

    """
    Создание баз для МТ
    Структура: hash - .TXT (без названия столбца)
    Лимит площадки: 134217728 Bytes (in binary) -> (128MB)
    Установленный лимит: 125829120 Bytes (in binary) -> (120MB)
    """
    sample.save_for_mytarget()

    """
    Создание баз для DV360/youtube
    Структура: MSI - .CSV (+ название столбца "Phone")
    Лимит площадки: нет
    Установленный лимит: нет
    """
    sample.save_for_youtube()


if __name__ == '__main__':
    hashing_bases()