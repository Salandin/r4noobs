# 1.2 - Pré-requisitos

## Conhecimentos Necessários

Para que você possa compreender tranquilamente neste curso, é necessário que você tenha conhecimentos básicos em qualquer outra linguagem, por exemplo:

  * PHP
  * Javascript
  * Ruby
  * Python

Qualquer uma destas linguagens acima, já é o suficiente. Mas claro, se você souber outra linguagem que não esteja listada, também será bem útil para prosseguirmos.

## Instalação

Para começarmos, precisamos instalar o **R** e **RStudio** em seu ambiente. Para isso, existem algumas formas de se instalar ambas as linguagens.

### R

#### Windows

No Windows conseguimos instalar via [web](https://cran.r-project.org/bin/windows/base/) ou via [chocolatey](https://chocolatey.org/).

Para instalar via Chocolatey, você pode executar via PowerShell ou pelo Prompt de Comando.

**Lembrando que ambos precisam executar como administrador**

```batch
choco install r.project
```

#### macOS

No Mac conseguimos instalar via conseguimos instalar via [web](https://cran.r-project.org/bin/macosx/) ou Homebrew.

Para instalar via Homebrew, você executará em ser terminal:

```sh
brew install r
```

Para instalar via Macports, você executará em ser terminal:

```sh
sudo port install R
```

#### Unix

 * Ubuntu/Linuxmint:

   Para instalar no Ubuntu ou Linuxmint, é necessário adicionar o repositório do R na sua lista de pacotes do Aptitude.

   Para isso, é necessário executar alguns comandos no seu terminal:

   ```sh
   # Instalar o R
   sudo apt-get update
   sudo apt-get install r-base
   ```

 * Arch Linux:

   Para instalar no Arch Linux é necessário executar apenas um comando no seu terminal:

   ```sh
   pacman -S r
   ```

 * openSUSE:

   Para instalar no openSUSE é necessário adicionar o repositório do R na sua lista de pacotes.

   Para isso, é necessário executar alguns comandos no seu terminal:

   ```sh
   VERSION=$(grep "^PRETTY_NAME" /etc/os-release | tr " " "_" | sed -e 's/PRETTY_NAME=//' | sed -e 's/"//g')
   zypper addrepo -f http://download.opensuse.org/repositories/devel\:/languages\:/R\:/patched/$VERSION/ R-base

   zypper install R-base R-base-devel
   ```

### RStudio

#### Windows

No Windows conseguimos instalar via [web](https://rstudio.com/products/rstudio/download/#download) ou via [chocolatey](https://chocolatey.org/).

Para instalar via Chocolatey, você pode executar via PowerShell ou pelo Prompt de Comando.

**Lembrando que ambos precisam executar como administrador**

```batch
choco install r.studio
```

#### macOS

No Mac conseguimos instalar via [web](https://rstudio.com/products/rstudio/download/#download) ou Homebrew.

Para instalar via Homebrew, você executará em ser terminal:

```sh
# Primeiro, precisamos instalar o Cask
brew install caskroom/cask/brew-cask

# Instalar o RStudio
brew cask install --appdir=/Applications rstudio
```

#### Unix

Nos sistemas Unix conseguimos instalar apenas via [web](https://rstudio.com/products/rstudio/download/#download)


**OBS.:** Para que tudo funcione corretamente, é estritamente necessário que R esteja instalado em seu computador.

Para testar a instalação, você pode executar este comando em seu terminal:

```
→ C:\Users\aleDsz› R --version
R version 3.6.0 (2019-04-26) -- "Planting of a Tree"
Copyright (C) 2019 The R Foundation for Statistical Computing
Platform: x86_64-w64-mingw32/x64 (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under the terms of the
GNU General Public License versions 2 or 3.
For more information about these matters see
https://www.gnu.org/licenses/.
```

Para continuar, é válido frisar que o curso foi feito em cima do R na versão **3.6.0**