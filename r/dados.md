<h1><b><i>3.2 Tipos de Dados</i></b></h1>
<p>Os tipos mais comuns são <i>character, numeric e interger</i>. E diferentes das outras linguagem, a declaração e a tipagem de dados é feito de forma automatica, ao atribuir a variável e os dados da mesma, automaticamente a variável é criada e sua classe é atribuida com forme o tipo de dado que você passa.</p>
<p>Para fazer essa atribuição, utilizamos os operadores: "<code><-</code>" ou "<code>=</code>".</p>
<p>veja o seguinte exemplo:</p>

    > vari <- 17
    > vari
    [1] 17
    > class(vari)
    [1] "numeric"

<p>Nesse exemplo, nós atribuimos um valor a varíavel "<code>vari</code>"
e verificamos a sua classe com o comando "<code>class()</code>".</p>


<p>Os dados do tipo Caracter é sempre representado entre aspas duplas <code>var <- "caracter"</code> ou aspas simples <code>var <- 'caracter'</code>, caso não tenha as aspas, vai dar um erro ao rodar o codigo</p>

<p>Os dados Integer são basicamente números inteiros, são definidos da seguinte forma:</p>

    > var <- 90L
<p>ou</p>
    
    > var <- as.integer(90)
   
<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/r/Coments.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/r/about_new.md">Anterior</a></h4><
