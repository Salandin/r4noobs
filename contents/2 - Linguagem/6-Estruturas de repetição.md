# 2.6 Estruturas de repetição

No r temos as estruturas de repetição `while` e `for` e como o proprio no diz eles servem para ter a repetição de algo, seja pra soma ou pra visulizão de dados.

```r
# While (enquanto)

# O while vai ficar repitindo o codigo enquando ele for verdadeiro
#Por exemplo, vamos definir a variavél 'i' com o valor 1 
#e vamos escrever um codigo que a cada repetição vai adicionar 1 e nos retornar o 1, ficaria assim:
i = 1

while(TRUE){
  i = i+ 1
  print(i)
}

#No console vai estar aparecendo o valor de i a cada vez que é somado 1
[1] 1
[1] 2
[1] 3
#...
[1] 49090943
[1] 49090944
#e assim por diante até forçar que o codigo pare de rodar

# For (Para)

#O for funciona de forma parecida com o while
# entretando, ele é mais utilizado quando você tem um lista com varios algoritimos 
#e quer os vizualizar ou somar um valor em cada item
#pra esse exemplo, vamos criar uma variavél com 90 valores

vari <-c(1:90)

#Para ver cada valor que tem na 'vari', a gente faz o seguinte codigo
for (i in vari){
    print(i)
}

#Que vai gerar o seguinte no console
[1] 1
[1] 2
[1] 3
[1] 4
[1] 5
#...
[1] 86
[1] 87
[1] 88
[1] 89
[1] 90
```

#### Break
Um problema do while é que ele vai estar rodando sempre que for verdadeiro, e as vezes ele sempre vai ser `TRUE`, então caso você só queira alguns valores e depois parar de rodar, a gente usa o `Break`

```r
i = 1

while(TRUE){
  i = i+ 1
  print(i)
  if (i == 90000){
    break
  }
}
```
Desta forma ele só vai rodar até o i ser igual a 90000