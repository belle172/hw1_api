FROM python:3

EXPOSE 7998

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "/usr/src/app/server.py" ]