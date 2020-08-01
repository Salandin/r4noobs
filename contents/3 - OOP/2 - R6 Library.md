
```{r}
#install.packages(R6)
library(R6)
```
# Classes
```{r}
pessoa <- R6Class("Pessoa",
                  public = list(
                  name = NULL,
                  idade = NULL,
                  initialize = function(name = NA, idade = NA){
                    self$name <- name
                    self$idade <- idade
                    self$apresen()
                  }
                  ))
```

#Metodos

```{r}
pessoa <- R6Class("Pessoa",
                  public = list(
                  name = NULL,
                  idade = NULL,
                  initialize = function(name = NA, idade = NA){
                    self$name <- name
                    self$idade <- idade
                    self$apresen()
                  },
                  apresen = function () {
                    retorno <- paste('Opa, me chamo', self$name,'e tenho', self$idade,'anos')
                    print(retorno)
                  }
                  ))
```
# Herança
```{r}
pessoa <- R6Class("Pessoa",
                  public = list(
                  name = NULL,
                  idade = NULL))
pessoa_acao <- R6Class("Acao",
                       inherit = pessoa,
                       public = list(
                       initialize = function (name = NA, idade = NA) {
                         self$name <- name
                         self$idade <- idade
                       },
                       apresen = function () {
                         retorno <- paste('Opa, me chamo', self$name,'e tenho', self$idade,'anos')
                         print(retorno)
                       },
                       fala = function () {
                         retorno <- paste(self$name,'Disse: Paralelepipedo')
                         print(retorno)
                       },
                       bebendo = function () {
                         retorno <- paste(self$name,'Está bebendo um monster geladinho hmmmmmmmmm, uma delicia')
                         print(retorno)
                       }
                       ))
```
```{r}
carlos <- pessoa_acao$new("Carlinhos da Guerra", 21)
carlos$apresen()
carlos$fala()
carlos$bebendo()
```
