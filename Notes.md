python3 dbgensetup.py --download_datasets --data_dir /app/zero-shot-data/datasets \
  --database_conn host=$POSTGRES_HOST,user=$POSTGRES_USER,password=$POSTGRES_PASSWORD,db=$POSTGRES_DB

-> The database to download from seems down