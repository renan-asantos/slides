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
    .columns {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 1rem;
    }
    
---
<!-- paginate: false -->
<style scoped>
h1 {text-align:center; margin-top:120px;}
h3 {text-align:center}
</style>

# Evoluindo o sistema
### Ana Dulce
### Renan de Assis


![bg right:40%](imagens/louvor.png)

---

# Quem é o Renan?

- (auto descrição)

![bg right:33%](imagens/eu.jpeg)

---
# Quem é o Renan?

- Bacharel em Física

![w:430 center](imagens/fisica.png)
![bg right:33%](imagens/eu.jpeg)

---
# Quem é o Renan?

- Bacharel em Física
- Trabalho com engenharia de software no Serasa
![center](imagens/serasa.png)
![bg right:33%](imagens/eu.jpeg)

---
# Quem é o Renan?

- Bacharel em Física
- Trabalho com engenharia de software no Serasa
- Gosto de vôlei, jogos de tabuleiro e tenho uma tatuagem do desenho Avatar
* Ajudo na organização de eventos Python Brasil
![bg right:33%](imagens/eu.jpeg)

---
# Quem é a Ana?

---

# Motivação

* "Evoluindo o sistema" qual sistema?
* Motivação da existência da oficina

<!--

- Sempre vi tutoriais de criar a primeira API com algum framework, 
seja com flask, django ou fastapi.
- É bem legal saber fazer isso mesmo, é a parte principal para nosso sistema
 estar minimamente funcional, mas um projeto de software não acaba aí.
- Existe muitos outros recursos para adicionarmos para melhorar a qualidade,
 confiabilidade e capacidade de manutenção do nosso projeto.

 Isso que vamos fazer juntos no dia de hoje

-->
---

# O que essa oficina NÃO vai te mostrar? (deixar mais simpatica)

- Não vai te mostrar como criar uma API com nenhum framework de Python
- Não vai entrar nos mínimos detalhes de uma API

---

# O que essa oficina vai te mostrar?

<div class="columns">
<div>

- configuração do ambiente
- documentação
- logs
- testes

</div>
<div>

- formatadores
- análise estática
- automação de comandos
- automação de hooks git

</div>
</div>

---

# BORA TIMEE (centralizado)

---

# Configuração inicial do ambiente

Antes de apresentarmos o sistema que vamos trabalhar, vamos configurar nosso ambiente inicial
(ainda decidindo se poetry ou UV, carai bora la já ta hora)

- definir versao do python
- instalar gerenciador de pacotes
- ativar ambiente virtual

---

# Subir o projeto

- clona o repositório de template
- Instalar as dependencias do projeto e subir ele, bater na url do /docs, ver o swagger e chamar um dos endpoints com sucesso
- então é isso, já ta pronto e funcional, ta fazendo sua atividade fim
- agora vamos melhorar as "bordas" dele

---

# Para poder melhorarmos o sistema, é bom entender minimamente o que ele faz

(Ana explica explica minimamente o que o projeto faz e quais os endpoints, como o banco está estruturado etc)

---

# Documentação

(grande incógnita)
(gráfico de visualizacao do banco)
acho que da pra meter um mkdocs simples em, ver live do du (https://www.youtube.com/live/O3bs4JtHrow) minuto 1h35

---

# Logs

- O que são?
- No que contribuem para o nosso sistema?

- Queremos dar visibilidade em que?

---

# Testes

- O que são?
- No que contribuem para o nosso sistema?

---

# Automatizando comandos no nosso sistema

- O que são?
- No que contribuem para o nosso sistema?

- Como fazer um bom teste?


---

# Formatadores automáticos

- O que são?
- No que contribuem para o nosso sistema?

---

# Análise estática (linters)

- O que são?
- No que contribuem para o nosso sistema?

---

# Automatizando comandos no nosso sistema

- O que são?
- No que contribuem para o nosso sistema?




<!-- --

https://github.com/marp-team/awesome-marp?tab=readme-ov-file#themes

https://github.com/dunossauro/fastapi-do-zero/tree/main/slides

https://marpit.marp.app/usage?id=constructor-options

# Colunas nos slides Marp
https://github.com/orgs/marp-team/discussions/192

https://dev.to/andyhaskell/write-your-tech-talk-slides-rapidly-with-marp-2c7g

https://stackoverflow.com/questions/69154809/how-to-align-image-below-text-header-in-marp-or-marpit

https://ayharano.github.io/pyse2024/#/

-->