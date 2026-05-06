# 📊 Consulta FIPE (Python)

Script simples para consultar valores de veículos na API da Tabela FIPE.

---

## ⚙️ Instalação

```bash
pip install cloudscraper
```

---

## ▶️ Uso

```python
import cloudscraper

scraper = cloudscraper.create_scraper()

url = "https://veiculos.fipe.org.br/api/veiculos/ConsultarValorComTodosParametros"

payload = {
    "codigoTabelaReferencia": 333,
    "codigoMarca": "",
    "codigoModelo": "",
    "codigoTipoVeiculo": 1,
    "anoModelo": 2026,
    "codigoTipoCombustivel": "",
    "modeloCodigoExterno": "005538-7",
    "tipoVeiculo": "carro",
    "tipoConsulta": "codigo"
}

response = scraper.post(url, json=payload)
data = response.json()

if data.get("codigo") == "0":
    print("Erro:", data.get("resultado"))
else:
    print(data.get("Modelo"))
    print(data.get("Valor"))
    print(data.get("MesReferencia"))
```

---

## 📦 Parâmetros principais

* `codigoTabelaReferencia`: tabela FIPE atual
* `codigoTipoVeiculo`: 1=carro, 2=moto, 3=caminhão
* `anoModelo`: ano do veículo
* `modeloCodigoExterno`: código FIPE
* `tipoConsulta`: `"codigo"`

---

## 🔗 Endpoints úteis

* `/ConsultarModelos`
* `/ConsultarModelosAtravesDoAno`
* `/ConsultarAnoModelo`
* `/ConsultarValorComTodosParametros`

Base: https://veiculos.fipe.org.br/api/veiculos/

---

## ⚠️ Notas

* Código `"0"` = erro na API
* Tabela FIPE muda mensalmente
* Use outros endpoints para descobrir códigos

---
