# import os
# import py_eureka_client.eureka_client as eureka_client
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import text

# from api.v1.routes import routes
# from config import Config
# port = int(os.environ.get('PORT', 8056))

# def create_app(config_class=Config):
#   app = Flask(__name__, instance_relative_config=True)
#   app.register_blueprint(routes)
#   app.config.from_object(config_class)
#   eureka_client.init(eureka_server="http://localhost:8761/eureka",
#     app_name="scoring-service-py",
#     instance_port=port)
#   return app



# # db = SQLAlchemy(app)


# if __name__ == "__main__":
#   create_app().run(debug=True, host='0.0.0.0', port=port)