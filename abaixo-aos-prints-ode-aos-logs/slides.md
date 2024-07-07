---
marp: true
theme: gaia
class: invert
paginate: true
style: |
    img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }
    
---
<!-- 
_class: invert && lead
_paginate: false 
-->
# Abaixo aos prints, ode aos logs! 
![bg right:40%](imagens/louvor1.png)
### Renan de Assis

<!-- To muito nervoso até porque... aí troca de slide -->
---
<!-- _class: invert lead -->
<style scoped>
h1 {font-size: 100px;text-align: center;}
</style>

# É minha primeira vez palestrando em um evento oficial!

---
<!--- _paginate: false -->
# Quem sou eu?

![bg right:33%](imagens/eu.jpeg)

---
<!--- _paginate: false -->
# Quem sou eu?

- Bacharel em Física

![w:430 center](imagens/fisica.png)
![bg right:33%](imagens/eu.jpeg)

---
<!--- _paginate: false -->
# Quem sou eu?

- Bacharel em Física

- Trabalho com engenharia de software no Serasa
![center](imagens/serasa.png)
![bg right:33%](imagens/eu.jpeg)

---
<!--- _paginate: false -->
# Quem sou eu?

- Bacharel em Física
- Trabalho com engenharia de software no Serasa
- Gosto de vôlei, jogos de tabuleiro e tenho uma tatuagem do desenho Avatar
* Já fiz aulas de dança de salão
* Auxilio na organização das Python Brasil

![bg right:33%](imagens/eu.jpeg)

---
<!-- _class: invert lead -->

# AVISOS

* Contexto de aplicações web
* Minhas considerações no que eu aprendi pela vida e tudo aqui é debatível
<!--
Tô considerando o contexto de aplicações web, então são aplicações que ficam o tempo inteiro de pé (em loop infinito digamos assim) rodando em um servidor recebendo requisições. Não sei como seriam usados logs em outros contextos e ficaria contente se outra hora alguém viesse me falar
Vou passar por cima de alguns conceitos aqui, visto que é uma palestra informativa e pra deixar gostinho de quero mais
-->

---
<!-- _class: invert lead -->

# AVISOS

- Contexto de aplicações web
- Minhas considerações no que eu aprendi pela vida e tudo aqui é debatível
- Palestra informativa e pra deixar gostinho de curiosidade

![w:350](imagens/gato-curioso.jpg)

---

<!-- _class: invert lead -->
<style scoped> h1 {font-size: 100px;text-align: center;} </style>

# O que são logs?

---
<style scoped> h1 {text-align: center;} </style>

# Não tem nada a ver com logaritmo
![w:600 center](imagens/logaritmo.jpg)

---

# O que são logs?

É uma expressão utilizada para descrever o processo de **registro** de **eventos** relevantes em um sistema computacional.

* Registro: "escrever" ou "marcar" algo em algum lugar
* Eventos que aconteceram no **passado** e podem ser **observados**

<!-- _footer: 1. https://pt.wikipedia.org/wiki/Log_de_dados -->
---

# Eventos relevantes?

Exemplos de eventos:
1. **log**in
2. **log**off
3. Algum erro no sistema
4. Um sucesso em uma requisição externa

---

# Quando usar prints?

* Retorno rápido em ambiente local
* Script de uso único
<!-- retorno rápido no ambiente local na sua maquina ambiente controlado ou se for em um script que vai rodar apenas uma vez pra um determinado fim -->

---

# Quando usar logs?

---
<!--- _paginate: hold -->
<style scoped> p {font-size: 100px;text-align: center;} </style>

# Quando usar logs?

**TODO O RESTO**

<!-- A seguir vou mostrar algumas funcionalidades dos logs que não existem nos prints e como é uma ferramenta poderosa -->

---

# Lib padrão de logging do python

![w:950 center](imagens/logging-lib.png)

<!-- _footer: https://docs.python.org/pt-br/3.11/library/logging.html -->
---

# Conceitos de logs - níveis

![w:1100 center](imagens/logging-niveis-codigo.png)

---

# Conceitos de logs - níveis

![w:1100 center](imagens/logging-info.png)

---

# Conceitos de logs - níveis

![w:1100 center](imagens/logging-niveis.png)

<!-- _footer: https://docs.python.org/pt-br/3/howto/logging.html#logging-howto -->
---

# Conceitos de logs - formatação

![w:1000 center](imagens/logging-format.png)

---

# Conceitos de logs - formatação

![w:1000 center](imagens/logging-format2.png)

---

# Conceitos de logs - armazenamento

- Relembrando: logs são registros de eventos em algum lugar

![w:1100 center](imagens/logging-saida-shell.png)


---


# Conceitos de logs - armazenamento

- Relembrando: logs são registros de eventos em algum lugar

![w:1100 center](imagens/logging-saida-arquivo.png)


---

# Logs + computacão em nuvem

<!-- 
No desenvolvimento web atual costumamos usar plataformas de computação em nuvem como a do Google (GCP) ou da Amazon (AWS)
-->
- GCP(Google), AWS(Amazon), etc
- Serviços para monitorar, armazenar e acessar logs: 
  - Cloud Logging (Google) 
  - CloudWatch (AWS)

![w:200](imagens/icon-cloud-logging.png) ![w:180](imagens/icon-cloudwatch.png)

---

![bg contain](imagens/gcp-logging.png)

---
<style scoped> h1 {font-size: 60px} </style>

