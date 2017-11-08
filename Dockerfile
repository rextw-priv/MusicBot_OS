FROM python

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt
RUN pip install aiotg
CMD ["python", "./setup.py"]
CMD ["python", "./app.py"]

EXPOSE 8080
