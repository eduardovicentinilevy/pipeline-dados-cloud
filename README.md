Pipeline de Processamento de Dados Financeiros na Nuvem
Este projeto consiste em um sistema de automação para extração, tratamento e armazenamento de dados de câmbio. O objetivo principal foi aplicar conceitos de Engenharia de Dados utilizando Python, banco de dados relacional e infraestrutura em nuvem no Google Cloud Platform.

O que o projeto resolve
A coleta manual de dados financeiros é ineficiente e sujeita a erros. Este sistema automatiza o processo de ponta a ponta, garantindo que as cotações do Dólar e do Euro sejam capturadas, limpas e armazenadas diariamente de forma padronizada.

Estrutura técnica
O desenvolvimento foi dividido em quatro pilares principais:

Extração de Dados: Uso da biblioteca requests para consumir dados em tempo real de uma API de cotações financeiras.

Tratamento com Pandas: Os dados passam por uma camada de processamento onde as informações são limpas e os tipos de dados são convertidos para o formato numérico correto para análise.

Persistência em SQL: Implementação de armazenamento usando SQLite, permitindo consultas históricas eficientes e integridade dos dados.

Implantação e Automação: O script foi implantado em uma máquina virtual (Compute Engine) no Google Cloud, com agendamento via Cron Job para funcionamento autônomo.

Competências Aplicadas
Engenharia de Dados: Construção de um fluxo completo de ETL (Extract, Transform, Load).

Administração de Sistemas: Configuração de ambiente Linux via terminal SSH e gestão de dependências no servidor.

Nuvem: Operação de instâncias e recursos dentro do ecossistema Google Cloud.

Controle de Versão: Gestão de código e implantação segura utilizando Git e GitHub.
