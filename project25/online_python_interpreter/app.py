from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    data = request.json
    code = data.get("code", '')
    
    try:
        output = subprocess.run(['python', '-c', code], capture_output=True, text=True, timeout=5)
        return jsonify({'output': output.stdout, 'error': output.stderr})
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Error: Code execution timed out. Please check your code for infinite loops or inefficiencies.'})
    except Exception as e:
        return jsonify({'error': f"Error:{str(e)}"})
    
if __name__ == '__main__':
    app.run(debug=True)



