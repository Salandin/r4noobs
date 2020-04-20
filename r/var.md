<h1><b><i>3.5 Variáveis</i></b></h1>

<p>Nesse topíco, eu estarei falando do retorno que uma variável pode dar, já que variável tudo o que você seta o valor com "<code> <- </code>"ou com"<code> = </code>".</p>

<p>Na linguagem R, uma variável é tratada como um vetror de uma única posição. É por esse motivo que você tem um retorno desse tipo:</p>


    > vari <- 17
    > vari
    [1] 17

<p>Você também o tipo com o comando "<code>is.</code>" que vai retornar um valor bolleano, True/False. Como você pode ver no exemplo abaixo:</p>

    x <- 123L
    y <- "He4rt Developers"
    z <- 32

    is.integer(x)
    [1]TRUE
    is.integer(y)
    [1]FALSE

    is.character(y)
    [1]TRUE
    is.character(z)
    [1]FALSE

    is.numeric(z)
    [1]TRUE
    is.numeric(x)
    [1]FALSE

    