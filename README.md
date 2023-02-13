![alt text](./img/pinPop.png)
# 1.Introducao e o problema de negocio

A pinPop é um marketplace ficticio de restaurantes, onde atraves de um aplicativo conecta restaurantes, entregadores e clientes.

Os restaurantes fazem o cadastro dentro da plataforma do pinPop, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

Esse projeto buscou entender melhor o negócio e com isso propicioar a uma analise de dados que permita tomadas de decisoes estrategicas com o escopo de alavancar o pinPop. Com isso, :

1. Realizar a analise exploratoria de dados dos restaurantes registrados dentro da plataforma;
2. Desenvolver um dashboard online que possa ser acessado e permita aplicacao de filtros de atributos e uma visualização de localizacao geografica dos restaurantes, dados por cidade, pais, tipo de culinaria, avaliacao e custo. 
   
# 2.Premissas

Algumas premissas foram assumidas:
1. Foram excluidas todas as informacoes que encontravam-se vazias ou NaN.
2. Foram consideradas apenas o principal tipo culinario de cada restaurante e para tanto, foi considerado como principal tipo culinario, o primeiro tipo cadastrado.
3. Considerou-se como criterio de desempate a coluna 'restaurante_id', considerando que o id de menor valor conrresponderia ao restaurante mais antigo cadastrado no aplicativo.
   
# 3.Planejamento da solucao:
### 3.1.Entrega
1. Painel online, hospedado em nuvem com a apresentação geral dos dados, podendo ser acessado atraves do link: [title](https://lununespires-world-restaurants-home-hvl5xm.streamlit.app/)


### 3.2.Ferramentas
- Python 3.9
- Jupyter notebook
- Streamlit

### 3.3.Processo
Para responder as questões de negócio, os dados foram coletados, processados, transformados, limpos e explorados.


# 4.Principais insights
- O pinPop atualmente encontra-se em 15 paises, sendo que a India e os Estados Unidos da America sao seus dois maiores mercados.
- O apesar da Inglaterra ser apenas o ter
- 

# 5.Conclusao
# 6.Proximos Passos

