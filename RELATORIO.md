# Trabalho 2 — Escalonamento de CPU

**Disciplina:** Sistemas Operacionais — ADS  
**Integrante:** Ana Keliny Romão de Souza  
**Linguagem:** Python 3

**Link do GitHub:** COLE_AQUI_O_LINK_DO_GITHUB

## 1. Objetivo

O trabalho implementa quatro algoritmos de escalonamento de CPU: FCFS, SJF, Prioridade e Round Robin. Foram utilizados os três cenários fornecidos no enunciado. Todos os processos chegam no instante 0 e o Round Robin utiliza quantum igual a 2.

## 2. Fórmulas

Como todos os processos chegam no instante 0:

- Turnaround = instante em que o processo terminou.
- Espera = Turnaround − tempo de CPU.
- Espera média = soma dos tempos de espera ÷ quantidade de processos.

## 3. Resultados

| Cenário | FCFS | SJF | Prioridade | Round Robin |
|---|---:|---:|---:|---:|
| 1 | 2,33 | 1,33 | 2,33 | 2,67 |
| 2 | 6,00 | 1,33 | 6,00 | 3,00 |
| 3 | 3,33 | 2,33 | 2,33 | 4,00 |

## 4. Conferência manual

### Cenário 1

Dados: P1=3, P2=1, P3=2.

**FCFS:** P1 0–3; P2 3–4; P3 4–6.  
Esperas: 0, 3, 4.  
Média = (0+3+4)/3 = **2,33**.

**SJF:** P2 0–1; P3 1–3; P1 3–6.  
Esperas: 0, 1, 3.  
Média = (0+1+3)/3 = **1,33**.

**Prioridade:** todas as prioridades são iguais. A ordem permanece P1, P2, P3.  
Esperas: 0, 3, 4.  
Média = **2,33**.

**Round Robin (quantum 2):** P1 0–2; P2 2–3; P3 3–5; P1 5–6.  
Turnaround: P1=6, P2=3, P3=5.  
Espera: P1=3, P2=2, P3=3.  
Média = (3+2+3)/3 = **2,67**.

**Regra escolhida:** SJF, porque apresentou a menor espera média, **1,33**.

### Cenário 2

Dados: P1=8, P2=2, P3=1.

**FCFS:** P1 0–8; P2 8–10; P3 10–11.  
Esperas: 0, 8, 10.  
Média = **6,00**.

**SJF:** P3 0–1; P2 1–3; P1 3–11.  
Esperas: P3=0, P2=1, P1=3.  
Média = **1,33**.

**Prioridade:** as prioridades são iguais, então a ordem permanece P1, P2, P3.  
Espera média = **6,00**.

**Round Robin (quantum 2):** P1 0–2; P2 2–4; P3 4–5; P1 5–7; P1 7–9; P1 9–11.  
Turnaround: P1=11, P2=4, P3=5.  
Espera: P1=3, P2=2, P3=4.  
Média = **3,00**.

**Regra escolhida:** SJF, porque apresentou a menor espera média, **1,33**.

### Cenário 3

Dados: P1=4/prioridade 3, P2=2/prioridade 1, P3=3/prioridade 2.

**FCFS:** P1 0–4; P2 4–6; P3 6–9.  
Espera média = (0+4+6)/3 = **3,33**.

**SJF:** P2 0–2; P3 2–5; P1 5–9.  
Esperas: 0, 2, 5.  
Média = **2,33**.

**Prioridade:** P2 0–2; P3 2–5; P1 5–9.  
Esperas: 0, 2, 5.  
Média = **2,33**.

**Round Robin (quantum 2):** P1 0–2; P2 2–4; P3 4–6; P1 6–8; P3 8–9.  
Turnaround: P1=8, P2=4, P3=9.  
Espera: P1=4, P2=2, P3=6.  
Média = **4,00**.

**Regra escolhida:** Prioridade, quando a prioridade dos processos for importante, pois P2 tinha a maior prioridade e foi atendido primeiro. A espera média foi **2,33**.

## 5. Respostas da análise

**No cenário 1, qual algoritmo teve menor espera média? Houve empate?**  
O SJF teve a menor espera média, **1,33**. Não houve empate.

**No cenário 2, o processo longo fez os curtos esperarem mais em qual algoritmo? Usem um resultado para mostrar isso.**  
No FCFS, o processo longo P1 executou primeiro por 8 unidades. Assim, P2 esperou **8** e P3 esperou **10**. A espera média foi **6,00**.

**No cenário 3, qual processo tinha a maior prioridade? Ele foi atendido primeiro no algoritmo de prioridade?**  
P2 tinha a maior prioridade, pois sua prioridade era 1. Sim, ele foi atendido primeiro.

**O que o Round Robin fez de diferente ao dividir a CPU em várias vezes?**  
O Round Robin dividiu a CPU em fatias de 2 unidades. Um processo pode executar uma parte, voltar para a fila e depois executar novamente. Isso evita que um único processo ocupe a CPU por todo o seu tempo de uma vez.

## 6. Relação com o Trabalho 1

A atividade mostra como o sistema operacional organiza o uso da CPU entre processos. Isso se relaciona ao Trabalho 1, em que foram observados processos no Linux e a utilização da CPU. As diferentes regras de escalonamento alteram a ordem de atendimento e o tempo que cada processo espera pela CPU.

## 7. Conferência com o programa

Foi feita uma conferência manual de um cenário para cada algoritmo, conforme solicitado no enunciado. Os resultados calculados manualmente coincidiram com os resultados produzidos pelo programa.

## 8. Uso de IA

Foi utilizado auxílio de inteligência artificial para apoiar a organização do código, dos cálculos e do relatório. O funcionamento do programa e os resultados foram conferidos.
