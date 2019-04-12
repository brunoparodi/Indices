#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys

import urllib.request
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from datetime import datetime
import os.path

class BuscaIndices():
    def buscadados(self):
        '''
        Busca dados do site da ANBIMA.
        :return: uma lista tratada com as informações de nome, data e índice e outros.
        '''
        url = 'http://www.anbima.com.br/indicadores/indicadores.asp'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        a = soup.find_all('td')

        info = []
        for item in a[4:72]:
            # deleta as seguintes informações, para a tabela ficar reduzida
            if (item.text.strip() == '' or
                    item.text.strip() == 'Data' or
                    item.text.strip() == 'Taxa % a.a.' or
                    item.text.strip() == 'Números índices / Variações Mensais' or
                    item.text.strip() == 'R$ / US$' or
                    item.text.strip() == 'R$ / EUR$' or
                    item.text.strip() == 'Rend. Mês (%)' or
                    item.text.strip() == 'Valor da Cota R$'):
                pass
            else:
                info.append(str(item.text.strip()))
        return info

    def tabela(self):
        '''
        recebe uma lista já tratada, com os dados do site da ANBIMA
        :return uma tabela
        '''

        info = self.buscadados()
        tb = PrettyTable(['Indicador', 'Data', 'Índice'], hrules=True)
        tb.add_row([info[1], info[2], info[3]])
        tb.add_row([info[4], info[5], info[6]])
        tb.add_row([info[7], info[8], info[9]])
        tb.add_row([info[10], info[11], info[12]])
        tb.add_row(['', info[13], info[14]])
        tb.add_row([info[15], info[16], info[17]])
        tb.add_row([info[18], info[19], info[20]])
        tb.add_row(['', info[21], info[22]])
        tb.add_row([info[23], info[24], info[25]])
        tb.add_row([info[26], info[27], info[28]])
        tb.add_row([info[29], info[30], info[31]])
        tb.add_row([info[32], info[33], info[34]])
        tb.add_row([info[35], info[36], info[37]])
        tb.add_row([info[38], info[39], info[40]])
        tb.add_row([info[41], info[42], info[43]])
        tb.add_row([info[44], info[45], info[46]])
        tb.add_row([info[47], info[48], info[49]])
        return str(tb)


a = BuscaIndices()
save_path = 'R:/Indices/'
name_data = datetime.now().strftime("%d_%m_%y_%H_%M_%S")

file = open(os.path.join(save_path, name_data + '_indice.txt'), 'w')
file.write('Retirado do site http://www.anbima.com.br/indicadores/indicadores.asp\n\n')
file.write(f'Última atualização do site: {a.buscadados()[0][35:54]}\n\n')
file.write(f'Salvo em {datetime.now().strftime("%d/%m/%y - %H:%M:%S")}\n\n')
file.write(a.tabela())
file.close()