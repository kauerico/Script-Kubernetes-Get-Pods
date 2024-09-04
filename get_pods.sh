#!/bin/bash

# Verifica se o número correto de argumentos foi fornecido
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <namespace> <cluster>"
    exit 1
fi

# Atribui os argumentos às variáveis
NAMESPACE=$1
CLUSTER=$2

# Executa o comando kubectl get pods com os parâmetros fornecidos
kubectl get pods --namespace "$NAMESPACE" --context "$CLUSTER"
