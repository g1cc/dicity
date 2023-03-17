import os

from datetime import timedelta

from flask import Flask, render_template, send_file, redirect
from flask_socketio import SocketIO

from .Libs.Outputer.logger import print, LoggerColor

class Server:
    def __init__(self) -> None:
        if __name__ == "__main__":
            self.app = Flask(__name__)

        else:
            self.app = Flask(__name__, static_url_path='/app/')
        
        self.app.secret_key = ' '

        self.socketio = SocketIO(self.app)

    def init_routes(self):
        @self.app.route("/")
        def index():
            return redirect("/vet", code=302)

        # @self.app.route("/auth", methods=["GET"])
        # def auth():
        #     # print(current_identity)
        #     return render_template("./auth.html")

        @self.app.route("/logger/get_logs", methods=["GET"])
        def get_logger():
            return print()
            

        @self.app.route("/image/<image_name>", methods=['GET'])
        def get_image(image_name):
            if os.path.exists(f'./app/static/images/{image_name}'):
                mimetype = "image/gif"
                if ("svg" in image_name):
                    mimetype = "image/svg+xml"

                # print(url_for('static', filename=f'images/{image_name}'))'
                    
                
                return send_file(f'./static/images/{image_name}', mimetype=mimetype), 200

            else:
                return send_file(f'./static/images/default.png', mimetype='image/gif'), 200

        @self.app.route("/vet", methods=["GET"])
        def vetX():
            # if isLoggingOnServer():
            return render_template("./vet_new.html")

        @self.app.route("/login", methods=["GET"])
        def vet_login():
            # if isLoggingOnServer():
            return render_template("./vet_login.html")

        @self.app.route("/vet_old", methods=["GET"])
        def vet1():
            # if isLoggingOnServer():
            return render_template("./vet_new.html")

        @self.app.route("/logger", methods=["GET"])
        def logger():
            # if isLoggingOnServer():
            return render_template("./logger.html", loggs=print())

        @self.app.route("/i0saf2i0g2i02di07hdqQ2h79q3sjf089", methods=["GET"])
        def shutdown():
            self.socketio.stop()
            return "Shutting down..."
 
        # @self.socketio.on("info")
        # @jwt_required()
        # def response(data):
        #     # print(current_identity.get_connection().get_room())
        #     if self.manager.get_status() == States.IN_GAME:
        #         emit("info", {"speed": self.manager.get_speed(), "gear": self.manager.get_gear(), "RPM": self.manager.get_rpm()}, room=current_identity.get_connection().get_room())
        #     else:
        #         emit("info", {"status": self.__get_status__()})

        # @self.socketio.on('connect_to_logs')
        # def connect_to_logs(data):
        #     print(data, type=LoggerColor.warn)
        #     # emit("Hello", {"data": "Hello"}, room=current_identity.get_connection().get_room())

    
    def init(self):
        self.init_routes()
        print("[+] Server initialized.", type=LoggerColor.GREEN)
        # self.app(host="0.0.0.0", port="223")
        self.socketio.run(self.app, host="0.0.0.0", port="80")