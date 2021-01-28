import requests
import json

class Osint:
    def __init__(self) -> None:
        pass
    
    def get_cep_info(self, cep: str) -> bool:
        r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if r.status_code == 200:
            cep_info = r.json()
            
            print('')
            for key, value in cep_info.items():
                if value.strip():
                    print(f'\033[31m{key.capitalize()}:\033[0m {value}')
        else:
            return False

    def get_cnpj_info(self, cnpj: str) -> int:

        # Recursive algorithm to print json data
        def get_values(data):
            if type(data) is dict:
                for key, value in data.items():
                    if key == 'text':
                        key = 'Nome'
                    elif key == 'qsa':
                        key = 'Quadro de sócios e administradores'
                    elif key == 'qual':
                        key = 'cargo'
                    
                    key = key.replace('_', ' ')

                    if type(value) is dict or type(value) is list:
                        if len(value) > 0 and key != 'billing':
                            print(f'\n\033[31m{key.capitalize()}:\033[0m')
                            get_values(value)
                    elif type(value) is str:
                            if key != 'status':
                                if key == 'situacao':
                                    print('')
                                
                                if value.strip():
                                    print(f'\033[31m{key.capitalize()}:\033[0m {value}')
            elif type(data) is list:
                for value in data:
                    if type(value) is dict or type(value) is list:
                        get_values(value)

        r = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')

        if r.status_code == 200:
            cnpj_info = r.json()

            status = cnpj_info['status']

            if status == 'OK':
                print('')
                get_values(cnpj_info)
                #print(cnpj_info)
                    
            else:
                message = cnpj_info['message']

                if message == 'CNPJ rejeitado pela Receita Federal':
                    return -1
                elif message == 'CNPJ inválido':
                    return 0 
        else:
            return -2