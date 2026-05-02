# Slack FAQ candidates - draft

Source: _temp/slack/course-data-engineering.threads.jsonl

Years included: 2025, 2026

Total threads analyzed: 3087

  - threads with at least one reply: 2782
  - threads with NO replies (unanswered questions): 305

Themes matched: 61

Threads not matching any theme keyword (need new themes / manual review): 899

Note: 'unmatched' = the question text didn't fire any theme regex; it does NOT mean the thread has no replies. Both answered and unanswered threads can be unmatched.

---

## Theme frequency summary

- Workflow orchestration (Mage/Kestra/Airflow/Prefect/Dagster): 385
- Postgres / pgcli / pgAdmin: 255
- dbt cloud / dbt core / models: 210
- BigQuery / data warehouse: 187
- Docker / docker compose errors: 139
- Terraform setup / errors: 138
- Certificate / passing criteria: 136
- Final project rules / scope / dataset: 115
- Homework submission / form / link: 112
- Joining mid-cohort / late start / what did I miss: 108
- NYC taxi dataset URL / 403 forbidden / where to get data: 99
- Spark / PySpark / cluster: 95
- Course start / cohort schedule: 89
- Project resubmission / second / last attempt: 89
- Windows / WSL / Mac M1 / OS-specific: 81
- Project deadline / extension / final attempt: 81
- Live session timing / timezone / format: 68
- Project peer review process: 68
- Kafka / streaming: 67
- Project as a team / two people / collaboration: 65
- GCP free credits / billing / account: 64
- AWS / Azure / Oracle / alternative cloud: 61
- Bruin (2026 cohort): 61
- Videos / playlist / where to watch: 60
- Project: how to evaluate / find peer projects to review: 60
- Homework deadline / late submission: 51
- Workshop (dlt / Bruin) - where to find / mandatory: 51
- Course platform login / account: 49
- Codespaces / Gitpod / VM environment: 48
- GCP service account / key / IAM: 46
- DuckDB: 46
- Where to find videos / playlist (current cohort): 44
- Project: minimum score / passing / how scored: 39
- How to join / register / enroll: 34
- Course calendar / google calendar / deadlines list: 33
- Where to start / first steps / what to install: 32
- Where is the live link / how to join the session: 30
- Certificate: when received / how to get: 29
- Learning in public / posting on social: 28
- Self-paced / previous cohort videos still relevant: 25
- Country / city / study buddy lookup: 21
- Homework answer doesn't match options: 21
- Homework include code / SQL / screenshots in repo: 19
- Recordings / live sessions / office hours: 17
- Score / leaderboard / points: 17
- Project: dashboard / Looker / visualization tool: 14
- Forking the repo / git workflow / pull updates: 14
- AI / LLM / ChatGPT for course / project: 12
- Recommended IDE / Cursor / Antigravity: 10
- Codespaces budget / out of free usage: 9
- Project: API key / private credentials / reproducibility: 9
- Tool substitutions (Podman, alternatives): 8
- Prerequisites / can I take the course: 7
- Cloud cost / how much will GCP cost / minimize expenses: 6
- Telegram / Slack channel access: 6
- Project: small dataset OK / dataset choice: 6
- Next zoomcamp / when does ML/MLOps/LLM start: 6
- FAQ document / contributing to FAQ: 5
- Project: architecture diagram / pipeline diagram tool: 3
- Quizzes / quiz access / quiz wrong answer: 2
- Removing oneself / changing email / account issues: 2

---

## Workflow orchestration (Mage/Kestra/Airflow/Prefect/Dagster) (385 threads)

### [2025-01-01] U085ZD19ZBQ (replies: 10)

Q: Hi guys, I've been trying out some steps from current course repo. In Week 2, I'm using Kestra to ingest NYC Taxi data from the provided github link into a postgres running on a local container. My containers launch OK and the Extract stage on Kestra runs OK. But just before creating tables on postgres, I get this error: *Cannot invoke "java.sql.Connection.rollback()" because "connection" is null*. I couldn't find any help online. Will be grateful for any ideas on what might be causing this.
   
   For ref: I'm simply running 'docker compose up' on the compose file placed here: data-engineering-zoom ...

A: Do you have postgres installed locally ? Try changing port mapping to - "5433:5432"
   ---
   in the 02_postgres_taxi.yaml file under `pluginDefaults`, try changing the url value to `jdbc:<postgresql://postgres:5432/kestra>` or `jdbc:<postgresql://localhost:5432/kestra>`
   ---
   @user I have the same error and tried your solution but the error persisted, is there anything else that should be changed?
   ---
   @user , @user’s first suggestion worked for me! I replaced host.internal.docker with postgres. The other suggestions didn't exactly work: changing 5433 to 5432 and using 'localhost'. Now, I'm able to proceed with execution but the last 'copy_in' stage runs indefinitely (&gt; 14 min). I'll work it out. But really grateful, your reply saved much time for me.
   ---
   @user did you change the url in the pluginDefaults section only? I noticed another url above it and tried to change it too but it didn't work either. How about the password in pluginDefaults did you leave it as kestra?
   ---
   @user Yes. I just changed the url in pluginDefaults of the flow yaml file. Kept all passwords, names exactly the same. No changes done to compose file either. The combination does run. We can connect if needed. I'm s ...

### [2025-01-02] Sebastian Restrepo (replies: 4)

Q: Hi all, are there any updates regarding videos for kestra and gcp? the current playlist only includes the postgres setup.
   Thanks!

A: Can you be more specific/what you think is missing? https://www.youtube.com/playlist?list=PLEK3H8YwZn1oPPShk2p5k3E9vO-gPnUCf
   ---
   Hi @user, thanks for answering. Currently there are no videos related to GCP and kestra. All videos are related to working locally with Postgres. Will mentions at the end of video "*DE Zoomcamp 2.2.3 - ETL with Postgres"* that we will now do an example on GCP putting all the data in bigQuery but this video is nowhere to be found.
   Also if you go by the numbering of the videos, there seem to be videos missing from the playlist  like 2.2.4 or 2.2.6......
   There is some text related to gcp on the readme here https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration
   but not much of an explanation as in videos related to kestra and postgres
   ---
   Ah, I see. That is an unknown to me. I'll see what I can find out.
   ---
   They will be published soon

### [2025-01-05] afşın özdemir (replies: 2)

Q: Hey everyone! I was wondering, does anyone know how can I reach the last years notes about airflow? the link in the README.md doesn’t work :disappointed:

A: 2022's airflow link still works. if that helps.
   ---
   Let me check again thanks!

### [2025-01-08] U04S8PDBB47 (replies: 12)

Q: Hi everyone! I’m trying to get through Week 2 ETL Pipelines with Kestra (https://www.youtube.com/watch?v=OkfLX28Ecjg&amp;list=PLEK3H8YwZn1oPPShk2p5k3E9vO-gPnUCf&amp;index=3&amp;ab_channel=Kestra), and I’m having some problems creating the *ETL pipeline with Postgres in Kestra*. It looks like Kestra did not interpolate the variables-- not sure if this is an error on Kestra’s runner/limitation? I’ve attached the YAML script I used on Kestra and the error log here. I tried troubleshooting, but after many tries, the issue appears to be with *Kestra’s output serialization mechanism*. Specifically,  ...

A: This is part of your log.
   &gt; echo "Downloading file from https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv.gz"
   &gt; curl -L "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv.gz" | gunzip &gt; "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"]
   It seems that variables within braces don't behave like variables, but rather as strings.
   Check out the dynamic variables https://kestra.io/docs/workflow-components/variables.
   I hope it works
   ---
   Thanks so much!! I'll take a look at this :pray: :pray: :pray:
   ---
   I ran into the same issue. I'm unsure about the direction above, as the variables resolved perfectly fine for the wget request (e.g. the log shows the command attempted to run `wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-02.csv.gz | gunzip &gt; green_tripdata_2019-02.csv`. I posted the question as a comment on the YouTube channel, and will respond here if I find a resolution.
   ---
   Yeah, I just spent a considerable amount of time today trying to debug aga ...

### [2025-01-09] Sauran (replies: 2)

Q: Hi there! Can somebody please let me know where can we can find text materials for Airflow? I found videos from 2022 on the matter, but can't find any notes on Github

A: maybe try the cohort 2022 folder
   ---
   You're genius! Thanks!

---

## Postgres / pgcli / pgAdmin (255 threads)

### [2025-01-01] U085ZD19ZBQ (replies: 10)

Q: Hi guys, I've been trying out some steps from current course repo. In Week 2, I'm using Kestra to ingest NYC Taxi data from the provided github link into a postgres running on a local container. My containers launch OK and the Extract stage on Kestra runs OK. But just before creating tables on postgres, I get this error: *Cannot invoke "java.sql.Connection.rollback()" because "connection" is null*. I couldn't find any help online. Will be grateful for any ideas on what might be causing this.
   
   For ref: I'm simply running 'docker compose up' on the compose file placed here: data-engineering-zoom ...

A: Do you have postgres installed locally ? Try changing port mapping to - "5433:5432"
   ---
   in the 02_postgres_taxi.yaml file under `pluginDefaults`, try changing the url value to `jdbc:<postgresql://postgres:5432/kestra>` or `jdbc:<postgresql://localhost:5432/kestra>`
   ---
   @user I have the same error and tried your solution but the error persisted, is there anything else that should be changed?
   ---
   @user , @user’s first suggestion worked for me! I replaced host.internal.docker with postgres. The other suggestions didn't exactly work: changing 5433 to 5432 and using 'localhost'. Now, I'm able to proceed with execution but the last 'copy_in' stage runs indefinitely (&gt; 14 min). I'll work it out. But really grateful, your reply saved much time for me.
   ---
   @user did you change the url in the pluginDefaults section only? I noticed another url above it and tried to change it too but it didn't work either. How about the password in pluginDefaults did you leave it as kestra?
   ---
   @user Yes. I just changed the url in pluginDefaults of the flow yaml file. Kept all passwords, names exactly the same. No changes done to compose file either. The combination does run. We can connect if needed. I'm s ...

### [2025-01-02] Sebastian Restrepo (replies: 4)

Q: Hi all, are there any updates regarding videos for kestra and gcp? the current playlist only includes the postgres setup.
   Thanks!

A: Can you be more specific/what you think is missing? https://www.youtube.com/playlist?list=PLEK3H8YwZn1oPPShk2p5k3E9vO-gPnUCf
   ---
   Hi @user, thanks for answering. Currently there are no videos related to GCP and kestra. All videos are related to working locally with Postgres. Will mentions at the end of video "*DE Zoomcamp 2.2.3 - ETL with Postgres"* that we will now do an example on GCP putting all the data in bigQuery but this video is nowhere to be found.
   Also if you go by the numbering of the videos, there seem to be videos missing from the playlist  like 2.2.4 or 2.2.6......
   There is some text related to gcp on the readme here https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration
   but not much of an explanation as in videos related to kestra and postgres
   ---
   Ah, I see. That is an unknown to me. I'll see what I can find out.
   ---
   They will be published soon

### [2025-01-03] shuokai (replies: 5)

Q: Hi team,
   I've been following a video tutorial where Alex explains how to set up a Python environment using a Dockerfile and configure PostgreSQL and pgAdmin services in a `docker-compose.yml` file. In the example, the Python service is set up separately.
   I was wondering: Is it okay to combine everything (Python, PostgreSQL, and pgAdmin) into a single `docker-compose.yml` file?
   For example, my goal is that when I run `docker-compose up`, all three services (Python, PostgreSQL, and pgAdmin) start simultaneously, creating three containers from three images.
   Are there any downsides or best practic ...

A: That's perfectly acceptable and best practice would be one docker compose file. The separate files/containers is just to demonstrate/learn about docker and how it works.
   ---
   Thank you for this
   ---
   Hi @user,
   
   My Current Issue:
   I’m trying to ensure that when I run `docker-compose up`, all three containers—pgAdmin, PostgreSQL, and the Python-based data ingestion service—start up and work together correctly.
   • I am able to run the `pgdatabase` and `pgadmin` containers without issues.
   • However, the `data_ingestion` container seems to not start as expected.
   What I’ve Tried:
   • I've double-checked the configuration, paths, and environment variables in the `docker-compose.yml` file.
   • I’m trying to mount the Python script into the container and run it automatically through the Dockerfile's entry point.
   Question:
   Could you please help me troubleshoot why the `data_ingestion` container is not running as expected? Do I need to update or modify my Docker Compose setup or Dockerfile in some way to ensure that the Python environment is set up correctly within the container and the ingestion script runs properly?
   Thank you for your help!
   
   Here's my current `docker-compose.yml` file:
   ```yaml
   
   
   ver ...

### [2025-01-04] U06P5LB5UKT (replies: 3)

Q: Hi folks, Good Day.!!
   I'm getting started with week-1 and completed docker-postgres setup. I noticed when I run the postgres docker image, it automatically creates this empty folder. Just wondering what this is and why its getting created? Any thoughts ??
   @user

A: Hey, @user! Here you go:  When you run the PostgreSQL Docker image for the first time, it creates the directory `/var/lib/postgresql/data` inside the container. This directory is where PostgreSQL stores its data files, including databases, tables, and logs. The creation of this empty folder happens because the PostgreSQL Docker image is designed to initialize a data directory upon startup.   If you have mounted a local directory to this path (e.g., using the `-v` option), the files in your local directory will be used as the data directory, and PostgreSQL will write its data there. If the local directory is empty when you first run the container, the PostgreSQL image will populate it with default files necessary for its operation.   This behavior is normal and expected as part of the initialization process of the PostgreSQL database when using Docker. If the folder appears empty after you run the container, ensure that the volume is mounted correctly and check for any permission issues that may prevent PostgreSQL from writing to the directory.
   ---
   @user - Yes i've mounted local directory. But docker automatically creates another folder named 'ny_taxi_postgres_data;C' in my host mac ...

### [2025-01-05] Dehao Zhang (replies: 4)

Q: Hi team, I was following video 1.2.2 and ran into issues with mapping volumes. I am using WSL2 on windows. Initially when I used the same format described in the video I got an "Error response from daemon: invalid mode: /var/lib/postgresql/data." message. After I switched to another format it ran fine with "database system is ready for connection" but my ny_taxi_postgres_data local folder is not populating as shown in the video (i.e., still empty after the container starts running). Should I be concerned? I am able to use pgcli to connect to the db fine, but just want to know if unable to get  ...

A: Hard to say. You might not really be coming back to that piece after running it so it won't matter if the data is actually persisted. Think you'd want to spend some time with ChatGPT giving it your configuration, the symptoms and any issues you are running into if you wanted to resolve it. You could also just use docker volumes and cut out the bind mounts all together.
   ---
   https://www.youtube.com/watch?v=olUKRq-FVyo
   ---
   @user Thank you so much for your thoughts and its good to know that we might not need to come back to that. I did spend some time with ChatGPT on this and unfortunately the suggestions didn't quite work. I tried "docker volume create" which also worked but didn't populate the folder either.  In general is it a best practice to set this up to enable data persistence outside of container?
   ---
   Docker volume won't populate a folder as it is a docker volume. As far as best practice it's hard to say. In the "real world" you would probably be running a Managed Postgres Instance and wouldn't need to worry about it. Between a bind mount and a docker volume you would probably be running on Linux for a "real personal project" so the bind mount would be a bit easier than trying ...

---

## dbt cloud / dbt core / models (210 threads)

### [2025-01-10] Manuel Guerra (replies: 2)

Q: Some questions about module 2 orchestration:
   
   &gt; Is it okay to work with flows using DBT when DBT is explained in module 4?
   &gt; I think the comparison of data lake vs data warehouse and ETL vs ELT that was explained in this module in cohorts from other years is missing.

A: 1. Yup! It's just a quick showcase of what you can do. DBT will be fully covered later on
   2. While their aren't dedicated videos on them, those concepts are covered in the videos
       a. Data Lakes vs Data Warehouses is covered when BigQuery is introduced in 2.2.6
       b. ETL vs ELT when dbt is introduced in 2.2.5 and 2.2.8
   ---
   Thanks Will !

### [2025-01-10] Rudy Desplan (replies: 1)

Q: Hi ,
   Can we use Airflow like in the previous zoomcamp and SQL-Mesh instead of DBT ?

A: Yes

### [2025-01-17] Randall Lionel Kharkrang (replies: 3)

Q: I feel i should skip some lectures from module 2 regarding bigquery and dbt, as those are not covered yet. what do u suggest @user?
   should i move on to module 3?
   
   I've implemented the simple postgres taxi workflow. quite nice stuff

A: Hey, @user! Here you go:  It's advisable to follow the course progression as intended. While DBT will be explained in module 4, the concepts related to BigQuery and DBT in module 2 serve as foundational knowledge that will be built upon later. Skipping these lectures might lead to gaps in understanding when you reach module 4.  Since you have already implemented the simple Postgres taxi workflow and found it beneficial, it may be a good idea to continue through module 2, ensuring you grasp the orchestration concepts and how they tie into DBT and BigQuery. After completing module 2, you can then proceed to module 3, as each module is designed to logically follow the previous one, enhancing your overall understanding of the material.
   ---
   Yeah we only cover things at a high level and leave those later modules to go into details
   ---
   Yes, i kind skimmed through the later kestra videos with bigquery and dbt. didnt really understand it. going to module 3 for now, and will come back to them later.
   
   also the tutorials in your website are pretty damn good. so thanks.

### [2025-01-17] YB (replies: 7)

Q: I executed `07_gcp_dbt.yaml` in kestra. The flow ran successfully. But when I view the generated `fact_trips` details in BigQuery, it only has 194 rows. I've not gone through the analytics engineering lessons yet but based on the dbt `fact_trips.sql` file, it is unioning all yellow and green rides without filters. So I'm expecting `fact_trips` to have 8 million (`green_tripdata`) + 124 million (`yellow_tripdata`) rows. Am I missing something?

A: @user can you share some light on this dbt question? :smile:
   ---
   thx @user for pointing this out, we'll change that question as indeed it can be confusing given the dbt week from Victoria uses BigQuery's public dataset, so the nr of rows can be different
   
   we'll swap the question for another
   ---
   New question will go live soon cc @user https://github.com/DataTalksClub/data-engineering-zoomcamp/pull/597
   ---
   @user @user Thanks for clarifying. I was actually trying to answer `Question 3. How many rows are there for the Yellow Taxi data for the year 2020?`. I understand I can just query the `yellow_tripdata` table since it has already combined 2019-01 to 2021-07 data. But since I've ran dbt in kestra, I thought I can use `fact_trips` table for all queries as it has both yellow + green data combined and the taxi zone lookup.
   
   My question is more on the confusion on how dbt works in the data modelling. My expectation would be the `fact_trips` table to contain all the individual rows from the green and yellow trips combined.
   ---
   My understanding is that the dbt project does some other things behind the scenes so you’re best to look at module 4 for more info on how it works
   ---
   After going t ...

### [2025-01-18] Abdelali (replies: 8)

Q: Hi everyone,
   I just reached the video titled '*DE Zoomcamp 2.2.5 - Orchestrate dbt Models with Postgres in Kestra*' and I found it a bit confusing since it introduced dbt, which is new for me and I know it will be covered in module 4. As we’re still in module 2, I couldn’t grasp the concepts fully. Is it okay to not understand it for now and skip it if it's not used in the rest of module 2?
   I plan to come back to it once dbt is properly introduced.

A: Yup - this video in module 2 is just to show you that Kestra can do dbt at a high level, which may be useful in a few modules time! For now, focus on the ETL videos on Postgres and bigquery
   ---
   Alright, thanks Will
   ---
   Hello Will, please I have similar question for the video titled: *DE Zoomcamp 2.2.6 - ETL Pipelines in Kestra: Google Cloud Platform*
   In the *06_gcp_taxi* flow you declared the variable gcs_file like this:
   `gcs_file: "gs://{{kv('GCP_BUCKET_NAME')}}/{{vars.file}}"`
   why we didn't use the render function for vars.file in this case, I mean like this:
   `gcs_file: "gs://{{kv('GCP_BUCKET_NAME')}}/{{render(vars.file)}}"`
   Thanks in advance
   ---
   We should use render when calling gcs_file?
   ---
   Sorry I didn't understand your question
   Btw when I said similar question, I wrote the question in this thread by mistake, I was actually referring to this
   https://datatalks-club.slack.com/archives/C01FABYF2RG/p1737202869902679
   ---
   ```variables:
     file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
     gcs_file: "gs://{{kv('GCP_BUCKET_NAME')}}/{{vars.file}}"
     table: "{{kv('GCP_DATASET')}}.{{inputs.taxi}}_tripdata_{{inputs.year}}_{{inputs.month}}"
     data: "{{outputs.extract.o ...

---

## BigQuery / data warehouse (187 threads)

### [2025-01-05] Imran (replies: 2)

Q: Hi everyone, I am working on week 3, data warehousing of the course. I am getting this error in BigQuery:
   Error while reading table: zoomcamp-25.zoomcamp.external_yellow_tripdata, error message: CSV table references column position 17, but line contains only 5 columns.; byte_offset_to_start_of_line: 553646035 column_index: 17 column_name: "congestion_surcharge" column_type: DOUBLE File: <gs://my-object-storage/yellow_tripdata_2019-01.csv>
   
   I ran this query:
   -- Create a non partitioned table from external table
   CREATE OR REPLACE TABLE zoomcamp-25.zoomcamp.yellow_tripdata_non_partitoned AS
   SELEC ...

A: Look at the error message... they're your hint to what you're doing wrong.
   
   The `yellow_tripdata_2019-01.csv` should contain 18 columns total.
   
   ```VendorID,tpep_pickup_datetime,tpep_dropoff_datetime,passenger_count,trip_distance,RatecodeID,store_and_fwd_flag,PULocationID,DOLocationID,payment_type,fare_amount,extra,mta_tax,tip_amount,tolls_amount,improvement_surcharge,total_amount,congestion_surcharge```
   And it seems yours only contain 5:
   
   &gt;  Error while reading table: (...), error message: CSV table references column position 17, *but line contains only 5 columns*
   I don't know what you did, but you've messed on the data serialization/upload to GCS
   ---
   You're right, somehow the data got messed up, I was just following the instructions in course.
   So i just deleted the January 2019 yellow taxi data and it worked with other months.
   Thank you

### [2025-01-10] Manuel Guerra (replies: 2)

Q: Some questions about module 2 orchestration:
   
   &gt; Is it okay to work with flows using DBT when DBT is explained in module 4?
   &gt; I think the comparison of data lake vs data warehouse and ETL vs ELT that was explained in this module in cohorts from other years is missing.

A: 1. Yup! It's just a quick showcase of what you can do. DBT will be fully covered later on
   2. While their aren't dedicated videos on them, those concepts are covered in the videos
       a. Data Lakes vs Data Warehouses is covered when BigQuery is introduced in 2.2.6
       b. ETL vs ELT when dbt is introduced in 2.2.5 and 2.2.8
   ---
   Thanks Will !

### [2025-01-13] Kareem Adel (replies: 2)

Q: Hi, does anyone know if I can use Azure Synapse instead of BigQuery for this course? I'm unable to create a free trial account in GCP due to problems with my credit card.

A: Yes you can
   ---
   Thank you, that sounds great

### [2025-01-13] Joshua Thomas (replies: 2)

Q: Hi all, Josh here hailing from ON, Canada. Excited to be learning with all of you! Quick question...does anyone know if it's okay to complete the course using AWS equivalents (eg. Redshift instead of BigQuery, etc)?

A: Never mind, saw it in the FAQ section of the launch vid (47:11 for those interested)
   ---
   AWS is costly as compared to GCP

### [2025-01-16] Przemek (replies: 5)

Q: #terraform
   Have you encounter issue with creating bucket with cloud storage admin role?
   I was able to create bigquery dataset, but for bucket I receive 403 error (commonly described here)
   
   The only way to handle it is to use service account with editor role. Is there some bug on GCP side?

A: have you tried @user whether it can address your question?
   
   Have you encounter issue with creating bucket with cloud storage admin role?
   I was able to create bigquery dataset, but for bucket I receive 403 error (commonly described here)
   
   The only way to handle it is to use service account with editor role. Is there some bug on GCP side?
   ---
   Hey, @user! Here you go:  Receiving a 403 error when trying to create a bucket, even with the Cloud Storage Admin role, suggests that the service account may not have the appropriate permissions or that the project ID used in the Terraform configuration is incorrect.   Ensure that you are declaring the correct Project ID, not just the Project name, in your Terraform configuration. The correct project ID can be found in your Google Cloud Platform (GCP) console dashboard.  If you have confirmed that the project ID is correct and you still encounter issues, you may need to check the roles assigned to the service account. If the service account lacks permissions for creating buckets, consider adding the Editor role to the service account as a temporary workaround or ensuring that all necessary roles are correctly assigned.  If the problem persists,  ...

---

## Docker / docker compose errors (139 threads)

### [2025-01-01] U085ZD19ZBQ (replies: 10)

Q: Hi guys, I've been trying out some steps from current course repo. In Week 2, I'm using Kestra to ingest NYC Taxi data from the provided github link into a postgres running on a local container. My containers launch OK and the Extract stage on Kestra runs OK. But just before creating tables on postgres, I get this error: *Cannot invoke "java.sql.Connection.rollback()" because "connection" is null*. I couldn't find any help online. Will be grateful for any ideas on what might be causing this.
   
   For ref: I'm simply running 'docker compose up' on the compose file placed here: data-engineering-zoom ...

A: Do you have postgres installed locally ? Try changing port mapping to - "5433:5432"
   ---
   in the 02_postgres_taxi.yaml file under `pluginDefaults`, try changing the url value to `jdbc:<postgresql://postgres:5432/kestra>` or `jdbc:<postgresql://localhost:5432/kestra>`
   ---
   @user I have the same error and tried your solution but the error persisted, is there anything else that should be changed?
   ---
   @user , @user’s first suggestion worked for me! I replaced host.internal.docker with postgres. The other suggestions didn't exactly work: changing 5433 to 5432 and using 'localhost'. Now, I'm able to proceed with execution but the last 'copy_in' stage runs indefinitely (&gt; 14 min). I'll work it out. But really grateful, your reply saved much time for me.
   ---
   @user did you change the url in the pluginDefaults section only? I noticed another url above it and tried to change it too but it didn't work either. How about the password in pluginDefaults did you leave it as kestra?
   ---
   @user Yes. I just changed the url in pluginDefaults of the flow yaml file. Kept all passwords, names exactly the same. No changes done to compose file either. The combination does run. We can connect if needed. I'm s ...

### [2025-01-02] Rabab (replies: 4)

