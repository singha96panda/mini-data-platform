import os
import sys

os.environ["HADOOP_HOME"] = r"C:\hadoop"
os.environ["hadoop.home.dir"] = r"C:\hadoop"

from pyspark.sql import SparkSession

from framework.yaml_parser import load_config
from framework.transformation_engine import apply_transformations


def main(config_file):

    config = load_config(config_file)

    spark = (
        SparkSession.builder
        .appName(config.get("job_name", "MiniDataPlatform"))
        .config(
            "spark.jars",
            "drivers/postgresql-42.7.13.jar"
        )
        .getOrCreate()
    )

    df = spark.read.csv(
        config["source"]["file"],
        header=True,
        inferSchema=True
    )

    df = apply_transformations(
        df,
        config["transformations"]
    )

    df.show()

    target = config["target"]

    jdbc_url = (
        f"jdbc:postgresql://"
        f"{target['host']}:{target['port']}/"
        f"{target['database']}"
    )

    properties = {
        "user": target["user"],
        "password": target["password"],
        "driver": "org.postgresql.Driver"
    }

    df.write.jdbc(
        url=jdbc_url,
        table=target["table"],
        mode="overwrite",
        properties=properties
    )

    print("Data loaded successfully")

    spark.stop()


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(
            "Usage: python -m jobs.spark_job <config_file>"
        )
        sys.exit(1)

    config_file = sys.argv[1]

    main(config_file)