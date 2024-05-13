from map_project import create_app
import os
from multiprocessing import Process



if __name__ == '__main__':
    app = create_app()
    app.app_context().push()
    app.run(debug=True, port = 80, host='0.0.0.0')
    
    
    
