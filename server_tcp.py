# Import the Socket framework.
import socket

# Socket configuration.
HOST, PORT = "localhost", 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def getPinState(pinNum):
  data = "gps::pinState:" + str(pinNum)
  try:
      sock.connect((HOST, PORT))
      sock.sendall(data + "\n")
      received = sock.recv(1024)
  finally:
      sock.close()

def setPinState(pinNum, pinState):
  data = "sps::pinNum:" + str(pinNum) + ",pinState:" + pinState
  try:
      sock.connect((HOST, PORT))
      sock.sendall(data + "\n")
      received = sock.recv(1024)
  finally:
      sock.close()

def getTimeDuration(pinNum):
  data = "gtd::pinNum:" + str(pinNum)
  try:
      sock.connect((HOST, PORT))
      sock.sendall(data + "\n")
      received = sock.recv(1024)
  finally:
      sock.close()

def setTimeDuration(pinNum, startTime, duration):
  data = "std::pinNum:" + str(pinNum) + ",startTime:" + startTime, ",duration:" + duration
  try:
      sock.connect((HOST, PORT))
      sock.sendall(data + "\n")
      received = sock.recv(1024)
  finally:
      sock.close()

if __name__ == "__main__":
  setPinState(11, "on")

print "Sent:     {}".format(data)
print "Received: {}".format(received)