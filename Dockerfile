FROM python:3.13.4-slim
LABEL Maintainer="OsmanKandemir"
COPY . /app
WORKDIR /app
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt
ENTRYPOINT ["python", "scanner.py"]


#docker build -t staticcodeanalysishelper .
#docker run -v <YOUR-PROJECT-PATH-FOLDER>:/static-code-analysis-helper/Project staticcodeanalysishelper -f /static-code-analysis-helper/Project -p <YOUR-PROGRAMMING-LANGUAGE>




