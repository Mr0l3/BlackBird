from .Banner import Banner
from os import system

class Console():
    def __init__(self) -> None:
        self.__user_option: int
        self.__options = {'console': ['Exit', 'Scanning', 'OSINT'],
                        'scanning': ['Exit', 'TCP Connection Scan'],
                        'osint': ['Exit', 'CEP Info', 'CNPJ Info']}
        self.banner: Banner = Banner()

    def start(self, module = 'Console') -> None:
        system('clear')
        # Print tool bannner
        print(f'\033[31m{self.banner.tool_name}\033[0m')
        print(f'\033[31m{69 * "-"}\033[0m')
        print(f'\033[31;5m{30 * " "}{self.banner.tool_author}\033[0m')
        print(f'\033[31m{69 * "-"}\033[0m')
        self.show_options(module)

    def show_options(self, module: str = 'Console') -> None:
        if  module == 'Console':
            print('')
        else:
            print(f'\n\033[37;1m{module.capitalize()} module\033[0m')
        for index, option in enumerate(self.__options[module.lower()], 0):
            print(f'\033[37;1m{index})\033[0m \033[31m{option}\033[0m')
        print('')

    def set_user_option(self) -> None:
        while True:
            try:
                opt = int(input('\033[37;4;1mBlackBird\033[0m \033[37;1m>\033[0m '))
            except ValueError:
                print("\033[31m[ERROR]\033[0m Unknown option")
                continue
            else:
                if 0 <= opt < len(self.__options):
                    self.__user_option = opt
                    break
                else:
                    print("\033[31m[ERROR]\033[0m Unknown option")
    
    def get_user_option(self) -> int:
        return self.__user_option
