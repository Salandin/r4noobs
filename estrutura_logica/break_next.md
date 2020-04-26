<h1><b><i>4.4 Break & Next</i></b></h1>

<h3><b>Break</b></h3>

<p>Então, como você pode ter pensado, o "<code>break</code>" serve para quebra um codigo e para de executar o mesmo, e como exemplo, eu vou usar o mesmo do repeat.</p>

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

<p>Como vocês podem ver, de novo, quando o a ficou igual a 8, ele "quebrou", caso contrario, iria continuar a repitindo o codigo até que você desligasse o pc.</p>

<h3><b>Next</b></h3>

<p>O "<code>next</code>" é um caso meio estranho, já que a função dele é fazer com que o codigo seja execultado mais uma vez, e de qualquer forma, o codigo vai ser excultado novamente até que se acabe a linha daquele codigo, bem de qualquer forma, veja o exemplo:</p>

    > a <- 1:19
    
    > for (i in a) {
    + if ( i == 3) {
    + next
    + }
    + print(i)
    + }