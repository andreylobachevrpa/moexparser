from datetime import datetime
from pathlib import Path
import pandas as pd



class Excel:
    def __init__(self, output_dir='result'):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def create_excel_file(self, usd_data, jpy_data):
        """Метод для создания excel файла"""
        usd = [[d[0], float(d[3]), d[4]] for d in usd_data]
        jpy = [[d[0], float(d[3]), d[4]] for d in jpy_data]
        
        df = pd.DataFrame({
            'Дата USD/RUB': [d[0] for d in usd],
            'Курс USD/RUB': [d[1] for d in usd],
            'Время USD/RUB': [d[2] for d in usd],
            'Дата JPY/RUB': [d[0] for d in jpy],
            'Курс JPY/RUB': [d[1] for d in jpy],
            'Время JPY/RUB': [d[2] for d in jpy],
            'USD/JPY': [usd[i][1]/jpy[i][1] for i in range(len(usd))]
        })

        filename = f"currency_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        filepath = self.output_dir / filename
        with pd.ExcelWriter(filepath, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Курсы')
        
            workbook = writer.book
            worksheet = writer.sheets['Курсы']
            money_format = workbook.add_format({
                'num_format': '_(* #,##0.0000_);_(* (#,##0.0000);_(* "-"??_);_(@_)',
                'align': 'right'
            })
            header_format = workbook.add_format({
                'bold': True,
                'align': 'center',
                'border': 1,
                'bg_color': '#F0F0F0'
            })
            worksheet.set_row(0, 25, header_format)
            worksheet.set_column(0, 0, 15)      # Дата USD (A)
            worksheet.set_column(1, 1, 15, money_format)  # Курс USD (B)
            worksheet.set_column(2, 2, 12)      # Время USD (C)
            worksheet.set_column(3, 3, 15)      # Дата JPY (D)
            worksheet.set_column(4, 4, 15, money_format)  # Курс JPY (E)
            worksheet.set_column(5, 5, 12)      # Время JPY (F)
            worksheet.set_column(6, 6, 15, money_format)  # USD/JPY (G)
        return str(filepath)
    
    def get_info(self, excel_filepath):
        """Метод для получения колличества строк в нужном склонении"""
        df = pd.read_excel(excel_filepath)
        num_rows = len(df)
        if num_rows % 10 == 1 and num_rows % 100 != 11:
            rows_str = f"В файле {num_rows} строка"
        elif 2 <= num_rows % 10 <= 4 and not (12 <= num_rows % 100 <= 14):
            rows_str = f"В файле {num_rows} строки"
        else:
            rows_str = f"В файле {num_rows} строк"
        return rows_str