import xml.etree.ElementTree as ET
from xml_reader import read_xml_files

def verify_xml_values(xml_directory, excel_data):
    xml_files = read_xml_files(xml_directory)
    mismatch = []

    for xml_path in xml_files:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        infNFe = root.find('.//{*}infNFe')
        if infNFe is None:
            continue
        chave = infNFe.get('Id','').replace('NFe','')

        total = root.find('.//{*}total')
        if total is None:
            continue
        vNF_elem = total.find('.//{*}vNF')
        if vNF_elem is None:
            continue

        # 1) valor no XML
        try:
            xml_val = float(vNF_elem.text)
        except:
            xml_val = None

        # 2) valor “raw” do Excel e normalizado
        excel_raw = excel_data.get(chave)
        excel_norm = None
        if excel_raw is not None:
            if isinstance(excel_raw, str):
                # ex: "103,40" -> "103.40"
                excel_norm = float(excel_raw.replace('.', '').replace(',', '.'))
            else:
                excel_norm = float(excel_raw)

        # 3) compara com tolerância de 0.0001
        if excel_norm is None or abs((xml_val or 0.0) - excel_norm) > 1e-4:
            mismatch.append((chave, xml_val, excel_raw))

    if mismatch:
        print("\n== Valores divergentes (ou faltando no Excel) ==")
        for chave, xv, ev in mismatch:
            print(f"{chave} | Valor XML = {xv} | Valor Excel = {ev}")
    else:
        print("Nenhuma divergência encontrada.")

def compare_files(xml_paths, excel_data):
    """
    Compara chaves de acesso entre XML e Excel.
    xml_paths: lista de caminhos completos para arquivos XML
    excel_data: dict {chave_acesso: valor_col_G}
    """
    xml_keys = set()
    for xml_path in xml_paths:
        print(f"[DEBUG] Lendo XML: {xml_path}")
        try:
            tree = ET.parse(xml_path)
        except Exception as e:
            print(f"  [ERROR] falha ao parsear {xml_path}: {e}")
            continue

        root = tree.getroot()
        infNFe = root.find('.//{*}infNFe')
        if infNFe is None:
            print(f"  [WARN] <infNFe> não encontrado em {xml_path}")
            continue

        chave = infNFe.get('Id', '').replace('NFe', '')
        xml_keys.add(chave)

    excel_keys = set(excel_data.keys())

    only_in_xml = xml_keys - excel_keys
    only_in_excel = excel_keys - xml_keys
    in_both = xml_keys & excel_keys

    print("\n== Chaves apenas no XML ==")
    for k in sorted(only_in_xml):
        print(k)

    print("\n== Chaves apenas no Excel ==")
    for k in sorted(only_in_excel):
        print(k)

    print("\n== Chaves em ambos ==")
    for k in sorted(in_both):
        print(k)