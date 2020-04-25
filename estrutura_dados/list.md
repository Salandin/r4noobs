<h1><b><i>4.5 Listas</i></b></h1>
<p>A Lista é uma estrutura de dados meio peculiar, já que pode conter uma matriz ou até mesmo outra lista dentro dela. Toda lista é atribuida usando o comando "<code>list()</code>" e cada dado é retornado com um "[[x]]", sendo o x  a posição do dado</p>

    > vetor<-c("a","s","f","h","j","k","i")
    > matriz<-matrix(data=1:10, nrow=5, ncol=5)
    > lista<-list(vetor, matriz)
    > lista

    [[1]]
    [1] "a" "s" "f" "h" "j" "k" "i"

    [[2]]
         [,1] [,2] [,3] [,4] [,5]
    [1,]    1    6    1    6    1
    [2,]    2    7    2    7    2
    [3,]    3    8    3    8    3
    [4,]    4    9    4    9    4
    [5,]    5   10    5   10    5

<p>Para acessar um item da lista, você usa o comando: </p>

    > lista[[1]][6]
    [1] "k"
    
    > lista[[1]][3]
    [1] "f"
    
    > lista[[2]][2,3]
    [1] 2
    
    > lista[[2]][3,3]
    [1] 3