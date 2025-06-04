# TWITTER_DATA_PIPELINE_USING_AIRFLOW
**Twitter Data Pipeline Using Apache Airflow**


* Build an automated data pipeline to fetch, clean, and store tweets
* Use Apache Airflow for scheduling and automation
* Store processed data in AWS S3
* Analyze and visualize tweet data

 Technologies Used**

* Python, Tweepy, Pandas
* Apache Airflow
* AWS S3
* Docker, Ubuntu
* TextBlob (for NLP)
* Matplotlib, Seaborn (for visualization)

---

**: System Architecture**

* Twitter API -> ETL Script -> AWS S3
* Orchestrated by Airflow DAG
* Deployed using Docker on Ubuntu


**: ETL Process**

* **Extract**: Tweets via Tweepy
* **Transform**: Clean text with pandas
* **Load**: Upload CSV to AWS S3
* Airflow DAG schedules the pipeline

---

**: Sentiment Analysis**

* TextBlob used to calculate polarity
* Tweets classified as positive, negative, neutral
* Countplot visualizes sentiment distribution

---

**: Word Cloud Visualization**

* Shows most frequently used words in tweets
* Created using WordCloud library
* Highlights tweet themes

---

**: Output **

* DAG success status in Airflow UI
* CSV file in AWS S3 bucket
* Sentiment graph and word cloud image

---

**Slide 9: Challenges Faced**

* Twitter API rate limits
* Docker and Airflow setup
* AWS permissions
* Resolved with retry logic, proper IAM setup, and testing

---

**Slide 10: Conclusion & Future Scope**

* Project automates real-time tweet collection and storage
* Scalable and reusable architecture
* Future scope:

  * Real-time streaming (Kafka)
  * Dashboards (Power BI/Tableau)
  * Sentiment trend over time

---


