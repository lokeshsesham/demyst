from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import random
import string

# Create a Spark session
spark = SparkSession.builder \
    .appName("Anonymize CSV") \
    .getOrCreate()

# Function to generate a random string
def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Register the UDF
random_string_udf = udf(lambda x: random_string(10), StringType())

# Load the CSV file into a DataFrame
df = spark.read.csv('data.csv', header=True)

# Anonymize the columns
df = df.withColumn('first_name', random_string_udf('first_name'))
df = df.withColumn('last_name', random_string_udf('last_name'))
df = df.withColumn('address', random_string_udf('address'))

# Save the anonymized data back to a new CSV file
df.write.csv('anonymized_data', header=True)

spark.stop()