
# Demo Project for AU Electricity Industry

In this task, I need to create a django CLI command to read values from CSV file (in NEM13 format) and create datase records.

## Demo

To run the project:

```
docker compose -f docker-compose.yml up -d --build
```

To test the project:
```
docker compose -f docker-compose.yml run web sh -c "python -m pytest"
```

To load csv into database, use the following command:

```
python manage.py load_nem13 <csv_file_path>
```

To load csv in docker container:

```
docker compose -f docker-compose.yml run web sh -c "python manage.py load_nem13 <csv_file_path>"
```

It might throw some errors which will be displayed as warning standart console message. For example, if the csv file contains row with empty values:
![empty columns in csv file](/images/error1.png)
![terminal error stating csv empty columns](/images/error2.png)