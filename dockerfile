FROM solr:8.10

COPY /datasets/json/restaurants.json /datasets/json/restaurants.json

COPY /datasets/json/schemas/restaurants_schema.json /datasets/json/schemas/restaurants_schema.json

COPY startup.sh startup.sh

ENTRYPOINT ["sh", "startup.sh"]
