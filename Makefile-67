all: clean collect process analyze

clean:
    rm -rf collect processed analysis

.PHONY: collect processed analysis 

collect:
    # This target is associated with data collection in the pipeline
    # First we create a folder for this data
    mkdir -p data/...
    # Next, we download the dataset from Kaggle's dataset link
    curl "https://www.kaggle.com/datasets/damienbeneschi/krakow-ta-restaurans-data-raw/download?datasetVersionNumber=5" > TA_restaurants_curated.csv
    # Finally, we planned to use a python script for scrapping more and completely reviews directly from tripadvisor pages
    python code/reviews_scrapping.py

process_all: process_cleaning process_separation
    #This step only stores the three csv files(restaurants, reviews and cuisine styles) in a database
    python3 code/database_storage.py

process_cleaning:
    # This target is reserved for data processing in pipeline
    # At first, we create an new folder for the process
    mkdir -p processed/...
    # Next, we run an script to clean all the dataset, basically removing null values from columns and setting to 0 all rating values with -1
    python3 code/clean_dataset.py

process_separation:
    # This target is reserved for data separation in pipeline
    python3 code/reviews_database.py
    python3 code/cuisine_styles_database.py
    #This step we remove reviews and cuisine styles columns from the main table
    python3 code/clean_all_dataset.py