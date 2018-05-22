from flask import Flask
import json
import sys
sys.path.append('/home/santiago/so-exam3')
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/v1/stats/cpu')
def cpu():
    info_cpu = Stats.porcentaje_cpu()
    return json.dumps({'CPU Porcentaje': info_cpu})

@app.route('/v1/stats/memory')
def memoria():
    info_memoria = Stats.memoria_disponible()
    return json.dumps({'Espacio en memoria': info_memoria})

@app.route('/v1/stats/disk')
def disco():
    info_disco = Stats.espacio_disco()
    return json.dumps({'Espacio en el Disco': info_disco})


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
