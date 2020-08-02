# 3.1 Reference Class

Reference Class é um dos 3 sistemas usado para Programação Orientada a Objetos.
No caso do sistema RC, ele é o mais parecido com as que temos em outras linguagens como em Python, Java ou em C++ por exemplo. E diferentemente dos sistemas S3 e S4,
os metodos pertencem a classe invés de terem funções genéricas.

# Classe
As classes é o que define as caracteristicas do objeto. para fazer isso usamos a função `setRefClass`, nela, é passada primeiro o nome da classe, depois os campos e entre outros.

No exemplo a baixo, a gente atribui a variavel `Remedio` como Classe `"remedio"`
e nos `fields` os atributos da classe.

```{r}
remedio <- setRefClass("remedio", #nome do metodo
                       fields = list(formula = "character",
                                     nome.comercial = "character",
                                     dosagem = "numeric")) 

#no fields é passado as variavéis e os tipos das variaveis.
#lembrando que é passado dentro da função list()
```

# Metodos
Metodos são basicamente funções que o seu objeto pode fazer. Para definir um metodo a gente passa uma lista com funções dentro desta forma:
`methods = list(nome_funcao = function() {sua funcao})`. Como no exemplo em que a gente vai definir a função `retorna_remedio()`. 

```{r}
remedio <- setRefClass("remedio",
                       fields = list(formula = "character",
                                     nome.comercial = "character",
                                     dosagem = "numeric"),
                       methods = list(retorna_remedio = function(x) {
                         retorno <- paste('O Remedio', nome.comercial,'tem a formula', formula,'e a dosegem de',dosagem ,'mg')
                         print(retorno)
                       }
                       ))
```

### Visualização dos atributos do objeto
Em R a gente define um objeto da seguinte forma:

```{r}
alpraz <- remedio(formula = "Alprazolam", nome.comercial = "Frontal", dosagem = 2)
```

Após isso, caso queiramos ver um atributo ou metodo, a gente faz da seguinte forma

```{r}
alpraz$formula
[1] "Alprazolam"

alpraz$nome.comercial
[1] "Frontal"

alpraz$dosagem
[1] 2

alpraz$retorna_nome() #quando é um metodo colocamos os parenteses na frente já que é uma função
[1] "O Remedio Frontal tem a formula Alprazolam e a dosegem de 2 mg"
```

# Herança
Herança é quando uma classe herda os atributos/metodos de uma outra. Fazemos essa herança usando a função `contains` e nela passamos o nome da classe que ela vai herdar `contains = "classe_primaria"`.

Nesse exemplo, a gente vai fazer os seguinte: deixar a classe `"remedio"` só com os atributos e a nova classe `"farmacia"` com os metodos. Alem disso, vamos adicionar mais um atributo e uma metodo novo.

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

Nesse casos para verificar os atributos/metodos, a gente atribuiu usando a classe `"farmacia"` em vez da `"remedio"`

```{r}
alpraz <- farmacia(formula = "Alprazolam", nome.comercial = "Frontal", dosagem = 2, receita=T)
```

```{r}

alpraz$formula
[1] "Alprazolam"

alpraz$nome.comercial
[1] "Frontal"

alpraz$dosagem
[1] 2

alpraz$retorna_nome()
[1] "O Remedio Frontal tem a formula Alprazolam e a dosegem de 2 mg"

alpraz$pergunta_receita()
[1] "Tem receita?"
[1] "Isso e uma receita de bolo, nao de Alprazolam . Volte mais tarde"
```