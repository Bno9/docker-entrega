Antes de começar, você precisa ter instalado:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- pip install podman
- pip install podman-compose

---Passo a passo

1. Clonar o repositório
  git clone https://github.com/Bno9/nome-do-repositorio.git
  cd docker-entrega

2. Criar e subir o container
   podman-compose up --build -d (--build atualiza a imagem e -d roda em segundo plano)

3. Acessar localhost
   http://localhost:8000

4. Parar o container
   podman-compose down

Por fim, use podman-compose logs -f para ver os logs
