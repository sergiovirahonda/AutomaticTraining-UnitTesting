FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-0
WORKDIR /root

RUN pip install pandas numpy google-cloud-storage scikit-learn opencv-python Flask jsonpickle

RUN apt-get update; apt-get install git -y; apt-get install -y libgl1-mesa-dev

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN git clone https://github.com/sergiovirahonda/AutomaticTraining-UnitTesting.git

RUN mv /root/AutomaticTraining-UnitTesting/data_utils.py /root
RUN mv /root/AutomaticTraining-UnitTesting/task.py /root
RUN mv /root/AutomaticTraining-UnitTesting/email_notifications.py /root
RUN mv /root/AutomaticTraining-UnitTesting/TEST_IMAGE.jpg /root

EXPOSE 5000

ENTRYPOINT ["python","task.py"]
