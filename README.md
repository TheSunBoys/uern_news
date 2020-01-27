# Feed UERN
### [UERN news](link)

#### sobre o projeto
- bot feito em python que analisa elementos de um rss e envia para um chat/grupo/canal do telegram usando a API
de um bot do telegram.

- ele foi criado com o proposito de ser notificado via telegram sobre as ultimas noticias da universidade e de sites relacioados a ela

#### informações sobre o codigo
- o token do bot e o id do tipo de chat que bot usará precisam estar em um arquivo chamado **.bot.json**,
para cria-lo basta usar o arquivo *rss.py* e modificar o final com seus dados e executar o mesmo.

- As urls ficam no arquivo *main.py*, responsavel por chamar os modulos necessarios e orquestar a execução do algoritmo, essas urls são passadas como argumento para a função *donwloadXML*, pode passar quantos argumentos desejar, desde que todos sejam urls para acessar um rss

- A partir da primeira execução do algoritmo, uma pasta **.database** será criada, a função dela é manter as ultimas versões dos rss para comparação, assim permite o bot mandar somente as novas informações do rss e não mandar mensagens duplicadas, desde que a pasta .database não seja apagada

- instruções sobre criar e manipular um bot telegram podem ser acessadas em: https://core.telegram.org/bots

##### este projeto não tem qualquer relação com a equipe administrativa da uern
