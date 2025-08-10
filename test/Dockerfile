FROM python:3.11-slim
WORKDIR /test
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "-q", "--maxfail=1"]
