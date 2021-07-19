from flask import Flask, request
from flask_cors import CORS
from ner.settings import Config
from ner.tagger import Tagger

tagger = Tagger()

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route('/ping', methods=['GET', 'POST'])
    def ping():
        return 'pong'

    @app.route('/tag', methods=['GET', 'POST'])
    def tag():
        text = request.get_json()
        res = tagger.foo("Bertín Osborne se fue a comer jamón Navidul a Santiago de Compostela")
        return 'this should return something with sense'

    # logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
    # logging.config.fileConfig(logging_conf_path)
    # log = logging.getLogger(__name__)
    # log.info('>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    return app

