<h1><b><i>4.5 Criando Funções</i></b></h1>
<p>Funções são um bloco de codigo tem o principal objetivo a reútilização, um exemplo é o "<code>print()</code>". Para criar uma função, você segue essa estrutura:</p>

    nome = function (argumento1 , … , argumento n) {

      Comandos da função

    }

<p>Vamos usar como exemplo, uma função que vai verificar se algo é par ou não</p>

    > par = function(x) {
    + if (x%%2==0) {
    + return("Sim")
    + }else if (!x%%2==0){
    + return("Não")
    + }
    + }
<p>Essa função pode parecer meio abstrata e caótica de inicio, mas mais daqui a pouco eu mostro uma forma mais facíl de fazer ela, mas nesse caso, eu posso usar ela pra explicar mais coisa.</p>

<p>Bem, por padrão a função vai retonar a ultima linha do codigo da função, entretando, quando a gente estiver usando pra verificar algo usando "<code>if</code>" não vai funcionar esse esquema, nisso a gente usa o "<code>return()</code>" e dentro do parentese você passa o que quer que ele retorne.</p>

<p>Também vemos o "!" que basicamente vai fazer com que o "<code>if</code>" verifique o contrario do que foi passado.</p>

    > par(9)
    [1] "Não"
    > par(2)
    [1] "Sim"

<p>E a forma mais simples de fazer essa função é:</p>

    > par = function(x) {
    + x%%2==0
    + }
    
    > par(9)
    [1] FALSE
    > par(2)
    [1] TRUE

<p>Ele vai basicamente verificar se x é modulo de 2, caso seja, ele retorna "<code>TRUE</code>, caso não seja, retorna "<code>FALSE</code>"</p>