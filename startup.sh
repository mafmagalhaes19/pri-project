#!/bin/bash

precreate-core restaurants

precreate-core cuisine-styles

precreate-core reviews

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Restaurants
# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/datasets/json/schemas/restaurants_schema.json \
    http://localhost:8983/solr/restaurants/schema

# Populate collection
bin/post -c restaurants /datasets/json/restaurants.json

# Restart in foreground mode so we can access the interface
solr restart -f


# Cuisine Styles
# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/datasets/json/schemas/cuisine_styles_schema.json \
    http://localhost:8983/solr/cuisine-styles/schema

# Populate collection
bin/post -c cuisine-styles /datasets/json/cuisine_styles.json

# Restart in foreground mode so we can access the interface
solr restart -f


# Reviews
# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/datasets/json/schemas/reviews_schema.json \
    http://localhost:8983/solr/reviews/schema

# Populate collection
bin/post -c reviews /datasets/json/reviews.json


# Restart in foreground mode so we can access the interface
solr restart -f