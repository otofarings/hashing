import hashlib as hs

# ---------------------------------------------------------------------------------------------------------------------
"""
Импорт данных из кофигурационного файла
"""
try:
    from config import PATH
    from config import LIMITS
except ImportError:
    raise Exception('Файл или модули не найдены')


# ---------------------------------------------------------------------------------------------------------------------
"""
Импорт функций из вспомогательного файла
"""
try:
    from functions import *
except ImportError:
    raise Exception('Файл не найден')


class Hash:
    def __init__(self):
        self.bases = {}

    @print_logs
    def import_bases(self):
        """
        Импорт баз
        """
        print_mes('Импорт баз')
        self.bases = get_all_in_folder(
            self.bases, PATH['hash_path']
        )

    @print_logs
    def hash_bases(self):
        """
        Хэширование баз
        """
        print_mes('Хэширование msisdn')
        for base in self.bases:
            self.bases[base]['df']['numbers'] = self.bases[base]['df']['numbers'].apply(
                lambda _: _.strip()
            )
            self.bases[base]['df']['phone'] = self.bases[base]['df']['numbers'].apply(
                lambda _: hs.md5(bytes(_, encoding='utf-8')).hexdigest()
            )
            print_mes(f'{self.bases[base]["name"]} готов')

    @print_logs
    def save_for_yandex(self):
        """
        Яндекс – hash - .CSV + название столбца "phone"
        """
        print_mes('Создание файлов для Яндекса')
        folder = comp_path(PATH['results_hash_path'], 'ya')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'])
            self.bases[base]['df']['phone'].to_csv(
                path_with_name, index=False
            )
            check_limit(path_with_name, LIMITS['yandex'])
            print_mes(f'{self.bases[base]["name"]} готов')

    @print_logs
    def save_for_facebook(self):
        """
        Фейсбук/IG – msisdn - .TXT
        """
        print_mes('Создание файлов для Фейсбука')
        folder = comp_path(PATH['results_hash_path'], 'fb')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'].replace('csv', 'txt'))
            self.bases[base]['df']['numbers'].to_csv(
                path_with_name, header=None, index=None, sep=' ', mode='a'
            )
            print_mes(f'{self.bases[base]["name"]} готов')

    @print_logs
    def save_for_vkontakte(self):
        """
        ВК – hash - .TXT
        """
        print_mes('Создание файлов для Вконтакте')
        folder = comp_path(PATH['results_hash_path'], 'vk')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'].replace('csv', 'txt'))
            self.bases[base]['df']['phone'].to_csv(
                path_with_name, header=None, index=None, sep=' ', mode='a'
            )
            check_limit(path_with_name, LIMITS['vkontakte'])
            print_mes(f'{self.bases[base]["name"]} готов')

    @print_logs
    def save_for_mytarget(self):
        """
        МТ – hash - .TXT
        """
        print_mes('Создание файлов для Майтаргета')
        folder = comp_path(PATH['results_hash_path'], 'mt')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'].replace('csv', 'txt'))
            self.bases[base]['df']['phone'].to_csv(
                path_with_name, header=None, index=None, sep=' ', mode='a'
            )
            check_limit(path_with_name, LIMITS['mytarget'])
            print_mes(f'{self.bases[base]["name"]} готов')

    @print_logs
    def save_for_youtube(self):
        """
        DV360/youtube - MSI - .CSV + название столбца "Phone"
        """
        print_mes('Создание файлов для Ютуба')
        folder = comp_path(PATH['results_hash_path'], 'dv')
        create_dir(folder)
        for base in self.bases:
            self.bases[base]['df'].rename(
                columns={self.bases[base]['df'].columns[0]: 'Phone'},
                inplace=True
            )
            path_with_name = comp_path(folder, self.bases[base]['name'])
            self.bases[base]['df']['Phone'].to_csv(
                path_with_name, index=None
            )
            print_mes(f'{self.bases[base]["name"]} готов')


if __name__ == '__main__':
    pass
