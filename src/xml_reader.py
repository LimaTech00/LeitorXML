import os

def read_xml_files(xml_directory):
    """
    Retorna a lista de paths completos de todos os .xml em xml_directory.
    """
    xml_files = []
    for nome in os.listdir(xml_directory):
        if nome.lower().endswith('.xml'):
            caminho = os.path.join(xml_directory, nome)
            if os.path.isfile(caminho):
                xml_files.append(caminho)

    # debug:
    print(f"[DEBUG] XML: encontrados {len(xml_files)} arquivos em '{xml_directory}'.")
    print(f"[DEBUG] Exemplos: {xml_files[:5]}")
    return xml_files