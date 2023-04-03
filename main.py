from bp import init_bp
from flask import Flask

def create_app():
    
    app = Flask(__name__)
    init_bp(app)
    # app configuration and routes here
    return app




# Run the Flask application
if __name__ == '__main__':
    app = create_app()
    app.run()