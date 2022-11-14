#!/bin/bash

precreate-core restaurants


# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 10

# Restaurants
# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/datasets/json/schemas/restaurants_schema.json \
    http://localhost:8983/solr/restaurants/schema

# Populate collection
bin/post -c restaurants /datasets/json/restaurants.json

# Restart in foreground mode so we can access the interface
solr restart -f
