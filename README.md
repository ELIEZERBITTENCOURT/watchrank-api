# Watch Rank com Django Rest framework

## Descrição

Watch Rank é uma aplicação web para mostrar e classificar filmes e programas de TV desenvolvido durante o curso de Django da Alura. Ele fornece uma API RESTful para acesso aos dados do catálogo de filmes e programas de TV, bem como pesquisar e filtrar esses itens.

## Recursos Principais

- Classificação e revisão de filmes e programas de TV
- Pesquisa e filtragem de filmes e programas de TV por diversos critérios
- Testes automatizados

## Tecnologias Utilizadas

- Django
- Django Rest Framework
- SQLite (para desenvolvimento)

## Configuração do Ambiente de Desenvolvimento

1 - Clone o repositório do projeto:

```bash
git clone https://github.com/ELIEZERBITTENCOURT/watchrank-api.git
 ```

2 - Instale as dependências do Python:

```bash
pip install -r requirements.txt
```

3 - Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

4 - Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

5 - Acesse a API em `http://localhost:8000/`.

## Testes

Para executar os testes automatizados, utilize o seguinte comando:

```bash
python manage.py test
```

## Contribuindo

- Abra uma issue para discutir sobre novas funcionalidades ou correções de bugs.
- Faça um fork do repositório e crie uma branch para sua contribuição (`git checkout -b feature/nova-feature`).
- Faça o commit de suas alterações (`git commit -am 'Adicionando nova feature'`).
- Faça o push para o repositório (`git push origin feature/nova-feature`).
- Abra um Pull Request.

## Licença

Este projeto é licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
