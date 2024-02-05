# Usa un'immagine di Python
FROM python:3.9

# Imposta la directory di lavoro
WORKDIR /app

# Copia il codice sorgente nella directory di lavoro
COPY . .

# Installa le dipendenze
RUN pip install -r requirements.txt

# Esponi la porta su cui Flask è in ascolto
EXPOSE 5000

# Comando per eseguire l'app Flask
CMD ["python", "webmain.py"]
