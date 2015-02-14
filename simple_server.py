# Import framework for SocketServer creation.
import SocketServer

# TCPHandler, allows server to send and receive TCP packets.
class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        # Grab the function name and function parameters.
        function_delimiter = self.data.find("::")
        function_call = self.data[:function_delimiter]
        function_params = dict(ks.split(":") for ks in self.data[function_delimiter + 2:].split(","))

        def gps(function_params):
            # Get the pinState from Arduino.
            self.request.sendall("pinNum:" + function_params[pinNum] + "pinState:on")

        def sps(function_params):
            # Set the pinState from Arduino.
            self.request.sendall("pinNum:" + function_params["pinNum"] + "pinState" + function_params["pinState"])

        # def gpd(function_params):
        #     # Get the pinTimeDuration from Arduino.
        #     self.request.sendall("pinNum:" + function_params[pinNum] + "startTime:11")

        # def spd(function_params):
        #     # Set the pinTimeDuration from Arduino.
        #     self.request.sendall("on")

        # Determine function to call based on pre-function delimiter.
        if function_call == "gps":
            gps(function_params)
        elif function_call == "sps":
            sps(function_params)
        elif function_call == "gtd":
            gtd(function_params)
        elif function_call == "std":
            std(function_params)



# Create and run server on script startup
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()