# Resultado - Desáfio CoorLab
olá, aqui está uma breve descrição de como foi implementada a soliçaõ para o desafio proposto.

## Backend

### Implementação
No backemd foram implementadas 3 rotas:

- /transport: responsável por fornecer todos os dados, caso necessário;
- /transport/\<city>: responsável por fornecer os dados de viagem para uma cidade específica;
  - Essa rota retornando, no máximo, duas possibilidades. A primeira delas sendo a mais rápida e a segunda a mais econômica
- /transport_cityes: responsável por fornecer o nome de todas as cidades com viagem disponível.
  

### Requisitos
- Python v3.7+
- framework flask

## Frontend