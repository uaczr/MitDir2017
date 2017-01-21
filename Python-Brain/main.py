import logger
import communicator
import threading
import time
com = communicator.communicator()

def pub_topic_1():
    global com
    while(True):
        while(not com.connected):
            time.sleep(1)

        topic_1 = communicator.topic("Penis", value=200)
        com.publish(topic_1)
        time.sleep(1)

def main():
    global com
    com.connect("127.0.0.1", 1883, 60)
    topic_sub = communicator.topic("Penis", value=200)
    com.add_sub_topic(topic_sub)
    thread_1 = threading.Thread(target=com.loop_forever)
    thread_2 = threading.Thread(target=pub_topic_1)
    thread_1.start()
    #thread_2.start()
    thread_1.join()
    #thread_2.join()


if __name__ == "__main__":
    main()