from app.__init__ import create_app
import os
from dotenv import load_dotenv
load_dotenv()

config_name = os.environ.get('FLASK_ENV', 'development')

app = create_app(config_name)

if __name__ == '__main__':
    
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', '5000'))
    
    debug = os.environ.get('DEBUG', 'False')
    
    print(f"\n {'='*60}")
    print(f" Starting Flask Application")
    print(f"{'='*60}")
    print(f"Enivronmnt:  {config_name}")
    print(f"Debug Mode:  {debug}")
    print(f"Database:    {app.config['SQLALCHEMY_DATABASE_URI']}")
    print(f"Server:    http://{host}:{port}")
    print(f"Health Check:   http://{host}:{port}/health")
    print(f"\n {'='*60}")
    
    app.run(
        host=host,
        port=port,
        debug=debug
        )