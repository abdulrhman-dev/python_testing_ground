from tabula import read_pdf
from pandas import ExcelWriter

from sys import argv

pdf_path = argv[1]
excel_path = argv[2]

try:
    print('Reading pdf...')
    dataframes = read_pdf(pdf_path, pages='all', stream=True)

    writer = ExcelWriter(excel_path, engine='openpyxl')
    for i, dataframe in enumerate(dataframes):
        if(i == 4):
            print(dataframe)
        print(f"Converting {i + 1 }...")
        dataframe.to_excel(writer, sheet_name=f'Sheet {i + 1}', index=False)
    writer.close()

    print("Successfully converted pdf file")
except Exception as error:
    print('An exception occurred:', error)