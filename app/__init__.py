import os
from eve import Eve
from people.app_settings import basedir

templates_dir = os.path.join(basedir, 'templates')


def create_app(config_name='app_settings.py'):

    app = Eve(
        settings=config_name,
        template_folder=templates_dir
    )

    return app
