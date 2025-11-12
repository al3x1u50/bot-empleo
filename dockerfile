FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install requests beautifulsoup4 lxml
CMD ["python", "buscador_empleo.py"]
