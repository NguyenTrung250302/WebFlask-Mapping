from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

markers = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/markers')
def get_markers():
    return render_template('makers.html', markers=markers)

@app.route('/add_marker', methods=['POST'])
def add_marker():
    data = request.get_json()
    marker = {
        'id': len(markers) + 1,
        'name': data['name'],
        'lat': float(data['lat']),
        'lon': float(data['lon']),
        'info': data['info']
    }
    markers.append(marker)
    return jsonify(marker)

@app.route('/delete_marker/<int:id>', methods=['DELETE'])
def delete_marker(id):
    global markers
    markers = [marker for marker in markers if marker['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
