# 7 - Funções em R

Funções são blocos de codigos que executam certas tarefas que normalmente precisam ser usados varias vezes, assim, para não ter que repetir esses codigos elas são agrupadas na função. Dando um nome à ela, será possivel chamar a função varias vezes.

Temos as funções nativas do R, como `print()`, `matrix()`, entre outros.

------------------------------------------------------------------------

> A função matrix(), cria uma matriz, nesse caso uma matriz 3x3, de valores de 1 a 9

```r
a <- matrix(1:9, ncol=3, nrow=3)
###      [,1] [,2] [,3]
###[1,]    1    4    7
###[2,]    2    5    8
###[3,]    3    6    9
```

------------------------------------------------------------------------

> A função print() retorna no console determinado valor, nesse caso o item na coluna 3 e na linha 3 da matrix "a"

```r
print(a[3,3])
### [1] 9
```

------------------------------------------------------------------------

Nesse caso, vamos falar sobre funções que o proprio usuário irá criar. Para isso, usamos o `function(_parametros_){_codigo_}`, onde passamos os parametros dentro do parenteses, e o que que a função vai fazer dentro das chaves.

------------------------------------------------------------------------

> Essa função iria verificar se o \`num\` é um numero par ou impar.

```r
function(num){
  num%%2 == 0
}
```

Entretanto, não definimos a função, logo não é possivel usa-lá.

Para definir-lá, faremos o seguinte:

```r
ONumeroEPar <- function(num){
  num%%2 == 0
}
```

assim, é possivel usar a função

```r
ONumeroEPar(10)
#[1] TRUE
```

> *** No R, ele já retorna o valor da ultima linha, no caso a cima `TRUE`, mas você pode usar o `return` pra terminar a função, assim qualquer valor produzido na função depois do `return` será ignorado.

Caso queira você também pode deixar as funções mais completas, adicionando funcionalidades ou deixando o seu retorno mais bonitinho, como por exemplo:

```r
ONumeroEPar <- function(num){
  if (num%%2 == 0){
    paste("O número", num, "é par")
  } else if (!num%%2 == 0){
    paste("O número", num, "é impar")  
  }
}

ONumeroEPar(2)
ONumeroEPar(1)
# [1] "O número 2 é par"
# [1] "O número 1 é impar"
```
