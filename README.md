# Calculadora Visual com Python
## Descrição
Este script Python implementa uma calculadora simples com uma interface gráfica do usuário (GUI) usando a biblioteca CustomTkinter. A calculadora suporta operações básicas, como adição, subtração, multiplicação e divisão.

## Como funciona
O programa define uma classe CalculatorApp que encapsula toda a funcionalidade da calculadora. A classe cria e gerencia uma janela de aplicativo e vários widgets, incluindo botões para números, operações e funções de controle (limpar e calcular), e uma entrada para exibir a expressão e o resultado.

Cada botão tem um comando associado que é executado quando o botão é pressionado. Os botões numéricos adicionam o número correspondente à expressão atual, os botões de operação definem a operação a ser realizada (substituindo qualquer operação existente no final da expressão) e os botões de controle limpam a expressão ou calculam o resultado.

O resultado é calculado usando a função eval do Python, que avalia a expressão como código Python. Isso significa que a expressão deve estar em um formato que o Python possa entender (por exemplo, 2+2 ou 3.14*10). Se a expressão não puder ser avaliada (por exemplo, devido a uma divisão por zero ou uma sintaxe incorreta), uma mensagem de erro será exibida.

## Como executar
Para executar este script em sua máquina, siga as etapas abaixo:

Certifique-se de ter Python instalado. Você pode baixar Python em https://www.python.org/downloads/. Este script foi escrito para Python 3 e pode não funcionar corretamente (ou não funcionar) em Python 2.

Instale a biblioteca CustomTkinter. Você pode fazer isso executando o comando pip install customtkinter em seu terminal ou prompt de comando. Se você tiver várias versões do Python instaladas, pode precisar usar pip3 em vez de pip.

Salve o script em um arquivo .py em seu computador. Por exemplo, você pode nomeá-lo calculator.py.

Execute o script usando Python. Você pode fazer isso abrindo um terminal ou prompt de comando, navegando até o diretório onde o arquivo .py está localizado e executando o comando python calculator.py (ou python3 calculator.py se você tiver várias versões do Python instaladas).

Se tudo estiver configurado corretamente, você deverá ver a janela da calculadora aparecer. Você pode usar a calculadora clicando nos botões com o mouse.