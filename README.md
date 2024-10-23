# Reddit-Batch-Data-Pipeline
- **Apache Airflow**: 
  - Orchestrates ETL jobs.
  - Commonly used to schedule batch jobs at regular intervals or based on events.

- **Data Ingestion**: 
  - Data from Reddit is ingested into the system via PostgreSQL.
  - Airflow manages the workflow process.

- **AWS Glue and Amazon Redshift**: 
  - Primarily handle data collection and transformation (ETL).
  - Store data in Redshift or query it using Amazon Athena.

- **Glue Crawlers and Data Catalog**: 
  - Help manage metadata for datasets.

- **BI Tools**: 
  - Tools such as Power BI, Tableau, Amazon QuickSight, and Looker Studio access data from Redshift/Athena to create reports.
