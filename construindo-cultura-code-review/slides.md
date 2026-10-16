---
marp: true
theme: your-theme
paginate: true
style: |
    img[alt~="center"] {
      display: block;
      margin: 0 auto;
    }
    /* layout de duas colunas */
    .columns {
      display: flex;
      gap: 2rem;
    }
    .column {
      flex: 1;
    }
---

<style scoped>
h1 {text-align:center; margin-top:120px;}
h3 {text-align:center}
</style>

# Construindo uma cultura de code review :rocket:
### Renan de Assis

![bg right w:400](imagens/tv-cultura-sem-fundo.png)

---
## Sumário

1. O que são PRs e Code Reviews?
2. Benefícios do Code Review
2. Code Review na era da IA
3. Dicas para autores de PRs
4. Dicas para revisores de PRs

---
## Quem sou eu?

- (auto descrição)

![bg right:33%](imagens/eu.jpeg)

---
## Quem sou eu?

- Bacharel em Física

![w:600 center](imagens/neil-degrasse-physics.gif)
![bg right:33%](imagens/eu.jpeg)

---
## Quem sou eu?

![bg right:33%](imagens/eu.jpeg)

<div class="columns">
  <div class="column">

- Bacharel em Física
- Engenheiro de software na Serasa
  
  </div>
  <div class="column">

![w:400 center](imagens/meme-serasa.png)

  </div>
</div>

---
## Quem sou eu?

![bg right:33%](imagens/eu.jpeg)

<div class="columns">
  <div class="column">

- Jogo vôlei
- Adoro jogos de tabuleiro e tenho uma tatuagem do desenho Avatar
- Ajudei uns anos na organização dos eventos Python Brasil

  </div>
  <div class="column">

![w:300 center](imagens/tattoo-avatar.jpeg)

  </div>
</div>

---
<style scoped> 
h2 {font-size:100px; text-align:center; margin-top:200px;}
</style>

## AVISOS

---
<style scoped>
h2 {font-size:60px; text-align: center}
img {margin-top: 30px}
</style>

## AVISOS

- Minhas considerações do que **eu** aprendi na vida
- Tudo aqui é debatível
![w:600 center](imagens/sei-nada-sei.png)

---

<!-- _class: slide-secao -->

## O que são PRs e Code Reviews?

---
## O que são PRs?

>> Pull Request é um recurso de plataformas de hospedagem de código Git para propor mudanças de uma branch para outra em um projeto de software.¹

![center](imagens/gitflow-pr.png)

<!-- _footer: 1. Definição própria -->
---

## O que são ~~PRs~~ MRs?

<div class="columns">
  <div class="column">

Gitlab possui um nome que eu prefiro: __MRs ou Merge-Requests__

  </div>
  <div class="column">

![center](imagens/meme-gitlab-github.png)

  </div>
</div>

<!--
PR é porque o mantenedor do projeto teria que dar um pull na branch com as alterações para testar e validar
MR é porque o mantenedor vai mergear as alterações na branch de destino
-->

<!-- _footer: 1. Definição própria -->
---
## O que são MRs?

![height:5in center](imagens/pr1.png)

---
## O que são MRs?

![height:4in center](imagens/pr2.png)

---

## O que são Code Reviews?

>> Revisão de código é o processo no qual o autor de uma MR disponibiliza seu código para pelo menos uma outra pessoa avaliar, essa podendo adicionar comentários para o entendimento, estabelencendo-se um diálogo¹

![w:650 center](imagens/gitflow-code-review.png)

<!-- _footer: 1. Definição própria -->

<!--
O revisor pode adicionar comentários no código sob revisão, procurando esclarecer dúvidas, sugerindo melhorias, indicando bugs, etc.
Estabelece-se um "diálogo" na forma de troca de comentários entre o autor do código e o seu revisor.
-->

---

## O que TAMBÉM É Code Review?

<div class="columns">
  <div class="column">

- Pair Programming, só que assíncrono
* Parte da tarefa
* Última barreira humana pré produção
* Acordo entre o time/área/empresa
  
  </div>
  <div class="column">

![w:600](imagens/pair-programming.png)

  </div>
</div>

<!--
Parte da tarefa: não tem como subir na main sem alguém revisar e sua tarefa só acaba quando vai pra main
-->

---

## O que NÃO É Code Review?

* Tarefa do time de QA
* "Bala de prata"
![w:550](imagens/bala-de-prata.png)

<!--
* Não vai testar e2e
* Não vai pegar TODOS os possíveis bugs
-->

