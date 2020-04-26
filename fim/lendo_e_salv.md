<h1><b><i>6.5 Lendo & Salvando Dados</i></b></h1>

<h3><b>Salvando</b></h3>

<p>Vamos supor que você fez essa matriz, que chamaremos "alprazolam"</p>

    > alprazolam = matrix(1:9000, nrow = 3000, ncol = 3000)

<p>E que você quer salvar ele,seja pra backup ou pra mandar pra alguém dar um olhada, você vai fazer o seguinte:</p>

    > save(alprazolam,"alprazolam.rdata")

<p>E o seu dado foi salvo, parabéns.</p>

<h3><b>Lendo o dado</b></h3>

<p>Então meu camarada, se você estiver em outro pc e quer trabalhar com a sua matriz de 9000 itens, você faz o seguinte: Primeiro veja onde que o r está pegando os dados, que provavélmente é a mesma da onde você tirou o seu arquivo no seu computador, mas caso você tenha esquecido, use o comando:</p>

    > getwd()

 <p>Que vai te retornar o local, e nesse local que ele te passar, você coloca o seu arquivo e faz o seguinte:</p>

    > load("alprazolam.RData")

<p>E pronto, é só fazer o que quiser na sua matrix.</p>

<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/fim/agrad.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/fim/import_dados.md">Anterior</a></h4>