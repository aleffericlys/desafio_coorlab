# Resultado - Desáfio CoorLab
olá, aqui está uma breve descrição de como foi implementada a solução para o desafio proposto.

## Backend

### Implementação
o backend foi construído em python com framework Flask para a criação das solicitações do banco de dados (nesse caso o arquivo `data.json`) com funções para a opção mais rápida e mais confortavel podendo ser usadas separadamente ou em conjunto.

No backemd foram implementadas 3 rotas:

- /transport: responsável por fornecer todos os dados, caso necessário;
- /transport/\<city>: responsável por fornecer os dados de viagem para uma cidade específica;
  - Essa rota retornando, no máximo, duas possibilidades. A primeira delas sendo a mais rápida e a segunda a mais econômica
- /transport_cityes: responsável por fornecer o nome de todas as cidades com viagem disponível.
  

### Requisitos
- Python v3.7+
- framework flask

## Frontend
A aplocacão do frontend foi iniciada com vue CDN nele os componentes foram criados com a ajuda de bootstrap5. como se trata de uma aplicação customisada foi feito um uso grande de CSS para formatação.

Foram criados vários componentes que se comunicam entre sí com meio de props e emits paar a ativação de certas funções e atributos.
 
Dentre os componentes criados estão:
- `AlertModal.vue`: componente que contém o modal de alerta para quando o usuário tentar fazer uma busca sem preencher os campos. Nele está o botão de fechar o modal e a mensagem de alerta caso o usuário tente fazer uma busca sem preencher os campos corretamente, com os campos corretamente preenchidos o ele emite um evento para o componente `Search.vue` para que a busca seja feita.
- `Search.vue`: componente que contém o formulário de busca. Nele estão os campos de destino, o botão de busca que vem de `AlertModal.vue` e as chamadas de api para o backend. Nesse componente também emite um evento para o componente `Calculator.vue` para que o resultado da busca seja exibido.
- `Result.vue`: componente onde o resultado da busca é exibido. ele recebe os dados da busca feita em `Search.vue` e exibe o resultado da busca, mostrando o nome da empresa, o tipo de leito, o tempo e custo total da viagem mais rápida e o nome da empresa, o custo total, o leito e a duração da viagem mais econômica. Quando o tempo de viagem da mais econômica e da mais rápida são iguais, o componente exibe apenas os dados da viagem com leito mais econômico. caso só haja uma opção de viagem, o componente exibe apenas os dados com o valor da opção leito.
- `Calculator.vue`: componente que contém o componentes de `Search.vue` e `Result.vue` e é responsável por receber os dados da busca feita em `Search.vue` e os enviar para `Result.vue` para que possa/am ser exibido/os o/os resultado/os da busca em `Result.vue`.
- `Sidebar.vue`: componente que contém a barra lateral com as paginas que serão exibidas na aplicação.
- `HomeView.vue`: componente que contém a página inicial e unica tela da aplicação, nela são exibidos os componentes `Sidebar.vue` e `Calculator.vue`.
- `App.vue`: componente principal que constrói a aplicação e contém o componente `HomeView.vue`.

### Requisitos
- VueJS 3
  