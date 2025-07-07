import os
from flask import Flask

from config import Config

from database import db
from routes.juegos_routes import VideoJuegos_bp
from routes.plantas_routes import plantas_bp 
from routes.genero_routes import genero_bp

app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(plantas_bp, url_prefix = '/plantas')
app.register_blueprint(VideoJuegos_bp, url_prefix = '/juegos')
app.register_blueprint(genero_bp, url_prefix = '/generos')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True)