Q: Hi All, I installed Docker on Mac, and I was testing it by using this (docker pull hello-world) on terminal but I got this error ( Error response from daemon: Head “https://registry-1.docker.io/v2/library/hello-world/manifests/latest”: unauthorized: incorrect username or password) any suggestion ?

A: Hi @user! We asked AI, and this is what it answered:
   
   The error you're seeing usually occurs when Docker is trying to access a private repository or when there's an authentication issue. Since you're trying to pull a public image (`hello-world`), it's likely due to a misconfigured Docker setup. 
   
   Try the following steps:
   
   1. *Logout and Login*: Run `docker logout` to reset your credentials, then try pulling the image again with `docker pull hello-world`.
   2. *Check Docker Configuration*: Ensure your Docker configuration doesn't have any authentication settings set for the Docker Hub registry. You can do this by checking the `~/.docker/config.json` file. If you find any authentication settings, remove them and try again.
   3. *Reset Docker Credentials*: Sometimes, resetting the credentials can resolve the issue. You can do this by deleting the `~/.docker/config.json` file (if it exists) and then trying the pull command again.
   
   If none of these steps work, consider reinstalling Docker or seeking further assistance from Docker support resources.
   ---
   Also it may happen when you have a typo in the image name
   ---
   Thank you worked with the first one
   ---
   Nop , I copied the command  from the D ...

### [2025-01-03] Gloria Quiceno (replies: 4)

Q: Hello all, does anyone have notes on creating docker resource in GCP with terraform? having issues with permission policies for the default service account and wondering if anyone have notes to overcome it?

A: Do you mean installing docker on the VM with Terraform or are you referring to some other type of docker resource?
   ---
   i mean executing terraform apply and not have iam service account permission errors
   ---
   @user
   terraform files here: https://github.com/gdq12/pipeline-performance-analysis/tree/main/1_extract_load/gcp
   
   error message for terraform apply:
   
   ```Error: Error creating Service: googleapi: Error 403: Permission 'iam.serviceaccounts.actAs' denied on service account <mailto:1023261528910-compute@developer.gserviceaccount.com|1023261528910-compute@developer.gserviceaccount.com> (or it may not exist).
   │ 
   │   with google_cloud_run_service.run_service,
   │   on main.tf (http://main.tf) line 78, in resource "google_cloud_run_service" "run_service":
   │   78: resource "google_cloud_run_service" "run_service" {```
   current iam permission I have in my project:
   
   ```bindings:
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.reader
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.writer
   - members:
     - serviceAccount:mage-extract-load@pi ...

### [2025-01-03] shuokai (replies: 5)

Q: Hi team,
   I've been following a video tutorial where Alex explains how to set up a Python environment using a Dockerfile and configure PostgreSQL and pgAdmin services in a `docker-compose.yml` file. In the example, the Python service is set up separately.
   I was wondering: Is it okay to combine everything (Python, PostgreSQL, and pgAdmin) into a single `docker-compose.yml` file?
   For example, my goal is that when I run `docker-compose up`, all three services (Python, PostgreSQL, and pgAdmin) start simultaneously, creating three containers from three images.
   Are there any downsides or best practic ...

A: That's perfectly acceptable and best practice would be one docker compose file. The separate files/containers is just to demonstrate/learn about docker and how it works.
   ---
   Thank you for this
   ---
   Hi @user,
   
   My Current Issue:
   I’m trying to ensure that when I run `docker-compose up`, all three containers—pgAdmin, PostgreSQL, and the Python-based data ingestion service—start up and work together correctly.
   • I am able to run the `pgdatabase` and `pgadmin` containers without issues.
   • However, the `data_ingestion` container seems to not start as expected.
   What I’ve Tried:
   • I've double-checked the configuration, paths, and environment variables in the `docker-compose.yml` file.
   • I’m trying to mount the Python script into the container and run it automatically through the Dockerfile's entry point.
   Question:
   Could you please help me troubleshoot why the `data_ingestion` container is not running as expected? Do I need to update or modify my Docker Compose setup or Dockerfile in some way to ensure that the Python environment is set up correctly within the container and the ingestion script runs properly?
   Thank you for your help!
   
   Here's my current `docker-compose.yml` file:
   ```yaml
   
   
   ver ...

### [2025-01-07] Abdelali (replies: 9)

Q: Hi, I’m using Docker Compose to set up PostgreSQL and pgAdmin containers, but after restarting, I lose my pgAdmin configuration. I created a `data_pgadmin` folder for persistence, but when I try to change its permissions using `sudo chown 5050:5050 data_pgadmin`, I get the error: 'Sudo is disabled on this machine. To enable it, go to the Developer Settings page in the Settings app.' How can I fix this on Windows? @user

A: Hey, @user! Here you go:  To fix the issue of losing pgAdmin configuration after restarting your Docker containers on Windows, you should utilize Docker volumes instead of trying to change folder permissions with `sudo`, which is not available in your environment.  You can modify your `docker-compose.yaml` file to define a volume for pgAdmin. This will help persist the configuration without needing to alter permissions on the host file system. Here's an example of how to set it up:  ```yaml services:   pgadmin:     image: dpage/pgadmin4     environment:       - PGADMIN_DEFAULT_EMAIL=admin@admin.com       - PGADMIN_DEFAULT_PASSWORD=root     volumes:       - pgadmin_data:/var/lib/pgadmin     ports:       - "8080:80"  volumes:   pgadmin_data: ```  By using a Docker volume (`pgadmin_data`), Docker handles the permissions internally, which avoids issues related to file system permissions on Windows. You do not need to run `sudo chown` commands, as the volume will be managed by Docker, ensuring that your pgAdmin configuration is preserved across container restarts.   Additionally, if you're using WSL, it is recommended to use Docker volumes to resolve any permission-related issues, as th ...

---

## Terraform setup / errors (138 threads)

### [2025-01-03] Gloria Quiceno (replies: 4)

Q: Hello all, does anyone have notes on creating docker resource in GCP with terraform? having issues with permission policies for the default service account and wondering if anyone have notes to overcome it?

A: Do you mean installing docker on the VM with Terraform or are you referring to some other type of docker resource?
   ---
   i mean executing terraform apply and not have iam service account permission errors
   ---
   @user
   terraform files here: https://github.com/gdq12/pipeline-performance-analysis/tree/main/1_extract_load/gcp
   
   error message for terraform apply:
   
   ```Error: Error creating Service: googleapi: Error 403: Permission 'iam.serviceaccounts.actAs' denied on service account <mailto:1023261528910-compute@developer.gserviceaccount.com|1023261528910-compute@developer.gserviceaccount.com> (or it may not exist).
   │ 
   │   with google_cloud_run_service.run_service,
   │   on main.tf (http://main.tf) line 78, in resource "google_cloud_run_service" "run_service":
   │   78: resource "google_cloud_run_service" "run_service" {```
   current iam permission I have in my project:
   
   ```bindings:
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.reader
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.writer
   - members:
     - serviceAccount:mage-extract-load@pi ...

### [2025-01-04] Akmal Fadhlurrahman (replies: 3)

Q: This is the Nth time I tried to follow DE Zoomcamp from start to finish, and I'm excited! One question, maybe for @user, is Terraform a CLI-only tools? because I tried to install it on my Windows machine and it does not show any standard installation GUI, only a glimpse of a black terminal before it fades away.

A: Hey, @user! Here you go:  Terraform is indeed a CLI (Command Line Interface) tool, which means it does not come with a standard installation graphical user interface (GUI). Instead, it operates entirely in the terminal. When you install Terraform on your Windows machine, you will interact with it through command-line commands. The fleeting appearance of a black terminal you mentioned is likely due to executing the installer directly, which may not provide a GUI.  To use Terraform effectively, you should open a command prompt or PowerShell window and run Terraform commands there. Make sure you have added Terraform to your system's PATH so that you can execute it from any terminal window. You can verify the installation by running the command `terraform version` in the terminal to see if it returns the version number, indicating that Terraform is installed correctly.
   ---
   How do I add terraform to system PATH? @user
   ---
   Hey, @user! Here you go:  To add Terraform to your system PATH, you need to follow these steps based on your operating system:  For Windows: 1. Download the Terraform executable from the [Terraform website](https://www.terraform.io/downloads.html). 2. Unzip the downloa ...

### [2025-01-05] Dennis Machel (replies: 5)

Q: Has anyone completed the initial setup with terraform?

A: @user starting point….
   ---
   Is that a question or a statement ?
   ---
   Yes, I watched this video from Luis to get github codespace setup and install terraform.  https://youtu.be/XOSUt8Ih3zA?si=IwCtJ-BfqbrTfo1j (https://youtu.be/XOSUt8Ih3zA?si=IwCtJ-BfqbrTfo1j)
   ---
   Thanks for this Cory :clap: :clap: :clap:
   ---
   Thank you! I was having the hardest time trying to get terraform into my codespace. This was very straightforward

### [2025-01-10] Abdelali (replies: 3)

Q: Hi all,
   In the "1.3.2 - Terraform Basics" video of DE Zoomcamp, I noticed a VM was used. Is it necessary, or can I follow along using a normal terminal instead (e.g., Git Bash, PowerShell, WSL)?
   Thanks in advance! @user

A: Hey, @user! Here you go:  Using a normal terminal such as Git Bash, PowerShell, or WSL is sufficient to follow along with the "1.3.2 - Terraform Basics" video of DE Zoomcamp. A VM is not strictly necessary for the course, as the tools and commands can be executed directly in these terminal environments. It's recommended to use the environment that you are most comfortable with.
   ---
   I only switched to a VM to keep it "cleaner." In my usual browser I have all my bookmarks, recently visited etc. Just easier to do it on a VM so it's kind of a blank slate. Using a VM is not necessary.
   ---
   I see , thank you so much

### [2025-01-10] Abdelali (replies: 11)

Q: Hello everyone,
   I just finished the first module. I managed to set up Docker, Postgres, GCP, and Terraform Locally, but as I finished the module I realized that all I was doing was following the steps you provided without fully understanding the logic behind them. It felt like I was memorizing the steps and the commands rather than truly grasping how and why these tools work together. Especially on the GCP-Terraform part
   I can repeat the same steps using the exact examples you used in the course, but I won’t be able to apply them to different scenarios.
   So, I have two questions please:
   1) Is t ...

A: you need to understand what you do and the bigger picture , and how they link
   ---
   *Terraform*, under the hood, is merely calling the specific provider (GCP / AWS / Azure / etc) for creating the resources. So, fully understand what it does under the hood, would take you months for a *single provider*, what you have to know is *where* and *how* you're gonna find the recipes to create each specific resource on a given cloud provider.
   
   For instance, on GCP, for the Container Registry (GCR), you need to follow this (https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_registry), while for creating a bucket on Object Storage (GCS), you need this (https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket)
   
   OTOH, for the Container Registry on AWS, you need this (https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecr_repository), while the Object Storage (S3) requires this (https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket)
   
   If you're looking to know more of Terraform and how to modularize your code, you'd have to look for other resources online, as it's not t ...

---

## Certificate / passing criteria (136 threads)

### [2025-01-09] Marios Moumouris (replies: 3)

Q: Hi guys, one questions regarding the cohort: do we have to participate in any live sessions in order to obtain the certificate? Or just by submitting our assignments on time is enough. Thank you! : )

A: You just need to complete and pass the final project to get the certificate.
   ---
   Thank you!
   ---
   I didn't know that we would be certified in the cause, the bootcamp is  free of charge.. thats so nice to hear it.

### [2025-01-13] Yash Sharma (replies: 5)

Q: @user for week 2, can i use mage or i have to stick with kestra to get the certificate?

A: Hey, @user! Here you go:  You can use Mage for Week 2 of the Data Engineering Zoomcamp. The course is designed to allow you to learn how to use the Mage platform for workflow orchestration, and it specifically focuses on authoring and sharing data pipelines with Mage. As long as you complete the required assignments and projects using Mage, you should be able to earn your certificate. If you have any further questions or need assistance with Mage, you can reach out on Slack.
   ---
   You can. We recommend using kestra, we made it really easy to use, the videos are high quality + much easier setup
   
   + from a job market perspective, you are better off with kestra
   ---
   Got it, thank you! How is kestra better from a job market perspective? Coming from a beginner
   ---
   compare GitHub stars of kestra vs mage
   
   the company is also in a much better shaped in terms of Enterprise adoption (doing well on kestra side) while mage has just launched their first commercial product like ~2 months ago (+ apparently faked their GH stars acc. to Dagster blog :clown_face:)
   ---
   Oh I didnt know kestra was much ahead of Mage. I thought it was just a very new tool in the market. Given new kestra $8m funding in 2024  ...

### [2025-01-17] Ayushi Sharma (replies: 6)

Q: Hello, Can someone tell me how can I fetch my certificate (Cohort-2024)?
   I am getting Access Denied error.
   Someone please help

A: Did you pass the course?
   ---
   Hey Alexey. Yes I passed the course in Cohort 2024 batch but did not save the certificate
   ---
   My Email ID: <mailto:ayushi.2210sharma@gmail.com|ayushi.2210sharma@gmail.com>
   ---
   https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/certificates.md did you try that?
   ---
   I did. Let me try again
   ---
   I got it now. Thanks much Alexey!

### [2025-01-20] Mer Arnel Manahan (replies: 1)

Q: @user do we need to set up the Virtual Machine to get the certificate?

A: Hey, @user! Here you go:  Setting up a Virtual Machine (VM) is not a requirement to obtain the certificate for the course. You can complete most of the course work without using a cloud environment, as everything except BigQuery can be run locally. If you prefer to work on your local machine, you can do so, and you can complete the course entirely without needing to set up a VM. Therefore, as long as you complete the required coursework, you will be eligible for the certificate regardless of your environment setup.

### [2025-01-22] Till Meineke (replies: 8)

Q: :alert: please be careful with our FAQ (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?tab=t.0#heading=h.pvlsdfiupcjk)
   
   I just had to restore this from beginning of January, not sure what else is broken
   
   
   > Course - how many Zoomcamps in a year?
   > There are multiple Zoomcamps in a year, as of 2025. More info at DTC Article (https://datatalks.club/blog/guide-to-free-online-courses-at-datatalks-club.html).
   > However, they are five separate courses, estimated to be during these months:
   > 1. Data-Engineering (Jan - Apr)
   > 2. MLOps (May - Aug)
   > 3. Machine Lear ...

A: @user timestamp 22 January, 04:51 of FAQ seems ok, but 22 January, 06:26 is already broken with changed text sizing
   ---
   Thank you!
   ---
   btw, thanks for releasing the 90 days limit here in slack
   ---
   I wish I had anything to do with it, but it's just slack randomly giving pro trial every now and then
   ---
   somebody broke the FAQ again, now the ZoomQABot stopped working
   &gt; There was an error: list index out of range
   ---
   Oh no =( did you revert it?
   ---
   no I asked Alex Litvinov
   ---
   people keep misusing the FAQ
   
   now there is a block of 100 empty lines

---

## Final project rules / scope / dataset (115 threads)

### [2025-01-14] HyperToast (replies: 5)

Q: @user for the DE Zoomcamp, can I present the final project without using GCP, AWS or Azure? More like local implementation.

A: Hey, @user! Here you go:  You can present your final project without using GCP, AWS, or Azure. The course allows you to choose alternatives to the technologies covered, including local implementations. However, if you use tools that weren't covered in the course, you should explain what those tools do. This flexibility enables you to tailor your project based on your preferences and the tools you're comfortable with.
   ---
   @user can you suggest alternatives to BigQuery?
   ---
   Hey, @user! Here you go:  I don't think I have an answer for this; you'll have to ask your fellows or instructors.
   ---
   for running things locally, duckdb is a possible alternative
   ---
   I see, thank you @user 
   
   The thing is i have some capacity in my on prem homelab. I'd love to utilize that instead of cloud. 
   
   Chatgpt suggests minio for the data lake store. 
   
   What are your thoughts?

### [2025-01-21] Abdelali (replies: 3)

Q: Hello everyone
   Can someone please help me with the *dbt-cloud setup* for module 4
   I tried to create a project on dbt, I followed the steps one by one, did the connection with bigquery, then there was a step called: *Development credentials,* it has three fields to fill: Dataset, Target name and Threads. Those fields are autofilled for me, should I keep them like that? or should I change the name of the dataset to the name of my bigquery dataset?
   Thanks in advance

A: You should use the BigQuery dataset name that you created with Terraform on module 1
   ---
   Alright thank you so much Bruno
   ---
   np!

### [2025-01-24] Madalena Neves (replies: 1)

Q: Hi, for this course do we need to deliver all homework assignments to get a certificate? Or the final project with peer review is enough? Couldnt find this on the FAQ doc.

A: Final project with peer review is enough

### [2025-02-07] Thorben Siebeneichler (replies: 17)

Q: Hey there, I have a more general question, maybe towards those that have already done some data science with third party data:
   For my final project of the course I would like to work with some open data of a national non-profit organization. They offer a free api under CC0 1.0 license, so permission for use is there. However, fetching a reasonable set of data will boil down to a few hundred, maybe a couple thousand requests. I am worried, that my ingestion pipeline would get blocked by DDoS protection, and I don’t wanna cause issues for them as well. Is there any experience with the ethics of  ...

A: Sounds logical to me. Maybe also include the process for gathering the data in your documentation. Scaping is and will continue to be a grey area. Do it for profit = crime. Do it for personal project = probably not a crime. Do it if you are OpenAI = Get valued at $260 Billion.
   ---
   Do they provide an api documentation? Maybe they say something about request rate and intervals. I would stick to their limits :wink: 
   
   You could setup (or hire) some proxys to hide your ip to not get blocked. Sometimes changing browser header helps when scraping. Or you could tell your router to reconnect to get a new ip. It doesn’t sound likely you would need these techniques
   ---
   Yeah, they offer api documentation but no mention of any rate limits.
   
   If you are curious, this is the API I want to go for: https://www.abgeordnetenwatch.de/api
   
   It is in german, but luckily translators are a thing :slightly_smiling_face:
   
   AFAIK, there are no contraints for the minimum size of the dataset our project needs to be based on, right? their filters allow for 1000 entities downloaded per request, so if I limit myself to a few dozen requests I could still get a meaningful set of data to show some stuff with, and nobod ...

### [2025-02-16] Viktorija Alexeeva (replies: 1)

Q: @user, creating a project in dbt-cloud, in development creds should we write existing name of dataset(which has tables with data for 2019 and 2020 trips) or we should use new dataset name? i don't understand, dbt will always create new separate dataset for his models or can use existing?

A: Hey, @user! Here you go:  In dbt Cloud, you should use the BigQuery dataset name that you created with Terraform in Module 1. This dataset is where you will run and build your models during development. If you have existing datasets with tables that contain data for 2019 and 2020 trips, you can use that existing dataset as long as it is properly configured for dbt.  dbt typically creates a new schema (dataset) for its models during development, which is usually named in the format `dbt_&lt;first initial&gt;&lt;last name&gt;`. However, you have the option to specify an existing dataset if it aligns with your development needs.   To ensure you don't encounter multiregion errors, make sure that the dataset you are using is created in the same region as your source data. If your source dataset is located in a specific region (e.g., EU), you should specify that same region for your dbt configuration.   If you decide to use the existing dataset, ensure that it is correctly referenced in the development credentials section of your dbt Cloud project setup.

---

## Homework submission / form / link (112 threads)

### [2025-01-01] Horeb SEIDOU (replies: 4)

Q: Hi everyone! :wave: I’m working on the Data Engineering Zoomcamp 2025 at my own pace. I just completed Week 1 and I’m ready to submit the homework. Could someone guide me through the process for submission? Thanks in advance!

A: After course starts on Jan 13th check out homework (https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2025) on github and course management platform (https://courses.datatalks.club/de-zoomcamp-2025/) for submission. (make sure you are logged in)
   
   you can check and compare last year cohort (https://courses.datatalks.club/de-zoomcamp-2024/) and leaderboard (https://courses.datatalks.club/de-zoomcamp-2024/leaderboard) on the platform for inspiration for your repo.
   
   Create a repo for HW, do written HW (in code if possible), fill in required fields on platform, add Homework URL to your repo/code,
   
   Hit `submit/update` button, and wait till HW is scored after due date or Alexey closes the form.
   
   (optional) for leaderboard: add Learning in public (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/learning-in-public.md) links (up to 7), and describe how you improved the FAQ (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing).
   
   (optional) fill in time spent on lectures and homework (hours)
   ---
   Great Lerner :+1:, congrats for finish homework
   ---
   The 2025 cohort is not started yet, are we required to d ...

### [2025-01-12] U08768VPL74 (replies: 5)

Q: guys i want to ask that this submitted link for Module 1 Homework: Docker & SQL cannot access? i try to figure it out but still error when i try to get in that link. Then, will the deadline for each homework in DE Zoomcamp 2025 be the same as the deadline for homework in DE Zoomcamp 2024?

A: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1 (https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1)
   ---
   Where is your link from?
   ---
   The link on github is broken, it says hw01 instead of hw1
   ---
   I created a pull request for that issue :slightly_smiling_face:
   ---
   Merged! Thank you!

### [2025-01-12] Mian Muhammad Ashhad (replies: 1)

Q: Hi everyone. Is there a schedule given to watch the lectures and submit the homework? I have university work besides this course so I just want to follow a pre-made schedule if that is possible.

A: Yes
   
   https://courses.datatalks.club/de-zoomcamp-2025/ (https://courses.datatalks.club/de-zoomcamp-2025/)

### [2025-01-13] Muyiwa Oladimeji (replies: 2)

Q: Which option between GitHub (https://courses.datatalks.club/accounts/github/login/) and Slack (https://courses.datatalks.club/accounts/slack/login/) is best for login to the Homework portal to submit the homework - https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1

A: i signed in with slack, couldn't login with github
   ---
   I just used Google

### [2025-01-14] Abrham Addis (replies: 2)

Q: Hi, team
   I'm just getting started on the courses. Does anyone know about the homework and where to submit it?

A: Hello!
   You can find them on the bootcamp's repo:
   https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2025
   ---
   Thanks!

---

## Joining mid-cohort / late start / what did I miss (108 threads)

### [2025-01-06] Suzan (replies: 7)

Q: Hello Team, am new here! What did i miss? :face_with_open_eyes_and_hand_over_mouth:

A: nothing, we start next week with 2025 cohort. you can already prepare your environment and start with module 1, to be set up and ready to go
   ---
   Okay thanks.
   ---
   Installation instructions for Mac :computer: ?
   ---
   FAQ (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing)
   try it out, if something is not working, ask (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/asking-questions.md) again
   ---
   Please use threads to keep the discussion more organized: https://datatalks.club/slack/guidelines.html#taking-part-in-discussions
   ---
   can anyone share the module 1 link ? or where can i find it ?
   ---
   see Repo (https://github.com/DataTalksClub/data-engineering-zoomcamp)

### [2025-01-06] Tiến Nguyễn Văn (replies: 1)

Q: Just arrived! What’d I miss?

A: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1736166958585549

### [2025-01-07] Lamine (replies: 2)

Q: can i still participate?

A: No you didnot.
   
   The course starts 13th Jan
   ---
   Please use threads to keep the discussion more organized: https://datatalks.club/slack/guidelines.html#taking-part-in-discussions

### [2025-01-18] James (replies: 1)

Q: I started doing the course in my own time, but lost track over Christmas. Is it too late to sign up to the 2025 cohort? @user

A: Hey, @user! Here you go:  It is not too late to sign up for the 2025 cohort. The registration form for January 2025 is still available, and you can register even if you lost track of the course during Christmas. The cohort is set to be live, and the planned end date is somewhere in April. You should be able to catch up and participate fully in the upcoming sessions.

### [2025-01-21] Chiamaka Okpe (replies: 4)

Q: Hi guys, I just joined the bootcamp. Do you think it'd be possible for me to complete the first module and submit the assignment before due date?

A: Hello Okpe, I am also joining today, but believe to catch up soon, so will you.
   ---
   Thank you!!
   ---
   I am also joining today, we will catch up
   ---
   Yes we will!! Thank you Azi-love

---

## NYC taxi dataset URL / 403 forbidden / where to get data (99 threads)

### [2025-01-06] Celine F (replies: 6)

Q: Hi team, I am getting 403 Forbidden Error after running `wget https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv` as instructed in the Setting up the Environment video (https://www.youtube.com/watch?v=ae-CV2KfoN0&amp;list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&amp;index=15). Is anyone else also getting it?

A: Please check the FAQ (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit)
   ---
   @user use this instead:
   https://github.com/DataTalksClub/nyc-tlc-data
   ---
   Hi @user How were you able to solve this issue? I'm facing the same.
   
   Did you just download the csv without using wget?
   ---
   We have a backup, so use it instead: https://github.com/DataTalksClub/nyc-tlc-data
   So the link should be https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz
     Note: Make sure to unzip the “gz” file (https://linuxize.com/post/how-to-unzip-gz-file/) (no, the “unzip” command won’t work for this.)
   “gzip -d file.gz”
   ---
   Btw, you guys can read the `.csv.gz` directly with pandas or even polars, without the need to even download with `wget` :
   
   with pandas:
   ```import pandas as pd
   
   endpoint = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
   df = pd.read_csv(endpoint, engine="pyarrow")```
   with polars:
   ```import polars as pl
   
   endpoint = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
   df = pl.read_csv(endpoint)```
   With polars you'd  ...

### [2025-01-09] Merilyn Chesler (replies: 1)

Q: For Module #1, am I free to use the NY Taxi Parquet file source and store the data directly into postgres without converting to csv? Thanks.

A: Yes if you want

### [2025-01-12] Luis Ruiz (replies: 1)

Q: why am i getting this error when I try to download the data.
   ```HTTP request sent, awaiting response... 403 Forbidden
   2025-01-12 19:04:59 ERROR 403: Forbidden.```
   @user

A: Hey, @user! Here you go:  The error "403 Forbidden" indicates that access to the requested resource is denied. This commonly occurs for a few reasons:  1. **Permission Issues**: The server hosting the data may have restrictions that prevent certain requests, such as those coming from scripts or automated tools like `curl`.  2. **User-Agent Restrictions**: Some servers check the User-Agent header of the request to determine if it is coming from a browser or a script. If it appears to come from a script, the server might block the request.  To bypass this issue, you can try specifying a User-Agent in your `curl` command. Here is an example of how to do this:  ```bash curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" -o yellow_tripdata_2021-01.csv.gz https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz ```  Alternatively, since there is a known issue with downloading the 2021 data directly from the TLC website, you can use the backup link provided in the course materials: https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_20 ...

### [2025-01-13] Merilyn Chesler (replies: 28)

Q: I'm getting the taxi_zone_lookup.csv directly from the NY website (https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv).  Is it ok if I pre-convert the taxi_zone_lookup.csv to parquet for HW 1 and use the parquet file for my hw submission?  Thank you.

A: I was doing HW1 on this question earlier. It did not ask for any code or specify any method to put the taxi_zone_lookup data into postgres. So I assumed I can do whatever as long as I can get it into postgres.
   
   I don't think it is necessary to convert to parquet though. It's just a 200+ row table to insert into postgres.
   ---
   @user I mean... ""you can""", but we generally don't use parquet for such small files like that. You're gonna have the opportunity to write it to parquet on week2 / week3 if you want to.
   
   The homework answered were created based on the CSV we have  available in here:https://github.com/DataTalksClub/nyc-tlc-data
   
   Just make sure you the file you got is the same, and you'll be fine :slightly_smiling_face:
   ---
   @user i was using green taxi, to follow same as video should be yellow taxi but  we need load all years on postgresql db or no ??
   ---
   @user for the homework, you're gonna be using, these two only:
   • https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
   • https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
   ---
   only one year or all monts from Yellow taxi data from 2019 to 2021
   - ...

### [2025-01-14] David Kirk (replies: 8)

Q: Hey everyone!  yet another technical question here. I am running into issues using Jupyter to run upload-data notebook.
   *Context:*  I have been using the youtube video guide https://youtu.be/ae-CV2KfoN0?si=dLQ-w4z-Jf4NJq9O and ran into no trouble up until 37:15 when came the time to use Jupyter (which I have nver used before)
   
   *Issue:* I unable to get the schema to upload the same way Alexey showed. Additionally, when I press play on jupyter I am now getting an error saying `PD is not defined` , however at the time of the jupyer code I do see pandas being imported
   
   could someone please give me ...

A: wait.. what.. ? "unable to get the schema to upload" ?? What does that mean??
   ---
   Can you link us to your code and point where it is breaking ?
   ---
   what i meant is that when I run
   
   ```pgcli -h localhost -U root -d ny_taxi```
   followed by the command `\dt` , I am not seeing anything populated in the schema
   
   I am in truth not sure where it it breaking since I was following the youtube video and I have never used Jupyter before
   ---
   Can you take a screenshot of WHERE the code breaks  on your jupyter environment?
   ---
   i may be getting somewhere, I was watching the video but didn’t see that in the course repo we have a different wget command. I will let you know if I am still struggling. Right now I am running into a `ModuleNotFoundError: No module named 'psycopg2`’ error so simple enough
   ---
   annnd that was it! thanks so much @user for being so reponsive. I am adding my solution to my original comment in case someone runs into the issue. It’s my fault for never having used Jupyter
   ---
   FWIW on the data file inspection I downloaded the parquet file and used pandas to convert from parquet file to csv file. In order do that I needed to install psycopg2, pyarrow, and fastparquet.  once those ar ...

---

## Spark / PySpark / cluster (95 threads)

### [2025-01-04] Gloria Quiceno (replies: 5)

Q: @user in spark python script trying to handle raised exceptions and have the if else statement continue to the next iteration without breaking. how can error messages be handles in spark? For instance:
   
   ```try:
           # read parquet into environment 
           df = spark.read \
               .option("header", "true") \
               .parquet(filename)
           print(f'loaded {filename} in spark session with dimensions ({df.count()}, {len(df.columns)})')
           return df
   except Py4JJavaError as e:os.system(f"rm -r {filename}")
           return (f"{filename} not a valid parquet file, aborted pipeline!! ...

A: Hey, @user! Here you go:  To handle exceptions in a Spark Python script and continue to the next iteration without breaking, you can use a `try-except` block effectively. The example you provided is almost correct, but it has a small issue with indentation and should properly return a value on exception handling. Here's a revised version that addresses these points:  ```python from pyspark.sql.utils import Py4JJavaError  def read_parquet(filename):     try:         # Read parquet into environment          df = spark.read \             .option("header", "true") \             .parquet(filename)         print(f'Loaded {filename} in Spark session with dimensions ({df.count()}, {len(df.columns)})')         return df     except Py4JJavaError as e:         os.system(f"rm -r {filename}")         print(f"{filename} not a valid parquet file, aborted pipeline!!!!")         return None  # Return None or handle as necessary to indicate failure  # Usage files = ["file1.parquet", "file2.parquet", "invalid_file.parquet"] dataframes = []  for file in files:     df = read_parquet(file)     if df is not None:         dataframes.append(df) ```  In this code snippet: - The `read_parquet` function attem ...

### [2025-01-10] Jobert Gutierrez (replies: 3)

Q: Hey colleagues, as far as a I understand we prefer spark over python when the task requires dealing with big data. But is there a tangible threshold to start using spark?

A: Probably when time of processing X amount of data without Spark is unreasonable. Between hours and days
   ---
   Makes sense. Thanks
   ---
   I have other follow-up questions:
   
   I wonder what is available between Pandas and Spark. Are those DuckDB and Polars?
   
   If I have no Spark cluster but need to process data ten times faster than my current processing with Pandas (including multithreading and pooling), will DuckDB or Polars achieve this?
   
   Should I jump straight into them?
   
   I am not sure.

### [2025-01-23] Imran (replies: 6)

Q: Hi all, I have setup the env on GCP machine as following the video by Alexey. I have installed Conda, Terraform, git, Docker etc.
   But later in videos related to Spark, he setup the python  path from Spark to allow pyspark import in Jupyter Notebook.
    I am unable to import pyspark in jupyter notebook as my python is pointing to Conda, and not Spark.
   What should I do?

A: What do you mean your python pointing to conda, not spark? Did you add pyspark to pythonpath?
   ---
   I have added these to bashrc:
   export SPARK_HOME=~/spark/spark-3.5.1
   export PATH=$SPARK_HOME/bin:$PATH
   export PATH=$SPARK_HOME/sbin:$PATH
   export MAVEN_HOME=/opt/maven
   export PATH=$MAVEN_HOME/bin:$PATH
   export PYTHONPATH="${SPARK_HOME}/python/:$PYTHONPATH"
   export PYTHONPATH="${SPARK_HOME}/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH"
   
   
   But I run which python, I get this path:
   (base) imran@de-zoomcamp-24:~$ which python
   /home/imran/anaconda3/bin/python
   ---
   Also when I run python in terminal, I am able to import pyspark.
   But unable to import pyspark when I do it in Jupyter notebook
   ---
   `which python` should still point to the same executable, it's expected
   ---
   You need to run jupyter in the same terminal
   ---
   It's working now  Thanks

### [2025-01-24] Koray Kanut (replies: 5)

Q: How to adjust PATH so that /usr/local/Cellar/openjdk@11/11.0.12 shows up in the finder to install Java correctly before setting up Spark? @user

A: Hey, @user! Here you go:  To adjust the PATH so that `/usr/local/Cellar/openjdk@11/11.0.12` shows up correctly in Finder after installing Java, you need to add the necessary environment variables to your shell configuration file. Here are the steps:  1. Install Java using Homebrew if you haven't already:     ```bash    xcode-select --install    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"    brew install java    ```  2. Open your terminal and edit your shell configuration file. If you are using Bash, this will be `.bash_profile`, and if you're using Zsh, it will be `.zshrc`. You can open it with a text editor, for example:     ```bash    nano ~/.bash_profile    ```     or     ```bash    nano ~/.zshrc    ```  3. Add the following lines to set the `JAVA_HOME` and update the `PATH`:     ```bash    export JAVA_HOME=/usr/local/Cellar/openjdk@11/11.0.12    export PATH="$JAVA_HOME/bin/:$PATH"    ```  4. Save the changes and exit the text editor.  5. To apply the changes made to your shell configuration, run:     ```bash    source ~/.bash_profile    ```     or     ```bash    source ~/.zshrc    ```  6. Confirm that Java is correctly insta ...

### [2025-01-26] Ashutosh Srivastava (replies: 11)

Q: @user While working on the Spark with SQL lesson, I'm getting the below error -
   ```Parquet column cannot be converted in file file:///home/ashtava/notebooks/data/raw/yellow/2023/02/yellow_tripdata_2023_02.parquet. Column: [passenger_count], Expected: double, Found: INT64.```
    I'm reading my file from a location `data/raw/yellow/2023/01` and trying to save it to another after processing and enforcing a custom schema defined below -
   ```schema_yellow = types.StructType([
       types.StructField('VendorID', types.IntegerType(), True), 
       types.StructField('tpep_pickup_datetime', types.TimestampNTZ ...

A: Hey, @user! Here you go:  The error you are encountering is due to a mismatch between the expected data type and the actual data type of the `passenger_count` column in the parquet file. The error message indicates that the parquet column is expected to be of type `double`, but it is found to be of type `INT64`.   In your schema definition, you have specified `passenger_count` as `types.DoubleType()`, which expects a floating-point number. However, the parquet file you are reading has this column defined as an integer type. To resolve this issue, you should change the schema definition for the `passenger_count` column to `IntegerType()` instead of `DoubleType()`.   Here's how you can modify the schema:  ```python schema_yellow = types.StructType([     types.StructField('VendorID', types.IntegerType(), True),      types.StructField('tpep_pickup_datetime', types.TimestampNTZType(), True),      types.StructField('tpep_dropoff_datetime', types.TimestampNTZType(), True),      types.StructField('passenger_count', types.IntegerType(), True),  # Change this line     types.StructField('trip_distance', types.DoubleType(), True),      types.StructField('RatecodeID', types.DoubleType(), True), ...

---

## Course start / cohort schedule (89 threads)

### [2025-01-02] Doreen Wanyama (replies: 1)

Q: Greetings everyone.  Has the 2025 zoomcamp already started ?

A: Not yet till 13th Jan

### [2025-01-02] Donatus (replies: 7)

Q: The class is starting on the 13th are we using the previous videos or there will be a new session for us?

A: To the best of my knowledge the videos that are currently available will be the ones used.
   ---
   Alright, so that means there won't be any class that we can join?
   ---
   Can you be more specific what you mean by "class"?? You are in this year's cohort.
   ---
   The class is starting on the 13th so I mean if there will be recorded sessions so we can watch again?
   ---
   Those will be recorded yes. Not necessarily "lessons" but more Q and A that Alexey does to answer students questions.
   ---
   Okay, thank you for the clarification.
   ---
   I updated some pins for this channel for cohort 2025

### [2025-01-03] Melchior Pedro-Rousselin (replies: 6)

Q: Hi, when is the official zoomcamp startdate ?

A: https://github.com/DataTalksClub/data-engineering-zoomcamp
   ---
   Ok thank you. And the link for the lauch is the right one ?
   ---
   oui. we will also share the links in the telegram channel and per email
   ---
   Thanks
   ---
   Do we have prep work to do before ?
   ---
   Feel free to start(Videos are available already)/get the tools setup. Jumping in is probably the best way to see where you may be lacking in knowledge. Python, SQL, Cloud, Docker etc.

### [2025-01-04] Prashant Madaan (replies: 1)

Q: Has the course already started ?

A: Official it's starting on January 13 but week 1 module remains same from previous cohorts.

### [2025-01-05] Shilpa Leo (replies: 3)

Q: Hello from Singapore! I've registered for the DE course starting next week. I added the Google calendar as well, but realized the timings are not Asia friendly. The launch happens at midnight SG time. :disappointed:
   Will the live sessions be recorded or how can folks like me seek support given the time diff? Thanks!

A: yes, it will be. we can also see the passed recorded live session as well.
   ---
   @user All video classes are already pre-recorded. The live sessions we'll have are mostly for Q&amp;A  and (maybe) live sessions for the workshops
   
   Start here: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   
   Video links are already embedded
   ---
   Will there be no further updates to videos? So I can move on my own (hopefully faster) schedule.

---

## Project resubmission / second / last attempt (89 threads)

### [2025-01-17] Merilyn Chesler (replies: 2)

Q: Once I submit my homework, I can resubmit to add optional links, right? @user

A: Hey, @user! Here you go:  You can resubmit your homework to add optional links. This is typically allowed once you have submitted your initial homework, as long as you adhere to the submission guidelines and deadlines. It's a good practice to check if there are any specific instructions regarding resubmissions in the course materials or announcements.
   ---
   You can update your submissions until the form is closed

### [2025-02-16] texnh (replies: 2)

Q: @user why do we have 2 project attempt deadlines?

A: Hey, @user! Here you go:  There are two project attempt deadlines to allow students a chance to pass the course even if they miss the first deadline or fail their initial submission. This structure is designed to accommodate circumstances such as time constraints, illness, or other engagements that might prevent timely submission. If a student does not submit or fails the first attempt, they can utilize the second attempt for a final chance to submit the project and successfully complete the requirements for the course.
   ---
   Or you can gain points for the leaderboard by doing a second project

### [2025-02-24] Austin McDaniel (replies: 4)

Q: Happy to be following the course, and appreciative of what you folks are doing.
   
   That being said, this past week my father was in the hospital. Between that and my interview studies, I've been a bit derailed from the course.
   
   I haven't started the 4th hw and I missed the workshop.
   
   Any suggestions on following and getting back on track for the rest of the course? I intend to still do the project and attempt to get the certification.

A: workshop is quickly done.
   
   week4 may take some time, but can be done quickly (https://datatalks-club.slack.com/archives/C01FABYF2RG/p1740253464900509?thread_ts=1740248357.766509&amp;cid=C01FABYF2RG)
   
   hope your father will get well soon :bouquet:
   ---
   you only need to pass the project to get the certificate, hw points are only relevant for leaderboard
   ---
   Fast recovery to your father!
   ---
   I hear a lot of people struggling with the videos so I'd like to recommend Manuel Guerra's course repo (https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes) this module especially.

### [2025-03-05] Nguyễn Tuấn Huy (replies: 1)

Q: hello, I see that Project Attempt 1 (https://courses.datatalks.club/de-zoomcamp-2025/project/project1) has been opened for submisson, but I have no idea about any requirements about that. Did I miss email notifications ? Please tell me. Thank you

A: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/projects
   
   and
   
   https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/project.md

### [2025-03-05] Linh Mai Hai (replies: 1)

Q: I joined zoomcamp today and finished NY Taxi Module 1. Just wondering if I can submit Project Attempt 2 after April 14 ?

A: If the form is closed on the course management platform, you can’t submit anymore.

---

## Windows / WSL / Mac M1 / OS-specific (81 threads)

### [2025-01-04] Akmal Fadhlurrahman (replies: 3)

Q: This is the Nth time I tried to follow DE Zoomcamp from start to finish, and I'm excited! One question, maybe for @user, is Terraform a CLI-only tools? because I tried to install it on my Windows machine and it does not show any standard installation GUI, only a glimpse of a black terminal before it fades away.

A: Hey, @user! Here you go:  Terraform is indeed a CLI (Command Line Interface) tool, which means it does not come with a standard installation graphical user interface (GUI). Instead, it operates entirely in the terminal. When you install Terraform on your Windows machine, you will interact with it through command-line commands. The fleeting appearance of a black terminal you mentioned is likely due to executing the installer directly, which may not provide a GUI.  To use Terraform effectively, you should open a command prompt or PowerShell window and run Terraform commands there. Make sure you have added Terraform to your system's PATH so that you can execute it from any terminal window. You can verify the installation by running the command `terraform version` in the terminal to see if it returns the version number, indicating that Terraform is installed correctly.
   ---
   How do I add terraform to system PATH? @user
   ---
   Hey, @user! Here you go:  To add Terraform to your system PATH, you need to follow these steps based on your operating system:  For Windows: 1. Download the Terraform executable from the [Terraform website](https://www.terraform.io/downloads.html). 2. Unzip the downloa ...

### [2025-01-05] Dehao Zhang (replies: 4)

Q: Hi team, I was following video 1.2.2 and ran into issues with mapping volumes. I am using WSL2 on windows. Initially when I used the same format described in the video I got an "Error response from daemon: invalid mode: /var/lib/postgresql/data." message. After I switched to another format it ran fine with "database system is ready for connection" but my ny_taxi_postgres_data local folder is not populating as shown in the video (i.e., still empty after the container starts running). Should I be concerned? I am able to use pgcli to connect to the db fine, but just want to know if unable to get  ...

A: Hard to say. You might not really be coming back to that piece after running it so it won't matter if the data is actually persisted. Think you'd want to spend some time with ChatGPT giving it your configuration, the symptoms and any issues you are running into if you wanted to resolve it. You could also just use docker volumes and cut out the bind mounts all together.
   ---
   https://www.youtube.com/watch?v=olUKRq-FVyo
   ---
   @user Thank you so much for your thoughts and its good to know that we might not need to come back to that. I did spend some time with ChatGPT on this and unfortunately the suggestions didn't quite work. I tried "docker volume create" which also worked but didn't populate the folder either.  In general is it a best practice to set this up to enable data persistence outside of container?
   ---
   Docker volume won't populate a folder as it is a docker volume. As far as best practice it's hard to say. In the "real world" you would probably be running a Managed Postgres Instance and wouldn't need to worry about it. Between a bind mount and a docker volume you would probably be running on Linux for a "real personal project" so the bind mount would be a bit easier than trying ...

### [2025-01-06] Dehao Zhang (replies: 5)

Q: Hi all. I am using WSL2 on Windows and I was trying to install pgcli but when I tried "pip install" I would get an error message saying "This environment is externally managed" and the suggestions such as creating a virtual environment didn't work either. "sudo apt install" worked. Should I always install packages that way going forward? I saw that using break-system-packages can override this but I heard it's not recommended. Thanks in advance

A: The "correct" way is to create a virtual environment. This is a valuable skill to have and definitely best practice. Messing with the system Python Packages could disrupt/corrupt/make the Linux subsystem unusable........ yeah, I'd just break-system-packages though. :sweat_smile: If you do go the virtual environment route, I'd suggest looking at UV.
   ---
   @user so something like python -m venv venv fixes this right?
   ---
   Yes it should. I believe this is a feature of Python 3.13. The way it comes, it does not simply let you install packages into the system install of Python.
   ---
   I tried creating a virtual environment in WSL2 using what @user described but got an error : "mypath/bin/python3', '-m', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1.". Chatgpt told me to check on ensurepip, which I did and the response was "ensurepip is disabled in Debian/Ubuntu for the system python." I have tried reinstalling Python too but still face the same issue. Tried to install uv too but it gave a message: "error: This revision of snap "astral-uv" was published using classic confinement and thus may perform arbitrary system changes outside of the security sandbox that sna ...

### [2025-01-07] Abdelali (replies: 9)

Q: Hi, I’m using Docker Compose to set up PostgreSQL and pgAdmin containers, but after restarting, I lose my pgAdmin configuration. I created a `data_pgadmin` folder for persistence, but when I try to change its permissions using `sudo chown 5050:5050 data_pgadmin`, I get the error: 'Sudo is disabled on this machine. To enable it, go to the Developer Settings page in the Settings app.' How can I fix this on Windows? @user

A: Hey, @user! Here you go:  To fix the issue of losing pgAdmin configuration after restarting your Docker containers on Windows, you should utilize Docker volumes instead of trying to change folder permissions with `sudo`, which is not available in your environment.  You can modify your `docker-compose.yaml` file to define a volume for pgAdmin. This will help persist the configuration without needing to alter permissions on the host file system. Here's an example of how to set it up:  ```yaml services:   pgadmin:     image: dpage/pgadmin4     environment:       - PGADMIN_DEFAULT_EMAIL=admin@admin.com       - PGADMIN_DEFAULT_PASSWORD=root     volumes:       - pgadmin_data:/var/lib/pgadmin     ports:       - "8080:80"  volumes:   pgadmin_data: ```  By using a Docker volume (`pgadmin_data`), Docker handles the permissions internally, which avoids issues related to file system permissions on Windows. You do not need to run `sudo chown` commands, as the volume will be managed by Docker, ensuring that your pgAdmin configuration is preserved across container restarts.   Additionally, if you're using WSL, it is recommended to use Docker volumes to resolve any permission-related issues, as th ...

### [2025-01-07] Chinaemerem Obidoo (replies: 17)

Q: Docker Desktop - Unexpected WSL error
   An unexpected error occurred while executing a WSL command.
   Either shut down WSL down with `wsl --shutdown`, and/or reboot your machine. You can also try reinstalling WSL and/or Docker Desktop. If the issue persists, collect diagnostics and submit an issue ⁠ (https://docs.docker.com/desktop/troubleshoot/overview/?utm_source=docker_desktop_error_dialog#diagnose-from-the-terminal).
   ```deploying WSL2 distributions
   ensuring data disk is available: exit code: 4294967295: running WSL command wsl.exe C:\Windows\System32\wsl.exe --mount --bare --vhd ```

A: There isn't anything else we can say other than *follow the instructions you were given:* 
   
   `Either shut down WSL down with wsl --shutdown, and/or reboot your machine. You can also try reinstalling WSL and/or Docker Desktop. If the issue persists, collect diagnostics and submit an issue ⁠.`
   ---
   I have done all these and it still doesnt work
   ---
   Did you install WSL2 before installing Docker ?
   ---
   Yes. I have one so
   ---
   *Did you make sure it (WSL2) was working properly before you tried to install Docker, though ?*
   ---
   yeah. i have checked from the command line
   ---
   That's very unlikely
   ---
   Honestly speaking now, debugging this blindly won't do. I don't even know what went wrong as I don't have your error logs
   
   Best advice I can give at this point is:
   • Make sure your WSL2 is installed properly (if it is, you should be able to open it up and issue commands with user that was created during the install - *if not - reinstall it)*
   • Do a fresh install with Docker Desktop (uninstall it all, and reinstall)
   From my perspective, it looks as in you might have overlooked or skipped a step,
   
   Also, what you can do is *collect the diagnose* (with the instructions you were provided with) to get a b ...

---

## Project deadline / extension / final attempt (81 threads)

### [2025-01-29] Tiago Costa (replies: 11)

Q: Hey @user, I'm thinking about the course, when does the project start and end? What is the deadline to start and finish the project for certification?

A: See course management platform (bookmarks), ok no dates for project on platform https://datatalks-club.slack.com/archives/C01FABYF2RG/p1734955873291289?thread_ts=1734898057.675589&cid=C01FABYF2RG
   
   2 weeks for project
   1 week evaluation
   ```if fail
     repeat```
   ---
   https://datatalks-club.slack.com/archives/C01FABYF2RG/p1737988119542099
   ---
   ok, but when will that day be? Do you have a date in mind? What is the date for the last homework? sorry for the questions
   ---
   Platform (https://courses.datatalks.club/de-zoomcamp-2025/) --&gt; last HW 11th Mar + 3 weeks = 1st April (round 1) , 22nd April (round 2)
   ---
   I'll add the dates to the platform - but please be aware that they are tentative and may change
   ---
   also note that the deadline that we show on the platform is for submitting the project, not for peer evaluation (so add one week)
   ---
   thank you :slightly_smiling_face:
   
   We can use Microsoft fabric for the project right, i mean to make all pipeline of data and bi for visual ?
   
   The project doenst have restrictions of tools right?
   ---
   Yes
   ---
   In this case, how should I submit the project later? I can copy the code from the fabric notebooks to a txt files,  and put images of the pipeline and ...

### [2025-02-16] Kashan Ahmed (replies: 1)

Q: what is the deadline to submit final project 1 and project 2?

A: There is only one project required for data Engineering Zoomcamp. However, you can upload it at first or second attempt. Check the course platform https://courses.datatalks.club/de-zoomcamp-2025/ (https://courses.datatalks.club/de-zoomcamp-2025/) 
   Ensure you are logged in to see the deadlines

### [2025-02-22] Hussain (replies: 3)

Q: Hi I need a bit of advice on the project any idea on the deadline and how to submit it ??? I assume we hace to share a github link but not sure ... any advice would be appreciated ?? thanks

A: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/5ad8dbb1e0425d14fce5e42270124d76d736d6f4/projects , you can find deadlines on the course website https://courses.datatalks.club/de-zoomcamp-2025/
   ---
   thanks for that am clear on the deadlines  but yet have no idea where to submit it .. i know its early but just asking
   ---
   how did you submit HW, if you did?
   
   there will be a link, when time comes. then you have two weeks for project submission and another week for reviewing three peer projects (mandatory  to pass the project)

### [2025-02-23] L (replies: 3)

Q: Hi, out of curious about the project deadline — what is the different expectation for the 2 attempts? Or we just need to choose one to submit? @user

A: Hey, @user! Here you go:  There is only one project required for the Data Engineering Zoomcamp. You have two attempts to submit it, but you only need to create and submit one project. The expectations for the two attempts are as follows: if you miss the first project deadline or fail your first submission, you have the opportunity to submit again for a second attempt. Essentially, the second attempt can be used if you either fail the first attempt or do not have the time to submit due to other commitments.
   ---
   Hey @user,
   do we have access to previous years projects for practice?
   ---
   Hey, @user! Here you go:  You can access previous years' projects for practice through the leaderboards on GitHub, which provide links to the projects. For example, you can find the projects from the 2024 cohort at this link: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/leaderboard.md. This resource will help you explore the work done in previous cohorts.

### [2025-03-04] Akhila Umma (replies: 1)

Q: @user I joined the zoom camp recently, do we have any deadline for final project ?

A: Hey, @user! Here you go:  Only one project is required for the Data Engineering Zoomcamp, which can be submitted in either the first or second attempt. The specific deadlines for the project are available on the course platform, which you can access at Course Management platform (https://courses.datatalks.club/de-zoomcamp-2025/). It is important to log in to view the deadlines.   The project work spans weeks one and two, while week three is dedicated to peer reviews. The course is expected to conclude on April 1st, 2025, which gives you a clear timeline for planning your project work and submissions.

---

## Live session timing / timezone / format (68 threads)

### [2025-01-11] Ziyad Ayman (replies: 2)

Q: Hey Guys,
   Should i start watching videos on youtube channel or just attend tomorrow's session?

A: Start watching the videos on the github repository. There won't be any live videos, I think only for the workshop.
   ---
   We'll have a launch stream tomorrow (Monday) at 17:00 CET

### [2025-01-11] Kristin Hooper (replies: 1)

Q: What do we need to get done before tomorrow’s Zoom session?

A: A python runtime and Docker at the very least

### [2025-01-12] Vijaya Solanki (replies: 2)

Q: looking forward to taking this course starting tomorrow. what time does this course start and how do we join the live stream?

A: Live stream Monday at 17:00 CET
   ---
   so is that 11am EST?

### [2025-01-12] Bhushan (replies: 4)

Q: Hello Team! :wave:
   I assume launch stream will start @4.30 AM IST? Is this correct?

A: 17:00 CET
   ---
   @user will we recieve any link or we can just go to youtube at 17:00 and check the live stream?
   ---
   You will receive a link but going to YouTube around 17:00 also works
   ---
   Thanks so much Alexey for the prompt help. Much appreciated.

### [2025-01-13] Akshay (replies: 2)

Q: hi everyone . When will course start in IST?

A: 21:30 Monday, Indian Standard Time (IST)
   ---
   thanks

---

## Project peer review process (68 threads)

### [2025-01-24] Madalena Neves (replies: 1)

Q: Hi, for this course do we need to deliver all homework assignments to get a certificate? Or the final project with peer review is enough? Couldnt find this on the FAQ doc.

A: Final project with peer review is enough

### [2025-02-07] Thorben Siebeneichler (replies: 17)

Q: Hey there, I have a more general question, maybe towards those that have already done some data science with third party data:
   For my final project of the course I would like to work with some open data of a national non-profit organization. They offer a free api under CC0 1.0 license, so permission for use is there. However, fetching a reasonable set of data will boil down to a few hundred, maybe a couple thousand requests. I am worried, that my ingestion pipeline would get blocked by DDoS protection, and I don’t wanna cause issues for them as well. Is there any experience with the ethics of  ...

A: Sounds logical to me. Maybe also include the process for gathering the data in your documentation. Scaping is and will continue to be a grey area. Do it for profit = crime. Do it for personal project = probably not a crime. Do it if you are OpenAI = Get valued at $260 Billion.
   ---
   Do they provide an api documentation? Maybe they say something about request rate and intervals. I would stick to their limits :wink: 
   
   You could setup (or hire) some proxys to hide your ip to not get blocked. Sometimes changing browser header helps when scraping. Or you could tell your router to reconnect to get a new ip. It doesn’t sound likely you would need these techniques
   ---
   Yeah, they offer api documentation but no mention of any rate limits.
   
   If you are curious, this is the API I want to go for: https://www.abgeordnetenwatch.de/api
   
   It is in german, but luckily translators are a thing :slightly_smiling_face:
   
   AFAIK, there are no contraints for the minimum size of the dataset our project needs to be based on, right? their filters allow for 1000 entities downloaded per request, so if I limit myself to a few dozen requests I could still get a meaningful set of data to show some stuff with, and nobod ...

### [2025-02-18] Ronald Cheung (replies: 2)

Q: *== Set up issues Module 4 ==*
   Hi all, I am stuck at this part of setting up the environment in Module 4 "Review your project settings"
   The instructor shows us that I should see this screen:
   https://user-images.githubusercontent.com/4315804/152606066-f4d70546-7a5e-414a-9df9-8efd090216f8.png
   
   But I cannot find this screen at all.
   My menu looks like this at this moment:
   https://drive.google.com/file/d/1K-T7dEInn6u0uYhS4ittzxyi-6bbKsCS/view?usp=sharing
   
   My left side menu looks very different.
   Did I do something wrong with setting up dbt?

A: Check my step by step set up if you want: https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/tree/main/4_Analytics-Engineering#setting-up-dbt-with-bigquery (https://github.com/ManuelGuerra1987/data-engineering-zoomcamp-notes/tree/main/4_Analytics-Engineering#setting-up-dbt-with-bigquery)
   ---
   The UI changed to a side nav, you can still find the same menu but now on the side. There's like a building icon and frrom there -&gt; settings

### [2025-03-11] Rui Carvalho (replies: 3)

Q: @user Where do i peer review? can i do it know or wait for the deadline?

A: Hey, @user! Here you go:  Peer reviews will take place after the project submission deadline. You will need to wait until the submission period is over to begin reviewing your peers' projects. This is because the peer review process is mandatory to pass the project, and you will be assigned projects to review during the designated review period.
   ---
   @user great, when is the deadline so i can add to my calendar?
   ---
   Hey, @user! Here you go:  You can find the preliminary due dates for the 2025 cohort here (https://courses.datatalks.club/de-zoomcamp-2025/). The deadlines are listed in your local time, so make sure to check that to add them accurately to your calendar.

### [2025-03-11] Christian Murphy (replies: 1)

Q: Hi, can someone please explain the peer review process for the final project? How will we know which 3 projects we've been assigned to review?

A: once you've submitted a project in the course management platform, a new section with all the peer review information will be enabled

---

## Kafka / streaming (67 threads)

### [2025-01-13] Wallace (replies: 2)

Q: @user Will we learn Apache Airflow? Will we use Kafka or Flink for streaming?

A: Hey, @user! Here you go:  Apache Airflow is not specifically mentioned as part of the core learning objectives in the course materials; however, you can use Airflow for your final project if you choose to do so.   As for streaming, the course includes Kafka as a streaming solution. There are references to using Kafka in the context of Python and recommendations for exploring various options, including RedPanda, as an alternative for those who may prefer Python over Java. Additionally, Flink is not mentioned in the provided excerpts, so it is unclear if it is covered in the course.   To summarize, you will have exposure to Kafka for streaming and can choose to use Airflow for your project, but there is no specific mention of learning Flink within the course materials provided.
   ---
   This year we'll be using Kestra instead of Airflow. Still, you can find the materials for Airflow on cohort 2022.
   
   Flink might be covered in Module 6, that is currently being reviewed by Zack WIlson. Gotta wait and see for now

### [2025-02-03] Dinesh (replies: 1)

Q: Hi Y'all, Happy Tuesday.!!
   For Week 2 - I used other orchestrator tool to complete the module but i'd love to learn about kestra and how its simplifies the workflow orchestrator. But would like to know if i need to be familiar with kestra before attending the office hours streaming today ??

A: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1738589194513179
   
   
   I think the office hours are mainly because of not sharing any credentials (https://datatalks-club.slack.com/archives/C01FABYF2RG/p1738520204522619), and if you have specific questions for completing the module with Kestra (https://datatalks-club.slack.com/archives/C01FABYF2RG/p1738336054387679)
   
   You can ask your questions in advance here: https://app.sli.do/event/aFZgu1o3nbgJTyX1AH1dtF

### [2025-03-03] Radu (replies: 3)

Q: Hello. Just got out from work and missed "Stream about streaming with Zach" live session. For this week, should I focus on that topic first or follow Zoomcamp streaming videos and then go with Zach's video?

A: We're still continuing with module 5 till Wednesday
   ---
   I assume that means I'm two days ahead of schedule and should focus on Zach's streaming video first. What about the Zoomcamp streaming videos—will they be updated?
   ---
   No, you'll use them for theory if you want and the Zach's video will be the practical part

### [2025-03-04] Gabi (replies: 6)

Q: Will the homework for week 6 be updated?
   I assume we will be using Apache Flink instead of Red Panda?

A: It will be updated. We will use both
   ---
   But we will use Flink instead of Spark for module 6
   ---
   thanks!
   ---
   Just a follow up here, should we follow along the videos that are now in Module 6 (Kafka, PySpark Streaming) or will these be updated since we are going to use Flink?
   ---
   You can check them too - up to you
   ---
   In the video with Zach we didn't cover anything from the theory side of things, so you can use the existing Kafka videos for that if you're interested

### [2025-03-05] envoamr (replies: 3)

Q: hey all, I'm wondering why the "Theoretical part: Kafka + Java (optional)" in week 6 streaming is optional? is it cause it's redundant to the pyflink stream or is it too complex or something else?

A: I think it's because working on streaming pipelines is only 10% to 20% of the usual Data Engineer job, as it was stated in the course videos. So I suppose it's not something that Data Engineer intern/junior will be doing, making their first steps on these entry level positions.
   Nevertheless, I hope @user will correct me if I'm wrong or give the definitive answer himself :slightly_smiling_face:
   ---
   All the modules are optional: you only select the ones you want to study and follow them
   
   For the project you can select either batch or stream. If you go with batch, then you don't really have to watch the streaming module right now
   ---
   So the optional videos in module 6 are the old videos from the previous cohorts. You can start watching them and see if you like them or they're too complex

---

## Project as a team / two people / collaboration (65 threads)

### [2025-01-16] Randall Lionel Kharkrang (replies: 3)

Q: question ofr module 2. @user, what would be the advised method of working with kestra for going through the videos and subsequently using in project? using docker or some sort of VM with gcp(im a little worried regarding resources for this rn)?
   
   or how do we use the UI demo directly? i.e creating new flows?

A: Hey, @user! Here you go:  For working with Kestra in Module 2, the advised method is to use Docker. Kestra employs Docker IN Docker, which allows you to isolate your code and leverage different programming languages effectively. This setup is recommended as it simplifies the learning process and makes it easier to follow along with the course, given that many other students will be using the same environment.   If you're concerned about resource usage, Docker tends to be lightweight compared to running a full virtual machine (VM), making it a practical choice for local development.   To use the UI demo and create new flows directly, you can run Kestra locally via Docker. Once you have Kestra up and running, you can access the intuitive user interface that allows you to create and manage flows easily.   Make sure to check out the documentation and the Blue Prints section on Kestra's website for guidance on setting up and creating flows, as they provide valuable examples and resources for getting started.
   ---
   Yes exactly, you can spin up kestra locally on your laptop in docker and add + run the flows directly from the local UI
   ---
   the setup to launch kestra on GCP VM was more of a bo ...

### [2025-01-30] Issa AlBawwab (replies: 1)

Q: In week 2 workflow orchestration, in "2. Hands-On Coding Project: Build Data Pipelines with Kestra" theres no videos, what am i supposed to do here? do i just to part 3 and follow along with the videos?

A: here are the videos https://www.youtube.com/playlist?list=PLEK3H8YwZn1oPPShk2p5k3E9vO-gPnUCf for module 2

### [2025-01-30] Oche Peter Anefu (replies: 4)

Q: Please what file type was used to create "service: untitled 2" from *DE Zoomcamp 1.2.2 - Ingesting NY Taxi Data to Postgres?*  and why is it not saved in the project folder?

A: Can you paste the code you are looking at here in the thread?
   ---
   from about time 1:40 - the docker-compose definitions, the file space he's writing those is called service:...
   https://www.youtube.com/watch?v=2JM-ziJt0WI&amp;list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&amp;index=5
   @user since we are not allowed to show pictures, I have to show the link instead. Thank you.
   ---
   No worries. No screenshot rule is to help people on mobile and so the channel doesn't get clogged up. Do you mean what type of file is the docker compose file he is defining the services in? If so, it's a docker-compose.yaml file. Although .yml works and that's what I usually use.
   ---
   ooh I get now. I should save those in a dockercompose.yaml. Thank you very much @user

### [2025-01-31] U06E3M469N2 (replies: 5)

Q: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration, do we need to go through this 2nd (ands-On Coding Project: Build Data Pipelines with Kestra) stage, or is it what we do in 3rs stage? (ETL Pipelines in Kestra: Detailed Walkthrough)

A: I’m not sure I’m following. You want to go through the 9 videos on the link you sent so you can complete the next homework task
   ---
   I was following through videos and I was confused this 2nd part wasnt included. let's just follow videos
   ---
   Can you send me a link to the 2nd part?
   ---
   there is no individual link, but it is inside of this page: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration, by 2nd part I meant: Hands-On Coding Project: Build Data Pipelines with Kestra
   ---
   I’m now following. Make sure to go through each stage in that readme to prevent issues later on.
   Most issues come from people skipping ahead

### [2025-02-03] L (replies: 2)

Q: Hi team, is the workshop a compulsory component to submit (in order to get the certificate)? How long does it take in estimate to complete the workshop? These info are needed to plan our learning schedule beforehand.

A: Nope
   Idk,maybe a few hours
   ---
   where is the link for workshop ? How I can register ?

---

## GCP free credits / billing / account (64 threads)

### [2025-01-03] Gloria Quiceno (replies: 4)

Q: Hello all, does anyone have notes on creating docker resource in GCP with terraform? having issues with permission policies for the default service account and wondering if anyone have notes to overcome it?

A: Do you mean installing docker on the VM with Terraform or are you referring to some other type of docker resource?
   ---
   i mean executing terraform apply and not have iam service account permission errors
   ---
   @user
   terraform files here: https://github.com/gdq12/pipeline-performance-analysis/tree/main/1_extract_load/gcp
   
   error message for terraform apply:
   
   ```Error: Error creating Service: googleapi: Error 403: Permission 'iam.serviceaccounts.actAs' denied on service account <mailto:1023261528910-compute@developer.gserviceaccount.com|1023261528910-compute@developer.gserviceaccount.com> (or it may not exist).
   │ 
   │   with google_cloud_run_service.run_service,
   │   on main.tf (http://main.tf) line 78, in resource "google_cloud_run_service" "run_service":
   │   78: resource "google_cloud_run_service" "run_service" {```
   current iam permission I have in my project:
   
   ```bindings:
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.reader
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.writer
   - members:
     - serviceAccount:mage-extract-load@pi ...

### [2025-01-09] YB (replies: 3)

Q: If I've already used up my GCP credits/trial period previously for a different course, just wondering what alternatives I can do? Simply use another google account that has not used GCP before?

A: I personally just used another Google account.
   ---
   me too
   ---
   just make sure you dont loose access to your account and get charged months later, lol

### [2025-01-10] Phong Thanh Phạm (replies: 1)

Q: hi guy! i can get 300$ GCP because i don't have visa card. How can i get GCP account?
   Thanks in advance

A: I have the same problem

### [2025-01-11] MohamedAliJmal (replies: 9)

Q: Could I get gcp without credit card??

A: Hi @user! We asked AI, and this is what it answered:
   
   Yes, you can get a Google Cloud Platform (GCP) account without a credit card. GCP offers a free tier with $300 in credits for the first 90 days. To sign up without a credit card, follow these steps:
   
   1. Go to the GCP website and click on "Get started".
   2. Select "Create a new account" and fill in the required information.
   3. Choose the "Free trial" option.
   4. Verify your account using a phone number or other methods.
   
   Note that some features may require a credit card for full access, but you can still use many GCP services within the free tier limits.
   ---
   Hm I don't think it's correct but try it
   ---
   Debit cards worked
   ---
   It didn't worked, is there any other solution?
   ---
   Get a different bank card?
   ---
   I don't have any bank card , also I m from tunisia and our banking system doesn't provide us with international transactions even if i have bank card i can use it only in tunisia
   ---
   Do the project locally. Browse the leaderbords from past cohorts for an inspiration if you need one
   ---
   I don't get it, could you explain more?
   ---
   You'll see it today in the launch steam

### [2025-01-11] Viktor Sokolov (replies: 1)

Q: Hi, folks! I wanted to set up the environment to start the course but realized that I am unable to get access to Google Cloud Platform because I don't have a credit card. Can anyone suggest other ways I can follow along with the course by replacing GCP with something else, are there clouds which don't require credit card for registration? I found this (https://www.localstack.cloud/pricing) tool which simulates the cloud locally, but I am not sure if I will be able to get my homeworks peer reviewed considering I will be using a different technology.

A: I done a local project during the 2024 cohort
   
   However I was doing homeworks on GCP

---

## AWS / Azure / Oracle / alternative cloud (61 threads)

### [2025-01-01] FabianB (replies: 4)

Q: does anyone have great content on how to minimize expenses on the cloud? (gcp or aws)

A: Minimize expenses of what exactly?
   ---
   pretty much everything, how to choose the appropriate instance size, how to decide if you need data storage, plus the additional details that i dont know
   ---
   That is a thing that is very specific to each task and will come with experience. You are in the right place though! Once you get started maybe look into AWS and GCP Certs. Having that knowledge will help guide you. Other than that, I'd say Google/ChatGPT what you are looking at and brain storm on reducing costs like that.
   ---
   this much i know, which is why i ask for specific content, but i guess this is the way forward

### [2025-01-09] U080DSRHY10 (replies: 7)

Q: To be able to do anything with compute engines on GCP, first we need to enable compute engine API, which is not free it seems. Has it always been this way, I never faced such a structure on Azure or AWS....Also my config is supposed to be "free" or am I missing sth?

A: If it is your first time signing up you should have free credits to use. If you have already used them you can create a new Gmail, re-sign up, and get them again. What they give you is way more than what you will need to complete the course.
   ---
   Please don't post screenshots or pictures of your code, they are very difficult to read.
   
   Instead, copy the code and put it in a code block.
   
   Follow these recommendations (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/asking-questions.md) to make it easier to help you.
   ---
   @user thanks for the response. I tried singing up with a new account and they caught me mentioning it is against their policy....:eyes:
   ---
   @user try to sign up using vpn or other pc, because it detect your ip address. For learning purpose I would go against it for once :grin:
   ---
   Or if you use virtual machine try to setup the network as Bridge adapter, it will allow your vm has its own ip.
   ---
   @user it is asking for creditcard info for identity verification anyway
   ---
   I forget about that point. Then maybe you could use aws and use their free tier account there. Otherweis pay.

### [2025-01-09] YB (replies: 3)

Q: If I've already used up my GCP credits/trial period previously for a different course, just wondering what alternatives I can do? Simply use another google account that has not used GCP before?

A: I personally just used another Google account.
   ---
   me too
   ---
   just make sure you dont loose access to your account and get charged months later, lol

### [2025-01-13] Kareem Adel (replies: 2)

Q: Hi, does anyone know if I can use Azure Synapse instead of BigQuery for this course? I'm unable to create a free trial account in GCP due to problems with my credit card.

A: Yes you can
   ---
   Thank you, that sounds great

### [2025-01-13] Gbenga Ogunmefun (replies: 9)

Q: Someone mentioned on the livestream that there is a channel for people that want to use AWS. Can anyone pls direct me to the channel?

A: Babanla. How we go run this course
   ---
   We go run am anyhow. We go sha make sure say we dey learn and we dey move forward
   ---
   have you been able to setup your cloud
   ---
   No, all debit cards keep on failing
   ---
   That's what I have been facing for more than a year
   ---
   Have any one been able to do that in the group
   ---
   I don't think so, people are resulting back to AWS
   ---
   I that of AWS working
   ---
   Wetin dey sup for here ooo. Shey we no go create 9ja Sub-channel liedis

---

## Bruin (2026 cohort) (61 threads)

### [2026-02-06] Brian (replies: 3)

Q: Hi @user, I noticed that in module 5, we have new module called data platform. I took a peek inside and there is Bruin. Will there be a new youtube playlist or course like in module 4 analytics engineering like what @user do? Or we just follow the steps written in the Bruin zoomcamp github?

A: There will be videos, yes. But if you want you can already start with the written instructions. @user will help if you get stuck, and he'll probably be happy about feedback too
   ---
   Hi! Could you share the link for your project Module 1 with me :slightly_smiling_face: Just want to see how others did it. This it's mine : https://github.com/benzaquenruth/Data-engine-zoom-camp
   ---
   @user the videos will become available this week, in the meantime feel free to reach out to me directly with any questions you may have.

### [2026-02-07] Parth Deshpande (replies: 3)

Q: _Hi, I wanted to know if there will be any videos about Bruin?_

A: Yes
   ---
   ok,thanks
   ---
   @user yes there will be tutorial videos released this week, in the meantime feel free to reach out to me if you have any questions or need help

### [2026-02-08] Nariman Baubekov (replies: 5)

Q: Hello! Is anyone having difficulties figuring out how to use Bruin in Module 5: Data Platforms? I'm reading the docs and the provided learning resources but still don't understand how the whole system works and what my input should look like.

A: @user said that there will be videos about Bruin. IMO, better we wait for the videos to get better understanding. tagging representative from Bruin @user
   ---
   Got it. Thank you for your response!
   ---
   Do you know when the videos will be out by the way?
   ---
   Hi there! The tutorial videos will be out this week, I will let you know once they are available
   ---
   Alright, thanks!

### [2026-02-16] Carlos (replies: 18)

Q: Am I the only one with the feeling that Bruin is just a less professional and much worse documented alternative to dbt?

A: I just watch the videos and i dont yet understand what's going on .
   ---
   Same feeling here. The first two videos seem more promotional than pedagogical and their documentation does not help much
   ---
   Would love to better understand how we can improve and help you out. Do you mind sharing specific parts that were confusing or you got stuck? If its easier we can also hop on a call and I can walk you through it.
   ---
   Hi Carlos &amp; Freeman, this is Burak, co-founder &amp; CEO at Bruin. I am sorry that you didn't have a good experience with Bruin and things are confusing.
   
   Like Arsalan said, we'd love to better understand where we fall short and what we can do better. I can assure you that the feedback we receive here will be treated with top priority internally.
   ---
   Hi Burak and Arsalan,
   
   Before anything else, thanks for your disposition and for your contribution with the course. My first question is, is there any documentation of the schema for the *.bruin.yml* file?
   
   I'm trying to understand the basics of a Bruin project by reading the documentation but I'm finding a few contradictory things. For instance, in the Quickstart (https://getbruin.com/docs/bruin/getting-started/introduction ...

### [2026-02-16] Harshit Lamba (replies: 6)

Q: Bruin claims to be an end to end platform for data ingestion, transformation and quality checks. While I would love to learn it, we have already done the transformation part using dbt. Which one is better to use - Bruin or dbt?

A: I'm wondering the same thing. We also have dlt (data load tool).
   ---
   One of the main benefits is to centralize the configuration and orchestration of all the layers/stages of the pipeline. This becomes especially beneficial in a production environment with a bigger team where maintaining multiple tools, configurations, and projects become complicated.
   
   Regarding transformations, bruin and dbt assets/models are fundamentally the same (i.e. materialization, dependencies, incremental strategies, etc.) - they mainly differ in the developer experience when creating and testing your pipelines. Would love to hear your feedback on this if you've tested both.
   ---
   yes, I guess we have so many options now
   ---
   @user does it replace dlt entirely?
   ---
   yes, it does
   ---
   so it brings dlt, dbt, airflow (kinda) together into a single place, so that you can have the full lineage together

---

## Videos / playlist / where to watch (60 threads)

### [2025-01-07] kabir s (replies: 1)

Q: Hi, I'm currently starting to set up the environment on a Mac. Do I follow the GitHub Codespaces video (https://www.youtube.com/watch?v=XOSUt8Ih3zA) or do I set up local environment on my Mac? If so, do I just follow Alexey's Introduction to Docker video?
   
   (Codespaces storage/time constraints aren't an issue, I have a student account)

A: I would just follow the local setup instructions to start.

### [2025-01-10] Koray Kanut (replies: 13)

Q: Another question, I have is, how can the presenter in the DE 2.2.3 video (https://www.youtube.com/watch?v=OkfLX28Ecjg&list=PLEK3H8YwZn1oPPShk2p5k3E9vO-gPnUCf&index=3&ab_channel=Kestra) access the postgres database with Pgadmin? We do not build a container for pgadmin in the same docker-compose.yml (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/02-workflow-orchestration/docker-compose.yml). We only have the postgres and the kestra in 2 containers. So that postgres shouldnt be reachable by anything except the Kestra in the other container. Or what am I missing? @user

A: Hey, @user! Here you go:  To access the Postgres database using PgAdmin while using the provided Docker setup, you need to consider the networking between the containers. The setup described in the course instructs to run both the Kestra server and the Postgres database in separate containers. However, the Postgres container should be accessible from your host machine, which allows you to connect to it using PgAdmin.  By default, when you run the Postgres container without any specific network configurations, it will be reachable on the default Postgres port (5432) from the host machine. You can connect to the Postgres database using PgAdmin by specifying the host as `localhost`, the port as `5432`, and using the credentials defined in the `docker-compose.yml` file.  If you have not set up any specific firewall rules or Docker network configurations that restrict access, you should be able to connect to the Postgres database without any issues. Ensure that you provide the correct username and password that you configured in your Docker setup.  If you still cannot access it, you may need to check your Docker container logs for any issues, or ensure that the Postgres service is runni ...

### [2025-01-12] Eden Chen (replies: 3)

Q: :wave:Hello, team! Is this zoom-camp on-live or watching video by ourselvies? When is the due time for each assignments? How long for each module?

A: I think the readme might answer your questions: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main?tab=readme-ov-file#taking-the-course
   ---
   Homework deadlines are here: https://courses.datatalks.club/de-zoomcamp-2025/
   ---
   Wonderful! Thank you very much David!!

### [2025-01-13] kabir s (replies: 3)

Q: Hi, I’m setting up GitHub Codespaces by watching the video in the playlist. Do I need to go back and watch the GCP video to configure GCP? or do I start straight from the code spaces video

A: You don't, codespaces is enough
   ---
   Please share the playlist @user
   ---
   https://youtube.com/playlist?list=PL3MmuxUbc_hKVX8VnwWCPaWlIHf1qmg8s&amp;si=U1iYa3wZLvAqQR4n (https://youtube.com/playlist?list=PL3MmuxUbc_hKVX8VnwWCPaWlIHf1qmg8s&amp;si=U1iYa3wZLvAqQR4n) here you go

### [2025-01-13] Devon Do (replies: 1)

Q: Hello, I am running all commands from github codespace. While following along the *Ingesting NY Taxi Data to Postgres* video, I ran the command to create a postgres container, but my ny_taxi_postgres_data folder is empty unlike the video. Am I missing a step?

A: I have solved my issue.
   
   Steps:
   1. Delete folder. sudo rm -rf ny_taxi_postgres_data/
   2. Rerun Docker command
   3. Change folder permissions. sudo chmod a+rwx ny_taxi_postgres_data/

---

## Project: how to evaluate / find peer projects to review (60 threads)

### [2025-01-24] Madalena Neves (replies: 1)

Q: Hi, for this course do we need to deliver all homework assignments to get a certificate? Or the final project with peer review is enough? Couldnt find this on the FAQ doc.

A: Final project with peer review is enough

### [2025-03-11] Rui Carvalho (replies: 3)

Q: @user Where do i peer review? can i do it know or wait for the deadline?

A: Hey, @user! Here you go:  Peer reviews will take place after the project submission deadline. You will need to wait until the submission period is over to begin reviewing your peers' projects. This is because the peer review process is mandatory to pass the project, and you will be assigned projects to review during the designated review period.
   ---
   @user great, when is the deadline so i can add to my calendar?
   ---
   Hey, @user! Here you go:  You can find the preliminary due dates for the 2025 cohort here (https://courses.datatalks.club/de-zoomcamp-2025/). The deadlines are listed in your local time, so make sure to check that to add them accurately to your calendar.

### [2025-03-11] Christian Murphy (replies: 1)

Q: Hi, can someone please explain the peer review process for the final project? How will we know which 3 projects we've been assigned to review?

A: once you've submitted a project in the course management platform, a new section with all the peer review information will be enabled

### [2025-03-12] shuokai (replies: 4)

Q: Hi team, does anyone want to partner up for the peer review process of the final project?

A: That's not really how it works. :slightly_smiling_face:
   ---
   You'll get 3 randomly assigned projects to review. You can also review other projects if you want (and I recommend doing it) but you won't receive any extra points for that
   ---
   Thank you @user  @user for the clarity! I assume assigned project will be given through the homework link?
   ---
   Yes on the course management platform

### [2025-03-18] Fabian Bryant (replies: 8)

Q: Hi there can I check what should be done for the case when my subscription for Google cloud will end before peer review is done? I can create a new account easily but data won’t be easily transferable between accounts?

A: Not sure I understand. The project should be reproducible/be able to run on the evaluators GCP Account. To evaluate others projects, yes, you can just create a new GCP Account and get the free credits again.
   ---
   It is reproducible but the data will be gone
   ---
   I’m injesting data and storing it in my current bucket
   ---
   If I create a new account the data in my old buckets won’t transfer over
   ---
   @user
   ---
   So that means the dashboard will have no data when the free trial ends
   ---
   As I will have to clear all running instances in gcp
   ---
   I would imagine the data would be publicly available/you would have instructions on how to get the data. If it is data you paid for or retrieved in some very obscure way, depending on the size, you could save it to parquet and put it on Github or some other public repo. Then have instructions on how to create the dashboard or a config file that creates it

---

## Homework deadline / late submission (51 threads)

### [2025-01-12] U08768VPL74 (replies: 5)

Q: guys i want to ask that this submitted link for Module 1 Homework: Docker & SQL cannot access? i try to figure it out but still error when i try to get in that link. Then, will the deadline for each homework in DE Zoomcamp 2025 be the same as the deadline for homework in DE Zoomcamp 2024?

A: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1 (https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1)
   ---
   Where is your link from?
   ---
   The link on github is broken, it says hw01 instead of hw1
   ---
   I created a pull request for that issue :slightly_smiling_face:
   ---
   Merged! Thank you!

### [2025-01-13] zeehow (replies: 2)

Q: Just curious about the time zone of deadline of Homework on the website: https://courses.datatalks.club/de-zoomcamp-2025/, what is the exact time zone for that? Thank for the replying in advanced!

A: Just found this message: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1707133506348919?thread_ts=1707133504.672589&amp;cid=C01FABYF2RG, the time zone should be the calendar is in Germany time, specifically CET (Central European Time) or Berlin time
   ---
   It's your local

### [2025-01-20] Shawn (replies: 1)

Q: Hi guys, I am super late to this course and now working on homework for week1. Does anyone know if we need to submit the homework through the link on github? Thank you!

A: hey, https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/01-docker-terraform/homework.md

### [2025-01-22] Kris (replies: 7)

Q: What's the deadline for the module 1 homework?

A: January 28
   ---
   What if homeworks is submitted later? Will I run risk of not getting a certificate?
   ---
   only project counts for certificate, homework count for leaderboard
   ---
   ah perfect, thanks - and the deadline for the project would be? @user
   ---
   see course management platform
   ---
   Hi so I can still submit a day late - just won't be in leaderboard right?
   ---
   You can only submit, when form still shows open. When Alexey hits his button, it will be closed and scored.

### [2025-01-24] Ivan C (replies: 2)

Q: Hi everyone,
   
   I have a bit of a late start.  Are the due dates for the homework absolute or we can answer a bit late(r)?

A: When form closes after due date, you can’t change anything anymore.
   
   But you only need to pass project at the end of the course to get certification.
   ---
   Thanks for the info!

---

## Workshop (dlt / Bruin) - where to find / mandatory (51 threads)

### [2025-01-24] Alex (replies: 1)

Q: Hey Engineering pros and prospects.
   Maybe a dumb question, but how should I set up my folder structure for the course? I'm looking at Alexey's 1.2.1 video setting up Docker, and he has /git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker
   
   Should I also have it this nested when I'm working through the course, or should I follow the Syllabus (Module 1, 2, workshop 1, etc), or just lump it in a single giant folder? I'm paranoid that if I might screw up something down the line if I don't have the right folder structure.

A: Personal opinion:
   you don't have to use same names, just use one big folder for the course, and inside it create a separate folder for each module. But to avoid confusion like you said, you can use same names as Alexey's (for example name the module 1 2_sql_docker)  at the beginning, then when you will finish the module and understand every file, what it does, and what is linked to, you can then rename it name of the module 01-docker-terraform  or whatever you like

### [2025-01-27] Sara sabater (replies: 4)

Q: @user I have finished the second module. What's next? 
   The workshop 1 directory, data ingestion, is empty.
   Should I go to the Module 3?

A: Hey, @user! Here you go:  To address your concerns about following the first video in Module 1:  1. It’s normal for the folders and files shown in the video to differ from the ones in the repository, as there may be updates or changes made to the repository after the video was recorded. It is generally okay to proceed with your practice even if there are discrepancies.  2. Regarding the setup of your environment, it is advisable to complete the video on setting up GCP and VM before diving into the main content of Module 1. This will help ensure that your environment is ready for the subsequent lessons.  3. If you are using Git Bash and the `ls` command returns a blank output, it likely means you are in a directory that does not contain any files or folders. Ensure you are in the correct directory where your files are located. You can navigate using the `cd` command to change directories.  4. To connect your GitHub account to Git Bash, you will need to configure your Git settings. You can do this by running the following commands in Git Bash:     ```bash    git config --global user.name "Your Name"    git config --global user.email "<mailto:your_email@example.com|your_email@example. ...

### [2025-01-28] Alexander Flick (replies: 3)

Q: @user I want to start with the Workshop 1: Ingestion with dlt, which needs to be submitted till 11 Februar 2025 00:00. However, the github provides just a link for registration (# Data ingestion with dlt
   Sign up here: https://lu.ma/quyfn4q8 (optional))  Can you share any more details?

A: Hey, @user! Here you go:  The Workshop 1: Ingestion with dlt will take place on February 10th, 2025, from 16:30 to 18:00 Berlin time. The registration link for the workshop is here (https://lu.ma/quyfn4q8). Additionally, the workshop is a part of the course materials that are already available online, and the homework for this workshop is due by February 11th, 2025, at 00:00.   For further details, you can check the workshop documentation at this link (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/workshops/dlt.md).
   ---
   We will have more details soon. It'll be a live video. You can check the 2024 cohort to get an idea of what dlt is, we also did a workshop last year
   ---
   Great, thank you!

### [2025-01-29] Leonardo Rodriguez (replies: 2)

Q: @user After week 2, should we continue to data warehousing, or should we do the workshop?
   
   It seems from the homework page the workshop goes first. Is there a video for it or is it live?

A: Hey, @user! Here you go:  The workshop comes before the data warehousing section according to the homework page. There should be a video available for the workshop, but it's recommended to check if it's live or recorded by referring to the course materials or announcements. If you're unsure, you may want to ask your fellow students or instructors for clarification on the format of the workshop.
   ---
   workshop will be live, check google calendar in bookmarks :bookmark_tabs:

### [2025-01-29] Leonardo Rodriguez (replies: 3)

Q: Anyone can tell me where the workshop info is? It's supposed to be done before module 3 right?

A: It will be live and we will explain everything on the stream
   ---
   ok thanks!
   ---
   the date is in google course calendar (https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) :smile:

---

## Course platform login / account (49 threads)

### [2025-01-02] Patrick Edosoma (replies: 6)

Q: Hello all, Happy New year. My friend registered for this course and he has no basic knowledge about python. What could you possibly suggest he do?

A: Learn Python. :neutral_face:
   ---
   Joking. Kind of. It may not be feasible for him to make it through this time around. Not to discourage him, he should give it a shot, but the learning curve will be quite steep and it really depends on how much time he has on his hands and how quickly he can pick it up. Sentdex on YouTube has some great intro videos if time is tight. CS50P is GREAT, but the time investment will be much larger. He could also just use ChatGPT to get started. Needs to probably learn variables, functions, loops, conditions and understand why/how Python is Object Oriented and what that means.
   ---
   It took me 3 years and 4 tries to get through CS50X. So my advice would be for him to jump right in and try to learn Python as much as he can. Doing this course might help guide his learning and even if he doesn't get through this cohort it will probably show what areas he is lacking in knowledge of Python. For this course, learning programming and I guess life in general I would say - try, and don't get discouraged, we all started somewhere.
   ---
   Is your friend a complete beginner, then I agree to Michael. But if he knows another language like Java, C or so, then python is easy  ...

### [2025-01-05] Shilpa Leo (replies: 3)

Q: Hello from Singapore! I've registered for the DE course starting next week. I added the Google calendar as well, but realized the timings are not Asia friendly. The launch happens at midnight SG time. :disappointed:
   Will the live sessions be recorded or how can folks like me seek support given the time diff? Thanks!

A: yes, it will be. we can also see the passed recorded live session as well.
   ---
   @user All video classes are already pre-recorded. The live sessions we'll have are mostly for Q&amp;A  and (maybe) live sessions for the workshops
   
   Start here: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   
   Video links are already embedded
   ---
   Will there be no further updates to videos? So I can move on my own (hopefully faster) schedule.

### [2025-01-13] Willy Dongmo (replies: 1)

Q: Hello,
   How can I check that I’m registered for this cohort?

A: You are. Everyone is

### [2025-01-13] deleted (replies: 2)

Q: Hi all! I tried to login to https://courses.datatalks.club/ with GitHub but it redirects to a page that says "Server Error (500)" anyone else encounter this?

A: I'm having the same issue. I cannot login, so I cannot submit my homework :-/
   ---
   Alexey mentioned he couldn't replicate the problem but where were reports of it happening. For now I've used this Slack account to login and it worked.

### [2025-01-13] Boris Li (replies: 4)

Q: Just learned from @user during today's live YouTube session (https://www.youtube.com/watch?v=X8cEEwi8DTM) that each homework available for taking submissions will be announced in this channel:
   
   ```Boris Li
   Roughly when will "Homework 1" be open for submission?
    
   
   Boris Li
   https://courses.datatalks.club/de-zoomcamp-2025/
   
   Bruno Oliveira
   @Boris Li , we'll let you guys know on the #course-data-engineering channel. Please stay tunedhttps://www.youtube.com/watch?v=X8cEEwi8DTM ```

A: @user I also noticed that the questions here: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1 do not match the questions here: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/01-docker-terraform/homework.md
   ---
   `https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/01-docker-terraform/homework.md`
   This one has been recently updated.
   
   The actual homework questions will be updated soon. Stay tunned! You guys will have at least 2 weeks to get through the Week 1 materials! :slightly_smiling_face:
   ---
   Thanks, @user.
   ---
   You're very welcome

---

## Codespaces / Gitpod / VM environment (48 threads)

### [2025-01-06] Julie Chen (replies: 6)

Q: Hi, I am following this tutorial (https://www.youtube.com/watch?v=XOSUt8Ih3zA) and am stuck on 4 minute mark. When I select "Open in VS Code Desktop" from the codespace browser, it does not automatically open in my VS code. I already have codespace installed as an extension in my VScode.

A: I also see this - not sure if this is the likely blocker?
   ---
   Can you try to update VSCode and possible also remove and re-add the extension and see if that works/helps
   ---
   ok I updated VS code and also re-installed the extension but that didn't seem to work. I do get the below pop up but it isn't showing me what's in codespace.
   ---
   I also tried clicking "Connect to.." and selected "Connect to Codespace" but then nothing happens next..
   ---
   I tried "open repo from github" but for some reason it is taking a while to even show any results
   ---
   @user Do you have any suggestions? do we need to have this set up by 1/13 or can I stay within the codespace browser for the time being until I get this figured out?

### [2025-01-09] U080DSRHY10 (replies: 7)

Q: To be able to do anything with compute engines on GCP, first we need to enable compute engine API, which is not free it seems. Has it always been this way, I never faced such a structure on Azure or AWS....Also my config is supposed to be "free" or am I missing sth?

A: If it is your first time signing up you should have free credits to use. If you have already used them you can create a new Gmail, re-sign up, and get them again. What they give you is way more than what you will need to complete the course.
   ---
   Please don't post screenshots or pictures of your code, they are very difficult to read.
   
   Instead, copy the code and put it in a code block.
   
   Follow these recommendations (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/asking-questions.md) to make it easier to help you.
   ---
   @user thanks for the response. I tried singing up with a new account and they caught me mentioning it is against their policy....:eyes:
   ---
   @user try to sign up using vpn or other pc, because it detect your ip address. For learning purpose I would go against it for once :grin:
   ---
   Or if you use virtual machine try to setup the network as Bridge adapter, it will allow your vm has its own ip.
   ---
   @user it is asking for creditcard info for identity verification anyway
   ---
   I forget about that point. Then maybe you could use aws and use their free tier account there. Otherweis pay.

### [2025-01-13] Devon Do (replies: 1)

Q: Hello, I am running all commands from github codespace. While following along the *Ingesting NY Taxi Data to Postgres* video, I ran the command to create a postgres container, but my ny_taxi_postgres_data folder is empty unlike the video. Am I missing a step?

A: I have solved my issue.
   
   Steps:
   1. Delete folder. sudo rm -rf ny_taxi_postgres_data/
   2. Rerun Docker command
   3. Change folder permissions. sudo chmod a+rwx ny_taxi_postgres_data/

### [2025-01-14] Dinesh (replies: 1)

Q: Hi Guys,
   Is it's mandatory to set up our develop environment in Google virtual machine that needed in later part of the course or we can do follow along with our local machine?
   @user

A: Hey, @user! Here you go:  It's not mandatory to set up your development environment in a Google virtual machine. You can follow along with your local machine if you prefer. However, keep in mind that you might face some challenges, especially if you are using Windows. The course allows for flexibility in choosing your environment, and you can also opt for GitHub Codespaces or set up a virtual machine if that suits your needs better.   That said, some parts of the course will utilize Google Cloud Platform (GCP), particularly BigQuery, so familiarity with GCP might be beneficial as you progress. Ultimately, choose the approach that aligns best with your project goals and personal preferences.

### [2025-01-14] Devon Do (replies: 2)

Q: Hi, I am trying to start up pgadmin on my github codespace, and after creating it through docker, I am able to open the page and see the login screen, but after I enter my credentials and try to login, the page attempts to load for a second and then remains completely blank. How do I fix this?

A: When I insepct the page in console I get the following error:
   ---
   docker run --rm -it \
       -e PGADMIN_DEFAULT_EMAIL="<mailto:admin@admin.com|admin@admin.com>" \
       -e PGADMIN_DEFAULT_PASSWORD="root" \
       -e PGADMIN_CONFIG_WTF_CSRF_ENABLED="False" \
       -p "8080:80" \
       dpage/pgadmin4
   
   Adding additional -e variable fixed it

---

## GCP service account / key / IAM (46 threads)

### [2025-01-03] Gloria Quiceno (replies: 4)

Q: Hello all, does anyone have notes on creating docker resource in GCP with terraform? having issues with permission policies for the default service account and wondering if anyone have notes to overcome it?

A: Do you mean installing docker on the VM with Terraform or are you referring to some other type of docker resource?
   ---
   i mean executing terraform apply and not have iam service account permission errors
   ---
   @user
   terraform files here: https://github.com/gdq12/pipeline-performance-analysis/tree/main/1_extract_load/gcp
   
   error message for terraform apply:
   
   ```Error: Error creating Service: googleapi: Error 403: Permission 'iam.serviceaccounts.actAs' denied on service account <mailto:1023261528910-compute@developer.gserviceaccount.com|1023261528910-compute@developer.gserviceaccount.com> (or it may not exist).
   │ 
   │   with google_cloud_run_service.run_service,
   │   on main.tf (http://main.tf) line 78, in resource "google_cloud_run_service" "run_service":
   │   78: resource "google_cloud_run_service" "run_service" {```
   current iam permission I have in my project:
   
   ```bindings:
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.reader
   - members:
     - serviceAccount:mage-extract-load@pipeline-analysis-446021.iam.gserviceaccount.com
     role: roles/artifactregistry.writer
   - members:
     - serviceAccount:mage-extract-load@pi ...

### [2025-01-16] Przemek (replies: 5)

Q: #terraform
   Have you encounter issue with creating bucket with cloud storage admin role?
   I was able to create bigquery dataset, but for bucket I receive 403 error (commonly described here)
   
   The only way to handle it is to use service account with editor role. Is there some bug on GCP side?

A: have you tried @user whether it can address your question?
   
   Have you encounter issue with creating bucket with cloud storage admin role?
   I was able to create bigquery dataset, but for bucket I receive 403 error (commonly described here)
   
   The only way to handle it is to use service account with editor role. Is there some bug on GCP side?
   ---
   Hey, @user! Here you go:  Receiving a 403 error when trying to create a bucket, even with the Cloud Storage Admin role, suggests that the service account may not have the appropriate permissions or that the project ID used in the Terraform configuration is incorrect.   Ensure that you are declaring the correct Project ID, not just the Project name, in your Terraform configuration. The correct project ID can be found in your Google Cloud Platform (GCP) console dashboard.  If you have confirmed that the project ID is correct and you still encounter issues, you may need to check the roles assigned to the service account. If the service account lacks permissions for creating buckets, consider adding the Editor role to the service account as a temporary workaround or ensuring that all necessary roles are correctly assigned.  If the problem persists,  ...

### [2025-01-19] Oscar Cortes (replies: 3)

Q: I noticed there are differences between the written instructions in the git hub repo and the videos.  This makes sense since the videos get reused where possible. Am I correct in assuming we should follow the git hub repo instructions if and when they are different?
   
   As one example, the section, Setup access for  IAM Roles for Service Account (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/1_terraform_gcp/2_gcp_overview.md#initial-setup:~:text=Add%20these%20roles%20in%20addition%20to%20Viewer%20%3A%20Storage%20Admin%20%2B%20Storage%20Object%20Admin%20% ...

A: I think either one will do the trick. I'd go for more not less to make sure you don't run into any issues. In the real world you would create a custom role with very specific permissions and give the service account that role. As this is just an introduction the broad permissions are okay.
   ---
   Thanks Michael, That makes sense as we definitely want to be careful about giving to much permissions in a real production environment.
   
   I ended up setting mine up a bit different following someone else's guide that had screenshots which was superhelfpul. But coming back now as a review.   One follow up question, of the two roles above which one is considered more restrictive and/or less restrictive?
   ---
   Disregard my last question, a quick search yielded that the roles created in the video containing the `Compute Admin` role gives us more power over the `Storage Object Admin` role.  I'm sure they serve different purposes but in terms of permissions, it appears to be the case.

### [2025-01-21] Ari Lamstein (replies: 2)

Q: @user I am following along video DE Zoomcamp 1.3.2 - Tearraform Basics. I have successfully created the account and assigned it the proper roles. But then the teacher says “But now we need a way to say we indeed have permissions to run as that service account. Click the little ellipse and we’re going to manage keys”.
   
   On my UI I don’t have a little ellipse (on his screen it’s under the column header “Actions” which I don’t have). How can I add the key for the service account?

A: Hey, @user! Here you go:  To add the key for the service account, you need to follow the steps for managing service account keys in the Google Cloud Console. If you don't see the "Actions" column with the little ellipse, it's possible that the UI has been updated or that your screen resolution is affecting how the options are displayed.  Here's how you can add the key for the service account:  1. Go to the Google Cloud Console: https://console.cloud.google.com/ 2. Navigate to the "IAM &amp; Admin" section in the sidebar. 3. Click on "Service accounts". 4. Find the service account you created for your project. You may need to select the project where the service account was created. 5. Click on the service account name to open its details. 6. Look for a section called "Keys". There you should see an option to "Add Key". 7. Click on "Add Key" and select "JSON" to create a new key. This will download a JSON file containing the key to your computer.  If the "Actions" column or the little ellipse is still not visible, consider checking if there are any display issues, or try accessing the console from a different browser or device. If the problem persists, you might want to consult your ...

### [2025-01-22] Kerem Yücedağ (replies: 1)

Q: Guys I am completely lost, Which video shows where to create a service account and generate keys for terraform and gcp? I am going through the *DE Zoomcamp 1.4.1 - Setting up the Environment on Google Cloud (Cloud VM + SSH access)* video. (https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=15) (40:50 seconds)
   
   * Now create a service account and generate keys like shown in the videos  ## *Which video shows this step?*
   * Download the key and put it to some location, e.g. `.gc/ny-rides.json`
   * Set `GOOGLE_APPLICATION_CREDENTIALS` to point to the file

A: this one: *DE Zoomcamp 1.3.2 - Terraform Basics*

---

## DuckDB (46 threads)

### [2025-01-22] Shawn (replies: 1)

Q: what is duckDB @user

A: Hey, @user! Here you go:  DuckDB is an in-process SQL OLAP (Online Analytical Processing) database management system designed for fast analytical queries. It operates similarly to SQLite, but it is optimized specifically for analytical workloads, allowing users to perform complex analyses on large datasets efficiently. DuckDB supports in-memory processing and can be used as part of data pipelines, such as those created with the dlt library, where it can serve as a destination for data loading and analysis.  In the context of the Data Engineering ZoomCamp course, DuckDB is utilized for storing and querying data within the pipelines created using the dlt library. This allows for flexible data processing, enabling users to load data from various sources and conduct analyses without the need for an external database server.

### [2025-01-28] David Nadler (replies: 1)

Q: I run the “docker compose up -d” in 02-worklow-orchestration ; then import the Getting Started Pipeline” in the flows subdirectory into my Kestra session;, create the flow; and then execute it. For me, the “query” task fails with the following message:
   
   2025-01-28 12:49:55.282namespacezoomcamp (http://localhost:8080/ui/flows?namespace=zoomcamp)flowId01_getting_started_data_pipeline (http://localhost:8080/ui/flows/edit/zoomcamp/01_getting_started_data_pipeline)taskIdqueryexecutionId7UY8pQDwyZZYenzlYm4i0T (http://localhost:8080/ui/executions/zoomcamp/01_getting_started_data_pipeline/7UY8pQDwyZZY ...

A: make sure to use the latest image, not develop, then restart all containers and you should be good  :+1: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1737297993401679

### [2025-02-26] Juwon (replies: 4)

Q: Why exactly do one need DBT? is it really necessary since i have python/duckdb.
   
   But sincerely need to know why DBT

A: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1740089995906229
   ---
   Think this should make it a bit more clear..... maybe.
   ---
   I really liked these reddit posts on this topic:
   Why is dbt so good? (https://www.reddit.com/r/dataengineering/comments/1cstq6v/why_is_dbt_so_good/)  and  Is dbt really necessary? (https://www.reddit.com/r/dataengineering/comments/119s7yv/is_dbt_really_necessary/)
   
   One comment even said, _*if you're doing ETL, then you probably shouldn't be using dbt.*_
   ---
   python and duckdb are not really "competitors" to dbt if you think about it, but at the end is about the developer workflow and the promotion to production that dbt brings to your project.
   Things like:
   •  integration with version control, tied directly to your promotion process = you can't promote to prod if it doesn't go on a PR
   • environment management = you have developer "sandbox" and you have production environments, where you run the xact same command but dbt takes care of adapting it 
   • DRY = developer efficiency! You write things once and resuse, whether that means modularization, macros as functions or variables 
   • Documentation adn testing framework = pretty self explanatory 
   • Dependen ...

### [2025-08-13] Omrane (replies: 6)

Q: @user Is DuckDb or clickhouse a good alternative for BigQuery?

A: Hey, @user! Here you go:  I don't think I have an answer for this; you'll have to ask your fellows or instructors.
   ---
   Yes
   ---
   @user Thank you
   ---
   Hi @user, how's it going for you?, using DuckDB/Clickhouse for the zoomcamp, thanks
   ---
   Hi 
   @user I'm still in week 2. Still haven't used it yet.
   ---
   Hi @user how's it going so far, you done a project?

### [2026-01-23] Dan Powers (replies: 4)

Q: I am interested in using an alternative architecture in lieu of my temporary Google setup. Copilot recommends this freeware alternative. For your workflow (Python, SQL, Docker, data analysis), the best free replacements are:
   CLI replacement:
   • 	LocalStack + AWS CLI
   • 	MinIO + mc CLI
   BigQuery replacement:
   • 	DuckDB (fastest, easiest)
   • 	ClickHouse (for larger workloads). Has anyone made any progress in substituting for GCP?

A: I haven't but sounds interesting. I'd get with Gemini or ChatGPT and have it make you the docker compose file. Probably going to run into issues that won't be supported well in the channel, but think it would be a great project for learning and for you to post/write about.
   ---
   Amazing :clap:
   ---
   Yes please create a post about it
   ---
   awesome:clap:

---

## Where to find videos / playlist (current cohort) (44 threads)

### [2025-01-02] Sebastian Restrepo (replies: 4)

Q: Hi all, are there any updates regarding videos for kestra and gcp? the current playlist only includes the postgres setup.
   Thanks!

A: Can you be more specific/what you think is missing? https://www.youtube.com/playlist?list=PLEK3H8YwZn1oPPShk2p5k3E9vO-gPnUCf
   ---
   Hi @user, thanks for answering. Currently there are no videos related to GCP and kestra. All videos are related to working locally with Postgres. Will mentions at the end of video "*DE Zoomcamp 2.2.3 - ETL with Postgres"* that we will now do an example on GCP putting all the data in bigQuery but this video is nowhere to be found.
   Also if you go by the numbering of the videos, there seem to be videos missing from the playlist  like 2.2.4 or 2.2.6......
   There is some text related to gcp on the readme here https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration
   but not much of an explanation as in videos related to kestra and postgres
   ---
   Ah, I see. That is an unknown to me. I'll see what I can find out.
   ---
   They will be published soon

### [2025-01-05] Dehao Zhang (replies: 4)

Q: Hi team, I was following video 1.2.2 and ran into issues with mapping volumes. I am using WSL2 on windows. Initially when I used the same format described in the video I got an "Error response from daemon: invalid mode: /var/lib/postgresql/data." message. After I switched to another format it ran fine with "database system is ready for connection" but my ny_taxi_postgres_data local folder is not populating as shown in the video (i.e., still empty after the container starts running). Should I be concerned? I am able to use pgcli to connect to the db fine, but just want to know if unable to get  ...

A: Hard to say. You might not really be coming back to that piece after running it so it won't matter if the data is actually persisted. Think you'd want to spend some time with ChatGPT giving it your configuration, the symptoms and any issues you are running into if you wanted to resolve it. You could also just use docker volumes and cut out the bind mounts all together.
   ---
   https://www.youtube.com/watch?v=olUKRq-FVyo
   ---
   @user Thank you so much for your thoughts and its good to know that we might not need to come back to that. I did spend some time with ChatGPT on this and unfortunately the suggestions didn't quite work. I tried "docker volume create" which also worked but didn't populate the folder either.  In general is it a best practice to set this up to enable data persistence outside of container?
   ---
   Docker volume won't populate a folder as it is a docker volume. As far as best practice it's hard to say. In the "real world" you would probably be running a Managed Postgres Instance and wouldn't need to worry about it. Between a bind mount and a docker volume you would probably be running on Linux for a "real personal project" so the bind mount would be a bit easier than trying ...

### [2025-01-12] Atoyebi-Tanimola Rofiyat (replies: 3)

Q: Hi everyone, I noticed that the 2025 playlist on YouTube does not have module 1 videos. is there a reason for that?

A: you should check the "Data Engineering Zoomcamp" playlist (without 2025)
   ---
   I'm finding the video list for module 1 in the repo here https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform  These are all from previous years, but seem correct, are they?
   ---
   They are

### [2025-01-17] Youssif Hisham (replies: 3)

Q: Hello everyone, i am on the data engineering zoomcamp cohort 2025, i am following the repo for the cohort but i can't seem to find the videos for the modules on the yt channel, any help?

A: You have to open the folder in the repo
   
   https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   ---
   Here Youtube link
   https://youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb (https://youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
   ---
   thank you

### [2025-01-19] Dana Young (replies: 4)

Q: Hey, following this video for the first module
   https://youtu.be/ae-CV2KfoN0?si=VXwqqoHuSGe_8Wf1&t=1716
   at the point where he connects to postgres with the pgcli command
   `pgcli -h localhost -U root -d ny_taxi`
   
   and i get this error
   `connection failed: could not connect to server: Connection refused`
   `Is the server running on host "127.0.0.1" and accepting`
   `TCP/IP connections on port 5432?`
   
   how do i resolve this? in the video he never activates postgres explicitly

A: Hey! Did you start docker compose services? They were started in the video few seconds back
   ---
   @user Hey you are right, i somehow I did skip forward. but also guess realizing i'm following an outdated video to the course?
   ---
   I watched the same video :sweat_smile:  the video is quite old but still actual for the current cohort
   ---
   @user yeah to be honest, it kind of feels like the videos and instructions for the course are scattered. i'll be following one like i'm watching 1.2.1 video and then people in there say you need to watch 1.4.1 (I think the video I linked). I feel like the reason people struggle on this section isnt the concepts but the organization of material. appreciative of the effort but i'm spending a lot of time stringing together the content.

---

## Project: minimum score / passing / how scored (39 threads)

### [2025-01-14] Neda Noormohammadi (replies: 7)

Q: Does anyone know how we will be scored? Will our level of activity during the course, such as publishing notes or homework on social media, affect the final score?

A: Getting the certificate only depends on you completing and passing the Final Project
   ---
   I recently learned that, in addition to receiving a certificate, the Zoomcamp will publish a list of the top 100 students based on certain criteria. Looking for what those criteria are.
   ---
   Homework scores -&gt; which include learning in public and contributions to the FAQ
   ---
   could you please elaborate on this? Are homework scores independent of contributions to the FAQs? What do you mean exactly by learning in public?
   ---
   I would review the course launch video. I believe that was all covered by Alexey there.
   ---
   As far as I remember from yesterday's video, you get a point for every question answered correctly and for each learning in public link.
   you can click the link it'll start the video at the right time.
   https://www.youtube.com/live/X8cEEwi8DTM?si=2GB8D4kXj_qazfgI&amp;t=1483
   ---
   You helped a lot. I really appreciate it. @user

### [2025-01-24] Karina K (replies: 4)

Q: Hi @user, have you seen "*Execution failed!* With last error: `no JSON input found` "? Not able to pass upload_to_gcs task. All worked well with Kestra when adding the values directly to the files. I was able to follow the tutorial, do the backfill as in the tutorial and for my project. Then I regenerated the service account auth-key(.json) and moved the credential values to the .env file. I was using secrets as per documentation. I started to get this error and as I was not able to solve this moved to my prev hard coded values set up. The error still persists. Have you seen this error in the  ...

A: Hey! Did you follow this guide? https://kestra.io/docs/how-to-guides/google-credentials
   ---
   I added the creds directly to the kv yaml file:
   tasks:
     - id: gcp_creds
       type: io.kestra.plugin.core.kv.Set
       key: GCP_CREDS
       kvType: JSON
       value: |
         {
           "type": "service_account" ...
   
   it was in tutorial as well. So I think the answer is yes.
   ---
   Try going to the KV Store tab in Namespaces and adding it in there too
   ---
   thank you I try it now

### [2025-02-07] Thorben Siebeneichler (replies: 17)

Q: Hey there, I have a more general question, maybe towards those that have already done some data science with third party data:
   For my final project of the course I would like to work with some open data of a national non-profit organization. They offer a free api under CC0 1.0 license, so permission for use is there. However, fetching a reasonable set of data will boil down to a few hundred, maybe a couple thousand requests. I am worried, that my ingestion pipeline would get blocked by DDoS protection, and I don’t wanna cause issues for them as well. Is there any experience with the ethics of  ...

A: Sounds logical to me. Maybe also include the process for gathering the data in your documentation. Scaping is and will continue to be a grey area. Do it for profit = crime. Do it for personal project = probably not a crime. Do it if you are OpenAI = Get valued at $260 Billion.
   ---
   Do they provide an api documentation? Maybe they say something about request rate and intervals. I would stick to their limits :wink: 
   
   You could setup (or hire) some proxys to hide your ip to not get blocked. Sometimes changing browser header helps when scraping. Or you could tell your router to reconnect to get a new ip. It doesn’t sound likely you would need these techniques
   ---
   Yeah, they offer api documentation but no mention of any rate limits.
   
   If you are curious, this is the API I want to go for: https://www.abgeordnetenwatch.de/api
   
   It is in german, but luckily translators are a thing :slightly_smiling_face:
   
   AFAIK, there are no contraints for the minimum size of the dataset our project needs to be based on, right? their filters allow for 1000 entities downloaded per request, so if I limit myself to a few dozen requests I could still get a meaningful set of data to show some stuff with, and nobod ...

### [2025-02-13] Jesse B (replies: 2)

Q: Just able to start the course and tried to submit HW1. However, the Homework 1 scoring is locked and states "This homework is already scored. You didn't submit your answers." AFAIK, there's no way to submit HW1 at this point?
   
   Did I do something wrong or is there a reset?
   Homework 1: Docker, SQL and Terraform (https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1)

A: think the response is https://datatalks-club.slack.com/archives/C01FABYF2RG/p1739449187256339
   ---
   HW1 is closed for scoring but you can check answers anyway

### [2025-03-13] Alexis Pantig (replies: 1)

Q: Whats the number of points we need to achieve on the project to pass?

A: Bumping (:

---

## How to join / register / enroll (34 threads)

### [2025-01-02] Patrick Edosoma (replies: 6)

Q: Hello all, Happy New year. My friend registered for this course and he has no basic knowledge about python. What could you possibly suggest he do?

A: Learn Python. :neutral_face:
   ---
   Joking. Kind of. It may not be feasible for him to make it through this time around. Not to discourage him, he should give it a shot, but the learning curve will be quite steep and it really depends on how much time he has on his hands and how quickly he can pick it up. Sentdex on YouTube has some great intro videos if time is tight. CS50P is GREAT, but the time investment will be much larger. He could also just use ChatGPT to get started. Needs to probably learn variables, functions, loops, conditions and understand why/how Python is Object Oriented and what that means.
   ---
   It took me 3 years and 4 tries to get through CS50X. So my advice would be for him to jump right in and try to learn Python as much as he can. Doing this course might help guide his learning and even if he doesn't get through this cohort it will probably show what areas he is lacking in knowledge of Python. For this course, learning programming and I guess life in general I would say - try, and don't get discouraged, we all started somewhere.
   ---
   Is your friend a complete beginner, then I agree to Michael. But if he knows another language like Java, C or so, then python is easy  ...

### [2025-01-02] Nash (replies: 4)

Q: How do you join this course?

A: You already have joined it. Welcome!
   ---
   Also check the pinned links and join the telegram channel with announcements
   ---
   I don't know what you're talking about
   ---
   If you are looking for Luxury Edition Tires for your small truck or SUV I would advise you to check around at your local tire shops. If they do not carry them there are plenty of options available through online retailers.

### [2025-01-05] Shilpa Leo (replies: 3)

Q: Hello from Singapore! I've registered for the DE course starting next week. I added the Google calendar as well, but realized the timings are not Asia friendly. The launch happens at midnight SG time. :disappointed:
   Will the live sessions be recorded or how can folks like me seek support given the time diff? Thanks!

A: yes, it will be. we can also see the passed recorded live session as well.
   ---
   @user All video classes are already pre-recorded. The live sessions we'll have are mostly for Q&amp;A  and (maybe) live sessions for the workshops
   
   Start here: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   
   Video links are already embedded
   ---
   Will there be no further updates to videos? So I can move on my own (hopefully faster) schedule.

### [2025-01-06] Omar Abdelaleem (replies: 1)

Q: Hello everyone, I want to register to the 2025 DE-Zoom camp, how can I do so?

A: https://airtable.com/appzbS8Pkg9PL254a/shr6oVXeQvSI5HuWD

### [2025-01-13] Willy Dongmo (replies: 1)

Q: Hello,
   How can I check that I’m registered for this cohort?

A: You are. Everyone is

---

## Course calendar / google calendar / deadlines list (33 threads)

### [2025-01-05] Shilpa Leo (replies: 3)

Q: Hello from Singapore! I've registered for the DE course starting next week. I added the Google calendar as well, but realized the timings are not Asia friendly. The launch happens at midnight SG time. :disappointed:
   Will the live sessions be recorded or how can folks like me seek support given the time diff? Thanks!

A: yes, it will be. we can also see the passed recorded live session as well.
   ---
   @user All video classes are already pre-recorded. The live sessions we'll have are mostly for Q&amp;A  and (maybe) live sessions for the workshops
   
   Start here: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   
   Video links are already embedded
   ---
   Will there be no further updates to videos? So I can move on my own (hopefully faster) schedule.

### [2025-01-12] Mian Muhammad Ashhad (replies: 1)

Q: Hi everyone. Is there a schedule given to watch the lectures and submit the homework? I have university work besides this course so I just want to follow a pre-made schedule if that is possible.

A: Yes
   
   https://courses.datatalks.club/de-zoomcamp-2025/ (https://courses.datatalks.club/de-zoomcamp-2025/)

### [2025-01-13] Patrick D. Faerber (replies: 2)

Q: Is there a calendar invite to add these classes to our google calendar?

A: • Subscribe to the public course Google calendar (https://club.us19.list-manage.com/track/click?u=0d7822ab98152f5afc118c176&amp;id=01691a16db&amp;e=49b4431dfe) (subscription works from desktop only)
   It should be worked~
   ---
   Thank you!

### [2025-01-13] Andrew Shao (replies: 2)

Q: Hi, I got the email a little late, and now I realize I missed the live class. I assume it will be posted on youtube? Also, I added the google calendar, but don't seem to see any events on it?

A: https://www.youtube.com/watch?v=X8cEEwi8DTM
   ---
   Thanks

### [2025-01-14] Hossein (replies: 2)

Q: Hi:) thanks for the first session! I couldn’t join live but I watched afterwards! Where I can see the course schedule?thanks:)

A: https://courses.datatalks.club/de-zoomcamp-2025/
   ---
   Thanks:) I checked it but it is for homework submission timing. Let me know that the next session is 28th of January? Then let me know what time?:) I appreciate :)

---

## Where to start / first steps / what to install (32 threads)

### [2025-01-04] U06P5LB5UKT (replies: 3)

Q: Hi folks, Good Day.!!
   I'm getting started with week-1 and completed docker-postgres setup. I noticed when I run the postgres docker image, it automatically creates this empty folder. Just wondering what this is and why its getting created? Any thoughts ??
   @user

A: Hey, @user! Here you go:  When you run the PostgreSQL Docker image for the first time, it creates the directory `/var/lib/postgresql/data` inside the container. This directory is where PostgreSQL stores its data files, including databases, tables, and logs. The creation of this empty folder happens because the PostgreSQL Docker image is designed to initialize a data directory upon startup.   If you have mounted a local directory to this path (e.g., using the `-v` option), the files in your local directory will be used as the data directory, and PostgreSQL will write its data there. If the local directory is empty when you first run the container, the PostgreSQL image will populate it with default files necessary for its operation.   This behavior is normal and expected as part of the initialization process of the PostgreSQL database when using Docker. If the folder appears empty after you run the container, ensure that the volume is mounted correctly and check for any permission issues that may prevent PostgreSQL from writing to the directory.
   ---
   @user - Yes i've mounted local directory. But docker automatically creates another folder named 'ny_taxi_postgres_data;C' in my host mac ...

### [2025-01-05] Esin Comak (replies: 1)

Q: Which tools I have to install for course?

A: Please use threads to keep the discussion more organized: https://datatalks.club/slack/guidelines.html#taking-part-in-discussions

### [2025-01-08] Francis (replies: 7)

Q: Good afternoon, everyone. Just new here. Where do I begin from?

A: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   ---
   is their a free trial of GCP?
   ---
   Yes
   ---
   do I need a business email
   ---
   Anything should work
   ---
   Thank you
   ---
   Did you start yet?

### [2025-01-09] Esin Comak (replies: 4)

Q: Hello everyone, I just started to new cohort but I am really confused abot where I have to start??? Completing module 1 is enough to 1st week of the course?? Please and please help me. I really eon’t know how I should follow. I am dissaponted at the beginning of 1st week

A: https://dezoomcamp.streamlit.app/
   ---
   https://www.youtube.com/watch?v=DPnAOu2csYA, this is what I got from the email, the pre-course Q&amp;A
   ---
   the course has not started until 1/13. this is week 0, if you'd like to start early you can.
   ---
   Disappointment is part of this industry. Welcome aboard :blush: (a joke)
   
   I would start by studying the Git repository

### [2025-01-13] Ahmed Alaa (replies: 5)

Q: What is required of me to prepare before the start of the stream I setup docker and Postgres and python

A: Docker and python
   ---
   Thanks
   ---
   Any  videos help me to set up and which clock will stream start??
   ---
   Supposed be now
   ---
   Sorry someone tell me it’s starting after one hour

---

## Where is the live link / how to join the session (30 threads)

### [2025-01-12] Vijaya Solanki (replies: 2)

Q: looking forward to taking this course starting tomorrow. what time does this course start and how do we join the live stream?

A: Live stream Monday at 17:00 CET
   ---
   so is that 11am EST?

### [2025-01-13] Gaurav Sharma (replies: 2)

Q: How to join today's live session?
   Will it be a youtube live session or any other platform?

A: Youtube live session. Check the #announcements channel
   ---
   Thanks @user

### [2025-01-13] Vijaya Solanki (replies: 4)

Q: Hello Everyone,
   so how do we join the session now?

A: literally check the message that was posted right above your message...
   ---
   yes i did check the message afterwards. Looks like it will be at 11am est. Thank You!
   ---
   so will it be at 11am est everyday?
   ---
   @user No. Videos are all pre-recorded. Live sessions might happen once in a way for QA and if I remember correctly for the DLT workshop

### [2025-01-15] U0877HQLRJA (replies: 3)

Q: I'm looking at the deeply-nested Terraform section of Module 1 (https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform), and have discovered a `broken link` to Audio (https://drive.google.com/file/d/1IqMRDwJV-m0v9_le_i2HA_UbM_sIWgWx/view?usp=sharing)

A: @user thank you. It seems that's from 3 years ago and hasn't been updated yet...
   ---
   I have no memory of it and probably we should just delete it. I'll do it :smiley:
   ---
   removed. we will never know what was inside

### [2025-01-31] Henry Eyo (replies: 6)

Q: At this point, I must voice out how I feel. I'm seeing week 2, week 3 and stuff from some folks and I'm wondering, am I really that busy to have missed out on these classes or their reminders? Could it be that if you don't show up here everyday, the cohort might just be over while waiting for the live session YouTube link to pop up in your mail. What exactly have I been missing, can someone kindly fill me in? Are we supposed to be learning on our own or there are instructors to take these courses once their time is due? When is the next class after Alex instructed us in the first week on GCP,  ...

A: As you might have noticed there is a github repo full of information (DE course is running since 2022).
   
   Read the FAQ :wink:
   
   For Homework there is the course management platform
   
   The top 7 pins will bring you up to date
   
   We are in week 2 atm, week 3 will start on monday with workshop see google calendar (https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)
   ---
   Are you in the telegram channel?
   ---
   From what I understand till now is, it is more like peer to peer learning where we help each other either through slack or telegram or anyhow online. So my advice is try to get as much as information from the FAQ and instruction trough the github repo. I dont think it would be like a traditional prpgramming course where there is a teacher and a regular class to teach step by step to solve the problem (altough there is already a record of the last cohort).
   ---
   Yes, I am but I am more frequent here than on the Telegram.
   ---
   So the important announcements are posted there, if you're already in the channel, you won't miss anything. If not, you need to watch messages from AuTomator, it reposts them here
   ---
   @user have you read the RE ...

---

## Certificate: when received / how to get (29 threads)

### [2025-02-09] ABHISHEK DAS (replies: 3)

Q: Hey I just got to know about the course, how can I ensure I get a certificate?

A: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1739049692771499?thread_ts=1739046981.602249&amp;cid=C01FABYF2RG
   ---
   Ok I'll follow asking questions (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/asking-questions.md) , sorry about that.
   ---
   Basically, just do the project on time and the certificate is yours.

### [2025-02-11] Rimsha Bashir (replies: 2)

Q: Hi everyone, nice to meet ya'all. I'm a software engineer, and new to this camp. Hoping I'm not late here! How long will the mterials be accessible and the certificate available?

A: As long GitHub doesn’t remove the materials, I guess.
   
   Certificates will be available after project evaluation - end of March/mid April. It will be on the course management platform (see bookmarks :bookmark_tabs: in this channel) for you to download. The ones from last year’s cohort are still available.
   ---
   Okay, great! Thanks so much!

### [2025-03-06] Vasupriya Narayanan (replies: 2)

Q: Hey guys,when is the last date to submit the project for 2025 to earn the certificate ?

A: As far as I know that is still to be decided.
   ---
   U can checkout the course management platform (https://courses.datatalks.club/de-zoomcamp-2025/) (see bookmarks tab :bookmark_tabs: ) for due dates. 
   
   Keep in mind, to get a certificate, you have to review 3 peer projects within a week after submission form closes and the evaluation form opens.

### [2025-03-23] Su (replies: 2)

Q: Hi all， for the final project，if  I attempt the first one, which is due at 1 April. How soon will I get my result/score for the certificate? And if it failed, I can make the attempt for the second time at 15 April?

A: You will see your results after the evaluation is over. But we will generate the certificates only after all the attempts are over
   ---
   Do we have a finish date for the evaluation? just want to check that if failing on the first attempt, will I have a chance/enough time to modify and summit again? or the avaluation will only finish after all the attempts are over?

### [2025-03-25] Amr Mahmoud (replies: 13)

Q: I have submitted the project and I have used dlt, how can I apply for a tshirt :'D ?

A: We will share a form soon
   ---
   Did you use DLT for data ingestion part ?  Vs using Kafka ?
   ---
   Hi, can I ask you what technologies you used to transform data thereafter?
   I was thinking to:
   • get the data to datalake with dlt
   • create table or external table in Bigquery 
   • transform with dbt.
   ---
   @user yes, i used it for data ingestion,that is to move it from gcs into bigquery
   ---
   @user i used dlt to move the data from gcs into big query then I used dbt to transform the data
   ---
   @user Looks good. I am also thinking of using your same approach. The only part I am still exploring is how to orchestrate all of them in kestra.
   ---
   @user thanks for your reply. Why did you prefer dlt in that step instead of using an external table? Just curious about your requirements.
   ---
   @user I am also a bit nervous about that part but I hope this page will give me something.
   https://dlthub.com/docs/walkthroughs/deploy-a-pipeline/deploy-with-kestra
   ---
   @user you are so welcome,
   do you mean why I didn't add the tables into bigquery manually?
   ---
   @user well, I thought that a pipeline would be more suitable as a final project more than doing them manually
   ---
   True, full automation would be good. Thank you!
    ...

---

## Learning in public / posting on social (28 threads)

### [2025-01-09] Mauduit Elouan (replies: 1)

Q: Hi everyone.
   
   Regarding learning in public and posting your progress on LinkedIn, since I’m French and aiming for French companies, do you think that posting in English would still attract French companies? Or should I publish in French?

A: I think you'd reach larger audiences if you post in english. As remote-first companies can also reach out to you. But honestly, that depends on your current network on LinkedIn...

### [2025-01-19] GUANYI LU (replies: 1)

Q: @user what is the benefit of post the learning in public links in homework?

A: Hey, @user! Here you go:  Posting learning in public links in your homework has several benefits:  1. **Point Accumulation**: For each learning in public link you submit, you earn an additional point towards your overall score in the course. This contributes to your total points displayed on the leaderboard, which includes points from homework, FAQs, and learning in public submissions.  2. **Visibility and Networking**: Sharing your learning publicly helps you expand your network. It increases your visibility in the community and may lead to opportunities such as invitations to meetups, conferences, or podcasts.  3. **Documentation of Progress**: Documenting your learning journey allows you to track your progress and reflect on the challenges you faced and how you overcame them, which can be beneficial for personal growth and understanding.  4. **Job Opportunities**: By showcasing your skills and knowledge publicly, you may attract potential employers or clients interested in your work.  These aspects make learning in public a valuable component of the course experience. For more details, you can refer to the learning in public document: Learning in Public Document (https://github. ...

### [2025-01-25] HAFIZ AZIZI (replies: 2)

Q: @user can we update the 'Learning in public links' even if the homework is closed?

A: Hey, @user! Here you go:  You can update your submissions until the form is closed. This means that even if the homework is closed, you should still be able to update the 'Learning in public links' if you have previously submitted your homework.
   ---
   When the form is closed, you can no longer submit learning in public links

### [2025-02-08] Issa AlBawwab (replies: 4)

Q: Hello i finished the dbt fundementals course before starting with module 4 upon @user advice, and I want to share about it on linked in, is it possible to use that post to get learning in public points?

A: Yes, go for it
   ---
   but its not part of a homework so where do i add the link
   ---
   You can do it for module 4
   ---
   good point

### [2025-04-06] Julia (replies: 2)

Q: Hi! Could you please tell me: if I add my own links under the "Learning in public links" section while reviewing other projects, will those links be counted towards my final score?

A: Will this count towards getting a passing grade? Or just for leaderboards?
   ---
   Yes. It's only for the leaderboard. Only the points you get for the actual project determine if you pass or not. But also peer review is mandatory for paying

---

## Self-paced / previous cohort videos still relevant (25 threads)

### [2025-01-11] Dinesh (replies: 1)

Q: Hi Team,
   I would like to learn/use Airflow for orchestration in modules 2. Can I learn from the previous cohort? Are they still relevant?
   @user

A: Hey, @user! Here you go:  You can use the Airflow videos from previous cohorts if you'd like. These materials are still relevant and can help you in learning Airflow for orchestration in module 2. However, keep in mind that the current course is using Kestra for orchestration this year. You can still learn Airflow independently and apply that knowledge to your projects.

### [2025-01-21] Julian Buccat (replies: 1)

Q: Hi all, I ended up doing a previous cohort's Week 1 homework using September 2019 dataset. I have updated the URL in my YAML to pull from the correct October 2019 dataset via URL, but simply replacing the URL didn't work or I accidentally broke something else.
   
   Im having trouble verifying if my service: taxi-ingest-green is actually ingesting the new, correct dataset to the designated table "green_taxi_data". I think im viewing the September 2019 dataset still via pgAdmin.
   
   is there a query I can run against the current data in table "green_taxi_data" that will confirm whether I have the right ...

A: ```select count(1) from <GREEN_TAXI_TABLE_NAME_HERE>```
   You should get 476,386 rows if you ingested the `green_tripdata_2019-10.csv` (needed for the homework)

### [2025-03-31] Kristina A (replies: 5)

Q: Hi, guys! If I start the Self-paced version now, will I have my task’s review by any mentor or smth like that? How can I check if I do everything correctly? Thank you in advance

A: No. Best way is to engage with the material and ask questions here in the slack channel when you hit a "brick wall". The channel is most active during the cohorts, but it's always a little bit active with folks that will help.
   ---
   Thank you, Michael :pray: :heart:  I really need it and I can’t wait until January, 2026 :sob:
   ---
   there are also some great notes from other students that can help you a lot
   ---
   Oh, thank you! How can I find them?
   ---
   At the bottom of each lesson, for example: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform#community-notes

### [2025-04-16] Gil Segev (replies: 4)

Q: This is not a question related to the course material but to my self-paced project. Any help is appreciated!
   
   I am trying to run Airflow in Docker (in WSL2), with the following Dockerfile being called in my docker-compose.yml.
   
   However it keeps failing on the `RUN apt-get update -qq && apt-get install vim -qqq`  command (see below), due to network issues with Docker in WSL2 (according to ChatGPT). I have already tried modifying  the Docker Engine config to route Docker's DNS to Google or Cloudfare (8.8.8.8 or 1.1.1.1) but still no success. Has anyone got experience solving network issues for D ...

A: Not the answer you are looking for, but I would highly recommend creating a Linux VM, either locally or in the cloud and just running it there. IMO there is no need to get bogged down with Windows stuff. Doesn't really add much to the tool belt.
   ---
   That being said you could try
   ```wsl --shutdown```
   and then try building your image
   ---
   Dockerfile:
   ```# Licensed to the Apache Software Foundation (ASF) under one or more
   # contributor license agreements.  See the NOTICE file distributed with
   # this work for additional information regarding copyright ownership.
   # The ASF licenses this file to You under the Apache License, Version 2.0
   # (the "License"); you may not use this file except in compliance with
   # the License.  You may obtain a copy of the License at
   #
   #    http://www.apache.org/licenses/LICENSE-2.0
   #
   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.
   ARG BASE_AIRFLOW_IMAGE=apache/airflow:2.10.5-python3.12
   FROM ${BASE ...

### [2025-05-31] Mike Presman (replies: 1)

Q: @user I want to do this course self-paced im not interested in the certificate, just the learning. How can I get started today?

A: Hey, @user! Here you go:  To get started with the course in a self-paced manner, follow these steps:  1. Access the course materials on GitHub, which are available for independent study. You can find them in the DE zoomcamp GitHub repo (https://github.com/DataTalksClub/data-engineering-zoomcamp). 2. Watch the course videos to begin your learning. 3. Join the [Slack community](https://datatalks.club/slack.html) to connect with other learners and get support as you progress through the course. 4. Refer to the [FAQ document](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing) for additional guidance and information.  By following these steps, you can start learning right away without the pressure of deadlines.

---

## Country / city / study buddy lookup (21 threads)

### [2025-01-13] Joel Nyongesa (replies: 7)

Q: Hi everyone, Joel here, from Kenya! Happy to be here with all of you!
   I'm looking for a study partner to help with accountability. Anyone?
   Let's get cracking!

A: Hi Joel, I am Ian, from Kenya as well. Lets get cracking
   ---
   Great Ian. I'm so excited about this course and happy to have you here as well!
   ---
   Cant wait to get my hands working:100:
   ---
   Hey Joel and Ian i am also from Kenya ... Looking forward to be studying with you guys.
   ---
   Great! We can form a study group/channel pals, what do y'all think?
   ---
   Agreed, I'm Griffin from Kenya too, looking forward to this...
   ---
   Its a good idea, i agree:100:

### [2025-01-13] Mona Y (replies: 3)

Q: Hi all anyone from Toronto :flag-ca:?

A: Also I am in Toronto
   ---
   Hello! I'm also from Toronto :slightly_smiling_face:
   ---
   I am in Toronto!

### [2025-04-22] Jia Zhang (replies: 1)

Q: hi  everyone, i'm in Torrance, LA, anybody wants to team up and study together sometimes?

A: We can team up virtually sometimes,

### [2025-09-15] Daud Chaznavi (replies: 6)

Q: *Hello everyone!*
    I’m starting the DE Zoomcamp today and was wondering if anyone else is just getting started (or recently started). It would be great to team up and keep each other accountable along the way.
   – Daud
    _P.S. Anyone else here from Stockholm?_

A: im starting it too . im not from Stockholm
   ---
   Hi Daud, I am planning to start DE Zoomcamp from next week and I am planning to spend 1 hour only every night. I too live near Stockholm, so lets connect and work together!
   ---
   Lets create a discord group! Hopefully there will be more of us
   ---
   Hi! I'm starting the course today. I would love to team up with other course takers, too.
   ---
   I am also starting the course today. Not from Stockholm though
   ---
   i have also started today !! keep going... !!

### [2026-01-06] Ranjan Yadav (replies: 4)

Q: Hey all!  Is anyone here looking for a learning/study buddy? I'd love to team up with someone motivated with this course to complete along with little projects discussion inbetween as I am already good with foundation.

A: Hey! Same here. I've been doing the previous year cohorts till now. week 5 and 6 are remaining though.
   ---
   Hey! Same here. I've just started my journey in data engineering, and I am incredibly motivated and fully committed to putting in the effort to succeed.
   ---
   i would like to collaborate with anyone.
   ---
   Interested too. Seeking to learn and grow in a community way.

---

## Homework answer doesn't match options (21 threads)

### [2025-01-18] Ryan Thackston (replies: 4)

Q: @user
   Hi I've got a question for #5 on Homework #1, I think some of the text is leftover from the 2024 cohort.
   https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/01-docker-terraform/homework.md
   
   *Question 5. Three biggest pickup zones*
   Which were the top pickup locations with over 13,000 in `total_amount` (across all trips) for 2019-10-18?
   Consider only `lpep_pickup_datetime` when filtering by date.
   
   *I may be doing something wrong but when I filter by Borough I get 3 that are over 13,000 total_amount for trips. When I filter by zone (which it looks like the ques ...

A: you're supposed to find the sum of total_amount (which is in dollars) not the trip_distance (in miles)
   ---
   Oh whoops ok
   ---
   Yep that makes sense. I got the answer now
   ---
   Just to piggy bag and in case someone else runs into a similar problem, I had issues with #total_amount and returning no result. But then realize it should be aggregated for that Zone, but not a single trip's total_amount.

### [2025-01-20] Cairo Cananea (replies: 4)

Q: Hi everyone!
   Working on homework week 1 and the results are different from option.
   Question 3, for example, I'm trying to fin how many trips for the dates and my query returns 104,830.
   Someone had the same problem? How did you fix it?

A: Hello, try not to write any Date or  time condition in the Where clause in your query, then you will get the same result as in the answer option.
   ---
   Hello @user - I’m curious, did it work for you?
   ---
   @user yes, it did work!
   ---
   I don’t know how you managed without these conditions,
   I still used them,
   for me it had different reasons (I just used a wrong column in the query). ;)

### [2025-01-23] M Zakie Arfiansyah (replies: 6)

Q: Hi, can I ask something about the question 3? In question number 3, it is stated that "During the period of October 1st 2019 (inclusive) and November 1st 2019 (exclusive)", what is the meaning of inclusive and exclusive? I have tried to create a query for the calculation of trips from October 1 - November 1, 2019, but the result of the addition is different from the answer option. my result on up to 1 mile is 88k. Is there anything wrong with my script? cc @user
   
   here's my script cmiiw
   ```SELECT
   	CAST(lpep_pickup_datetime AS DATE) AS Day_pickup,
   	COUNT(1)
   FROM
   	green_trip_data
   WHERE
   	trip_dist ...

A: Hey, @user! Here you go:  The terms "inclusive" and "exclusive" specify whether the endpoints of the date range are included in the query. "Inclusive" means that the starting date (October 1st, 2019) is included in the count, while "exclusive" means that the ending date (November 1st, 2019) is not included. Therefore, you should only count trips that occurred on or after October 1st, 2019, up to but not including November 1st, 2019.  Your current script is counting trips using the `between` operator, which is inclusive on both ends. This means that your query includes trips on November 1st, which should not be counted according to the question.   To fix your query, you need to adjust the date condition in your `WHERE` clause. Use the following script:  ```sql SELECT     CAST(lpep_pickup_datetime AS DATE) AS Day_pickup,     COUNT(1) FROM     green_trip_data WHERE     trip_distance &lt; 1     AND CAST(lpep_pickup_datetime AS DATE) &gt;= '2019-10-01'     AND CAST(lpep_pickup_datetime AS DATE) &lt; '2019-11-01' GROUP BY     Day_pickup ORDER BY     Day_pickup ASC; ```  This revised query uses `&gt;=` for October 1st and `&lt;` for November 1st, ensuring that trips from October 1st throu ...

### [2025-02-08] Gregory Choong (replies: 27)

Q: Anyone else on Module 3 for Datawarehousing? I think i'm doing it wrong since i'm getting different answers for the homework. I went ahead and created the external table for the yellow trip data. I also created a regular table via this code. When ever I try to query both of them. I both get 155 MB for read data. Am I missing something or doing something wrong?
   
   ```CREATE OR REPLACE TABLE `zoomcamp-03-450318.nytaxi_yellow.yellow_tripdata`
   AS SELECT * FROM `zoomcamp-03-450318.nytaxi_yellow.external_yellow_tripdata````

A: hint: you are missing a small detail in the question, read it again
   ---
   It's the estimated? Where can we figure out that information. IN some of the notes it shows a notification window, but I do not see it.
   ---
   Ah! I need to remove the caching.
   ---
   Was able to figure out the answer that way.
   ---
   That's strange—I unchecked "Use Cached Results," but both queries still processed 155MB.
   ---
   @user The question asks for "estimated" not "processed"
   ---
   I might have missed it—did you find the estimated bytes in the *Execution Details* tab?
   ---
   no need to run the query, you just select it and the estimated amount will appear at the top right
   ---
   :tophat::sparkles:thank you Abdelali!!
   ---
   Sorry adding on to this thread, im also getting both the same 155MB. I have disabled caching and selected the query to run to show at the top right but both still shows the same answer any help would be appreciated!
   ---
   can you show us the query you used for creating the external table + the query you're using to select the count
   ---
   ```select count(distinct PULocationID) from my-project-57990-1714709310544.zoomcamp.yellow_tripdata;
   
   select count(distinct PULocationID) from my-project-57990-1714709310544.z ...

### [2025-02-11] Ahmad Ryan Permana (replies: 4)

Q: Why is it that when I try to calculate the number of different PULocationIDs for the entire dataset in both tables (external_yellow_tripdata and table_yellow_tripdata) the results are the same for bytes processed but the multiple choice in homework 3 does not have the same answer for the results of both tables? should the cache results be enabled? @user

A: Hey, @user! Here you go:  When counting the distinct PULocationIDs for both the external table (`external_yellow_tripdata`) and the regular table (`table_yellow_tripdata`), you may find that the processed bytes are the same (e.g., 155.12 MB). This is likely because both queries might be processing the same amount of data due to how the COUNT(DISTINCT column) function operates, as it needs to evaluate distinct values from the entire dataset.  However, the homework asks for the **estimated amount** of data read, which can differ significantly from the processed data. The estimated bytes for each table can be different based on how they are structured (e.g., whether they are external, materialized, partitioned, or clustered). In your case, the external table may have an estimated read size that is smaller or larger than the regular table, depending on the data organization and query optimizations.  Regarding caching results, it is important to disable it when trying to get the estimated amounts, as cached results can affect the metrics you see. The discussion in the Slack thread indicates that disabling caching is necessary to get the correct estimated bytes. If you have unchecked "Us ...

---

## Homework include code / SQL / screenshots in repo (19 threads)

### [2025-01-12] U08768VPL74 (replies: 5)

Q: guys i want to ask that this submitted link for Module 1 Homework: Docker & SQL cannot access? i try to figure it out but still error when i try to get in that link. Then, will the deadline for each homework in DE Zoomcamp 2025 be the same as the deadline for homework in DE Zoomcamp 2024?

A: https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1 (https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1)
   ---
   Where is your link from?
   ---
   The link on github is broken, it says hw01 instead of hw1
   ---
   I created a pull request for that issue :slightly_smiling_face:
   ---
   Merged! Thank you!

### [2025-01-13] Muyiwa Oladimeji (replies: 2)

Q: Which option between GitHub (https://courses.datatalks.club/accounts/github/login/) and Slack (https://courses.datatalks.club/accounts/slack/login/) is best for login to the Homework portal to submit the homework - https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1

A: i signed in with slack, couldn't login with github
   ---
   I just used Google

### [2025-01-18] Viktorija Alexeeva (replies: 2)

Q: @user, pls advice, to submit homework 1 I should answer on questions on datatalks platform (https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1) and add homework URL. this URL should contain path to my github repo, correct? in my repo I need only txt file with SQL scripts?

A: Hey, @user! Here you go:  To submit Homework 1, you need to answer the questions on the DataTalks platform at https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1 and include your homework URL. This URL should point to your GitHub repository where you will upload your code for solving the homework.   In your repository, it is recommended to include all relevant code, and while you can have a text file containing SQL scripts, you might also include other formats like Jupyter notebooks or code files for any other solutions you developed. If your solution includes SQL or shell commands that are not in traditional file formats, such as scripts, you should include these directly in the README file of your repository.   Make sure your repository is structured in a way that clearly presents your work, as it can also serve as a portfolio for future employment.
   ---
   Txt is fine, but I'd use markdown

### [2025-01-22] Saanu (replies: 4)

Q: @user should all homework be in a single repository or each homework should have its own repository?

A: Hey, @user! Here you go:  Each homework should have its own repository. This allows you to organize your work better and makes it easier for coaches and potential employers to review your progress and projects individually. You can create a separate GitHub repository for each homework assignment, containing the relevant code, scripts, or any other files related to that specific homework.
   ---
   @user this is wrong, you can put it all in a single repository (just organize it with folders for each module), and have the assignmens/code put on their respective folders
   ---
   Yes but for the project it's better to create a separate repo
   ---
   @user thanks for the clarification. 
   @user this is noted, thanks.

### [2025-01-22] Sajjad Hossain (replies: 8)

Q: Hi, can anyone please clarify if there needs to be anything committed in github repo for Moduel-1 Homework (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2025/01-docker-terraform/homework.md)? Just we just need to submit the homework here (https://courses.datatalks.club/de-zoomcamp-2025/homework/hw1)? I am bit confused about what should we provide in homework URL.

A: well it says:
   
   &gt; When submitting your homework, you will also need to include a link to your GitHub repository or other public code-hosting site.
   &gt; This repository should contain the code for solving the homework.
   &gt; When your solution has SQL or shell commands and not code (e.g. python files) file format, include them directly in the README file of your repository.
   so what exactly is unclear?
   ---
   you can create subfolders for each week/homework
   ---
   Thank for pointing it out. I was confused on adding them directly in the README, now creating separate readme for homework solves that as I was thinking to adding them in the primary readme which doesn't make sense. Thanks again
   &gt; When your solution has SQL or shell commands and not code (e.g. python files) file format, include them directly in the README file of your repository.
   ---
   I think, we can create a separate markdown (.md) file in the repository that contains the solution code. Then use the file URL as the solution URL. Is my opinion right or wrong?:pray:
   ---
   @user i didn’t understand what should i do in homework url, could you please help me ?
   ---
   Sure,
   What we need to do is following these steps
   
   1. create a direct ...

---

## Recordings / live sessions / office hours (17 threads)

### [2025-01-01] Sherry Li (replies: 4)

Q: Hi everyone , will there be any recording for the zoom camp? Thank u

A: Ask @user 
   
   &gt; Hi everyone , will there be any recording for the zoom camp? Thank u
   ---
   Hey, @user! Here you go:  Recordings for the Data Engineering Zoomcamp are available on the YouTube channel of DataTalksClub. It is advisable to subscribe to the channel and check the course playlist for all the videos related to the course. You can find the playlists for the 2024 cohort, which will include the recordings.   If you have any further questions, feel free to ask!
   ---
   https://datatalks-club.slack.com/archives/C01FABYF2RG/p1734926196083809?thread_ts=1734898057.675589&amp;channel=C01FABYF2RG&amp;message_ts=1734926196.083809 (https://datatalks-club.slack.com/archives/C01FABYF2RG/p1734926196083809?thread_ts=1734898057.675589&amp;channel=C01FABYF2RG&amp;message_ts=1734926196.083809)
   
   There will be live sessions when course starts on 13th Jan and for dlt workshop. See google calendar  (https://calendar.google.com/calendar/?cid=ZXIxcjA1M3ZlYjJpcXU0dTFmaG02MzVxMG9AZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ)
   ---
   https://datatalks-club.slack.com/archives/C01FABYF2RG/p1735530947573509 (https://datatalks-club.slack.com/archives/C01FABYF2RG/p1735530947573509)

### [2025-01-13] Matt (replies: 1)

Q: Hi @all will the opening lecture be provided as recording? Thank you

A: Yes

### [2025-01-13] Almulham Albusaidi (replies: 1)

Q: @user when is the next office hours?

A: Hey, @user! Here you go:  There won't be any weekly office hours for the 2025 cohort, as mentioned in the Slack thread. However, it's noted that there might be some calls during the Capstone period to address questions, but those will be announced in advance. You can check the Google Calendar for any updates regarding office hours.

### [2025-01-14] Yinglu Deng (replies: 2)

Q: Hi I’m new to here class. Just watched the live session recording, and where should I begin before hw1? Should I start watching the FAQ documentation? cuz I don’t see much prerequisite materials for first hw. Thanks

A: This material from last year should be relevant https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   ---
   thanks

### [2025-01-15] Olakunle Opajobi (replies: 3)

Q: Hello 
   
   Please how do I access the recording of the lecture??
   
   And is the class everyday??

A: You can access it here https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   ---
   I find that on both my work laptop and my personal one, the videos don't always show up at that link. There should be a video for every place the movie camera :movie_camera: symbol, but often they are missing when I look at the rendered version of the Readme. But there's an easy workaround if others are also having this problem: view the raw markdown code and you can see the video links. You can access the raw markdown with the "code" button on the README.md file. That takes you here:
   https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/01-docker-terraform/README.md?plain=1
   ---
   Thank you @user @user

---

## Score / leaderboard / points (17 threads)

### [2025-01-29] Nguyễn Tuấn Huy (replies: 3)

Q: hello everyone, I have submitted week1 homework, where I can find my score ?

A: https://datatalks-club.slack.com/archives/C01FABYF2RG/p1738149619184809?thread_ts=1738148857.084409&amp;cid=C01FABYF2RG
   ---
   thank you @user
   ---
   it will show up after scoring

### [2025-01-29] Shyam Gupta (replies: 2)

Q: @user where is the leaderboard for 2025 cohort?

A: Hey, @user! Here you go:  I don't think I have an answer for this; you'll have to ask your fellows or instructors.
   ---
   https://courses.datatalks.club/de-zoomcamp-2025/leaderboard, but HW has not jet been scored. Alexey will hit his button within the next 22h

### [2025-01-30] U088H3X5S4C (replies: 3)

Q: I'm sorry, how can I rename my name in the leaderboard?

A: With "Edit" button :
   ---
   https://courses.datatalks.club/de-zoomcamp-2025/enrollment
   ---
   I created an issue (https://github.com/DataTalksClub/course-management-platform/issues/78) on course management platform repo to add a button to the overview page (https://courses.datatalks.club)

### [2025-01-30] Nick (replies: 2)

Q: @user where can I see scores from the course management system and leaderboard as well?

A: Hey, @user! Here you go:  Scores and leaderboards can be checked on the course management platform itself after the deadline for each homework is reached. You will find your points displayed at the top of the homework page, and the leaderboard will reflect the total points you have earned, which includes points from homeworks, FAQs, and Learning in Public contributions. For more details, refer to the course management platform as indicated in the bookmarks.
   ---
   Hey, @user! Here you go:  Scores and leaderboards can be checked on the course management platform. After submitting your homework, it will be graded, and you will see your score on the homework page itself. The leaderboard will display the sum of all points you've earned from homeworks, FAQs, and Learning in Public contributions. For more details, refer to the course management platform (see bookmarks) https://datatalks-club.slack.com/archives/C01FABYF2RG/p1738072515842509?thread_ts=1738072267.907829&amp;cid=C01FABYF2RG.

### [2025-02-08] Issa AlBawwab (replies: 4)

Q: Hello i finished the dbt fundementals course before starting with module 4 upon @user advice, and I want to share about it on linked in, is it possible to use that post to get learning in public points?

A: Yes, go for it
   ---
   but its not part of a homework so where do i add the link
   ---
   You can do it for module 4
   ---
   good point

---

## Project: dashboard / Looker / visualization tool (14 threads)

### [2025-01-18] Mohamed Hassan (replies: 2)

Q: I need to know .. as we will build the ETL process with great tools we will learn.
   
   what makes us use these tools instead of Power BI for the whole ETL process?
   
   
   Update: This is answer for that question
   
   https://www.reddit.com/r/BusinessIntelligence/comments/keklwj/power_bi_is_so_powerful_you_dont_even_need_an_etl/

A: 1. Scale
   2. Relability
   and more
   ---
   At my company, our BI Tool (Looker for us), is just one of many consumers of the modeled data in our data warehouse. Other consumers include:
   • ML Team for EDA, research, and model development
   • Analytics Team for SQL & python analytics that can't be handled easily in Looker)
   • Reverse ETL (pushing modeled data back into upstream data systems like Salesforce)
   • Internal APIs
   • Other business analytics tools (e.g. Amplitude)
   All of these consumers benefit from having modeled data that they can trust. As a data engineer, I would be vary of any proposed meta solution. For one, putting all of your eggs in one basket is a risky long term proposal. You're subject to vendor lock. One component of the solution may not turn out to scale the way your business needs, etc.

### [2025-03-30] Leonardo Rodriguez (replies: 2)

Q: @user I am not able to connect to looker studio for some reason. It says: `Could not connect to server. If the problem persists, try again in a few minutes.` . Is this a common error?

A: Hey, @user! Here you go:  This error message typically indicates a connectivity issue with Looker Studio, which can occur for various reasons. It is not uncommon for users to experience temporary connection problems, especially during peak usage times or due to network issues.  You can try a few steps to troubleshoot the issue:  1. **Check Your Internet Connection:** Ensure that your internet connection is stable and functioning correctly.  2. **Clear Your Browser Cache:** Sometimes, cached data can cause issues. Clearing your browser's cache and cookies may resolve the problem.  3. **Try a Different Browser or Incognito Mode:** Switching to a different browser or using incognito mode can help eliminate browser-related issues.  4. **Check Looker Studio Status:** Occasionally, Looker Studio may experience outages. You can check if there are any ongoing issues with the service.  5. **Retry After Some Time:** If the problem persists, waiting a few minutes and trying to connect again can often resolve temporary connectivity issues.  If these steps do not resolve the issue, you may need to consult with your peers or instructors for further assistance.
   ---
   @user Did you find the solution ...

### [2025-03-31] Blessing (replies: 1)

Q: @user and @everyone
   
   I need clarity on this part:
   • Cloud
       ◦ 0 points: Cloud is not used, things run only locally
       ◦ 2 points: The project is developed in the cloud
       ◦ 4 points: The project is developed in the cloud and IaC tools are used
   Does this mean we can not use docker to spin up Airflow and any visualization tool we want to use because docker is ran locally? I need to be clear on this please, anyone

A: Hey, @user! Here you go:  Using Docker to spin up Airflow or any visualization tool locally would not meet the criteria for cloud usage in the evaluation. According to the evaluation criteria, if the project runs only locally, it will receive 0 points. The project must be developed in the cloud to earn at least 2 points, and to achieve 4 points, it must be developed in the cloud with Infrastructure as Code (IaC) tools like Terraform.  If you intend to run these services on a local machine, they will not count towards the cloud component of the evaluation. It is essential to deploy your services in a cloud environment, such as GCP or AWS, to meet the project requirements.

### [2025-04-01] JENNIFER WANG (replies: 7)

Q: For the project evaluation, how should we evaluate if the link to the dashboards (e.g., Looker) isn’t public or is restricted? There were no outputs/screenshots of what the dashboards might look like within the README, just an external link to Looker. I have requested access to the Looker dashboard, but if the student does not reply/grant me access, how should I rate this? I can’t see the dashboards…:woman-shrugging::skin-tone-2:
    @user @user Thanks for any guidance!!! :pray::skin-tone-2:

A: Hey, @user! Here you go:  For project evaluation, if the link to the Looker dashboard is not public or is restricted, and there are no outputs or screenshots included in the README, it's essential to follow the guidelines for reproducibility. Ideally, projects should include detailed steps to recreate the dashboard and ideally provide screenshots to ensure that evaluators can assess the project without needing access to external links.  If you requested access to the Looker dashboard and the student does not respond or grant access, you should evaluate the project based on the documentation provided. According to Alex's clarification in the Slack thread, while it's ideal to re-run everything, reviewing the code for errors and missing instructions is also acceptable. If you cannot view the dashboard, it's reasonable to rate the project lower due to the lack of accessibility and documentation.  Additionally, it might be helpful for students to include as much information as possible in their README to avoid these situations, especially when they are aware that evaluators may not have access to external tools.
   ---
   Hey, @user! Here you go:  If the Looker dashboard is not publicly acces ...

### [2025-04-29] Pedro Coutinho (replies: 3)

Q: @user
   About peer evaluation.
   In some cases, there's no actual dashboard provided, just a screenshot.
   Would that still count for dashboard evaluation criteria?

A: Hey, @user! Here you go:  A screenshot of a dashboard can be considered for the dashboard evaluation criteria, as it provides a visual representation of the work. However, the effectiveness of the evaluation may be limited compared to having access to the actual dashboard. If the screenshot is clear and demonstrates the insights intended from the dashboard, it may still warrant some points.   On the other hand, if the evaluation criteria expect an interactive dashboard or if the documentation is insufficient, then points may be deducted. The key is to ensure that the documentation and visuals lead the evaluator to understand the insights provided by the dashboard. If the documentation is lacking, it might lead to lower scores, as participants should learn to document correctly.   In summary, a screenshot can count, but the overall quality and clarity of the documentation and visuals will determine the points awarded.
   ---
   Up to you but I'd still give some points. Since they took a screenshot, there must be the actual dashboard somewhere
   ---
   Thanks for the feedback, Alexey.
   I think 2 out of 4 points strikes a fair middle ground for those.
   
   
   I realize I might have a biased perspective ...

---

## Forking the repo / git workflow / pull updates (14 threads)

### [2025-01-19] Cory (replies: 1)

Q: I'm struggling to get Kestra working and connected to a database.  I just forked the data-engineering-zoomcamp to a new clean repo on my git hub and launched in a clean github codespace. After doing this I followed the instructions here https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/02-workflow-orchestration in the readme
   ```cd 02-workflow-orchestration/
   docker compose up -d```
   `Once the container starts, you can access the Kestra UI at http://localhost:8080.` -&gt;This works
   Then curl all of the flows to kestra
   `curl -X POST http://localhost:8080/api/v1/flows/import -F f ...

A: For context (and we're gonna update the README shortly), the flows are looking for a database using this configuration: https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/02-workflow-orchestration/postgres/docker-compose.yml
   
   ```version: "3.8"
   services:
     postgres:
       image: postgres
       container_name: postgres-db
       environment:
         POSTGRES_USER: kestra
         POSTGRES_PASSWORD: k3str4
         POSTGRES_DB: postgres-zoomcamp
       ports:
         - "5432:5432"
       volumes:
         - postgres-data:/var/lib/postgresql/data
   volumes:
     postgres-data:```
   You may need to update the Postgres DB name in kestra at the bottom where Plugin Defaults are defined as well as the user and password

### [2025-01-20] U06EF2U124U (replies: 4)

Q: Hi all, I just started but am excited! Do you all clone the repo to start like in this video?

A: Hello
   it's not necessary, but you can do it if you want
   ---
   What are other ways to follow along?
   ---
   you can make your own directory, and follow the steps one by one, I think this way is better cuz you'll learn how to write your own docker files, terraform...
   ---
   Please don't post screenshots or pictures of your code, they are very difficult to read.
   
   Instead, copy the code and put it in a code block.
   
   Follow these recommendations (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/asking-questions.md) to make it easier to help you.

### [2025-01-25] Sohan Madhana (replies: 1)

Q: @user Hi how do I start with the zoomcamp? Should I download the project and make a branch to do the homework and notes in that branch?

A: Hey, @user! Here you go:  To start with the Zoomcamp, you should begin by watching the videos in the course repository. Specifically, you can start with Module 1 and follow the videos in order, as they are structured to guide you through the material effectively. The relevant resources are available in the GitHub repository: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform.  Regarding the homework, it is recommended to check the homework section in the GitHub repository. You can create a branch in your local project to manage your homework and notes effectively. This approach allows you to keep your work organized and makes it easier to track changes.  Make sure to start with the introductory videos and progress through the modules sequentially to build a solid foundation for your assignments.

### [2025-01-27] Viktorija Alexeeva (replies: 1)

Q: @user , I am not sure that have organised my study correctly. I cloned datatalks git repo to local machine and did changes in that prepared files. But since I don’t push changes into datatalks main repo , I will loose all corrections after pull from repo to update files from week2. Should I recreate the same repo on my GitHub account?

A: Hey, @user! Here you go:  Creating your own repository on GitHub is a good approach to ensure that your changes and corrections are not lost when you pull updates from the main DataTalksClub repository. By forking the repository to your GitHub account, you can freely make changes, commit them, and push updates without worrying about losing your work when syncing with the original repository.  After forking the repository, clone your forked version to your local machine and make your changes there. This way, you will maintain your own version of the files while also being able to pull updates from the main repository when necessary.  To do this, follow these steps: 1. Go to the original repository on GitHub. 2. Click the "Fork" button to create a copy of the repository in your account. 3. Clone your forked repository using the HTTPS link: `git clone https://github.com/[your-github-username]/data-engineering-zoomcamp.git`. 4. Make your changes locally and commit them. 5. Push your changes to your forked repository: `git push origin main` (or the name of your branch).  This approach allows you to keep your modifications while still being able to update your local copy with changes fro ...

### [2025-02-01] Viktorija Alexeeva (replies: 4)

Q: @user, please advise, whether i do everything correctly. I have forked original repo. in order to load updates from original repo to forked repo, i need to use commands:
   ```$ git fetch upstream
   $ git merge upstream/main
   $ git push origin main```
   is it enough? or should i do smth more?

A: Hello from DE FAQ Bot! :robot_face: 
   Please note that I'm under active development. The answers might not be accurate since I'm just a human-friendly interface to the  DE Zoomcamp FAQ (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit#heading=h.o29af0z8xx88), this Slack channel, and this course's GitHub repo (https://github.com/DataTalksClub/data-engineering-zoomcamp).
   Thanks for your request, I'm on it!
   ---
   There was an error: list index out of range
   ---
   Hello from DE FAQ Bot! :robot_face: 
   Please note that I'm under active development. The answers might not be accurate since I'm just a human-friendly interface to the  DE Zoomcamp FAQ (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit#heading=h.o29af0z8xx88), this Slack channel, and this course's GitHub repo (https://github.com/DataTalksClub/data-engineering-zoomcamp).
   Thanks for your request, I'm on it!
   ---
   There was an error: list index out of range

---

## AI / LLM / ChatGPT for course / project (12 threads)

### [2025-03-04] Jubril (replies: 3)

Q: hello i am having trouble ingesting data into bigquery whereby setting location has been a problem with dlt. dlt only offers two options EU or the default US but my location is "europe_west1". the error i get when set to EU is - (404 POST https://bigquery.googleapis.com/bigquery/v2/projects/dbt-analytics-engr/queries?prettyPrint=false: Not found: Dataset dbt-analytics-engr:dbt_source_dataset was not found in location EU) and when i set it to europe_west1 the error I get is operation not permitted so i presume *dlt doesnt allow one to explicitly define the location apart from EU and US*. Any he ...

A: I just went ahead with US for my tasks. There shouldn't be much to worry about.
   ---
   the issue i got is that all my datasets are already in europe_west1
   ---
   Easiest way I would be to move them, re-upload them. I had trouble initially with different regions so I just went ahead with the US for my entire exercises. But wait on others to respond to this. I'm totally new to all this.

### [2025-04-02] Till Meineke (replies: 3)

Q: Did anyone try and succeed in `vibe-coding` the whole project?

A: Looks like this project (https://github.com/victorfxz/Mental-Well-being-Monitor) tried.
   ---
   I don’t think so.
   
   Although you can find
   &gt; add your images accordingly
   in the `README.md` , I guess the participant was just using an LLM to improve it. I don’t know, if `vibe-coding` would give you bilingual comments in your code (maybe instructed). The project is also missing the whole cloud part.
   
   I would really like to see some examples :i_see_what_you_did_there:
   
   I tried, but failed. Here are some of my VSCodeInsiders/GitHubCopilot/AgentMode/Claude 3.7 Sonnet instructions (keep in `.github/` of project) and custom prompts (keep in `.github/prompts` of project), but as I said they failed and need improvement.
   
   Have not tried the whole MCP (model context protocol) stuff, maybe this could also improve vibe coding.
   ---
   always funny to see what happens :unicorn_face:

### [2025-06-16] Jobert Gutierrez (replies: 8)

Q: Hi @user , I took the #course-data-engineering using Kestras as orchestrator. Now, I'm taking #course-mlops-zoomcamp and decided to stick with kestra to orchestrate my ML pipeline. I think I streamlined the pipeline with Postgres for local backend, Kestra and MLFLow using a docker-compose.yml file. However, I got an error to save a produced file (artifact) that I've not been able to solve even with usage of chatgpt. May you helpme to identify whats wrong?

A: My docker-compose file is:
   ```volumes:
     postgres-data:
     kestra-data:
     mlflow-data:         # Stores MLflow metadata and artifacts
     mlflow-db-data:      # Stores PostgreSQL data for MLflow backend
   
   services:
     postgres:
       image: postgres:16.6
       volumes:
         - postgres-data:/var/lib/postgresql/data
       environment:
         POSTGRES_DB: kestra
         POSTGRES_USER: kestra
         POSTGRES_PASSWORD: k3str4
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGRES_USER}"]
         interval: 30s
         timeout: 10s
         retries: 10
       networks: [default]
   
     kestra:
       image: kestra/kestra:latest
       user: "root"
       command: server standalone
       volumes:
         - kestra-data:/app/storage
         - /var/run/docker.sock:/var/run/docker.sock
         - /tmp/kestra-wd:/tmp/kestra-wd
         - /var/run/docker.sock:/var/run/docker.sock
       environment:
         KESTRA_CONFIGURATION: |
           datasources:
             postgres:
               url: jdbc:<postgresql://postgres:5432/kestra>
               driverClassName: org.postgresql.Driver
               username: kestra
               password: k3str4
           kestra:
             server:
               basicAuth:
                 enabled: f ...

### [2026-01-26] Călina Cenan (replies: 4)

Q: Hi everyone! I just learned about this course :smile: (from ChatGPT!!)
   I guess I’m a bit late for the cohort in progress now, but are there any plans for a next course? I also couldn’t find a schedule of the current course (how long is each module, when is the due date for homeworks?), in case I could eventually catch up :slightly_smiling_face:

A: this is the schedule of the current cohort; we just started about 2 weeks ago. I'm sure you can stilll catch up
   ---
   yeah  u can catch up it  just  module  1  completed and  module 2 started
   ---
   Hi Călina! That’s interesting!
   
   Please read the pinned messages for details on how the course works and all important links.
   
   In short, you can still join, we’ve just started Module 2 and you can easily catch up. One module typically lasts one week. We run this course once per year. So the next cohort will start in one year.
   ---
   oh then I will definitely try to catch up rather than wait for another year! :smile:

### [2026-01-27] U09FV721QLQ (replies: 21)

Q: Hi everyone!
   
   Did anyone try to to run "02_python.yaml" flow found in the repo in kestra? I was following along the youtube videos and trying to execute the flows that are shown in the video but in this one I keep getting this error:
   I saw that in youtube some people in the comments reported similar issues but I couldn't find any solution in kestra's slack channel. Did anyone managed to fix this? I've tried to use some other docker images with different python versions but always get a similar error. (ps: I also tried chatgpt but it just started hallucinating some kestra variables that didn't  ...

A: Can you share the execution logs?
   ---
   Yes, of course.
   ---
   Hmmm...I'm new to Kestra as well, so I'm shooting in the dark and using chatGPT - maybe you should switch the containerImage to python:3.12-slim and then add "pythonVersion": "3.12"?
   ---
   OR you could remove the containerImage property whatsoever, so it will default to python:3.13-slim
   ---
   from what I managed to look up right now is that the latest version of python is 3.14 (that's the version that python:slim image will try to use), so there's incompatibility between the image that you're pulling (python:slim) and the python version that kestra is trying to use (3.13 as default). At least that's my hypothesis, but I might be completely wrong.
   ---
   That's the exact python version in python:slim image
   ---
   so either change the image to python:3.13-slim or add pythonVersion: "3.14" in the flow and try if that helps
   ---
   Hi, I was having the same issue and fixed it somehow by
   1. changing to python:3.12-slim
   2. removing the dependencies property and add     beforeCommands: - pip install --no-cache-dir requests kestra
   Hope that helps.
   ---
   Hmm interesting. Sounds like it could be related to `uv` but unclear.
   
   Could you open an issue o ...

---

## Recommended IDE / Cursor / Antigravity (10 threads)

### [2025-01-21] Alejandro (replies: 7)

Q: is anyone here using pycharm as IDE?

A: vsc
   ---
   yep, me
   ---
   Good to know! :slightly_smiling_face: are you using any dependency manager like poetry?
   ---
   not really yet, I decided to go plain old way for week 1 to run everything from terminal, including venv creation, pip install, etc, since module is very primitive and doesn't require multiple dependencies. But I'm thinking of optimizing it further on
   ---
   ok, thanks for the response
   ---
   @user We had a quick conversation about `uv` here (follow 'till the end of the thread):
   https://datatalks-club.slack.com/archives/C01FABYF2RG/p1736961538787209?thread_ts=1736959762.691299&amp;cid=C01FABYF2RG
   ---
   thanks I will read it :slightly_smiling_face:

### [2025-02-04] Shivakumar Marulshetty (replies: 9)

Q: Hey guys! I'm trying to populate Postgresql table with parquet file of ny_taxi data using Python but When I run this `df_parquet.head(0).to_sql('yellow_taxi_data', con=connection, if_exists='replace')`
   I'm getting *AttributeError: 'Engine' object has no attribute 'cursor'*
   What do I do?
   Any suggestion with this would help me move forward with the course, Thanks!

A: 1. Did you install required library for postgres?
   2. Did you make the connection before executing this query?
   ---
   ```engine  = create_engine('<postgresql://root:root@localhost:5432/ny_taxi>')
   df_csv.head(0).to_sql('yellow_taxi_data', con=engine, if_exists='replace') ```
   ---
   Thanks Dinesh, and I have installed sqlalchemy and psycopg2
   ---
   Let's put this into separate cells and try to run it.
   Also hope the postgre container is up and running - able to accept connection
   ---
   Yeah the postgres is live and i ran those 2 line on 2 different cells, I browsed the internet but still couldn't figure out the problem.
   ---
   @user  
   I'm getting AttributeError: 'Engine' object has no attribute 'cursor'. Can you help?
   ---
   Hey, @user! Here you go:  The error "AttributeError: 'Engine' object has no attribute 'cursor'" indicates that you're trying to access a cursor directly from the SQLAlchemy engine object, which is not the correct approach. Instead, you should use a connection object to interact with the database.  Here's how you can resolve this issue:  1. **Use a Connection Object**: Instead of using the engine directly for data operations, create a connection object by calling `engine.connect()` o ...

### [2025-02-05] Mayank Gulati (replies: 4)

Q: And I have a generic question regarding Kestra @user
   Coming  from a python programming background, I found the syntax in Kestra (or maybe yaml) to be very tricky, I had to do a lot to experiments let's say in order to make python script work in kestra, and similar things.
   So, is it possible to use flow editor functionality within kestra in VSCode or similar where I don't need to worry about syntax and also take advantage of other functionality like autocomplete suggestions, etc?

A: We have a VSCode plugin that allows you to build workflows locally, but the Kestra Editor is built on top of VS Code so should feel quite similar. What issues have you found? Maybe I can share some resources to make it easier?
   ---
   primarily, how to build pipeline using kestra's flow editor in vscode locally?
   Is there some vscode extention to connect kestra with vscode?
   ---
   yes we have a vscode extension to allow you to write the YAML in VSCode with auto complete
   ---
   could you please explain in detail how this docker container of kestra hosted at port 8080 (for zoomcamp) be accessed through  local vscode to update the flows in kesta?

### [2026-02-18] Laurent (replies: 5)

Q: Hello everybody,
   
   I discovered and joined the Zoomcamp a few weeks ago, and first of all I’d like to say a big thank you to the creators and instructors for the dedication you’ve put into it. I was far from expecting this much from a free course.
   
   I’m slowly making my way through the modules and catching up with the current week on Bruin. To add to a remark that has already been mentioned several times — and to nitpick a little — it would have been nice to coordinate things upstream, in particular regarding the dataset (NY rides, green/yellow, years 2019, 2022–2023, 2025-01, etc.) between dev  ...

A: hey, this is co-founder of Bruin, thanks a lot for the feedback. Bruin has been running on production for the past 2.5 years across tens of companies, from large multi-national teams all the way to smaller teams, therefore we are confident on the core technology, although I admit that our public docs have quite a long way to go and we are doing our best to improve them.
   1. Bruin would connect to your existing database, would not override the database itself unless you have tables with the same exact names under the same exact schema. do you mind expanding a bit more about what you would like Bruin to do? 
   2. `bruin init` is supposed to just create a git repo if there's not one, and if there is it shouldn't mess with it at all. could you please expand on what folders do you mean?
   3. warning is "normal" as in it is not really a problem, but we should improve. we created an internal ticket.
   4. We can take a look at the naming, although many of our users use either one or the other, therefore a longer name would just take up more space. you can right click the names and hide some of the tabs you would not want to use.
   5. seems like a bug, created a ticket.
   really appreciate all the fee ...

### [2026-02-23] Zoltan Nyiri (replies: 17)

Q: 05-data-platforms (https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/05-data-platforms) Bruin: ideas for learning/digging deeper.
   
   • I recall airflow, kestra, dbt all had some way to visualize executions. What do we have in bruin?
   • During testing "bruin run" I saw my network spiked at every execution, so I defaulted to green taxi data, smaller than yellow. It would be nice to download once and reuse after.
   • The AI generated versions (MCP layered, and MCP with full prompt) both check for total_fare non_negative. We do have some negative rows due to refunds. How to run the p ...

A: • Bruin's VSCode (https://getbruin.com/docs/bruin/vscode-extension/overview.html#data-lineage) extension has a lineage view that can show you the execution order of assets in a pipeline. 
   • Bruin supports incremental loading via ingestr assets (https://getbruin.com/docs/ingestr/getting-started/incremental-loading.html). When properly configured, this will eliminate unnecessary reloading.
   ---
   • You can use the --only (https://getbruin.com/docs/bruin/commands/run.html#flags) flag to run just the asset without the checks (`--only main`). If you just want to run checks: `--only checks`
   ---
   With regards to your question about `time_interval` materialisation, I would need more information.
   
   Depending on your `incremental_key` and `granularity` there's a chance that only a subset of data is deleted. So your assumation about data doubling might be what's misleading you.
   ---
   for more information: https://getbruin.com/docs/bruin/assets/materialization.html#time-interval
   ---
   Let me know if you have any other questions regarding Bruin :slightly_smiling_face:
   ---
   Also, for AI agent, actually you don't need them. You can use everything on your own via cli or vscode extension.
   ---
   Agents are just ...

---

## Codespaces budget / out of free usage (9 threads)

### [2025-01-09] Marios Moumouris (replies: 4)

Q: Hey guys, another quick question: I am aiming to use the GitHub Codespaces and not my personal computer. Should I start the course with "DE Zoomcamp 1.4.2 - Using Github Codespaces for the Course" video - or do I follow the normal sequence of the course material? Also, is there any any resource or video on how we set-up the free account in GCP? Thank you very much!

A: Codespaces is kind of an aside IMO. I would follow the normal sequence. Setting up the free account should be in the playlist. If not, if you just give it a Google you'll see it's pretty straight forward.
   ---
   Yes but if don't plan to run the tools locally, doesn't that mean that I have set up the environment somewhere first so I can follow what is being done at the course?
   ---
   hi, i’m trying to start the same way as you, with GitHub Codespaces. What worked for you? in what order did you watch the videos?
   ---
   I just watched the github Codespaces video first in order to configure it and now I will continue with the rest of the videos. I am also planning to try to configure everything locally, or at least get the idea of it.

### [2025-02-23] Abdiel Josue Sandio Noubissi (replies: 1)

Q: @user how can i solve this issue? Low disk space available (&lt;5%). Please free some space to ensure your codespace continues to work correctly.

A: Hey, @user! Here you go:  To resolve the issue of low disk space in your GitHub Codespace, consider the following steps:  1. **Delete Unused Files**: Check for and remove any unnecessary files or directories that you no longer need in your Codespace. This could include old project files, temporary files, or large datasets that are not required for your current work.  2. **Clean Up Docker Images**: If you've been using Docker extensively, you might have accumulated a lot of unused Docker images. Run the following command to remove dangling images:    ```bash    docker image prune    ```    Additionally, you can remove all unused images (not just dangling ones) with:    ```bash    docker image prune -a    ```  3. **Check for Large Files**: You can use the `du` command to identify large files and directories:    ```bash    du -h --max-depth=1    ```    This will give you a summary of disk usage for the top-level directories. You can then navigate into the larger directories and repeat the command to find specific files to delete.  4. **Limit Logging**: If you have applications running that generate logs, ensure that logging is not excessively verbose or that logs are being rotated and ...

### [2025-07-27] Hung Linda (replies: 1)

Q: @user I use codespace and keep receiving this warning - Low disk space available (&lt;5%). Please free some space to ensure your codespace continues to work correctly. What should I do?

A: Hey, @user! Here you go:  To resolve the low disk space warning in your GitHub Codespace, you can take the following steps:  1. **Check Disk Usage**: Use the command `$ sudo du -sh *` to see what files or directories are taking up the most space. This will help you identify large files that you may not need.  2. **Remove Unnecessary Files**:     - Delete any large installers or files that are no longer needed. For instance, if you have an Anaconda installer and you have already installed Anaconda, you can remove it using:      ```bash      rm -rf &lt;anacondainstaller_fpath&gt;      ```    - Clean up Anaconda itself to free up space:      ```bash      conda clean --all -y      ```  3. **Purge Unused Data**: If you're using Kestra or any other data management tool, consider purging any unnecessary data or logs. For Kestra, you can refer to the purge flow documentation to remove old executions or data that you no longer need.  4. **Delete Unused Docker Images**: If you've been working with Docker, you might have accumulated unused images. You can remove them using:    ```bash    docker system prune -a    ```  5. **Manual Cleanup**: If you have specific files or directories that you c ...

### [2026-01-23] Patrick Herve (replies: 3)

Q: Hello everyone,
    Somehow, every time I ran the ingestion command to add data, I was being charged on GitHub for using the codespaces. At some point, I received a prompt saying that I had reached my monthly limit and needed to add credit. Instead of adding credit, I decided to set everything up on my local machine (pgAdmin, Docker).
   Will working on my local machine instead of the codespaces affect my progress?

A: in my opinion, it's even better. better to have a local and free storage for personal usage.
   
   The transfert of workspace is complicated and all your git branch go with that (git is local).
   
   Here is my setup :
   VS Code + remote (local) WSL/win 10 pro
   ---
   You get 60 hours of free runtime and 15gb of storage per month for free. You can check if you reached that limit on your GitHub settings under billing. https://github.blog/changelog/2022-11-09-codespaces-for-free-and-pro-accounts/ (https://github.blog/changelog/2022-11-09-codespaces-for-free-and-pro-accounts/)
   ---
   A friend helped me move my setup to my local machine after he told me it's not good practice to save key files in Codespaces. We had a little difficulty at first with getting git setup to work after the move, but after we resolved that it has been totally fine to work locally.

### [2026-01-25] Lynn zhang (replies: 1)

Q: Hi, I can not access the codes/homework in codespaces now, this is the error: You are out of monthly free usage or have exceeded your budget for Codespaces. Increase your budget to continue using Codespaces.  Have I lost all the codes?  What can I do? Thanks in advance

A: I just increased to pro, so the code is back.

---

## Project: API key / private credentials / reproducibility (9 threads)

### [2025-03-30] Peter Stan (replies: 3)

Q: Hi all, have a question about project reproducibility, criteria look like this
   &gt; • Reproducibility
   &gt;     ◦ 0 points: No instructions how to run the code at all
   &gt;     ◦ 2 points: Some instructions are there, but they are not complete
   &gt;     ◦ 4 points: Instructions are clear, it's easy to run the code, and the code works
   assuming I use GCP, terraform, airflow, spark, DBT, there are different ways to use it, but at the end there is always the GCP - should the instruction assume user will provide the GCP keys to run the airflow pipeline?

A: Yes. Provide instructions to reproduce, but it is on the evaluator to generate any necessary service accounts, API keys etc.
   ---
   how does it work, if your project is on aws and the evaluators don’t want to or can’t create an account? I know I can (and should) document everything for reproducibility.
   ---
   That's the route I would take. Document it VERY well. Or better yet, make a video walkthrough if that's an option. At the end of the day remember the evaluator is going to be someone just like you on the other side. Try to make their life/evaluating as easy as possible.

### [2026-01-29] Filipe Fiedler (replies: 6)

Q: Hi everyone. Is there a way to run the ingestion/backfill part of a Kestra pipeline fully via code (CLI/API), without relying on manual steps in the UI?
   My goal is reproducibility: someone should be able to clone the repo + run a command (or CI job) that triggers the backfill for a given date range.
   I tried using the Kestra API to trigger backfills but couldn’t get it working. Is this supported in the open-source edition, or only in the paid offering?
   If Kestra can’t do this, is Airflow a better fit for “code-only” backfills and reproducible ingestion?

A: been wondering the same thing and I havent found any. Maybe I should tag @user
   ---
   You can trigger backfills with the API: https://kestra.io/docs/concepts/backfill#trigger-backfill-via-an-api-call (https://kestra.io/docs/concepts/backfill#trigger-backfill-via-an-api-call)
   ---
   Thanks, Brian and Will. I tried following the example in the docs, but it didn’t work for me. After some digging, I realized the curl endpoint differs in the open-source version: it should be `/api/v1/main/triggers` (not `/api/v1/main/release/triggers`, which seems to be for the Enterprise/Release feature)
   ---
   ah okay, will investigate
   ---
   Should be fixed
   ---
   Thanks, Will! I really appreciate it!

### [2026-02-10] Vadim Sokoltsov (replies: 10)

Q: Hello everyone! :wave:
   
   Have a couple of questions again about the capstone project's structure :sweat_smile:
   1. Let us say, each component of the pipeline (processing, ingestion, ...) is located in separate folder
       ◦ What about containerization of each step? Should this mini-app representing particular step contain distinct Dockerfile?
       ◦ What about tests? Should they be located withi this folder?
   2. Streaming task:
       ◦  I am filling the data lake in real-time (via Flink, Spark, ...) 
       ◦ Moving data from data lake to data warehouse - how can it be done?
           ▪︎ For example, `eve ...

A: How would you do this in a software engineering project?
   ---
   2. Yes, but every 10 minutes is more like a batch job, you don't need Kafka or flink for that
   ---
   Okay, I got you. So you mean that there is a process that generates data, then you ingest it and put it into a data lake. Now that it's in the data lake, you want to process it every 10 minutes, right?
   
   For that, you can use Kestra, DLT, or whatever you want. You just need a scheduler that runs every 10 minutes and launches your processing logic. DLT could be a good framework for processing, but you can also implement everything in Python.
   ---
   So for dbt, you can use it for data transformation from when it's already in the data lake to your data warehouse. You can use dbt, but you can also use any other transformation tool.
   ---
   Reproducibility means that it should be possible for someone to reproduce your setup. 
   
   Let's say you finish the project and give it to me, but I don't have access to you to ask questions. Given the README, is it enough? Does it have enough information for me to fully reproduce it? The project can be in the cloud or it can be local, but it has to be self-contained. It must have all the information I ne ...

### [2026-03-23] Nicholas (replies: 1)

Q: I'm going to use an API for my data, which ofc involves an API key (private).
   
   How can I work with this considering there is some points on "reproducibility"? No API key = no reproducibility, atleast for the extraction part.
   
   My guess is I'll aim for the 2 points in "2 points: Some instructions are there, but they are not complete" and thats it.
   
   Another alternative is to use examples of the response from the API and save it in github as a json file. (similar to what was done in the taxi module)

A: yes, no API = no reproducibility. but you can still pass the project

### [2026-03-27] Wali Mohamed (replies: 1)

Q: to get the marks for reproducibility what should it be able to reproduce. is it just gcp resources or extracting , ingesting and transforming and putting into warehouse?
   @user

A: Hey, @user! Here you go:  To receive marks for reproducibility in your final project, it is essential to reproduce the entire data pipeline process, which includes extracting, ingesting, transforming, and loading data into the warehouse. While having GCP resources set up is important, your project must also demonstrate the complete workflow from data extraction to data loading into BigQuery.   It's advisable to provide thorough documentation on how to configure your project to ensure that peer reviewers can accurately assess your work, even if they encounter challenges in setting up the necessary GCP components. This documentation could include instructions on obtaining credentials, creating GCP resources such as the project ID, dataset, and GCS bucket, and any specific configurations required to run the project effectively.  In cases where API keys are involved, consider providing example responses from the API and saving them in your GitHub repository as JSON files, similar to the taxi module approach. This method enhances reproducibility while maintaining the integrity of your project.   For additional details on GCP infrastructure relevant to your project, refer to the document ...

---

## Tool substitutions (Podman, alternatives) (8 threads)

### [2025-01-03] Helmi Aziz (replies: 4)

Q: Hello. Can I use Podman instead of Docker for this course? The dialect and mechanism should be similar to Docker and hopefully lighter too for my machine.

A: I don't see that as an issue. Two things to keep in mind though:
   1. You will need to use Docker for the homework. The homework's do not count towards getting the certificate though. 
   2. You probably shouldn't expect too much support/assistance in the Channel if you run into Podman issues.
   ---
   If I could verify that my homework also works for users with Docker (perhaps writing some guides on how to run it with Docker, if needed), would my answers still count?
   ---
   Grading is automated...mostly I believe. You can look at the previous year's homeworks to get an idea of where you might have issue.
   ---
   Most of the questions in homework 1 are about SQL, so it should be okay

### [2025-01-22] GUANYI LU (replies: 17)

Q: Hi All, the second module set up is really confusing, I have watched the FAQ video but it didn't solve my problem. I have 2 yml files, The first one is docker-compose.yml, this is exactly the same as in the module 2 :    volumes:
   ```  postgres-data:
       driver: local
     kestra-data:
       driver: local
   
   services:
     postgres:
       image: postgres:latest
       volumes:
         - postgres-data:/var/lib/postgresql/data
       environment:
         POSTGRES_DB: kestra
         POSTGRES_USER: kestra
         POSTGRES_PASSWORD: k3str4
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -d $${POSTGRES_DB} -U $${POSTGR ...

A: please move the error messages to the thread and shorten them if possible
   
   ```postgres-1  | 2025-01-22 23:11:41.469 UTC [50] FATAL:  database "kestra" does not exist```
   ---
   postgres-1  | 2025-01-22 23:11:17.604 UTC [42] FATAL:  database "kestra" does not exist,
   ```kestra-1    | Exception in thread "main" io.micronaut.context.exceptions.BeanInstantiationException: Bean definition [javax.sql.DataSource] could not be loaded: Error instantiating bean of type  [javax.sql.DataSource]
   kestra-1    |
   kestra-1    | Message: Failed to initialize pool: FATAL: database "kestra" does not exist
   kestra-1    | Path Taken: DatasourceFactory.dataSource(DatasourceConfiguration datasourceConfiguration)
   kestra-1    |   at io.micronaut.context.DefaultBeanContext.initializeContext(DefaultBeanContext.java:2000)
   kestra-1    |   at io.micronaut.context.DefaultApplicationContext.initializeContext(DefaultApplicationContext.java:314)
   kestra-1    |   at io.micronaut.context.DefaultBeanContext.configureAndStartContext(DefaultBeanContext.java:3318)
   kestra-1    |   at io.micronaut.context.DefaultBeanContext.start(DefaultBeanContext.java:345)
   kestra-1    |   at io.micronaut.context.DefaultApplicationContext.start(De ...

### [2025-02-03] Husain Ridwan (replies: 1)

Q: Can I use AWS for the course instead of GCP? I've been having issues completing my sign up for GCP

A: #de-course-aws, but no official support guaranteed

### [2025-03-03] Aruna (replies: 2)

Q: Hi Team, I have signed up for the data engineering course today. In the Data Engineering Doc (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?tab=t.0#heading=h.6aqyv6s6tphz) it is mentioned to use a Google Cloud Account, Can I use AWS account instead? Please let me know if this is not the right channel to post such questions.

A: #de-course-aws not officially suported
   ---
   Thanks @user

### [2025-03-13] Juwon (replies: 1)

Q: Can I use my own dataset during my project instead of the listed ones? I'm building a blockchain-based pipeline and want to source my data from an API like Chainlink.

A: Of course

---

## Prerequisites / can I take the course (7 threads)

### [2025-01-02] Alwi Ramadhan (replies: 5)

Q: Halo Everyone, I just wondered do we have to know about SQL and Python to follow this course? or is this course will be beginner friendly (from scratch) ?

A: I am not sure why somebody added the "YES" to your message.
   
   Just take a look at the first homework https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2024/01-docker-terraform/homework.md and the videos of the course: https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb
   
   Both SQL and Python are required.
   ---
   Yes probably is to the first part - about knowing SQL and Python before starting the course
   ---
   This is a beginner's course, but you will make your life easier if you have at least a basic knowledge of the following tools:
   • SQL
   • Python
   • Git
   • Docker
   • Linux command line
   ---
   Your prerequisites list is good. Here are my recommendations:
   For Docker &amp; PostgreSQL hands-on practice:
   • Complete Docker's tutorial (2 hours) from previus data camps 
   • Build and run a basic PostgreSQL container
   • Practice basic CRUD operations in PostgreSQL
   Regarding environments:
   1. Ubuntu VM is recommended for Docker due to Windows compatibility issues
   2. GitHub Codespaces alternative:
       ◦ Good for quick starts
       ◦ Monitor free tier usage (60 hours/month)
   Smart preparation:
   1. Create dedicated Gmail for GCP free tier ($200 credit)
   2. Only activate ...

### [2025-01-13] mustafa bozkaya (replies: 1)

Q: @user hi.  The content for the installation and prerequisite  part of module the 2025 group is not in this one. Where can we find it? https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2025/01-docker-terraform (https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/cohorts/2025/01-docker-terraform) is not here

A: I *think* that folder is just for the cohort to view homework information. Everything we need for module 1 is here: https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform. I'm just starting today so if this is incorrect, apologies :slightly_smiling_face: .

### [2025-01-14] Yinglu Deng (replies: 2)

Q: Hi I’m new to here class. Just watched the live session recording, and where should I begin before hw1? Should I start watching the FAQ documentation? cuz I don’t see much prerequisite materials for first hw. Thanks

A: This material from last year should be relevant https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform
   ---
   thanks

### [2025-11-23] Sarvesh Nand (replies: 3)

Q: Hello everyone, i wanted to ask that
   How can i practice for python for Data engineering specifically?
   and how much sql do i have to know? some say to know everything and some say that you don't have to become a database administrator

A: Python: if, loops, functions, collections (list, set, dict)
   SQL: joins, group by
   ---
   so i don't have to know python in very depth like here i was struggling with leetcode
   ---
   You will not need to invert binary trees in this course

### [2026-01-05] Eniola Oyebode (replies: 2)

Q: I am a beginner, is the course beginner-friendly?

A: Depends on what you mean by beginner. You need to be able to program and use terminal
   ---
   Alright
   
   Thank you so much

---

## Cloud cost / how much will GCP cost / minimize expenses (6 threads)

### [2025-01-01] FabianB (replies: 4)

Q: does anyone have great content on how to minimize expenses on the cloud? (gcp or aws)

A: Minimize expenses of what exactly?
   ---
   pretty much everything, how to choose the appropriate instance size, how to decide if you need data storage, plus the additional details that i dont know
   ---
   That is a thing that is very specific to each task and will come with experience. You are in the right place though! Once you get started maybe look into AWS and GCP Certs. Having that knowledge will help guide you. Other than that, I'd say Google/ChatGPT what you are looking at and brain storm on reducing costs like that.
   ---
   this much i know, which is why i ask for specific content, but i guess this is the way forward

### [2025-01-13] Madalena Neves (replies: 2)

Q: Hi everyone,
   Do we need to pay for GCP for this course?

A: No. They give $300 of free credits for a new account
   ---
   Thank you!

### [2025-02-01] Cairo Cananea (replies: 2)

Q: Hey guys, after complete the week 2, did you delete the data from GCS? To prevent extra costs? Or this data will be used on other modules ahead?

A: Storage is extremely cheap:
   
   Say you've uploaded 25 GiB of Data to the most expensive region: `southamerica-west`
   
   I would cost you: $0.030  per GB
   = 25 * $0.030
   = $0.75 per month
   
   https://cloud.google.com/storage/pricing#north-america
   
   if you've completed the Terraform in module 1, you should've set an Auto deletion policy after 30 or 60, so you'll be fine .
   ---
   great! tks for answer!!!

### [2025-02-07] MOHAMMAD NAKIBUL EZAZ (replies: 4)

Q: Hi guys. Can you tell me how much do I need to spend on cloud to finish this course? I'm a beginner and I'm afraid of accidental cost in the cloud. Also, I've been affected by lay off recently and I would like to finish this course with no to minimum cost.
   
   Can you guys guide me how can I do that?
   @user

A: Hey, @user! Here you go:  You can minimize or eliminate your cloud costs while completing the course by taking advantage of free trials and running most of the course materials locally.   1. **Free Trials**: Many cloud providers offer free trial credits. If you utilize these credits, you can complete various tasks without incurring costs.   2. **Local Alternatives**: The course can be mostly completed without using cloud services. Almost everything covered in the course (except for BigQuery) can be run locally. This means you can set up your environment on your own machine and avoid cloud expenses altogether.   3. **Cloud Storage Costs**: If you do choose to use cloud storage, it's relatively inexpensive. For example, storing 25 GiB of data in a high-cost region would only amount to about $0.75 per month. If you have set an auto-deletion policy using Terraform, as suggested in module 1, you can avoid ongoing storage fees.  By leveraging these strategies, you should be able to complete the course with minimal to no costs.
   ---
   If you're using the $300 GCP free trial, I think the course will likely cost between $20 and $50.
   ---
   You have a free budget of $300. That's totally sufficient ...

### [2025-02-20] U0865NE4L4T (replies: 9)

Q: Need help with a doubt -
   &gt; *Wouldn't ETL be on a lower cost side compared to ELT?*
   As opposed to dumping it in DW first and then transforming, would't it be much cost efficient to transform data before actually saving in DB tables? I am little confused.

A: What does an Analytics Engineer do? Could it be possible there are multiple teams in an organization that may wish to use the data, parts of the data, or the data transformed in a specific way???
   ---
   One idea of ELT is to use the power of a cloud warehouse to process your data faster.
   
   It depends on where your T is done.  If you transform on a prepaid on-prem engine, and account for all the maintenance costs, it may be cheaper.
   
   One big thing I've seen with ELT, is you have to manage your compute usage, and turn it off when not needed
   ---
   It's a good question. As mentioned above, there area a lot of things to consider, mainly dependent on the type of data you're dealing with, and that's why it's not uncommon to find some kind of ETLT out in the wild.
   
   But in general, when it comes to data for analytical purpose, historically ETL was used because data storage and transformation was very expensive. The more compute you needed, you had to buy an entire new server that was costly and time consuming process, in addition to maintenance. (Still the case today, or worse as hardware demand has gone down and therefore so has availability). Therefore, you needed to transform before it hit you ...

---

## Telegram / Slack channel access (6 threads)

### [2025-03-08] David G (replies: 1)

Q: Has week 6 began yet? I only ask as I haven't seen a notification in the telegram channel

A: it is available now, so you can start it

### [2026-01-08] Breeca Shi (replies: 1)

Q: Hi everyone, I am new here ready for the coming DE zoomcamp cohort. Is the telegram group mandatory? Will the course announcement only be available there?

A: As per email received from Datatalks club, telegram group is not mandatory and they will repost all the announcements from the channel to Slack.

### [2026-01-12] Tate (replies: 1)

Q: @user  is there a data engineering telegram channel?

A: Hey, @user! Here you go:  Yes, there is a Telegram channel for course announcements. You can join it at this link: [course Telegram channel with announcements](https://t.me/dezoomcamp).

### [2026-01-15] Hamza Ayaz (replies: 1)

Q: Hello All , is there a WhatsApp or telegram group for this cohort where we can discuss the problems if we are stuck somewhere ? or we can make one if there isn’t. Thank you

A: This slack channel is the best place for that

### [2025-12-30] Goldian023 (replies: 0)

Q: :wave: Hello, team! I'm looking for a study buddy, primarily just to remind each other, to help each other, and talk about the course materials (preferably has telegram cuz i dont have one -.- in case there is announcements there , but its fine if you dont). Is anyone interested? (my timezone is  UTC +8)

---

## Project: small dataset OK / dataset choice (6 threads)

### [2025-03-10] Viktorija Alexeeva (replies: 17)

Q: hi, my dataset for project is in kaggle. did anybody managed to download files from kaggle using kestra? wanted to automate this process, but can't find solution. right now only can download and unzip manually using bash.

A: If you can do it in bash you should be able to do it in Kestra. Did you search the Blue Prints? https://kestra.io/blueprints/s3-parallel-uploads Could also ask in the Kestra Slack. They are usually super helpful.
   ---
   Michael is right, you can use the Shell Commands task to automate anything you’re already doing with bash.
   
   You can also use our http.Download task followed with an ArchiveDecompress to get what you’re after
   ---
   Hi, using command in bash 'kaggle datasets download -d thedevastator/airbnb-prices-in-european-cities' i got zip file in my folder. so I was trying to create flow to download, unzip and upload csv files into gcs. but got error on the first step download_kaggle_dataset: Failed http request with response code '404' and body. i guess that i need to use http.request instead of http.download, but i don't understand which example suits me. my flow for now:
   ```id: upload_kaggle_to_gcs
   namespace: de-project
   
   tasks:
     - id: download_kaggle_dataset
       type: io.kestra.plugin.core.http.Download
       uri: https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities.zip
   
     - id: unzip_dataset
       type: io.kestra.plugin.compress.ArchiveDecompress
       algorit ...

### [2025-03-15] Leonardo Rodriguez (replies: 1)

Q: @user For the project, is the volume of the data something that is considered? as in, should we be looking for larger datasets?

A: Hey, @user! Here you go:  Yes, the volume of the data is considered for the final project. While there is no strict requirement to work with gigabytes of data, it is recommended to aim for a dataset that is "Big"-ish. Datasets that are too small, such as 250kB, may not be sufficient for meaningful transformations and analysis. A dataset with roughly 100k rows is acceptable, as long as it is reasonable in size. You can refer to a list of datasets available for your project here: list of datasets (https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_7_project/datasets.md).

### [2025-04-21] Kate Chen (replies: 3)

Q: What about a project related to NYC Yellow Taxi data?

A: Bumping this, have same question. Project is similar to what we have done during learning time. If a project is given to review then we can consider some anti-plagiarism pre-checks were done and we are supposed to rate it?
   ---
   Consider no anti-plagiarism pre-checks are done, and that is your evaluation work.
   
   If the project is just the stuff we did in course rate it with 0 points. 
   
   Check also https://datatalksclub-projects.streamlit.app (https://datatalksclub-projects.streamlit.app) for plagiarism (not mandatory)
   ---
   Using the NYC taxi dataset in the project is not allowed

### [2026-03-17] Jovanka Rakic (replies: 2)

Q: Hello everyone,
   Is there a minimum dataset size requirement for the final project, or is dataset size not a major factor?

A: same question here
   ---
   no such requirement

### [2026-04-01] Misha Davies (replies: 12)

Q: For project review: How should I review someone’s project if they used the taxi scripts from the training itself? For example, I just confirmed their scripts for dbt marts are the scripts provided in the training. Other scripts have slight differences but are otherwise very similar to what was produced during the training. They appear to be mainly focusing on a different year of the taxi data than what was analyzed in the training videos and homeworks. Is this acceptable? @user

A: Hey, @user! Here you go:  Using the taxi scripts from the training for a project is not acceptable, as the NY_Taxi data cannot be used for the project. The course explicitly states that it is not okay to utilize NY_Taxi data, which implies that using the scripts associated with that data is also not permissible.  If the project scripts closely resemble those provided in the training, especially if they are based on the NY_Taxi data, they would not meet the project's requirements. It's important to ensure that the work submitted is original and adheres to the course guidelines. Therefore, review should focus on whether the scripts and data used are compliant with the project requirements, which exclude the NY_Taxi data and its related scripts.
   ---
   @user How should I rate and indicate this on the review form?
   ---
   Hey, @user! Here you go:  Peer review is not currently open, as it will be available after the project submission deadline. Once the peer review period begins, you will be able to rate and indicate your feedback on the review form for the projects you are evaluating. Until then, you won't be able to submit any reviews. Make sure to check the course updates for the exact time ...

---

## Next zoomcamp / when does ML/MLOps/LLM start (6 threads)

### [2025-04-09] L (replies: 2)

Q: Question: For our GCP account. If I don’t wish to use it anymore after the course, do I need to do anything? I assume it will not charge me after the free trail ended?

A: I think, they most likely will if you have used BQ/GCS or keep storage from VM
   ---
   Correct. Just make sure to delete any VMs, Buckets, Datasets etc. and also shut down all projects just to be safe.

### [2025-05-09] Syed Zain Ali (replies: 1)

Q: When next zoomcamp will start and we can join?

A: January

### [2025-11-07] Νικος Αθανασουλας (replies: 6)

Q: Hello team! Could anyone share a roadmap for the entire field of Data, ML, and AI? I’m currently attending the ML Zoomcamp (about 60% done) and have started the Data Engineering Zoomcamp (around 10% completed) — both are great so far! What should come next — MLOps-&gt; LLMs, or something else? Are there any good theoretical courses from universities like Stanford or Harvard? Also, could you recommend some books? I’d like to get a complete overview of the whole field.

A: Our courses should give you a good overview. But each of these areas is huge, it'd be hard to suggest anything meaningful. Maybe finish the courses first and then see which thing you liked the most - and then go deeper
   ---
   @user, I want to start the data engineering course following the YouTube video. Can I use LocalStack to simulate AWS since GCP is monetized, and I can't afford it. Is localstack possible?
   ---
   Please use threads to keep the discussion more organized: https://datatalks.club/slack/guidelines.html#taking-part-in-discussions
   ---
   You can try
   ---
   You can also do everything locally without gcp or localstack
   ---
   You'll just have to skip the Terraform par t

### [2026-02-20] Alysia Liao (replies: 2)

Q: Hi Team! I know we are getting cloed to being done with this zoomcamp and it has been a very informative and helpful journey for me. I can't speak for others, but for myself, I have deepen a lot of my understand about data infrustucutre. Very grateful for @user and all the instructors in various different course. Naturally, I am thinking about what's next after finishing the data engineering zoomcamp. I transformed into a data engineer myseflt couple months ago from being a data analyst for 3 years. I feel like my foundation as a data engineer still pretty weak especially my knowledge of pytho ...

A: I know AI can do a lot these days but overly reply on AI never sit right with me. AI meant to be a tool, not a cheat code or even cheat yourself into believeing that you are a data engineer without knowing the basics or master basic programming laugauage such as sql, python and so on. This is just my option.
   ---
   I think practice is the only way

### [2026-04-19] ryano (replies: 1)

Q: hello @user,
   what is the next course close to Data engineering?

A: Hey, @user! Here you go:  The next course close to Data Engineering is "Big Data Platforms, Autumn 2022: Introduction to Big Data Processing Frameworks" offered by the University of Helsinki. This course is free and can be accessed through the following link: https://big-data-platforms-22.mooc.fi/. Additionally, you can explore the "Awesome Data Engineering Learning Path" at https://awesomedataengineering.com/ for more resources related to data engineering.

---

## FAQ document / contributing to FAQ (5 threads)

### [2025-01-22] Till Meineke (replies: 8)

Q: :alert: please be careful with our FAQ (https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?tab=t.0#heading=h.pvlsdfiupcjk)
   
   I just had to restore this from beginning of January, not sure what else is broken
   
   
   > Course - how many Zoomcamps in a year?
   > There are multiple Zoomcamps in a year, as of 2025. More info at DTC Article (https://datatalks.club/blog/guide-to-free-online-courses-at-datatalks-club.html).
   > However, they are five separate courses, estimated to be during these months:
   > 1. Data-Engineering (Jan - Apr)
   > 2. MLOps (May - Aug)
   > 3. Machine Lear ...

A: @user timestamp 22 January, 04:51 of FAQ seems ok, but 22 January, 06:26 is already broken with changed text sizing
   ---
   Thank you!
   ---
   btw, thanks for releasing the 90 days limit here in slack
   ---
   I wish I had anything to do with it, but it's just slack randomly giving pro trial every now and then
   ---
   somebody broke the FAQ again, now the ZoomQABot stopped working
   &gt; There was an error: list index out of range
   ---
   Oh no =( did you revert it?
   ---
   no I asked Alex Litvinov
   ---
   people keep misusing the FAQ
   
   now there is a block of 100 empty lines

### [2025-02-05] texnh (replies: 1)

Q: @user any guidelines to contribute to FAQ google doc?

A: Hey, @user! Here you go:  To contribute to the FAQ Google Doc, follow these guidelines:  1. When adding a new FAQ entry, ensure the question is formatted as “Heading 2”. 2. Feel free to improve existing entries if you notice anything that is off, but do not change the overall formatting of the document. 3. Avoid making any visual improvements; if you need to do that, make a copy for your own reference first. 4. The document should remain in a “pageless” format. 5. Include your name and the date for reference when applicable.  When submitting your contributions on the homework submission page, you should include links to either the FAQ entry you added or a link to a Slack question you answered. It's advised to paste the proper URL to the FAQ rather than the question itself.   This process helps maintain the quality and organization of the FAQ document while allowing for contributions from all participants.

### [2025-02-20] Dehao Zhang (replies: 4)

Q: Does anyone else face issues with the FAQ document? When I opened it, it appeared everything was crossed off for some reason (suggesting mode). I don't want to tag the instructors, but is there a way to notify the course instruction team about this?

A: You just did! Thanks, I'll take a look
   ---
   rolled it back to the previous ok state and edited it a bit
   ---
   thanks for letting us know!
   ---
   Thank you!

### [2026-02-06] Brian (replies: 1)

Q: @user where is the faq for de zoomcamp? how can I contribute to faq?

A: Hey, @user! Here you go:  The FAQ for the Data Engineering ZoomCamp can be found at this link: https://datatalks.club/faq/data-engineering-zoomcamp.html.  To contribute to the FAQ, you can follow these steps: - Create a pull request (PR) if you can improve the text or structure of the repository. - If you find that you received help with a problem that is not already in the FAQ, you can add that information to help other students.   Additionally, you can also contribute by starring the repository and sharing it with friends if you find it useful.

### [2026-05-02] Ibrahim Zaki (replies: 6)

Q: Hi @user,
   I hope you're doing well.
   I’m writing to ask for some clarification regarding the *Project Last Attempt*. In my second attempt, I received a score of *22*, which unfortunately wasn't enough to pass. I realized afterward that I missed out on additional points because I didn't participate in peer reviews or FAQ contributions—I mistakenly focused only on the project code itself, waiting to share everything once I had the certificate.
   I was very happy to see the "Last Attempt" opportunity opened. I am currently working on the improvements you suggested and aiming to implement as much as  ...

A: doing peer review in a mandatory step
   ---
   please don't tag me
   ---
   How can I start doing it now?
   Also, is there any other step that can affect my score or help me getting the certificate rather than the project and peer reviewing.
   ---
   No, the attempt is over now. I'll fix the bug so it won't show you what you see
   ---
   *Thank you for the clarification. Just one last quick question to make sure I have everything covered:*
   *Since the "Learn in Public" (LiP) and "Peer Review LiP" links aren't visible in the current form for this attempt, where should I submit them once I share my work?*
   *Thanks again for your time.*
   ---
   After the project submission deadline

---

## Project: architecture diagram / pipeline diagram tool (3 threads)

### [2025-03-31] Viktorija Alexeeva (replies: 4)

Q: Hi, what tool do you use to create diagram where pipeline is shown? @user

A: Hey, @user! Here you go:  The diagram showing the pipeline is created using Mermaid, which is a JavaScript-based diagramming and charting tool that uses Markdown-inspired syntax. In the provided example, the diagram illustrates the flow of data extraction, transformation, and querying in a simple format.  Here's the code snippet used for the diagram:  ```mermaid graph LR   Extract[Extract Data via HTTP REST API] --&gt; Transform[Transform Data in Python]   Transform --&gt; Query[Query Data with DuckDB] ```  You can use similar Mermaid syntax to create your own diagrams for visualizing data pipelines or workflows.
   ---
   Think draw.io (http://draw.io) would be the simplest to start with and fairly easy to use.
   ---
   Lucidchart was fine for me
   ---
   draw.io (http://draw.io) works best. excalidraw is great too

### [2026-03-01] Vadim Sokoltsov (replies: 4)

Q: Hello everyone! :wave:
   
   Have couple of questions about capstone 1 project
   1. For a while I am working on it, and I decided to do the deployment + CD in a :sparkles: fancy way:sparkles:  from the beginning, so I have almost ~wasted~ spend all of my GCP credits :pepe-sad:  For today there is more than enough data for the dashboard (~48kk records in BigQuery), but if by the time of the assignment I will remove the most resource-consuming parts (GKE / managed Kafka / ...) and provide explanation for what time frame data is available - will it be enough for achiving the highest mark on `cloud deplo ...

A: Hey Vadim!
   
   Happy to weigh in on the dbt questions.
   
   Event-triggered is not natively supported. dbt doesn't watch for new data arriving. The standard pattern is to use an external trigger. For example, a Cloud Function or Pub/Sub message that calls the dbt Cloud API when new data lands in BigQuery.
   
   *How frequently should you run dbt on streaming data?* With incremental models, dbt only processes new records since the last run, so you can run it quite frequently without reprocessing everything. That said, there's a practical floor. Every 5-15 minutes is the typical minimum for near-real-time use cases. Running more frequently than that adds startup/compilation overhead and BigQuery slot costs without much benefit. For true sub-minute latency you'd need a dedicated stream processor like Flink upstream of dbt.
   
   If you're on dbt Core v1.9+, the new *microbatch* incremental strategy is worth looking at for large time-series datasets. It splits execution into independent time-window batches, handles late-arriving data, and makes backfills much easier.
   
   *How is dbt scheduled in production?* Most commonly via dbt Cloud's built-in job scheduler, but you can also use orchestrators like Airf ...

### [2026-04-21] Spark (replies: 1)

Q: Hello team 
   Quick question, has anyone used a good AI tool for generating architecture diagrams?  
   I’m looking for something that can create clean, production-quality diagrams (preferably AWS-style or similar).  
   Would love to hear your recommendations or experiences

A: Gemini worked for me

---

## Quizzes / quiz access / quiz wrong answer (2 threads)

### [2025-02-02] Viktorija Alexeeva (replies: 4)

Q: Hi, mentors. Pls advise, what do you expect for hw2 submission link? Only .md file with scripts to answer quiz questions or also working files such as docker-compose, flows files?

A: Working files
   ---
   Basically if someone takes your code, they should be able to rerun the whole thing and reproduce the results
   ---
   Alexey, would like to clarily. in order to save changes in prepared files i made fork from original repo. and also i have created another repo for homework files. should i delete hw repo and just add .md files with sql scripts to forked repo? some mess in my head, sorry
   ---
   Up to you, it doesn't really matter if it's a fork or not

### [2025-02-02] Ari Lamstein (replies: 12)

Q: I am struggling to understand what to store in git for this week’s homework with Kestra.
   
   For module 1 I put the actual SQL commands I actually ran to get the answers (link (https://github.com/arilamstein/de-zoomcamp-2025-hw/blob/main/01-docker-terraform-hw.txt))
   
   But for module 2 I completed the assignment within the Kestra UI. (Backfill the first 7 months of 2021).
   
   And as I look at the module 2 quiz it looks like I can complete the answers by looking at the GCP ui.
   
   The prompt for the homework says:
   > ATTENTION: At the end of the submission form, you will be required to include a link to yo ...

A: you could take some pictures and show how you drew your conclusions.
   
   Embed them in a markdown file in HW repo. Be creative :celebrate:
   ---
   Provide the YAML flow, and evidence of a few successful executons
   ---
   but *don’t* share *any credentials* on github :bangbang:
   ---
   DO NOT PUSH THE FLOWS PLEASE, one of the flows has your credentials
   ---
   I think you only need to write the three queries you used in the readme file
   ---
   It'll be hard to make people avoid this mistake as anything (even pinned messages) are lost through the flood of messages here
   ---
   @user @user @user I've asked some of you already in DMs, but if you stumble upon anyone pushing their flows to github,
   
   *PLEASE*, I humbly ask for your help to  tell them to refer to that pinned post first:
   
   https://datatalks-club.slack.com/archives/C01FABYF2RG/p1738520204522619
   
   Thank you!
   ---
   Michael Shoemaker was very clear in this video (https://www.youtube.com/watch?v=Y2ux7gq3Z0o&amp;t=4m18s) about risks exposing credentials
   ---
   @user Yes, but in this video: DE Zoomcamp 2.2.6 - ETL Pipelines in Kestra: Google Cloud Platform (https://youtu.be/nKqjjLJ7YXs?si=wBQ7iGvjZj6FB7HY&amp;t=277) for the time frame between *4:37~4:52* it is exac ...

---

## Removing oneself / changing email / account issues (2 threads)

### [2025-11-26] Ella S. Park (replies: 1)

Q: hello team, Hope you are all well! I have an admin-related question, I signed up for the Data engineering bootcamp starting next January, but unfortunately Im not able to attend it anymore, is there a way to remove myself from the signup ? I was looking for some information about it but couldnt find any, I'd appreciate your help :slightly_smiling_face: Thanks a lot!

A: There's no way but it's okay, you can just sign up for any other future cohort

### [2025-12-25] Linliang (replies: 1)

Q: Hi everyone, has anyone received the inscription confirmation email for 2026? I'm still waiting for the mine.

A: It's not enabled yet. I wanted to do it last week but then holidays happened

---

