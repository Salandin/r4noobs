<h1><b><i>6.4 Importando Dados</i></b></h1>
<h3><b>RStudio</b></h3>
<p>Pra importar dados no R pelo RStudio é muito simples, é só ir em <b>"Import data"</b>, selecionar o tipo de dado que quer e procurar pelas suas pastas.</p>
<img src="https://cdn.discordapp.com/attachments/695812124282322968/704069456296411157/unknown-42.png" heigth="150" width="550">

<h3><b>R Console</b></h3>
<p>Mas se você estiver usando a proprio console do R, a situação é outra, você vai usar um "<code>read.TipoDeArquivoQueVocêQuer</code>", como os citados abaixo:</p>

<ul>
    <li>read.table()</li>
    <li>read.csv()</li>
    <li>read.xlsx()</li>
    <li>readLines()</li>
</ul>

<p>Também tem outra questão que é se o seu arquivo estiver no desktop o caminho dele será "C:\Users\Nome\Desktop", isso no windowns vai dar um erro, então trocamos as contra-barras por barras, ficando assim: "C:/User/Nome/Desktop"<p>

<h4><i>Xlsx</i></h4>
<p>Para poder importar um dado Exel, primeiro você vai ter que instalar ele usando o comando: "<code>install.packages("xlsx")</code>"  e pois o <code>library("xlsx")</code>, após isso segue a normal com o "<code>read.xlsx()</code>"</p>

<h4>Url<h4>

<p>Para fazem a importação de algo da internet, a gente tem que usar o "<code>url()</code>", como no exemplo:</p>

    > conexao <- url("https://heartdevs.com")
    > linhas_pagina <- readLines(conexao)
    > print(head(linhas_pagina))
    [1] "<!DOCTYPE html>"                                                               
    [2] "<html lang=\"pt-br\">"                                                         
    [3] "  <head>"                                                                      
    [4] "    <meta charset=\"utf-8\" />"                                                
    [5] "    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\" />"               
    [6] "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />"

<h4 align="Right"><a href="https://github.com/SaLandini/r4noobs/blob/master/fim/lendo_e_salv.md">Proximo</a></h4>
<h4 align="Center"><a href="https://github.com/SaLandini/r4noobs">Voltar ao git</a></h4>
<h4><a href="https://github.com/SaLandini/r4noobs/blob/master/fim/pack.md">Anterior</a></h4>