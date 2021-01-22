from vidstream import ScreenShareClient
import threading
sender  = ScreenShareClient('192.168.43.157',9999)
t = threading.Thread(target=sender.start_stream)
t.start()


while input("") != 'STOP':
    continue
sender.start_stream()