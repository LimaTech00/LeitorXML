import os

def read_excel_file(path):
    """
    Retorna um dict {chave_acesso: valor_da_coluna_G}.
    Suporta .xlsx (openpyxl) e .xls (xlrd).
    """
    ext = os.path.splitext(path)[1].lower()
    excel_data = {}

    if ext == ".xlsx":
        import openpyxl
        wb = openpyxl.load_workbook(path, data_only=True)
        sheet = wb.active
        for row in sheet.iter_rows(min_row=2):
            # antes: row[0] // agora coluna C = índice 2
            chave = str(row[2].value).strip() if row[2].value else ""
            valor = row[6].value  # coluna G
            if chave:
                excel_data[chave] = valor

    elif ext == ".xls":
        import xlrd
        wb = xlrd.open_workbook(path)
        sheet = wb.sheet_by_index(0)
        for i in range(1, sheet.nrows):
            # coluna C = 2, coluna G = 6
            chave = str(sheet.cell_value(i, 2)).strip()
            valor = sheet.cell_value(i, 6)
            if chave:
                excel_data[chave] = valor

    else:
        raise ValueError(f"Formato não suportado: {ext}")

    # debug:
    print(f"[DEBUG] Excel: lidas {len(excel_data)} entradas.")
    print(f"[DEBUG] Chaves Excel (amostra): {list(excel_data.keys())[:5]}")
    return excel_data