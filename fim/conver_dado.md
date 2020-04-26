<h1><b><i>6.2 Conversão de Dados</i></b></h1>
<p>É possivel que em algum momento que você esteja mexendo com R, você terá que fazer a conversão de um tipo Integer para numeric, por exemplo. Para isso, usamos o "<code>as.TipoDeDadoQueVocêQuerFazerAConversão</code>", caso tenha ficado meio confuso, temos uma lista para as possíveis conversões que se pode fazer.</p>

<ul>
    <li><code>as.numeric()</code></li>
    <li><code>as.character()</code></li>
    <li><code>as.vector()</code></li>
    <li><code>as.matrix()</code></li>
    <li><code>as.data.frame()</code></li>
    <li><code>as.Date()</code></li>
    <li><code>as.factor()</code></li>
</ul>

<p>E para ver se realmente foi feita a conversão, usamos o "<code>class()</code>", como no exemplo</p>

    > matriz <- matrix(1:9, nrow=3, ncol=3)
    > matriz
         [,1] [,2] [,3]
    [1,]    1    4    7
    [2,]    2    5    8
    [3,]    3    6    9
    > class(matriz)
    [1] "matrix"

    > integer <- as.integer(matriz)
    > integer
    [1] 1 2 3 4 5 6 7 8 9
    > class(integer)
    [1] "integer"