FROM python

WORKDIR /app

COPY . .

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN pip install --no-compile --no-cache-dir -r requirements-prod.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0","--port=83"]
