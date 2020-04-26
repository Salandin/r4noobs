<h1><b><i>4.2 If, Else & Else if</i></b></h1>

<h3><b>If</b></h3>

<p>O "<code>If</code>" é basicamente o "se algo for", a gente vai usar o "<code>If</code>" para ver se tal coisa realmente é tal coisa, meio confuso, não? Para explicar melhor, vamos fazer uma variavél "a" sendo igual a 1.</p>

    > a = 1

<p>Certo, coisa simples, agora, vamos fazer um codigo que imprima "Top" se a for igual a 1, é aí que entra o "<code>if</code>", pois a gente vai fazer isso:</p>

    > if (a==1) print("Top")
    [1] "top"

<h3><b>Else</b></h3>

<p>Ele seria um "se não", como assim? Você pode perguntar, então, vamos fazer com que agora a variável "a" seja igual a 2</p>

    > a = 2

<p>Ok, agora vamos fazer o seguinte, vamos verificar se a é igual a 1 ou não,caso for, imprime de novo o "top", caso contrario vai imprimir "Joaquim".</p>

    > if (a==1) {
    + print("top")
    + } else { print("Joaquim")
    + }

<p>Como que "a" não é 1, ele vai imprimir "Joaquim"</p>

    [1] "Joaquim"

<h3><b>Else if</b></h3>

<p>Ele é basicamente um "<code>else</code>" que pode verificar outra condição, veja o exemplo:</p>
<p>Agora o nosso "a" é 3, e nós vamos verificar se é menor ou maior que 6</p>

    > a = 3 
    > if (a > 6){
    + print("talvez sim")
    + } else if (a < 6){
    + print("Talvez não")
    + }
    [1] "Talvez não"
 
<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_logica/repeat_for_while.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_logica/seção_sobre.md">Anterior</a></h4>