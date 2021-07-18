# Teste técnico

## Como usar
Primeiramente, para acessar é necessário estar com o Docker instalado.

Para iniciar a aplicação, a única coisa que se deve fazer é ir até a pasta do projeto através do CMD e executar o comando `docker compose up -d`. Com isso, o Docker criará dois containers, um para o Banco Mysql, e outro para a Api.

Para testar a aplicação, recomendo o uso de alguma tecnologia de requisições, como Postman ou Insomnia. O projeto estará rodando em localhost na porta 5000, então acesse através da url `http://localhost:5000/`
Existem dois endpoint possíveis de serem acessados, sendo eles: `/api/basic` e `/api/advanced`, sendo o primeiro para a parte básica do teste e o segundo para a que envolve banco de dados.

No endpoint `/api/basic` é possível enviar (através do método Get) dois parâmetros, sendo eles: `total_days` e `gain_per_day`. Enviando tudo corretamente, retornará o resultado.

No endpoint `/api/advanced` é possível enviar requisições através dos métodos Get e Post. O primeiro método serve para conulta e deve ser enviado com os parâmetros `profissao` e `total_days`, e isso retornará o resultado. O segundo método serve para cadastro deve ser enviado com os parâmetros `profissao` e `valor_diario`, e caso tudo esteja correto, será salvo no banco de dados.


Qualquer dúvida ou problema, por favor, entre em contato. Meu celular: 47 9 8807-9176. Meu email: vergiliopoleza@gmail.com.
