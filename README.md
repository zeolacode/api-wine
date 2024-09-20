# WineApp

Bem-vindo ao repositório da WineApp, uma aplicação dedicada a amantes de vinho!!!

## Pré-requisitos

Antes de começar, certifique-se de que você tem o Docker instalado e rodando em sua máquina. Se você não tem o Docker instalado, visite [a página oficial de instalação do Docker](https://docs.docker.com/get-docker/) e siga as instruções para a sua plataforma.

## Construindo a Imagem Docker

Para fazer o deploy da WineApp, você primeiro precisa construir uma imagem Docker a partir do código fonte. Abra um terminal e navegue até o diretório raiz do projeto, onde o Dockerfile está localizado. Então, execute o seguinte comando:

```bash
docker build -t wineapp:v1 .
```

Este comando diz ao Docker para construir uma imagem a partir do Dockerfile no diretório atual, marcando-a com a tag `wineapp:v1`.

## Rodando a Aplicação

Após a construção da imagem, você pode iniciar um container baseado nessa imagem com o seguinte comando:
```bash
docker run -d -p 8000:8000 --name wineapp wineapp:v1
```
Aqui está o que cada parte do comando faz:

- `docker run`: Instrui o Docker a executar um container.
- `-d`: Roda o container em modo detached, o que significa que ele roda em background.
- `-p 8000:8000`: Mapeia a porta 8000 do container para a porta 8000 do host, permitindo que você acesse a aplicação pelo navegador.
- `--name wineapp`: Atribui o nome wineapp ao container, facilitando sua gestão.
- `wineapp:v1`: Especifica qual imagem usar para criar o container, neste caso, a imagem que você construiu no passo anterior.

## Acessando a Aplicação

### Test Get `/api/health`
Com o container rodando, abra seu navegador e acesse `http://localhost:8000/api/health` para interagir com a WineApp.

### Test POST `/api/predict`
Execute o script `test.sh` utilizando o comando abaixo:
```bash
bash test.sh
```
#### Or, use `Postman`:
Para testar a API com Postman, siga os passos abaixo:

1. Abra o Postman e crie uma nova requisição.
2. Defina o método da requisição para `POST`.
3. Insira a URL do endpoint que você deseja testar. Por exemplo, `http://localhost:8000/api/predict`.
4. Na aba `Body`, selecione `raw` e escolha `JSON` como formato.
5. Copie e cole o JSON de entrada no campo de texto. Aqui estão alguns exemplos de JSON que você pode usar para testar:

**Exemplo 1:**

- **Input:**
```json
{
  "alcohol": 14.23,
  "malic_acid": 1.71,
  "ash": 2.43,
  "alcalinity_of_ash": 15.6,
  "magnesium": 127.0,
  "total_phenols": 2.8,
  "flavanoids": 3.06,
  "nonflavanoid_phenols": 0.28,
  "proanthocyanins": 2.29,
  "color_intensity": 5.64,
  "hue": 1.04,
  "od280_od315_of_diluted_wines": 3.92,
  "proline": 1065.0
}
```

- **Output esperado:**
```json
{"prediction":0}
```

**Exemplo 2:**

- **Input:**
```json
{
  "alcohol": 12.34,
  "malic_acid": 2.45,
  "ash": 2.46,
  "alcalinity_of_ash": 21,
  "magnesium": 98,
  "total_phenols": 2.56,
  "flavanoids": 2.11,
  "nonflavanoid_phenols": 0.34,
  "proanthocyanins": 1.31,
  "color_intensity": 2.8,
  "hue": 0.8,
  "od280_od315_of_diluted_wines": 3.38,
  "proline": 438
}
```

- **Output esperado:**
```json
{"prediction":1}
```

**Exemplo 3:**

- **Input:**
```json
{
  "alcohol": 12.85,
  "malic_acid": 3.27,
  "ash": 2.58,
  "alcalinity_of_ash": 22,
  "magnesium": 106,
  "total_phenols": 1.65,
  "flavanoids": 0.6,
  "nonflavanoid_phenols": 0.6,
  "proanthocyanins": 0.96,
  "color_intensity": 5.58,
  "hue": 0.87,
  "od280_od315_of_diluted_wines": 2.11,
  "proline": 570
}
```

- **Output esperado:**
```json
{"prediction":2}
```

6. Após inserir o JSON de entrada, clique em `Send` para fazer a requisição.
7. O Postman exibirá a resposta da API no painel de resposta. Compare o resultado com o output esperado fornecido acima.

Repita esses passos para cada exemplo de JSON fornecido para testar diferentes entradas na sua API.