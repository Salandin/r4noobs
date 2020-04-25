<h1><b><i>4.6 Arrays</i></b></h1>
<p>Em quanto os vetores tem apenas uma dimenção e a matriz tem duas dimenções, um arrays tem n dimenções.</p>

<ul>
    <p>Para fazer um array, você vai usar os seguintes comandos:</p>
    <li><code>array()</code></li>
    <li><code>dim=c(x,y,z)</code></li>
    <li><code>dimname=list()</code></li>
</ul>
<p>O comando "<code>array()</code>" é a base do seu array, dentro do parenteses, você passa primeiro o valor que vai dentro das tabelas do array. Depois você passa o comando "<code>dim=c(x,y,z)</code>", e dentro dos parenteses você vai passar 3 valores, que eu representei por x,y,z, <b>x</b> é a quantidade de linhas, <b>y</b> é a quantidade de colunas e <b>z</b> a quantidade de matrizes. E você também pode passa o comando <code>dimname=list()</code> que vai ser sempre um lista e com ele é possivel nomear as linhas, colunas e tabelas respectivamente ao passar vetores dentro do parentese. Veja o exemplo:</p>

    > nomes<-c("Wesley","Rafael","Murilo")
    > semanas<-c(1,2,3,4)
    > mes<-c(1,2,3)
    > presenca<-c(TRUE,FALSE)

    > array1 <- array( presenca, dim = c(3,4,3), dimname=list(nomes,semanas,mes))
    > array1

    , , 1

               1     2     3     4
    Wesley  TRUE FALSE  TRUE FALSE
    Rafael FALSE  TRUE FALSE  TRUE
    Murilo  TRUE FALSE  TRUE FALSE

    , , 2

               1     2     3     4
    Wesley  TRUE FALSE  TRUE FALSE
    Rafael FALSE  TRUE FALSE  TRUE
    Murilo  TRUE FALSE  TRUE FALSE

    , , 3

               1     2     3     4
    Wesley  TRUE FALSE  TRUE FALSE
    Rafael FALSE  TRUE FALSE  TRUE
    Murilo  TRUE FALSE  TRUE FALSE

<p>Para acessar um valor você usa o seguinte comando:</p>

    > array1[2,4,3]
    [1] TRUE

<p>sendo o primeiro numero a linha, o segundo a coluna e o último a tabela.</p>