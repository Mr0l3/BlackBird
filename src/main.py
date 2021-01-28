from Console import Console
from sys import exit

import Modules


if __name__ == '__main__':
    try:
        c = Console()
        module = 'console'

        while True:
            # if not in console, print module name
            if module != 'console':
                c.start(module)
            else:
                c.start()   
            c.set_user_option()

            option = c.get_user_option()
            if option == 0:
                raise KeyboardInterrupt
            
            # Initialize a module if in console
            if module == 'console':
                if option == 1:
                    module = 'scanning'
                    scan_module = Modules.Scanning()
                elif option == 2:
                    module = 'osint'
                    osint_module = Modules.Osint()
            
            # If not in "module" console executes the option of the chosen module
            # Scanning Module
            elif module == 'scanning':
                # TCP Conn Scan
                if option == 1:
                    print('Starting TCP Scan...')
            
            # OSINT module
            elif module == 'osint':
                # CEP info tool
                if option == 1:
                    while True:
                        cep = str(input('CEP (only numbers): ')).strip()

                        if cep.isdigit():
                            break
                        else:
                            print("\033[31m[ERROR]\033[0m Invalid CEP")
                            continue

                    if osint_module.get_cep_info(cep) == False:
                        print("\033[31m[ERROR]\033[0m CEP not found")
                    input('Press ENTER to continue')
                # CNPJ info tool
                elif option == 2:
                    while True:
                        cnpj = str(input('CNPJ (only numbers): ')).strip()

                        if cnpj.isdigit():
                            break
                        else:
                            print("\033[31m[ERROR]\033[0m Invalid CNPJ")
                            continue
                    
                    code = osint_module.get_cnpj_info(cnpj)

                    # Error messages
                    if code == -2:
                        print("\033[31m[ERROR]\033[0m An error occured while retrieving info")
                    elif code == -1:
                        print("\033[31m[ERROR]\033[0m CNPJ rejected by Receita Federal")
                    elif code == 0:
                        print("\033[31m[ERROR]\033[0m Invalid CNPJ")
                        
                    input('Press ENTER to continue')
    
    except KeyboardInterrupt:
        print('\033[31mGood Bye!\033[0m')
        exit(0)
        
