FROM gcr.io/deeplearning-platform-release/tf2-cpu.2-0
WORKDIR /root

RUN pip install pandas numpy google-cloud-storage scikit-learn opencv-python Flask jsonpickle

RUN apt-get update; apt-get install git -y; apt-get install -y libgl1-mesa-dev

RUN git clone https://github.com/sergiovirahonda/AutomaticTraining-UnitTesting.git

RUN mv /root/AutomaticTraining-UnitTesting/data_utils.py /data_utils.py
RUN mv /root/AutomaticTraining-UnitTesting/task.py /task.py
RUN mv /root/AutomaticTraining-UnitTesting/email_notifications.py /email_notifications.py
RUN mv /root/AutomaticTraining-UnitTesting/TEST_IMAGE.jpg /TEST_IMAGE.jpg

EXPOSE 5000

ENTRYPOINT ["python","task.py"]
