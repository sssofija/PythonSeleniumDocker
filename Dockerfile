FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN chmod +x wait-for-selenium.sh

CMD ["pytest", "--alluredir=allure-results", "--maxfail=1", "--disable-warnings", "-q"]
