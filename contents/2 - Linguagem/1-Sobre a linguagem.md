# 2.1 Sobre a Linguagem

R é uma linguagem multi-paradigma mas com foco no paradigma funcional, mais voltada para o uso de estudo estatísticos e visualização de dados.

Foi criado originalmente por Ross Ihaka e por Robert Gentleman no departamento de Estatística da Universidade de Auckland, Nova Zelândia. Atualmente é mantido por uma comunidade de colaboradores voluntários que contribuem com código fonte da linguagem e com a expansão de funcionalidades por bibliotecas.

## Extensão

Na liguagem R, temos dois tipos de extensão de arquivo principais, o .r e o .rdata, entretanto existem outras extensões de arquivos que você pode achar no RStudio.

#### arquivo_com_extensão.r 
Um arquivo com extensão .r, é o seu script, o codigo que vai ser execultado pelo software que você estiver usando.

#### arquivo.rdata
No arquivo com essa extensão, vai estar salva a sua area de trabalho, que é os objetos, variáveis, tabelas entre outras coisas que você usou na última vez que usou o R.

#### arquivo.rproj
É o projeto que foi criado no RStudio, nele vai ter informações do projeto que são usadas para personalizar o comportamento do RStudio, como carregar configurações do RStudio; Também é usado para ver se deve carregar o arquivo .rhistory e o arquvio .rdata.

#### arquivo.rhistory
Neste arquivos vai ter o histórico de comandos digitados, é bem semelhante ao .bash_history, já que ambos permitem por exemplo, usar a setinha para cima pra acessa um comada digitado anteriormente de forma mais rapida.

#### arquivo.rd
Nos arquivos .rd são gravados os objetos R, eles são basicamente o "coração" de um pacote r.

#### arquivo.rmd
É um arquivo que contem a sintaxe do markdown com blocos de código R que podem ser escritos e executados e eles vem com suporte paras os arquivos Html, Pdf e Word.

#### arquivo.rnw
É um arquivo que usar o _**Sweave**_ que é uma funcionalidade do R que permite  ter comandos, saídas computacionais e/ou gráficos incluídos automaticamente no texto, sem a necessidade de fazer tal inclusão manualmente e passo a passo. Este macanismo também permite que o texto seja agilmente e automáticamente atualizado para qualquer mudança ou inclusão de dados e/ou nas análises, acelerando muito o processo de edição de textos.


## Código fonte

O codigo fonte do R está dispónivel sobre a licença GNU GNL, isso quer dizer que você tem a liberdade de usar o R para:

- Executa-lo para qualquer propósito.
- Estudar como que ele funciona e adaptá-lo ás suas necessidades.
- Redistribuir cópias de modo que vai ajudar o próximo.
- Aperfeiçoar o programa e liberar os seus aperfeiçoamentos, de modo que toda a comunidade beneficie deles.

Há um conjunto básico de pacotes que vem com o R já na sua instalação e muitos outros estão disponíveis na rede de distribuição do R (CRAN).