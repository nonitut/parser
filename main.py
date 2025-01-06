import requests
from bs4 import BeautifulSoup as bs
# from config import  HEADERS , PARAMS
import re
# import re - регулярные функции 

class Parser: 
    def __init__(self):
        self.url = "https://www.finmarket.ru/currency/rates/"
        
    def get_html_code(self) -> bs:   
        html_code = requests.get(self.url).text
        # print(html_code)
        soup = bs(html_code, "html.parser")
        return soup
    
    def table_parser(self, html_code: bs):
        table = html_code.find(class_="karramba")
        tbody = table.find("tbody")
        currentcy = tbody.find_all("tr")
        return currentcy  
        # return в данном случае логическое завеершение моей функции
        # print(table)
        
        
    def convert_encoding(self, text, from_encoding='iso-8859-1', to_encoding='CP1251'):
        return text.encode(from_encoding).decode(to_encoding)


    def convert_frrom_data(self, text):   
        currency_quotation = text[:3]
        currency_name = ""
        currency_num = ""
        text = text[3:]
        #  ttext = text[3:] убираем таким образом из результата 
        pattern_reggular_function = r"([^\d]+)([\d,]+\+[\d,]+)"
        match = re.match(pattern_reggular_function, text)
        
        if match:
            currency_name = match.group(1)
            currency_num = match.group(2)
            
            pattern = r"[+-][\d,]+" 
            
            # print(currency_quotation, currency_name, currency_num )
            currency_change = re.search(pattern, currency_num).group(0)
            print(currency_change)
        
    def currentcy_parser(self, currentcy: list[bs]):
        try: 
            for td in currentcy:
                per = self.convert_encoding (td.text)
                print(self.convert_frrom_data (per))
        except: 
            pass
    # Если try не отработает, то выводим except , pass - пропустить функцию 
    
    # corrupted_text = 
    # decoded_text = corrupted_text.encode('latin1').decode('utf-8')
    # print(decoded_text)
    
parser = Parser()
l = parser.get_html_code()
newone = parser.table_parser(l)
parser.currentcy_parser(newone)
# get получаем данные 
# post 200 / 201 нормик сайт получил данные