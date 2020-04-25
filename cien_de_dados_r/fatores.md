<h1><b><i>5.2 Fatores</i></b></h1>

<p>É um tipo de dado usados para armazenar variáveis categóricas, que podem ser categóricas ou continuas, mas calma que algo mais caótico está por vir (ou não), bem, as unicas diferenças entre as variáveis categóricas e as variáveis continuas é que as categoricas estão "presas" em um número limitado de catégoria.</p>

<p>Para fazer um fator usamos a função:"<code>factor()</code>" que irá nos retornar os "Níveis de fatores" de seu vetor como por exemplo:</p>

    > bin<-c(0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,0)
    > binf<-factor(bin)
    > binf
    [1] 0 1 1 1 0 0 0 1 0 0 1 1 0 0 1 1 1 0 
    Levels: 0 1
<p>O exemplo acima tem dois Factor Levels (0 e 1), sendo variável categórica.</p>
