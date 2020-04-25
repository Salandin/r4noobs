<h1><b><i>4.8 Attach, Detach & With</i></b></h1>

<h3><b>Attach</b></h3>
    <p>Se fizermos um Data Frame com as variavéis dentro do comando <code>data.frame()</code>, como o exemplo abaixo:</p>

    > fata<-data.frame(part = c("a","b","c")
    + , id = c(1,5,7)
    + , dev = c(TRUE,FALSE,TRUE)
    + )
    
    > fata
      part id   dev
    1    a  1  TRUE
    2    b  5 FALSE
    3    c  7  TRUE
<p>Se quisermos pesquisar algum dos vetores dela, não será possivél, vai um erro falando que não existe esse objeto, com isso, usamos a função "<code>attach()</code>", que tornará possivél essa pesquisa

<h3><b>Detach</b></h3>
<p>De forma muito simplificada, ao usar essa função, ela vai reverter a mudanção feita pela função "<code>attach()</code>"</p>
<h3><b>With</b></h3>

<p>Em teoria, o <code>with()</code> tem função semelhante do <code>attach()</code>, entretanto, ele não torna possivél a busca, mas sim a utilização de uma função, com por exemplo:</p>

    > with(fata,sum(id))
    [1] 13