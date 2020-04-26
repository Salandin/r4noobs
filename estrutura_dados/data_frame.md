<h1><b><i>5.7 Data Frame</i></b></h1>
<p>O Data Frame é uma estrutura de dados que se assemelha a uma tabela de um banco de dados, permitindo você adicionar diferentes tipos de dados nele. Ele é basica um conjunto de vetores de comprimento igual</p>
<p>Para montar um data frame, precisamos, primeiro ter os vetores já pronto</p>

    > participantes<-c("Rafael","Murilo","Otavio")
    > idade<-c(16,18,17)
    > dev<-c(TRUE,TRUE,FALSE)

<p>após isso usamos o comando "<code>data.frame()</code>"</p>

    > tabela<-data.frame(participantes, idade, dev)
    > tabela
      participantes idade   dev
    1        Rafael    16  TRUE
    2        Murilo    18  TRUE
    3        Otavio    17 FALSE    

<p>Para acessar algum item, usamos o seguinte comando:</p>
 
    > tabela[4,]
<p>Com esse mesmo comando, também pode se usado para adicionar alguns dados ao data frame, da seguinte forma:</p>

    > tabela[4,]<-c('Wesley',16,FALSE)
    > tabela
      participantes idade   dev
    1        Rafael    16  TRUE
    2        Murilo    18  TRUE
    3        Otavio    17 FALSE
    4        Wesley    16 FALSE

<p>É provavél que dê o seguinte erro: "<code>Error in `[<-.data.frame`(`*tmp*`, 4, , , value = list(as.character("Algo que você escreveu"),  : 
  unused argument (alist())</code>". Com isso use o comando: "<code>stringAsFactor=FALSE</code>", dessa forma:</p>

    > tabela<-data.frame(participantes, idade, dev,stringsAsFactors=FALSE) 
    
    > tabela[4,]<-c('Wesley','16','FALSE')
    
    > tabela
      participantes idade   dev
    1        Rafael    16  TRUE
    2        Murilo    18  TRUE
    3        Otavio    17 FALSE
    4        Wesley    16 FALSE
 
 
<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_dados/attach_detach_with.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/estrutura_dados/arrays.md">Anterior</a></h4>