# Pesquisa de Satisfação

Script simples em Python para coletar e contabilizar avaliações de satisfação de um serviço via linha de comando.

## Como funciona

O programa pergunta repetidamente como o usuário avalia o serviço, aceitando três respostas válidas: `excelente`, `bom` ou `ruim`. A cada resposta válida, um contador correspondente é incrementado. O usuário pode digitar `sair` a qualquer momento para encerrar a coleta e ver o resumo final.

Entradas inválidas não interrompem o programa — ele avisa o usuário e pede uma nova resposta.

## Requisitos

- Python 3.x (não usa bibliotecas externas)

## Como executar

```bash
python pesquisa_satisfacao.py
```

## Exemplo de uso

```
Como você avalia nosso serviço? (excelente/bom/ruim) ou digite 'sair' para encerrar: excelente
Como você avalia nosso serviço? (excelente/bom/ruim) ou digite 'sair' para encerrar: bom
Como você avalia nosso serviço? (excelente/bom/ruim) ou digite 'sair' para encerrar: talvez
Resposta inválida. Por favor, digite 'excelente', 'bom', 'ruim' ou 'sair'.
Como você avalia nosso serviço? (excelente/bom/ruim) ou digite 'sair' para encerrar: sair

Resultados da pesquisa de satisfação:
Excelente: 1
Bom: 1
Ruim: 0
```

## Estrutura do código

- **Contadores**: três variáveis (`excelente`, `bom`, `ruim`) que armazenam a quantidade de cada tipo de resposta.
- **Loop principal**: um `while True` que roda até o usuário digitar `sair`.
- **Validação**: respostas fora do conjunto esperado geram uma mensagem de erro e uma nova tentativa, sem encerrar o programa.
- **Resultados**: ao final, o total de cada categoria é exibido no terminal.

## Possíveis melhorias futuras

- Ignorar espaços em branco extras na entrada (`.strip()`).
- Calcular percentuais além dos totais absolutos.
- Salvar os resultados em um arquivo (CSV ou JSON).
- Adicionar tratamento para entrada vazia.