# pri-project
Projetos da cadeira Processamento e Recuperação de Informação lecionada na FEUP, no ano letivo de 2022/2023.

Dataset: https://www.kaggle.com/datasets/damienbeneschi/krakow-ta-restaurans-data-raw

## DOCKER

### Build

To build the image, run `docker build . -t restaurants_solr` 

### Run

To execute it, run `docker run --name restaurants_info -p 8983:8983 restaurants_solr`


## Stop and delete container

To do it, run `docker stop restaurants_info`

Projeto realizado por:
  - Mafalda Magalhães (up201707066@edu.fe.up.pt)
  - Maria Francisca Almeida (up201806398@edu.fe.up.pt)
  - Tomás Torres (up201800700@edu.fe.up.pt)
