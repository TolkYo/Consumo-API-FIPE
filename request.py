#https://veiculos.fipe.org.br/api/veiculos/ConsultarModelos
#https://veiculos.fipe.org.br/api/veiculos/ConsultarModelosAtravesDoAno
#https://veiculos.fipe.org.br/api/veiculos/ConsultarAnoModelo
#https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros

import cloudscraper
import json

scraper = cloudscraper.create_scraper()

url = 'https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros'

payload = {
    "codigoTabelaReferencia": 333,
    "codigoMarca": '',
    "codigoModelo": '',
    "codigoTipoVeiculo": 1,
    "anoModelo": 2026, 
    "codigoTipoCombustivel": '',
    "modeloCodigoExterno": "005538-7",
    "tipoVeiculo": "carro",
    "tipoConsulta": "codigo"
}

try:
    response = scraper.post(url, json=payload)
    response.raise_for_status()
    
    data = response.json()
    
    if "codigo" in data and data["codigo"] == "0":
        print(f"Erro: {data['resultado']}")
    else:
        print(f"--- Dados do Veículo ---")
        print(f"Modelo: {data.get('Modelo')}")
        print(f"Valor:  {data.get('Valor')}")
        print(f"Mês de Ref: {data.get('MesReferencia')}")

except Exception as e:
    print(f"Erro na requisição: {e}")