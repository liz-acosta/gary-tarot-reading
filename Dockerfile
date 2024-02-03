FROM python:latest

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/gary-tarot/venv/bin:$PATH"

WORKDIR /gary-tarot

RUN python -m venv /gary-tarot/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./
COPY static/ ./static
COPY templates/ ./templates

EXPOSE 5000

ENTRYPOINT [ "python", "/gary-tarot/app.py" ]