# CREATE TABLE user_actions (user_id VARCHAR(255),
#     name VARCHAR(255),
#     action VARCHAR(255),
#     timestamp VARCHAR(255),
#     subscribe VARCHAR(255)
# );

# Add postgresql JDBC Driver on Cnt7-naya-cdh63 container
#sudo wget -P /opt/drivers/ https://jdbc.postgresql.org/download/postgresql-42.3.6.jar

#pip install python-telegram-bot==13.7

import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql import types as T


# conection between  spark and kafka
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.1 pyspark-shell'

bootstrapServers = "Cnt7-naya-cdh63:9092"
topics = 'stock'

driver_location = "/opt/drivers/postgresql-42.3.6.jar"

spark = SparkSession\
    .builder\
    .appName("stock_bot") \
    .config("spark.driver.extraClassPath", driver_location) \
    .getOrCreate()

# ReadStream from kafka
df_kafka = spark\
    .readStream\
    .format("kafka")\
    .option("kafka.bootstrap.servers", bootstrapServers) \
    .option("subscribe", topics)\
    .load()

schema = T.StructType()\
    .add("user_id", T.StringType())\
    .add("name", T.StringType())\
    .add("action", T.StringType())\
    .add("timestamp", T.StringType())\
    .add("subscribe", T.StringType())

botdf = df_kafka\
    .select(F.col("value").cast("string"))\
    .select(F.from_json(F.col("value"), schema)
            .alias("value")).select("value.*")


def _write_streaming(df, epoch_id):

    df.write \
    .format("jdbc") \
    .mode('append') \
    .option("truncate", 'true') \
    .option("url", f"jdbc:postgresql://postgresql-container:5432/postgres") \
    .option("driver", "org.postgresql.Driver") \
    .option("dbtable", 'public.user_actions') \
    .option("user", 'postgres') \
    .option("password", 'NayaPass123!') \
    .save()
#
botdf.writeStream \
     .foreachBatch(_write_streaming) \
     .start() \
     .awaitTermination()
