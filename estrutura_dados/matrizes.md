<h1><b><i>5.4 Matrizes</i></b></h1>
<p>Em R, as matrizes é uma estrutura de dados homogêneal, ou seja, deve ter os mesmos tipos de dados. Para fazer uma matriz, usamos o comando "<code>matrix()</code>", dentro do parentese, usamos os camandos:"<code> data=</code>","<code> nrow=</code>","<code> ncol=</code>".</p>


    > M <- matrix(data=1:12, nrow=4, ncol=4)
    > M
         [,1] [,2] [,3] [,4]
    [1,]    1    5    9    1
    [2,]    2    6   10    2
    [3,]    3    7   11    3
    [4,]    4    8   12    4

<p>Você também pode usar um vetor no data, deste que todos os dados sejam do mesmo tipo de dado (sempre verefique se as colunas e as linhas multiplicadas é igual a quantidade de dados do seu vetor, e caso não saiba o tamanho de seu vetor use o "<code>length()</code>" ).</p>

    > Vet <- c(1,2,3,4,5,6,7,8,0,9,7,4,2,4,5)
    > length(Vet)
    [1] 15 
    > matrize = matrix(data= Vet, nrow = 3, ncol = 5)
    > matrize
         [,1] [,2] [,3] [,4] [,5]
    [1,]    1    4    7    9    2
    [2,]    2    5    8    7    4
    [3,]    3    6    0    4    5

<p>Por padrão, as matrizes são organizadas por colunas, mas você pode organizalas por linha usando o comando: "<code>byrow=TRUE</code>"</p>

    > matrize = matrix(data= 1:15, nrow = 3, ncol = 5)
    > matrize
         [,1] [,2] [,3] [,4] [,5]
    [1,]    1    4    7   10   13
    [2,]    2    5    8   11   14
    [3,]    3    6    9   12   15
    

    > matrize = matrix(data= 1:15, nrow = 3, ncol = 5, byrow = TRUE)
    > matrize
         [,1] [,2] [,3] [,4] [,5]
    [1,]    1    2    3    4    5
    [2,]    6    7    8    9   10
    [3,]   11   12   13   14   15

<ul>
<p>também há duas caracteristicas das matrizes que são:</p>
<li>Se você não definir o "<code>data=</code>", todos os valores da matrizes serão NA</li>

    > M2 = matrix(nrow=6, ncol=9)
    > M2
         [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8] [,9]
    [1,]   NA   NA   NA   NA   NA   NA   NA   NA   NA
    [2,]   NA   NA   NA   NA   NA   NA   NA   NA   NA
    [3,]   NA   NA   NA   NA   NA   NA   NA   NA   NA
    [4,]   NA   NA   NA   NA   NA   NA   NA   NA   NA
    [5,]   NA   NA   NA   NA   NA   NA   NA   NA   NA
    [6,]   NA   NA   NA   NA   NA   NA   NA   NA   NA

<li>E você pode usar apenas um valor na sua matrix</li>

    > M3 = matrix(data= "He4rtDevelopers" ,nrow=3, ncol=3) 
    > M3 
         [,1]              [,2]              [,3]             
    [1,] "He4rtDevelopers" "He4rtDevelopers" "He4rtDevelopers"
    [2,] "He4rtDevelopers" "He4rtDevelopers" "He4rtDevelopers"
    [3,] "He4rtDevelopers" "He4rtDevelopers" "He4rtDevelopers"

</ul>
<p>Para acessa um dado da matrix, é usado o seguinte comando:</p>

    > M3[2,3]
    [1] "He4rtDevelopers"

<p>Com o primeiro valor sendo a linha e o segundo valor a coluna</p>

<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_dados/list.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_dados/len_e_scan.md">Anterior</a></h4>