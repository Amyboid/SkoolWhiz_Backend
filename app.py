from flask import Flask
from flasgger import Swagger
from src.database import initialize_database
from src.routes.routes import bp as tasks_bp  # Import the blueprint

app = Flask(__name__)
swagger = Swagger(app)

initialize_database()

# Register the blueprint
app.register_blueprint(tasks_bp, url_prefix='/')  # You can change the prefix as needed

if __name__ == "__main__":
    app.run(debug=True)