# Logs + ferramentas de monitoramento e observabilidade

- Existem ferramentas muito mais poderosas de monitoramento da performance das aplicações (APM)
- Podem integrar com serviços de computação em nuvem
- Logs, traces, infraestrutura, rastreio de erros, dashboards, etc

![w:200](imagens/newrelic.png) ![w:200](imagens/sentry.png) ![w:400](imagens/datadog.png)

---
<style scoped> h1 {font-size: 110px; text-align: center; margin-top: 180px;} </style>

# Loguru

---
<style scoped> h1 {font-size: 55px} </style>

# Simplificação de logs em python com loguru

![w:1100 center](imagens/loguru-intro-code.png)

<!-- _footer: https://loguru.readthedocs.io/en/stable/ -->
---
<style scoped> h1 {font-size: 55px; margin-bottom: 150px} </style>

# Simplificação de logs em python com loguru

![w:1100 center](imagens/loguru-intro-saida.png)

---

<style scoped> h1 {font-size: 55px} </style>

# Simplificação de logs em python com loguru

Apenas um comando para configurações

![w:1000 center](imagens/loguru-add.png)

---
<style scoped> h1 {font-size: 55px} </style>

# Simplificação de logs em python com loguru

Formatação de strings com sintaxe mais recente **{ }** ao invés de **%**

![w:1100 center](imagens/loguru-syntax-format.png)
![w:1100 center](imagens/loguru-syntax-format-saida.png)


---
<style scoped>
  p {
     font-size: 55px;
     text-align: center;
     margin-top: 180px;
    } 
</style>

**A MELHOR FUNCIONALIDADE**
(na minha opinião)

---
<style scoped>
  p {
     font-size: 55px;
     text-align: center;
     margin-top: 250px;
    } 
</style>

**Logs estruturados**

![bg right:50%](imagens/meme-wow2.png)

<!-- Explicar o que são aqui -->

---
<style scoped> h1 {font-size: 55px} </style>

# Simplificação de logs em python com loguru

![w:1100 center](imagens/loguru-struct.png)

- Saída do log em formato JSON
- Informações facilmente manipuláveis

---
<style scoped> h1 {font-size: 55px; margin-bottom:170px} </style>

# Simplificação de logs em python com loguru

![w:1100 center](imagens/loguru-struct-simplificado.png)

---
<style scoped> h1 {font-size: 55px} </style>

# Simplificação de logs em python com loguru

- Consigo adicionar informações personalizadas do meu fluxo

![w:1100 center](imagens/loguru-bind.png)
![w:1100 center](imagens/loguru-bind-saida.png)


---
<style scoped> h1 {font-size: 55px} </style>

# Simplificação de logs em python com loguru

- E adicionar essas informações em todo um contexto

![w:1100 center](imagens/loguru-contextualize.png)

---
<style scoped> h1 {font-size: 55px; text-align: center;margin-top: 260px;} </style>

# Usem, testem, fuçem o loguru

---

# Agradecimentos

- Equipe de organização da Python Sudeste s2
- Eduardo Mendes (vide Dunossauro) pela [live de python Nº198](https://www.youtube.com/watch?v=PGAOqAWuwC0) sobre logs que inspirou essa palestra
![w:500 center](imagens/thumb-dunossauro.jpg)

---

## Dúvidas?

Linkedin: /in/renan-asantos/
Telegram: @renan_asantos
Github: renan-assis-santos

![w:500 center](imagens/slide-encerramento.png)


<!--

https://github.com/marp-team/awesome-marp?tab=readme-ov-file#themes

https://github.com/dunossauro/fastapi-do-zero/tree/main/slides

https://marpit.marp.app/usage?id=constructor-options

https://dev.to/andyhaskell/write-your-tech-talk-slides-rapidly-with-marp-2c7g

https://stackoverflow.com/questions/69154809/how-to-align-image-below-text-header-in-marp-or-marpit

https://ayharano.github.io/pyse2024/#/

# Boas práticas em python (10min)

1. Para que cada nível de log é recomendado?
2. É legal adicionar um nível de log mais baixo (tipo DEBUG) quando estiver testando
3. E em produção ser INFO pra cima
4. Colocar apenas o necessário na mensagem e o resto deixar pro json
5. Recomendações de segurança do que logar e o que não. Tirar informações sensíveis
6. O que gravar no log?
    6.1 **Data/hora (timestamp), nome do arquivo que gerou o log**![alt text](<carbon (1).png>)
    6.2 **Nome da função, Caminho de um arquivo, linha do código que gerou o log**
    6.3 **Mensagens padronizadas (sucesso/falha de execução)**
    6.4 **Informações úteis para usuários/desenvolvedores**

* Quando criamos essas aplicacoes e rodamos localmente na nossa máquina da pra debugar (colocar uns print na hora e testar pra ver o que tá rolando), mas em um servidor n da pra mexer no código que tá rodando de forma tão simples e rápida e dps tirar ou iniciar um debugger.
* Com logs da pra ter uma visão constante e em "níveis" de criticidade como informativos, de avisos ou de erros no nosso sistema.
* Em resumo logs vão ajudar em dois pontos: ajudar um desenvolvedor a ver o que tá rolando no sistema sem precisar modificar o código e com isso ver onde tá algum erro e corrigir e a outra é colocar alertas tipo "se der algum log crítico me avisa no whats" algo assim.

-->