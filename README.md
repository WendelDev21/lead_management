# API de Gerenciamento de Leads

Esta é uma API simples de gerenciamento de leads desenvolvida com **Django** e **Django REST Framework**. A API permite realizar operações básicas de CRUD (criar, ler, atualizar e excluir) em uma lista de leads.

## Funcionalidades

- **Cadastro de Leads:** Adicione leads com informações como nome, e-mail, telefone e mensagem.
- **Edição de Leads:** Atualize os detalhes dos leads existentes.
- **Exclusão de Leads:** Remova leads que não são mais relevantes.
- **Listagem de Leads:** Visualize todos os leads cadastrados de forma organizada.
- **Documentação Automatizada:** Interface interativa de documentação via Swagger.

## Instalação

1. Clone o repositório:

    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Rode as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

4. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Rotas

Aqui estão as rotas disponíveis na API:

- **GET** `/api/leads/`  
  Retorna a lista de todos os leads cadastrados.
  
- **POST** `/api/leads/`  
  Cria um novo lead. Exemplo de payload:
  ```json
  {
    "name": "Nome do Lead",
    "email": "email@exemplo.com",
    "phone": "123456789",
    "message": "Mensagem do lead"
  }
  ```

- **GET** `/api/leads/{id}/`  
  Retorna os detalhes de um lead específico.

- **PUT** `/api/leads/{id}/`  
  Atualiza os dados de um lead. Exemplo de payload:
  ```json
  {
    "name": "Nome Atualizado",
    "email": "email@novo.com",
    "phone": "987654321",
    "message": "Mensagem atualizada"
  }
  ```

- **DELETE** `/api/leads/{id}/`  
  Exclui um lead específico.

- **GET** `/swagger/`  
  Acesse a documentação interativa da API através do Swagger.

## Deploy

O projeto está hospedado no **Render** e pode ser acessado através do seguinte link:

[https://lead-management-1ypy.onrender.com/](https://lead-management-1ypy.onrender.com/)

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---

Essa estrutura oferece uma visão clara sobre as funcionalidades da API, como instalá-la e acessar suas rotas. Se precisar de mais detalhes ou ajustes, é só me avisar!
