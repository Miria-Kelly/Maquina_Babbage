# Simulação da Máquina Analítica de Babbage

Este projeto foi desenvolvido durante o **primeiro período do curso de Ciência da Computação** como uma forma de representar, de forma simples, o funcionamento da **máquina analítica** criada por **Charles Babbage** na década de 1830 — considerada um dos primeiros modelos teóricos de computador da história.

---

## Como funciona

A entrada de dados é feita através de um arquivo chamado `cartao.in`, que simula cartões perfurados, onde:
- A letra **X** representa o bit `1`
- A letra **O** representa o bit `0`

Cada linha desse arquivo contém **16 dígitos** que controlam o funcionamento da máquina.

---

### Estrutura dos 16 dígitos

- **4 primeiros dígitos** → Instrução a ser executada  
- **8 dígitos seguintes** → Indicam o endereço de memória  
- **4 últimos dígitos** → Valor binário a ser inserido

> Exemplo: `XOXO OOXO XXOX OOXX` (exemplo fictício)

---

## ▶️ Como usar

1. **Edite o arquivo `cartao.in`**, colocando as instruções conforme a estrutura acima.
2. **Execute o arquivo principal**:
   ```bash
   python maquina.py
o resultado sairá no arquivo "cartão.out"

instrução dos 16 digitos do "cartao.in"
<img width="757" height="674" alt="image" src="https://github.com/user-attachments/assets/a1af96e0-19b2-4dcd-9667-b73913262f68" />


