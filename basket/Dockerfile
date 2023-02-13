FROM python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements-prod.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0","--port=83"]