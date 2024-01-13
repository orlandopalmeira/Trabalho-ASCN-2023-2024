<img src='EEUM_logo.png' width="30%"/>

<h3 align="center">Mestrado em Engenharia Informática <br> Trabalho prático de Computação Paralela <br> 2023/2024 </h3>

---
<h3 align="center"> Colaboradores &#129309 </h2>

<div align="center">

| Nome                           | Número  |
|--------------------------------|---------|
| Ana Rita Santos Poças          | PG53645 |
| João Pedro Vilas Boas Braga    | PG53951 |
| Orlando José da Cunha Palmeira | PG54123 |
| Miguel Silva Pinto             | PG54105 |
| Pedro Miguel Castilho Martins  | PG54146 |

</div>

### Nota: 18.6 / 20

<h3><i>Keywords</i></h3>
ASCN, Aplicações e Serviços de Computação em Nuvem, aplicacoes e servicos de computacao em nuvem, universidade do minho, uminho, miei, mei, engenharia informatica

<br>

# Comandos do trabalho

### Ligar os clusters e set-up do cluster kubernetes
```ansible-playbook gke-cluster-create.yml```

### Deploy da aplicação completa
```ansible-playbook laravelio-deploy.yml```

### Deploy da aplicação completa com um numero especifico de replicas do servidor aplicacional
```ansible-playbook laravelio-deploy.yml -e "l_reps=3"```

### Deploy da aplicação completa com um numero especifico de replicas do servidor aplicacional e sem HorizontalPodAutoscaler(HPA) - Tem De Ser Nesta Ordem!
```ansible-playbook laravelio-deploy.yml -e "l_reps=1" --skip-tags hpa```

### Deploy da aplicação mas sem ser feito o seeding da base de dados
```ansible-playbook laravelio-deploy.yml -e "seed_database=false"```

### Deploy da aplicação mas sem ser feito o seeding da base de dados e com um numero especifico de replicas do servidor aplicacional
```ansible-playbook laravelio-deploy.yml -e "seed_database=false l_reps=3"```

### Deploy da aplicação sem HorizontalPodAutoscaler(HPA)
```ansible-playbook laravelio-deploy.yml --skip-tags hpa```


### Comando de teste para verificar se o playbook está a funcionar
```ansible-playbook test-all.yml```

### Comando de teste para verificar se o playbook está a funcionar, após ter criado o cluster (não faz deploy nem undeploy da aplicação)
```ansible-playbook tests-only.yml```


### Undeploy completo da aplicação
```ansible-playbook laravelio-undeploy.yml```

### Undeploy da aplicação mas sem ser removido o PersistentVolumeClaim(PVC) para manter persistência dos dados
```ansible-playbook laravelio-undeploy.yml --skip-tags pvc```


### Desligar os clusters
```ansible-playbook gke-cluster-destroy.yml```



# Descrição dos playbooks

## gke-cluster-create.yml
Criação dos clusters GKE

## gke-cluster-destroy.yml
Eliminação dos clusters GKE

## laravelio-deploy.yml
Deploy da aplicação completa

## laravelio-undeploy.yml
Undeploy da aplicação completa

## reload-laravel.yml
Reload da aplicação Laravel, como mecanismo de manutenção da aplicação, sem apagar os seus dados

## test-all.yml
Testa o deployment de toda a aplicação, funcionalidades da aplicação, e por fim verifica o correto terminamento da aplicação

## tests-only.yml
Testa apenas as funcionalidades da aplicação, já com a aplicação a correr, sem executar o deploy nem o undeploy da aplicação

## gcp-create-vms.yml
Criação das VMS de carga

## test-load.yml
Testa a aplicação com um load testing, com um número de threads e de iterações por defeito, ou com um número de threads e de iterações especificado pelo utilizador, pressupondo a criação das VMS de carga

## gcp-import-dashboard.yml
Importa o dashboard JSON para o projeto definido



# Casos de uso do sistema

## Mostrar persistência dos dados
1. Deploy da aplicação:
    ```ansible-playbook laravelio-deploy.yml```

2. Fazer login na aplicação:
    Aceder ao endereço http://<app_ip>/login
    Com as credenciais:
    - username: testing
    - password: password

3. Criar uma nova thread no fórum:
    Aceder ao endereço http://<app_ip>/forum/create-thread

4. Undeploy da aplicação sem eliminar o pvc:
    ```ansible-playbook laravelio-undeploy.yml --skip-tags pvc```


5. Redeploy da aplicação sem fazer seeding da base de dados para não gerar conflitos:
    ```ansible-playbook laravelio-deploy.yml -e "seed_database=false"```

6. Verificar a thread criada anteriormente:
    Aceder ao endereço http://<app_ip>/forum

## Load testing
1. Criação das VMS e provisionamente (Java, Jmeter) para o load testing:
    ```ansible-playbook gcp-create-vms.yml```

2. Execução do load testing:
    ```ansible-playbook test-load.yml```
    Os resultados do load testing são guardados na diretoria "./results"

2.1. Execução do load testing com um número de threads e de iterações diferente do default:
    ```ansible-playbook test-load.yml -e "threads=10 iters=100 load_file=tests/load_forum.jmx"```


3. Remoção das VMS:
    Na execução do create-vms, clicar Ctrl+C + C para indicar a continuação da execução do playbook que elimina as VMS:
    
