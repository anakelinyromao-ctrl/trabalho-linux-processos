# Trabalho 2 — Escalonamento de CPU

**Disciplina:** Sistemas Operacionais  
**Curso:** ADS  
**Integrante:** Ana Keliny Romão de Souza  
**Linguagem:** Python 3

## Objetivo

Implementar e comparar quatro algoritmos de escalonamento de CPU:

- FCFS (First Come, First Served)
- SJF (Shortest Job First)
- Prioridade
- Round Robin, com quantum 2

Todos os processos chegam no instante 0, conforme o enunciado.

## Como executar

1. Instale o Python 3.
2. Abra o terminal na pasta do projeto.
3. Execute:

```bash
python trabalho_escalonamento_cpu.py
```

O programa mostra, para cada cenário, a sequência de execução, o tempo de espera, o turnaround e a média do tempo de espera.

## Dados utilizados

### Cenário 1 — Processos curtos
P1 = 3, P2 = 1, P3 = 2. Prioridades: 1, 1, 1.

### Cenário 2 — Curtos e longos
P1 = 8, P2 = 2, P3 = 1. Prioridades: 1, 1, 1.

### Cenário 3 — Prioridades diferentes
P1 = 4 (prioridade 3), P2 = 2 (prioridade 1), P3 = 3 (prioridade 2).

No algoritmo de Prioridade, o menor número representa a maior prioridade.

## Resultados das médias

| Cenário | FCFS | SJF | Prioridade | Round Robin |
|---|---:|---:|---:|---:|
| 1 | 2,33 | 1,33 | 2,33 | 2,67 |
| 2 | 6,00 | 1,33 | 6,00 | 3,00 |
| 3 | 3,33 | 2,33 | 2,33 | 4,00 |

## Conferência

Os cálculos manuais apresentados no relatório foram comparados com a saída do programa. Os resultados coincidiram.

## Arquivos

- `trabalho_escalonamento_cpu.py` — código-fonte.
- `README.md` — instruções e resumo.
- `RELATORIO.md` — relatório com resultados, conferência manual e análise.
- `RELATORIO.pdf` — versão em PDF para entrega.

## Git

Cole aqui o link do repositório GitHub antes de entregar:

`COLE_AQUI_O_LINK_DO_GITHUB`

> Observação: o trabalho foi desenvolvido com auxílio de IA, conforme permitido no enunciado. O código e os resultados foram conferidos.
