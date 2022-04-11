from typing import Optional
from pydantic import BaseModel, Field


class ItemsSchema(BaseModel):
    Autor: str = Field(...)
    Data_traducao: str = Field(...)
    Versao_Uniclass: str = Field(...)
    versao_secclas: int = Field(..., gt=0)
    code_tabela: float = Field(..., le=4)
    nivel_item: int = Field(...)
    Group: str = Field(...)
    Subgroup: str = Field(...)
    Section: str = Field(...)
    Object: str = Field(...)
    code_item: str = Field(...)
    title_item: str = Field(...)
    titulo_SECClasS: str = Field(...)
    review: bool = Field(...)
    descricao_SECClasS: str = Field(...)
    especialidade: str = Field(...)
    keywords: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "Autor": "SECClasS",
                "Data_traducao": {
                    "$date": "2021-06-25T00:00:00.000Z"
                },
                "Versao_Uniclass": "1.8",
                "versao_secclas": 1,
                "code_tabela": "Elementos/ funções",
                "nivel_item": 2,
                "Group": "25",
                "Subgroup": "30",
                "Section": "",
                "Object": "",
                "code_item": "EF_25_30",
                "title_item": "Doors and windows",
                "titulo_SECClasS": "Portas e janelas",
                "review": false,
                "descricao_SECClasS": "",
                "especialidade": "Genérico",
                "keywords": "",
            }
        }

    def ResponseModel(data, message):
        return {
            "data": [data],
            "code": 200,
            "message": message,
        }

    def ErrorResponseModel(error, code, message):
        return {"error": error, "code": code, "message": message}
