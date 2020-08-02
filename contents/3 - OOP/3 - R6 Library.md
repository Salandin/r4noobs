# 3.3 R6 Library

A biblioteca R6 é similhar ao Ref. Classes. Entretanto, o R6 é mais simples de se entender pois é baseado no sistema S3 e o RC é baseado no S4.

Para poder usar o R6, a gente tem que primeiro instalar a biblioteca, assim rodamos os seguintes codigos:

```{r}
#install.packages(R6)
library(R6)
```

Após instalarmos a biblioteca, já podemos definir as classes.

# Classes

Para definir um classe com essa biblioteca, usamos a função `R6Class`, primeiro passamos o nome da classe e depois passamos os atributos dentro de uma lista

Para definir os atributos, a gente pode passar pelo `public` ou pelo `private`

### Public

Usando o `public`, você passa uma lista com os atributos e funções, que poderam ser acessados fora da função. e para oassar o valor para o atributo dentro da função `ìnitialize`, fazemos o segunte: 

`function(atributo1 = algo) { self$atrbuto <- atributo1}`

```{r}
pessoa <- R6Class("pessoa",
                  public = list(
                  name = NULL,
                  idade = NULL,
                  initialize = function(name = NA, idade = NA){
                    self$name <- name
                    self$idade <- idade
                  }
                  ))
```

Para podermos passar os atributos, usamos o `$new()` depois do nome da classe

```{r}
carlos <- pessoa$new("Carlinhos da Guerra", 21)
```

```{r}
carlos$name
[1] "Carlinhos da Guerra"
 
carlos$idade
[1] 21

carlos
<pessoa>
  Public:
    clone: function (deep = FALSE) 
    idade: 21
    initialize: function (name = NA, idade = NA) 
    name: Carlinhos da Guerra
```

### Private

Usando o `private`, a gente passa os atributos e funções que __SÓ__ podem ser acessadas dentro da classe, e no lugar do `self$atri`, usamos o `private$atri`

```{r}
pessoa <- R6Class("pessoa",
                  public = list(
                  initialize = function(name = NA, idade = NA) {
                    private$name <- name
                    private$idade <- idade
                  }
                  ),
                  private = list(
                    name = NULL,
                    idade = NULL
                  ))
```

Ao visualizarmos temos o seguinte:

```{r}
carlos$name
NULL

carlos$idade
NULL

carlos
<pessoa>
  Public:
    clone: function (deep = FALSE) 
    initialize: function (name = NA, idade = NA) 
  Private:
    idade: 21
    name: Carlinhos da Guerra
```

# Metodos
Os metodos são funções que são definidas dentro da public list ou dentro da private list. com o R6, a gente tem um metodo obrigatório que é um `initialize`, é nela que passamos os valores dos atributos ou outros metodos que vão ser executados após a definição do objeto.

```{r}
pessoa <- R6Class("pessoa",
                  public = list(
                  initialize = function(name = NA, idade = NA){
                    private$name <- name
                    private$idade <- idade
                    self$apresen()
                  },
                  apresen = function () {
                    retorno <- paste('Opa, me chamo', private$name,'e tenho', self$idade,'anos')
                    print(retorno)
                  }
                  ),
                  private = list(
                    name = NULL,
                    idade = NULL
                  ))
```

Ao definirmos a classe, vamos ter o seguite retorno:

```{r}
carlos <- pessoa$new("Carlinhos da Guerra", 21)
[1] "Opa, me chamo Carlinhos da Guerra e tenho  anos"
```

# Herança
Herança é quando uma classe herda os atributos e metodos de outra. Para fazer isso com a R6 Library, a gente define o `inherit` passando o nome da função após definir o nome que vai herdar da seguinte forma `inherit = nome_classe1`.

```{r}
pessoa <- R6Class("pessoa",
                  private = list(
                  name = NULL,
                  idade = NULL))

# Nesse codigo, a gente definiu os atributos na primeira classe 
# e a segunda classe vai pegar os atributos e passar para os metodos.


pessoa_acao <- R6Class("acao",
                       inherit = pessoa,
                       public = list(
                       initialize = function (name = NA, idade = NA) {
                         private$name <- name
                         private$idade <- idade
                         self$apresen()
                       },
                       apresen = function () {
                         retorno <- paste('Opa, me chamo', private$name,'e tenho', private$idade,'anos')
                         print(retorno)
                       },
                       fala = function () {
                         retorno <- paste(private$name,'Disse: Paralelepipedo')
                         print(retorno)
                       },
                       bebendo = function () {
                         retorno <- paste(private$name,'Está bebendo um monster geladinho hmmmmmmmmm, uma delicia')
                         print(retorno)
                       }
                       ))
```

Para definir um objeto com uma classe com herança, a gente usa a classe que vai herdar.

```{r}
carlos <- pessoa_acao$new("Carlinhos da Guerra", 21)
[1] "Opa, me chamo Carlinhos da Guerra e tenho  anos"
```

OBS: para podermos visualizar os outros metodos, a gente faz o seguinte `objeto$nomeFuncao()`.

```{r}
carlos$fala()
[1] "Carlinhos da Guerra Disse: Paralelepipedo"

carlos$bebendo()
[1] "Carlinhos da Guerra Está bebendo um monster geladinho hmmmmmmmmm, uma delicia"
```
