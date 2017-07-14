from flask import Flask, Response, render_template
from datetime import datetime
from psutil import virtual_memory
import json
app = Flask(__name__)


def memory_usage_in_json():
    mem = virtual_memory()
    timestamp = datetime.now().isoformat()
    result = {
        'total': mem.total,
        'avail': mem.available,
        'percent': mem.percent,
        'used': mem.used,
        'free': mem.free,
        'active': mem.active,
        'inactive': mem.inactive,
        'buffers': mem.buffers,
        'cached': mem.cached,
        'shared': mem.shared,
        'timestamp':timestamp
    }
    return json.dumps(result)


@app.route('/')
def memorygui():
    return render_template('memory_monitor.html')

@app.route('/memory')
def memory_usage():    
    result = memory_usage_in_json()
    response = Response(
        response=result,
        status=200,
        mimetype='application/json'
    )
    return response






if __name__ == '__main__':
    app.run()