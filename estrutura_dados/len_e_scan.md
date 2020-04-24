<h1><b><i>4.3 Length e Scan</i></b></h1>

<h3><b>- Length</b></h3>
<p>A função <i>Length</i> vai retornar o tamanho do seu vetor, servindo para mudar o valor de algum dado do seu vetor. como no exemplo:</p>

    > vetor<-c(1,4,6,8,5,3,2,5,7,6,4,7,8,3,55,76,34,78,23,87)
    > length(vetor)
    [1] 20 
    
    > vetor[20]<-NA
    > vetor
    [1]  1  4  6  8  5  3  2  5  7  6  4  7  8  3 55 76 34 78 23 NA

<h3><b>- Scan</b></h3>

<p>O Scan seria o "<code>input()</code>" de outras liguagens, em outras palavras, é usando esse comando que você irá conseguir digitar os dados, como no exemplo:</p>

<ul>
    
    > meuVetor = scan()

<li>Ao apertar enter, você pode ir digitando os dados, usando espaço para separar.</li>

    > meuVetor = scan()
    1: 1 2 3 9 5
    6: 2 5 6
    
<li>Após digitar os valores, aperte enter sem nenhum valor, será considerado que já entrou todos os valores. com isso aparecerá isso:</li>
    
    Read 8 items

<li>Com isso ao verificar o seu vetor, esse é o resultado</li>

    > meuVetor
    [1] 1 2 3 9 5 2 5 6

</ul>

<p>Normalmente o "<code>scan()</code>" espera dados do tipo numérico, então, para passar outros tipos, você usa dentro do parentese o "<code>what=""</code>" como por exemplo:</p>

    > meuVetor = scan(what="character")

<p>ou</p>'

    >meuVetor = scan(what="boolean")