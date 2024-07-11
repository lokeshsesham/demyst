from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

# Initialize Spark session
spark = SparkSession.builder.appName('CSVAnonymization').getOrCreate()

# Read the CSV file into a Spark DataFrame
df = spark.read.csv('sample.csv', header=True)

# Anonymize the specified columns
df = df.withColumn('first_name', lit('ANONYMIZED'))
df = df.withColumn('last_name', lit('ANONYMIZED'))
df = df.withColumn('address', lit('ANONYMIZED'))

# Write the anonymized DataFrame to a new CSV file
df.write.csv('anonymized_sample_spark.csv', header=True)

# Stop the Spark session
spark.stop()
