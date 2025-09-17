# main.py

import os
from xml_reader import read_xml_files
from excel_reader import read_excel_file
from comparer import compare_files, verify_xml_values

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1) Verificar XML (valores vPag vs Excel col G)")
        print("2) Comparar XML com Excel (nomes)")
        print("3) Sair")
        opc = input("Opção: ").strip()

        if opc == "1":
            xml_dir = input("Pasta de XMLs: ").strip()
            excel_path = input("Arquivo Excel: ").strip()
            excel_data = read_excel_file(excel_path)
            verify_xml_values(xml_dir, excel_data)

        elif opc == "2":
            xml_dir = input("Pasta de XMLs: ").strip()
            excel_path = input("Arquivo Excel: ").strip()
            xml_files = read_xml_files(xml_dir)
            excel_names = read_excel_file(excel_path)  # se for lista, adapte
            compare_files(xml_files, excel_names)

        elif opc == "3":
            print("Encerrando.")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()