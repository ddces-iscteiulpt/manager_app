from datetime import datetime


def items_helper(items) -> dict:
    return {
        "id": str(items['_id']),
        "Autor": items['Autor'],
        "Data_traducao": datetime.fromtimestamp(items['Data_traducao']),
        "Versao_Uniclass": items['Versao_Uniclass'],
        "versao_secclas": int(items['versao_secclas']),
        "code_tabela": items['code_tabela'],
        "nivel_item": int(items['nivel_item']),
        "code_item": items['code_item'],
        "title_item": items['title_item'],
        "titulo_SECClasS": items['titulo_SECClasS'],
        "review": bool(items['review']),
    }

 # "Group": "20", "Subgroup": "", "Section": "", "Object": "",
 # "descricao_SECClasS": "", "especialidade": "Genérico", "keywords": "",
 # "tabela_id": str(items['tabela_id'])

