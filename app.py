from flask import Flask, Response

# Create Flask application instance
app = Flask(__name__)

# Define hostname and port to match original Node.js implementation
hostname = '127.0.0.1'
port = 3000

# Define route handler for all paths
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    # Return 'Hello, World!' with Content-Type text/plain and status code 200
    return Response('Hello, World!\n', mimetype='text/plain')

# Start the server if this file is run directly
if __name__ == '__main__':
    # Log server startup message similar to the original Node.js implementation
    print(f"Server running at http://{hostname}:{port}/")
    # Run the Flask application on the specified hostname and port
    app.run(host=hostname, port=port)