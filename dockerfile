FROM solr:8.10

COPY restaurants.json /datasets/json/restaurants.json

COPY restaurants_schema.json /datasets/json/schemas/restaurants_schema.json

COPY startup.sh startup.sh

ENTRYPOINT ["sh", "/scripts/startup.sh"]
