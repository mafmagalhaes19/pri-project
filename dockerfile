FROM solr:8.10

COPY restaurants.json /datasets/json/restaurants.json

COPY restaurants_schema.json /datasets/json/schemas/restaurants_schema.json

COPY cuisine_styles.json /datasets/json/cuisine_styles.json

COPY cuisine_styles_schema.json /datasets/json/schemas/cuisine_styles_schema.json

COPY reviews.json /datasets/json/reviews.json

COPY reviews_schema.json /datasets/json/schemas/reviews_schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
