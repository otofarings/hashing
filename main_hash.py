import hashlib as hs
import time

# ---------------------------------------------------------------------------------------------------------------------
"""
Импорт данных из кофигурационного файла
"""
try:
    from config import PATH
    from config import LIMITS
    from config import LOG_MES
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

    def import_bases(self):
        """
        Импорт баз
        """
        print_mes(LOG_MES['1'])
        start_time = time.time()
        self.bases = get_all_in_folder(
            self.bases, PATH['hash_path']
        )
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд')
        print_mes(f'{LOG_MES["1"]} завершено', True)

    def hash_bases(self):
        """
        Хэширование баз
        """
        print_mes(LOG_MES['2'])
        start_time = time.time()
        for base in self.bases:
            self.bases[base]['df']['numbers'] = self.bases[base]['df']['numbers'].apply(
                lambda _: _.strip()
            )
            self.bases[base]['df']['phone'] = self.bases[base]['df']['numbers'].apply(
                lambda _: hs.md5(bytes(_, encoding='utf-8')).hexdigest()
            )
            print_mes(f'{self.bases[base]["name"]} готов')
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд')
        print_mes(f'{LOG_MES["2"]} завершено', True)

    def save_for_yandex(self):
        """
        Яндекс – hash - .CSV + название столбца "phone"
        """
        print_mes(LOG_MES['3'])
        start_time = time.time()
        folder = comp_path(PATH['results_hash_path'], 'ya')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'])
            self.bases[base]['df']['phone'].to_csv(
                path_with_name, index=False
            )
            check_limit(path_with_name, LIMITS['yandex'])
            print_mes(f'{self.bases[base]["name"]} готов')
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд')
        print_mes(f'{LOG_MES["3"]} завершено', True)

    def save_for_facebook(self):
        """
        Фейсбук/IG – msisdn - .TXT
        """
        print_mes(LOG_MES['4'])
        start_time = time.time()
        folder = comp_path(PATH['results_hash_path'], 'fb')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'].replace('csv', 'txt'))
            self.bases[base]['df']['numbers'].to_csv(
                path_with_name, header=None, index=None, sep=' ', mode='a'
            )
            print_mes(f'{self.bases[base]["name"]} готов')
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд')
        print_mes(f'{LOG_MES["4"]} завершено', True)

    def save_for_vkontakte(self):
        """
        ВК – hash - .TXT
        """
        print_mes(LOG_MES['5'])
        start_time = time.time()
        folder = comp_path(PATH['results_hash_path'], 'vk')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'].replace('csv', 'txt'))
            self.bases[base]['df']['phone'].to_csv(
                path_with_name, header=None, index=None, sep=' ', mode='a'
            )
            check_limit(path_with_name, LIMITS['vkontakte'])
            print_mes(f'{self.bases[base]["name"]} готов')
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд')
        print_mes(f'{LOG_MES["5"]} завершено', True)

    def save_for_mytarget(self):
        """
        МТ – hash - .TXT
        """
        print_mes(LOG_MES['6'])
        start_time = time.time()
        folder = comp_path(PATH['results_hash_path'], 'mt')
        create_dir(folder)
        for base in self.bases:
            path_with_name = comp_path(folder, self.bases[base]['name'].replace('csv', 'txt'))
            self.bases[base]['df']['phone'].to_csv(
                path_with_name, header=None, index=None, sep=' ', mode='a'
            )
            check_limit(path_with_name, LIMITS['mytarget'])
            print_mes(f'{self.bases[base]["name"]} готов')
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд')
        print_mes(f'{LOG_MES["6"]} завершено', True)

    def save_for_youtube(self):
        """
        DV360/youtube - MSI - .CSV + название столбца "Phone"
        """
        print_mes(LOG_MES['7'])
        start_time = time.time()
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
        print_mes(f'Время выполнения: {time.time() - start_time:.4f} секунд')
        print_mes(f'{LOG_MES["7"]} завершено', True)


if __name__ == '__main__':
    pass
