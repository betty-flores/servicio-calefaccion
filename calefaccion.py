from flask import Flask, jsonify, request
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)

rest_port = 8001
host = "calefaccion-service.herokuapp.com"
eureka_client.init(eureka_server="http://52.73.98.2:8099/eureka/",
                   app_name="calefaccion",
                   instance_port=rest_port, instance_host=host)

@app.route('/temperatura/<temperatura>', methods=['POST'])
def enceder_calefaccion(temperatura):
    print(temperatura)
    if int(temperatura)<15:
        return "Encendida"
    else:
        return "Apagada"

@app.route("/", methods=['GET'])
def hello():
    return {"welcome": "welcome to my rest api"}

if __name__ == "__main__":
    app.run(port="8001")