---
<!-- _class: slide-secao -->

## Benefícios do Code Review 

---

## Benefícios do Code Review

* Além de identificar, previne possíveis bugs
* Aumenta a qualidade do software escrito
* Diminui o risco de dívidas técnicas
* __Oportunidade de aprendizado (para ambos)__

---

## Benefícios do Code Review

Uma boa cultura de code review pode indicar falhas no seu processo...

* Complexidade da tarefa
* Entendimento do que era preciso
* Necessidade

<!--
1. Quanto tempo em review? Quantos arquivos alterados? Ficou muito tempo porque o codigo tava grande e era pesaroso de revisar? Pode indicar que as tasks nao estao bem quebradas

2. Quantas alterações foram pedidas? A pessoa que fez nao entendeu bem a task? nao sabe muito bem como trabalhar naquele projeto?

3. Depois de aprovada ficou parada? Era mesmo tao importante aquela alteracao?
-->

---

<!-- _class: slide-secao -->

## Code Review na era da IA

---

Dado que a IA existe...
* Volume de código gerado é muito maior
* O "pair programming assíncrono" agora é síncrono com humano + IA
* Escrever código era mais lento que revisá-lo. A IA inverteu essa lógica¹

<!-- _footer: 1. [The Final Bottleneck](https://lucumr.pocoo.org/2026/2/13/the-final-bottleneck/) -->

---

<div class="columns">
  <div class="column">

> E se fizermos um agente para revisar MRs?

* Se a IA escreve o código e a IA também revisa, quem é o responsável?
* Com quem está o conhecimento do código?
  
  </div>
  <div class="column">

![w:600 center](imagens/ia-cycle.png)

  </div>
</div>

---

<div class="columns">
  <div class="column">

> E se fizermos um agente para revisar MRs?

- Se a IA escreve o código e a IA também revisa, quem é o responsável?
- Com quem está o conhecimento do código?
  
  </div>
  <div class="column">

![w:600 center](imagens/o-que-esse-codigo-faz.gif)

  </div>
</div>

---

## Qual a importância do Code Review agora?

* Autores de MRs cada vez menos revisando a saída das IAs
* O review humano vira uma validação de intenção mais do que correção de bugs
* "O time entende o código gerado?” passa a ser critério de DoD
* Limite de WIP importante é: "quantas mudanças o time consegue entender simultaneamente?"

<!--
* Então é no review que vai ser pego erros e ajustes
* ...
* Para perpetuar o conhecimento
* Antes n podia ter mta coisa in progress, hj essa etapa ja ta mais rapida, mas precisa de um limite de code review
-->

---
<!-- _class: slide-secao -->

## Dicas para autores de MRs

<!-- "Agora que entendemos como a IA mudou um pouco o jogo, vamos ver algumas dicas pra quem abre uma MR..."-->

---
## Dicas para autores de MRs

- MRs pequenas
- Sem juntar **várias** mini melhorias

![bg w:400 right](imagens/meme-big-mr.png)

---
## Dicas para autores de MRs

<div class="columns">
  <div class="column">

O primeiro revisor é sempre **você**!
- CI
- Conflitos
- Testes unitários
- Linter/formatter
- Subiu em dev?
  
  </div>
  <div class="column">

![w:700 center](imagens/meme-review-my-code.png)

  </div>
</div>

---
## Dicas para autores de MRs

<div class="columns">
  <div class="column">

O primeiro revisor é sempre **você**!

**IA**: Não peça para alguém revisar o que nem você mesmo revisou¹
  
  </div>
  <div class="column">

![w:700 center](imagens/meme-review-my-code.png)

  </div>
</div>

<!-- _footer: 1. [Guidelines for Respectful Use of AI](https://skamille.medium.com/guidelines-for-respectful-use-of-ai-affcc85d7072) -->

---
## Dicas para autores de MRs

<div class="columns">
  <div class="column">

Crie uma MR em draft
- opinião rápida sobre a abordagem
- “erre rápido” para corrigir rápido
  
  </div>
  <div class="column">

![w:650 center](imagens/draft-mr.png)

  </div>
</div>

---
## Dicas para autores de MRs

<div class="columns">
  <div class="column">

Crie uma MR em draft
- opinião rápida sobre a abordagem
- “erre rápido” para corrijir rápido
  
  </div>
  <div class="column">

![w:650 center](imagens/draft-mr2.png)

  </div>
</div>

---
## Dicas para autores de MRs

<div class="columns">
  <div class="column">

Forneça __contexto__ para quem vai ler a MR
- Escreva uma descrição clara e bem exemplificada
- Adicione imagens, gifs, vídeos
  
  </div>
  <div class="column">

![w:650 center](imagens/descricao-mr.png)

  </div>
</div>

---
## Dicas para autores de MRs

<div class="columns">
  <div class="column">

- Discutir nos comentários, não no pv
- Responda o quanto antes os comentários
- Muitas sugestões de melhoria? Abra outro ticket
  
  </div>
  <div class="column">

![w:700 center](imagens/comentario.png)

  </div>
</div>

<!--
1. Discuta as sugestões de preferência nos comentários da própria PR para que todos vejam ou acompanhem e se não estiverem se entendendo, façam uma ligação.
2. Vira um bate bola rapido e fecha logo a mr
3. Se a sugestão que outra pessoa der for modificar muito o código ou não impactar negativamente, pergunte se pode abrir um ticket de dívida técnica linkando aquela sugestão
-->

---
## Dicas para autores de MRs

<div class="columns">
  <div class="column">

- Não leve para o pessoal, você não é seu código
- __Seja gentil e se coloque no lugar do revisor__
  
  </div>
  <div class="column">

![w:700 center](imagens/comentario.png)

  </div>
</div>

<!--
Sempre responda um comentário, mesmo que com um emoji 🙂, não feche o comentário que alguém fez uma pergunta, a pessoa nao sabe se voce acatou, recusou a sugestao etc

Não leve para o pessoal, você não é seu código
-->

---
<!-- _class: slide-secao -->

## Dicas para revisores de MRs

---
## Dicas para revisores de MRs

<div class="columns">
  <div class="column">

Adquira contexto antes de revisar
- O autor caprichou na descrição? Então use-a!
- Leia o card atrelado à tarefa

  </div>
  <div class="column">

![w:600 center](imagens/descricao-mr.png)

  </div>
</div>

---
## Dicas para revisores de MRs

_Roteiro pessoal_
- Começe pelos arquivos não de código fonte, adições de libs, arquivos de configurações, documentação
- Alterne entre o código fonte e os testes
- Siga o fluxo desde o começo, por exemplo 
  `endpoint` -> `service` -> `utils`

---
## Dicas para revisores de MRs
Nos arquivos de código...

<div class="columns">
  <div class="column">

- Analise nomes de variáveis, estão claros e intuitivos?

  </div>
  <div class="column">

![w:500](imagens/bad-variable-names.png)

  </div>
</div>

---
## Dicas para revisores de MRs
Nos arquivos de código...
<div class="columns">
  <div class="column">

![w:500](imagens/bad-variable-names.png)

  </div>
  <div class="column">

![w:600](imagens/good-variable-names.png)

  </div>
</div>

---
## Dicas para revisores de MRs

<div class="columns">
  <div class="column">

Nos arquivos de código...


- Existe over-engineering?
- Quem ler entenderá a solução no futuro? 

  </div>
  <div class="column">

![w:700](imagens/overengineering.png)

  </div>
</div>

---
## Dicas para revisores de MRs

<div class="columns">
  <div class="column">

Lembre do Zen do Python:

>> Simple is better than complex

__IA__: tende a deixar mais complexo, então cuidado¹

  </div>
  <div class="column">

![w:700](imagens/antiover-eng.png)

  </div>
</div>

<!-- _footer: 1. [Guidelines for Respectful Use of AI](https://skamille.medium.com/guidelines-for-respectful-use-of-ai-affcc85d7072) -->

---
## Dicas para revisores de MRs
Nos arquivos de testes...

<div class="columns">
  <div class="column">

- Estão corretos e bem arquitetados?
- Bons nomes?

  </div>
  <div class="column">

![](imagens/teste-ruim.png)

  </div>
</div>

---
## Dicas para revisores de MRs
Nos arquivos de testes...

<div class="columns">
  <div class="column">

- Estão corretos e bem arquitetados?
- Bons nomes?


  </div>
  <div class="column">

![w:700](imagens/teste-bom.png)

  </div>
</div>

---
## Dicas para revisores de MRs



<div class="columns">
  <div class="column">

Nas MRs mais críticas, faça checkout da branch, rode você mesmo e valide

  </div>
  <div class="column">

![w:700](imagens/checkout-branch.gif)

  </div>
</div>

---
## Dicas para revisores de MRs
Ao comentar na MR...

- Adicione sugestões de código

![w:750](imagens/sugestao-codigo.png)

---
## Dicas para revisores de MRs
Ao comentar na MR...

<div class="columns">
  <div class="column">

- Selecione trechos de código específicos
- Explique sua sugestão, coloque referências, exemplos, imagens, etc

  </div>
  <div class="column">

![w:700](imagens/sugestao-codigo2.png)

  </div>
</div>

---
## Dicas para revisores de MRs
Ao comentar na MR...

- __Enalteça__ pontos interessantes, elogie códigos bons e comente se aprendeu algo novo

![center](imagens/elogio.png)

---
## Dicas para revisores de MRs

<div class="columns">
  <div class="column">

- Se você não está revisando a MR de alguém, essa pessoa está travada.

* **IA**: Dilema do revisor (“Cognitive Debt”)

<!-- manter padrões anteriores e virar gargalo, ou aprovar no ritmo que o código chega e torcer para os testes peguem problemas que a revisão perdeu
-->

  </div>
  <div class="column">

![w:500 center](imagens/meme-mr-travada.png)

  </div>
</div>

---
## Dicas para revisores de MRs

<div class="columns">
  <div class="column">

- Não façam LGTM
- Sem approve da confiança

  </div>
  <div class="column">

![w:430 center](imagens/meme-lgtm.png)

  </div>
</div>

---
## Dicas para revisores de MRs

<div class="columns">
  <div class="column">

- Cuidado com o efeito manada
- Revisem, nem que seu review não "conte"

  
  </div>
  <div class="column">

![height:4in](imagens/elephant-herd.gif)

  </div>
</div>

<!--
Não é porque o senior e spec aprovou que voce nao pode negar e revisar com calma. "Só porque uma figura de autoridade aprovou, não significa que você deve ignorar seu próprio julgamento.” você deve também revisar as PRs dos sêniors/specs com igual critério. 

Não é só porque eles são mais experientes que não cometem erros
-->

---
<!-- _class: slide-secao -->

## O que quero que levem com vocês

---
## O que quero que levem com vocês

* Code review é um pair programming assíncrono ("diálogo")
* Parte da __sua__ tarefa
* Aumenta a qualidade do software
* __Oportunidade de aprendizado__

---
# Agradecimentos

<div class="columns">
  <div class="column">

Palestra do [André Girol de Code Review na Python Brasil 2021](https://www.youtube.com/watch?v=qgouvDvfz6k)

  </div>
  <div class="column">

![w:800](imagens/palestra-girol.png)

  </div>
</div>

---
# Agradecimentos

<div class="columns">
  <div class="column">

Post no blog do Osvaldo Santana - [Agilidade em tempos de IA](https://osantana.me/agilidade-em-tempos-de-ia/)

  </div>
  <div class="column">

![w:600](imagens/post-agilidade-tempos-ia.png)

  </div>
</div>

---
## Dúvidas?

<div class="columns">
  <div class="column">

Linkedin: /in/renan-asantos/
Telegram: @renan_asantos

![w:500 center](imagens/slide-encerramento.png)

  </div>
  <div class="column">

Slides no QRCode


![w:350 center](imagens/qrcode-slides.png)

  </div>
</div>


<!--

**Resumido (40min)**

1. Quem sou eu? (1min)
2. O que são PRs e Code Reviews? (3min)
3. Importância de code reviews (4min)
4. Code reviews na era da IA (3min)
5. Dicas para autores de uma PR (12min)
6. Dicas para revisores de PRs (12min)
7. Dúvidas (5min)

1. Quem sou eu? (conectar minha história com o tema, "Passei por projetos onde code review era um 'ritual de aprovação' sem sentido e outros onde era a chave para o crescimento do time. Hoje quero compartilhar o que aprendi nessa jornada.”)
2. O que são PRs e Code Reviews? (prefiro muito mais o termo do Gitlab MR, mas PR é mais popular)
    1. Pair Programming só que assíncrono, isso da benefícios e malefícios
    2. O que é Code Review? Parte da sua task, reducao de bugs, custos, troca de conhecimento
    3. O que não é? QA (n vai testar e2e), bala de prata (n da pra pegar todos os bugs)
3. Importância de code reviews
    1. Aumentar a qualidade do software
    2. diminuir o risco de dívidas técnicas
    3. oportunidade de aprendizado e trocas de conhecimentos (para ambos)
    4. Última barreira pré produção (Explicar o que é produção)
    5. Um bom code review pode indicar falhas no seu processo
        1. Complexidade: Quanto tempo em review? Quantos arquivos alterados? Ficou muito tempo porque o codigo tava grande e era pesaroso de revisar? Pode indicar que as tasks nao estao bem quebradas
        2. Precisão: Quantas alterações foram pedidas? A pessoa que fez nao entendeu bem a task? nao sabe muito bem como trabalhar naquele projeto?
        3. Necessidade: Depois de aprovada ficou parada? Era mesmo tao importante aquela alteracao?
    7. Memes de REVIEW REBELO, xkcd
4. Code Reviews na era de IA
5. Dicas para autores de uma PR:
    1. PRs PEQUENAS
    2. O primeiro revisor é sempre você (verifique os testes, se subiu em dev, se o CI ta passando, se não tem conflitos a serem resolvidos)
    3. Siga os padrões que o projeto tiver (line-lenght, code-style, etc etc), se tiver um linter, formatter, pre-commit, rode ele (CONTRIBUTING.md)
    4. Escreva uma descrição clara e bem exemplificada do que seu código altera, com imagens, vídeos, formatação boa, como testar. Documentação futura da funcionalidade
    10. Crie uma PR em draft, “erre rápido” para corrijir rápido, opinião rápida sobre a abordagem
    5. Discuta as sugestões de preferência nos comentários da própria PR para que todos vejam ou acompanhem e se não estiverem se entendendo, façam uma ligação.
    6. Se a sugestão que outra pessoa der for modificar muito o código ou não impactar negativamente, pergunte se pode abrir um ticket de dívida técnica linkando aquela sugestão
    7. Responda o quanto antes os comentários que as pessoas fizerem. Vira um bate bola rapido e fecha logo a mr
    8. Seja gentil, sempre responda um comentário, mesmo que com um emoji 🙂, não feche o comentário que alguém fez uma pergunta, a pessoa nao sabe se voce acatou, recusou a sugestao etc
    9. Não leve para o pessoal, você não é seu código
6. Dicas para quem vai revisar a PR
    0. Não façam LGTM (Look Good To Me), não façam approve da confianca, é algo para ser acordado entre todos do time
    1. Não sei como funciona em cada empresa, mas revisem, nem que seu review não “conte”
    2. Leia atentamente a descrição da PR, se houver. "O autor caprichou na descrição? Então use-a! Ela é seu guia para entender o contexto e o que testar.”
    3. Leia o card atrelado a ela, se houver (ali podem existir boas informações de negócio para te dar contexto)
    4. A solução é adequada ao projeto, em termos de design de código? Segue os code style?
    5. Existe over-engineering? Muita complexidade? Quem ler entenderá a solução no futuro? Lembrando do Zen do Python “Simple is better than complex”
    6. Começem pelos arquivos não do código fonte em si (modificação no pyproject ou requirements seja para libs ou configurações; README,)
    7. Sigam para os arquivos de testes automatizados, estão corretos e bem arquitetados?
    8. Ao ir para os arquivos de código…
    9. Vejam nomes de variáveis, estão claros? foo, bar, var, etc. Ao inves de um comentario explicando a variavel, poderia ela mesmo ter um nome explicativo (exemplo do cron)
    10. Tem algo que precisa ser atualizado na documentação? Mudou a forma de subir local e precisa atualizar o README? Alguma env foi modificada?
    11. Não vai dar pra fazer em todas, mas naquelas mais críticas, faça checkout da branch, rode no seu ambiente local, valide por si mesmo, mas não gaste muito tempo nisso
    12. Coloque sugestões de código e nao só de palavras, mande o trecho como sugestao pra pessoa, exemplo feature gitlab
    13. Explique sua sugestão de alteração da PR, coloque referências, exemplos etc
    14. Enalteça pontos interessantes, elogie códigos bons, comente se aprendeu algo novo
    17. Efeito manada: não é porque o senior e spec aprovou que voce nao pode negar e revisar com calma. "Só porque uma figura de autoridade aprovou, não significa que você deve ignorar seu próprio julgamento.” você deve também revisar as PRs dos sêniors/specs com igual critério. Não é só porque eles são mais experientes que não cometem erros
    18. Se você não está revisando uma PR de alguém, ela está travada por sua causa. Se não estiver extremamente focado em algo, se tiver acabado de sair de uma reunião e tem 30min até a próxima, via revisar
7. Referências
    1. Palestra Code Review do Andre Girol - https://www.youtube.com/watch?v=qgouvDvfz6k

-->