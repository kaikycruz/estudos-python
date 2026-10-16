import argparse
import re
import sys

import requests
from pydantic import BaseModel, ValidationError

BASE_URL = "https://viacep.com.br/ws"


class Endereco(BaseModel):
    cep: str
    logradouro: str
    bairro: str
    localidade: str
    uf: str


def validar_cep(text: str) -> str:
    cep = text.strip().replace("-", "")
    if not re.fullmatch(r"\d{8}", cep):
        raise ValueError("CEP inválido: informe 8 dígitos")
    return cep


def consultar_cep(cep: str) -> Endereco:
    url = f"{BASE_URL}/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError) as erro:
        raise RuntimeError("Não foi possível consultar a API") from erro

    if "erro" in data:
        raise ValueError("CEP não encontrado")

    try:
        return Endereco(**data)
    except ValidationError as erro:
        raise RuntimeError("Resposta da API em formato inesperado") from erro


def main():
    parser = argparse.ArgumentParser(description="Consulta um endereço pelo CEP na ViaCEP")
    parser.add_argument("cep", help="CEP com 8 dígitos, com ou sem hífen")
    args = parser.parse_args()

    try:
        cep = validar_cep(args.cep)
        endereco = consultar_cep(cep)
    except (ValueError, RuntimeError) as erro:
        print(erro)
        sys.exit(1)

    print(f"CEP: {endereco.cep}")
    print(f"Logradouro: {endereco.logradouro}")
    print(f"Bairro: {endereco.bairro}")
    print(f"Localidade: {endereco.localidade}")
    print(f"UF: {endereco.uf}")


if __name__ == "__main__":
    main()