# 8 - Lidando com erros

Três tipos de condições integradas são fornecidas na linguagem R, que podem ser lançadas como exceções do código.

#### Erros

São os mais graves, geralmente encerram a função ou interrompem a execução do codigo.

#### Avisos

Os avisos nôs dizem se algum erro ocorre durante a execução de uma função, também é capaz de lidar parcialmente com o problema.

#### Mensagens

Elas são usadas para informar sobre alguns problemas leves ao usuário.

------------------------------------------------------------------------

Essas três condições tem as suas respectivas funções (`stop`, `warning` && `message`), que podem ser invocadas para aumentar a condição dada.

##### `stop()` exemplo:

```r
for(i in 0:10){
  if(i != 5){
    print(paste("i é igual a", i))
  } else if (i == 5){
    stop("i é igual a 5, logo vou parar, obrigado.")
  }
}

#[1] "i é igual a 0"
#[1] "i é igual a 1"
#[1] "i é igual a 2"
#[1] "i é igual a 3"
#[1] "i é igual a 4"
#Error: i é igual a 5, logo vou parar, obrigado.
```

##### `warning()` exemplo:

```r
for(i in 0:10){
  if(i != 5){
    warning(paste("considere isso um aviso. i=",i))
  }else if (i == 5){
    stop("i é igual a 5, logo vou parar, obrigado.")
  }
}

#Warning: considere isso um aviso. i= 0
#Warning: considere isso um aviso. i= 1
#Warning: considere isso um aviso. i= 2
#Warning: considere isso um aviso. i= 3
#Warning: considere isso um aviso. i= 4
#Error: i é igual a 5, logo vou parar, obrigado.
```

##### `message()` exemplo:

```r
mensagemDoDia = "Bom dia, essa é a mensagem do dia"

message(mensagemDoDia)
print(mensagemDoDia)

#Bom dia, essa é a mensagem do dia
#[1] "Bom dia, essa é a mensagem do dia"
```

------------------------------------------------------------------------

Para esse exemplo, passamos a função `ONumeroEPar` do arquivo passado

```r
funcao_pra_quebrar <- function(num){
  if (num%%2 == 0){
    paste("O número", num, "é par")
  } else if (!num%%2 == 0){
    paste("O número", num, "é impar")  
  }
}
```

Talvez você repare que não vai rolar passar uma `char` ou uma `string` como parametro, logo vai dar erro

```r
funcao_pra_quebrar("uma string qualquer")
# Error in num%%2 : non-numeric argument to binary operator
```

Assim, é possivel substituir a mensagem de erro pradão pra outra onde fica mais facil compreender o erro. Usamos a função \``tryCatch` para implementar um codigo que é executado quando um erro é gerado.

```r
funcao_pra_quebrar <- function(num){
  tryCatch(
    error = function(cnd){
        cat("ERRO: olha, isso não é um int, confere ai ::: valor passado = '",num,"'")
      },
    if (num%%2 == 0){
      paste("O número", num, "é par")
    } else if (!num%%2 == 0){
      paste("O número", num, "é impar")  
    } 
  )
}

funcao_pra_quebrar("eita, vai quebrar o codigo")
# ERRO: olha, isso não é um int, confere ai ::: valor passado = ' eita, vai quebrar o codigo '
```

é claro, nem sempre é bom ser tão amigavel nos retornos do erro, em alguns casos é melhor ser mais direto

```r
funcao_pra_quebrar <- function(num){
  tryCatch(
    error = function(cnd){
        cat("ERRO: não é um int, não é possivel executar a função::: valor passado = '",num,"'")
      },
    if (num%%2 == 0){
      paste("O número", num, "é par")
    } else if (!num%%2 == 0){
      paste("O número", num, "é impar")  
    } 
  )
}

funcao_pra_quebrar("eita, vai quebrar o codigo")
# ERRO: não é um int, não é possivel executar a função::: valor passado = ' eita, vai quebrar o codigo '
```
