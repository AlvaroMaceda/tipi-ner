from flask import Flask
from flask_cors import CORS
from ner.settings import Config

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/ping', methods=['GET', 'POST'])
    def ping():
        return 'pong'

    # logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
    # logging.config.fileConfig(logging_conf_path)
    # log = logging.getLogger(__name__)
    # log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    return app

