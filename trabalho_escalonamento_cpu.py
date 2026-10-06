# Trabalho 2 - Escalonamento de CPU
# Sistemas Operacionais - ADS
# Integrante: Ana Keliny Romão de Souza

CENARIOS = {
    1: [
        {"nome": "P1", "tempo": 3, "prioridade": 1},
        {"nome": "P2", "tempo": 1, "prioridade": 1},
        {"nome": "P3", "tempo": 2, "prioridade": 1},
    ],
    2: [
        {"nome": "P1", "tempo": 8, "prioridade": 1},
        {"nome": "P2", "tempo": 2, "prioridade": 1},
        {"nome": "P3", "tempo": 1, "prioridade": 1},
    ],
    3: [
        {"nome": "P1", "tempo": 4, "prioridade": 3},
        {"nome": "P2", "tempo": 2, "prioridade": 1},
        {"nome": "P3", "tempo": 3, "prioridade": 2},
    ],
}


def mostrar_resultado(nome_algoritmo, processos, ordem, termino):
    print(f"\n=== {nome_algoritmo} ===")
    print("Sequência:", " -> ".join(
        f'{nome}({inicio}-{fim})' for nome, inicio, fim in ordem
    ))
    print("Processo | Espera | Turnaround")

    espera_total = 0

    for processo in processos:
        nome = processo["nome"]
        espera = termino[nome] - processo["tempo"]
        espera_total += espera
        print(f"{nome} | {espera} | {termino[nome]}")

    media = espera_total / len(processos)
    print(f"Tempo médio de espera: {media:.2f}")


def fcfs(processos):
    tempo_atual = 0
    termino = {}
    ordem = []

    for processo in processos:
        inicio = tempo_atual
        tempo_atual += processo["tempo"]
        termino[processo["nome"]] = tempo_atual
        ordem.append((processo["nome"], inicio, tempo_atual))

    mostrar_resultado("FCFS", processos, ordem, termino)


def sjf(processos):
    lista = sorted(processos, key=lambda p: p["tempo"])
    tempo_atual = 0
    termino = {}
    ordem = []

    for processo in lista:
        inicio = tempo_atual
        tempo_atual += processo["tempo"]
        termino[processo["nome"]] = tempo_atual
        ordem.append((processo["nome"], inicio, tempo_atual))

    mostrar_resultado("SJF", processos, ordem, termino)


def prioridade(processos):
    # Neste trabalho, menor número significa maior prioridade.
    lista = sorted(processos, key=lambda p: p["prioridade"])
    tempo_atual = 0
    termino = {}
    ordem = []

    for processo in lista:
        inicio = tempo_atual
        tempo_atual += processo["tempo"]
        termino[processo["nome"]] = tempo_atual
        ordem.append((processo["nome"], inicio, tempo_atual))

    mostrar_resultado("PRIORIDADE", processos, ordem, termino)


def round_robin(processos, quantum=2):
    fila = [
        {"nome": p["nome"], "restante": p["tempo"], "tempo": p["tempo"]}
        for p in processos
    ]

    tempo_atual = 0
    termino = {}
    ordem = []

    while fila:
        processo = fila.pop(0)

        inicio = tempo_atual
        execucao = min(quantum, processo["restante"])
        tempo_atual += execucao
        processo["restante"] -= execucao

        ordem.append((processo["nome"], inicio, tempo_atual))

        if processo["restante"] > 0:
            fila.append(processo)
        else:
            termino[processo["nome"]] = tempo_atual

    mostrar_resultado("ROUND ROBIN (quantum=2)", processos, ordem, termino)


def executar_cenario(numero, processos):
    print("\n" + "=" * 50)
    print(f"CENÁRIO {numero}")
    print("=" * 50)

    print("Processos:")
    for processo in processos:
        print(
            f'{processo["nome"]} - Tempo: {processo["tempo"]} '
            f'- Prioridade: {processo["prioridade"]}'
        )

    fcfs(processos)
    sjf(processos)
    prioridade(processos)
    round_robin(processos, quantum=2)


if __name__ == "__main__":
    for numero, processos in CENARIOS.items():
        executar_cenario(numero, processos)
