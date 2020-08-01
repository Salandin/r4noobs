# 3.1 Reference Class

# Classe

```{r}
Remedio <- setRefClass("remedio",
                       fields = list(formula = "character",
                                     nome.comercial = "character",
                                     dosagem = "numeric"))
```

# Metodos

```{r}
Remedio <- setRefClass("remedio",
                       fields = list(formula = "character",
                                     nome.comercial = "character",
                                     dosagem = "numeric"),
                       methods = list(retorna_nome = function(x) {
                         returno <- paste('O Remedio', nome.comercial,'tem a formula', formula,'e a dosegem de',dosagem ,'mg')
                         print(returno)
                       }
                       ))
```

# Herança

```{r}
remedio <- setRefClass("remedio",
                       fields = list(formula = "character",
                                     nome.comercial = "character",
                                     dosagem = "numeric"))
farmacia <- setRefClass("farmacia",
                       fields = list(receita = "logical"),
                       contains="remedio",
                       methods = list(retorna_nome = function() {
                         returno <- paste('O Remedio', nome.comercial,'tem a formula', formula,'e a dosegem de',dosagem ,'mg')
                         print(returno)
                       },
                       pergunta_receita = function(receita = T) {
                         print('Tem receita?')
                         if (receita) {
                           fala1 <- paste('Isso e uma receita de bolo, nao de', formula,'. Volte mais tarde')
                           print(fala1)
                         }else{
                            print('Você precisa da receita')
                         }
                       }))

```
```{r}
alpraz <- farmacia(formula = "Alprazolam", nome.comercial = "Frontal", dosagem = 2, receita=T)
alpraz$formula
alpraz$nome.comercial
alpraz$dosagem
alpraz$retorna_nome()
alpraz$pergunta_receita()
```