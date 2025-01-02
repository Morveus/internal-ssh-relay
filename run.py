from flask import Flask, request, jsonify
import subprocess
import argparse

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_command():
    try:
        data = request.get_json()
        if not data or 'command' not in data:
            return jsonify({'error': 'No command provided'}), 400
            
        # Validate required SSH parameters
        required_params = ['ssh_host', 'ssh_user', 'ssh_password', 'command']
        if not all(param in data for param in required_params):
            return jsonify({'error': 'Missing required SSH parameters'}), 400

        # Construct the sshpass command using parameters from request
        ssh_command = [
            'sshpass',
            '-p', data['ssh_password'],
            'ssh',
            '-o', 'StrictHostKeyChecking=no',
            '-o', 'UserKnownHostsFile=/dev/null',
            f'{data["ssh_user"]}@{data["ssh_host"]}',
            data['command']
        ]

        # Execute the command
        result = subprocess.run(
            ssh_command,
            capture_output=True,
            text=True
        )

        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run SSH command execution server')
    parser.add_argument('--port', type=int, default=5000, help='Port to listen on (default: 5000)')
    args = parser.parse_args()
    
    app.run(host='0.0.0.0', port=args.port)
