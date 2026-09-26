FROM eclipse-temurin:17-jdk

WORKDIR /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

ENV JAVA_HOME=/opt/java/openjdk
ENV PATH="${JAVA_HOME}/bin:${PATH}"

CMD ["python3", "-m", "jobs.spark_job", "configs/employee_etl.yaml"]