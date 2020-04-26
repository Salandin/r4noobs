<h1><b><i>5.2 Vetores</i></b></h1>
<p>Os vetores permitem guardar um conjunto de dados do mesmo tipo, você faz a atribuição de um vetor usando "<code>c()</code>" e cada elemento é separado por vírgulas, veja o exemplo:</p>

    > vetNum<-c(1, 5, 8, 4, 7)
    > vetBool<-c(True, False, True)
    > vetInter<-c(12L, 23L, 90L)
    > vetNum
    [1] 1 5 8 4 7
    > vetBool
    [1] TRUE FALSE TRUE
    > vetInter 
    [1] 12 23 90

<p>É possível ver apenas um desses dados escrevendo o nome do vetor e colocando o a posição do dado dentro de colchetes.</p>

    > vetTest<-c(1,4,2,7,9,5)
    > vetTest[1]
    [1] 1
    > vetTest[4]
    [1] 7
    > vetTest[6]
    [1] 5
    
<p>Caso você tenha 20 elementos num vetor, e coloque "<code>vetor[22]</code>" ou "<code>vector[34]</code>" no terminal, será retornado o valor "<code>NA</code>"</p>

    > vetTeste<-c(0,1,2,3,4,5,6,7,8,9)
    > vetTeste[11]
    [1] NA
    
<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_dados/len_e_scan.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_dados/sobre.md">Anterior</a></h4>