<h1><b><i>4.3 Repeat, While & For</i></b></h1>

<h3><b>Repeat</b></h3>
<p>Bem, agora o nosso "a" vai ser 0</p>

    > a = 0

<p>Certo, agora vamos fazer o seguinte, vamos fazer um codigo que vai se repitir até que a seja igual a 8</p>

    > repeat {
    + if (a == 8) break else
    + a<-a+1
    + print(a)}
    
    [1] 1
    [1] 2
    [1] 3
    [1] 4
    [1] 5
    [1] 6
    [1] 7
    [1] 8

<p>Bem, explicando o codigo, o "<code>repeat</code>" vai ficar repitindo o codigo que você escreveu dentro das chaves. Nesse caso, primeiro ele vai ver se a é igual a 8, depois ele vai fazer atribuir a "a" o seu valor anterior mais 1, e depois vai imprimir o "a". Com isso, ele vai ficar repitindo o codigo até que o "a" seja 8, aí ele execulta o "<code>break</code>" que veremos na proxima aula, mas você já deve saber a sua função</p>

<h3><b>While</b></h3>

<p>Basicamente, é a mesma coisa que o "<code>repeat</code>", entretanto, ele é mais "limpo" e você não vai precisar passar o "<code>break</code>", seja o mesmo exemplo acima, mas usando "<code>while</code>"</p>

    > while (a < 8) {
    + a<-a+1;
    + print(a) }
    [1] 1
    [1] 2
    [1] 3
    [1] 4
    [1] 5
    [1] 6
    [1] 7
    [1] 8

<h3><b>For</b></h3>

<p>para explicar o "<code>for</code>", vamos passar sequencia no nosso querido "a"</p>

    > a <-c(1:19)
    > a
    [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19

<p>Então, o "<code>for</code>" faz o seguinte, para cada item em tal coisa, faça algo. De novo, é possivél que você esteja começando a duvidar da minha capacidade em explicar logica e que também não entendeu nada, mas não se preocupa que é simples, veja o exemplo:</p>

    > for(i in a) print(i + 1)
    [1] 2
    [1] 3
    [1] 4
    [1] 5
    [1] 6
    [1] 7
    [1] 8
    [1] 9
    [1] 10
    [1] 11
    [1] 12
    [1] 13
    [1] 14
    [1] 15
    [1] 16
    [1] 17
    [1] 18
    [1] 19
    [1] 20

<p>Agora eu acho mais facíl de entender, então, para cada item em a, imprima ele adicionando 1 ao valor original, ou "<code>for(i in a) print(i + 1)</code>".</p>

<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_logica/break_next.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_logica/if_else.md">Anterior</a></h4>