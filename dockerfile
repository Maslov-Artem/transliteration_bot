FROM python:3.12-rc
ENV BOT_TOKEN=$BOT_TOKEN
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]
