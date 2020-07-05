# 2.4 Operadores Logícos

Assim como em outras linguagens, eles são usados nas estruturas de condição e em alguns casos para deixar o codigo mais simples.

```r
# '==' igual a 
if a == 1{
    print('É igual')
}
# Esse codigo vai ver se o valor de a é igual a 1, caso for, vai printar 'É igual'.


# '!=' diferente de
if a != 1{
    print('Não é igual')
}
# Esse codigo vai ver se o valor de a é diferente de 1.


# '|' ou
if a == 1 | a != 0 {
    print('É diferente de 0 ou igual a 1')
}
# Esse codigo vai ver se o valor de a é igual a 1 ou diferente de 0.


# '&' e
if a == 1 & a != 0 {
    print('É diferente de 0 e igual a 1')
}
# Esse codigo vai ver se o valor de a é igual a 1 e diferente de 0.


# '>' e '>=' maior que e maior ou igual que
if a >= 1 & a > 0 {
    print('É maior ou igual a 1 e maior que 0')
}
#Esse codigo vai ver se o valor de a é maior ou igual a 1 e maior de 0.

# '<' e '<=' menor que e menor ou igual que
if a >= 1 & a > 0 {
    print('É menor ou igual a 1 e menor que 0')
}
#Esse codigo vai ver se o valor de a é maior ou igual a 1 e maior de 0.
```