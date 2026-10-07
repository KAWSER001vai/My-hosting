from flask import Flask, render_template, jsonify, request
import psutil
import os

app = Flask(__name__)

# Route: Home Page
@app.route('/')
def home():
    return render_template('index.html')

# API Route: System Live Stats
@app.route('/api/stats', methods=['GET'])
def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    active_processes = len(psutil.pids())
    
    return jsonify({
        'cpu': cpu,
        'ram': ram,
        'processes': active_processes
    })

# API Route: Run shell command or restart bot
@app.route('/api/action', methods=['POST'])
def perform_action():
    data = request.json
    action_type = data.get('action')
    app_name = data.get('app_name')
    
    # Logic for process management
    if action_type == 'restart':
        # logic to restart python bot
        return jsonify({'status': 'success', 'message': f'{app_name} restarted successfully!'})
    elif action_type == 'stop':
        return jsonify({'status': 'success', 'message': f'{app_name} stopped!'})
        
    return jsonify({'status': 'error', 'message': 'Invalid Action'})

if __name__ == '__main__':
    # Required dependencies: pip install flask psutil
    app.run(host='0.0.0.0', port=5000, debug=True)
