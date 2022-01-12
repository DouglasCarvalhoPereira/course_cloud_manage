# GERENCIAMENTO DE CLOUD GOOGLE


Gerencimamento de configurarções com o objetivo de atender demandas em escala.

Puppet, diferente da linguagem Python que é declarativa ou seja, precisamos escrever o passao a passo da ação que queremos executar. O Puppet dizemos o "ESTADO" queremos alcançar, tornando a linguagem Puppet DSL muito mais rápio de fácil de aprender.

Puppet DSL inclui:

1. Variaveis
    - Puppet Facts, São as variáveis que representam as caracteristicas do sistemas.

2. Condicionais
3. Funcções

## Puppet

Padrão atual para gerenciamento de configurações.  


#CONFIGURANDO UMA MAQUINA VIRTUAL

1 - https://console.cloud.google.com/

2 -  Criar ou Selecionar um Projeto

3 - No menu lateral esquerdo cliquemos em "Computer Engine"

4 -  Em seguida "VM instances"

5 -  Clicamos em "Create" ou "Criar"

6 - Agora selecionamos as configurações da máquina.

    1. Nome
    2. Região e Zona
    3. Tipo de Máquina
    4. Disco de Inicialização entre outras opções.

    Obs:. Ao terminar as configurações da VM, os comandos que devem ser usados na linha de comando para criar uma máquina identica ou "Disk Image" são gerados em um arquivo logo abaixo. Ideal que seja salvo para criação de máquinas futuras.


7 - 