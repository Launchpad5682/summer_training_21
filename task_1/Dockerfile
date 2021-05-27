FROM centos:latest
RUN yum install python3 -y
RUN  pip3 install scikit-learn numpy pandas
COPY ./dataset/salary.csv ./dataset/
COPY ./ml_model/linear_reg.py ./ml_model/
CMD ["python3","ml_model/linear_reg.py"]
