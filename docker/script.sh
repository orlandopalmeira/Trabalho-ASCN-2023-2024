#!/bin/bash

if [ "$seed_db" = "true" ]; then
    echo "Com seed..."; 

    while true; do
        # Executa o comando php artisan migrate --seed
        php artisan migrate --seed
        # Verifica o status de saída do comando
        if [ $? -eq 0 ]; then
            # Se o comando for bem-sucedido, sai do loop
            echo "Migrate executado com sucesso."
            break
        else
            # Se o comando falhar, exibe uma mensagem e tenta novamente após um intervalo
            echo "Erro. A tentar de novo..."
            sleep 5  # Intervalo de 5 segundos antes de tentar novamente
        fi
    done
fi

npm run build
php artisan serve --host=0.0.0.0
