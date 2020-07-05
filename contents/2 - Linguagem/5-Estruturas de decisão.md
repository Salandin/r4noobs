# 2.5 Estruturas de decisão

As estruturas de decisão são basicamente um 'se tal coisa tiver o valor 1, faz x ação, caso ter o valor 2, faz ação y e caso for 3, faz ação z', pra entender melhor, eu vou passar o exemplo e comentar sobre.


#### 'if' se
A gente já viu o 'if' topico passado, mas agora a gente vai entender melhor o que que ele faz.

```r
#vamos definir um variavel 'r' com o valor de '4noobs'
r <- '4noobs'

#agora vamos escrever o seguinte, se o valor de r for igual a '4noobs', printa 'É igual'.
#basicamente igual ao que a gente viu anteriormente
if (r == '4noobs'){
    print('É igual')
}
#como a gente deu o valor '4noobs' pra r, vai ser printado no console 'É igual'.
[1] 'É igual'
```

#### 'else' caso não for
O 'else' vai fazer uma ação caso o if estiver errado.

```r
# Agora a nossa vaiável r, vai receber o valor 2
r <- 2

#e vamos ver se é r igual a 1
if (r == 1){
    print('É igual a 1')
}
#como que r é igual a 2, não será retornado nada
#mas caso você precise que retorne algo caso estaja errado, você usa o else
if (r == 1){
    print('É igual a 1')
} else {
    print('É igual a outro valor')
}
# ao rodar o codigo
[1] "é igual a outro valor"
```

#### 'else if'
A diferença do 'else if' pro 'else' é que nele você usar pra verificar outra coisa.

```r
#Aqui a gente vai continuar com o exemplo anterior
r <- 2

#e vamos verificar se ele é igual a dois antes do else, com isso o codigo ficaria assim
if (r == 1){
    print('É igual a 1')
} else if (r == 2){
    print('É igual a 2')
}else {
    print('É igual a outro valor')
}
# ao rodar o codigo, temos no console
[1] "É igual a 2"
```
