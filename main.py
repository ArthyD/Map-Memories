from map_project.ihm import IHM
from map_project import create_app
import os



if __name__ == '__main__':
    #ihm = IHM()
    app = create_app()
    #ihm.mainloop()
    app.run(debug=True, port = 80, host='0.0.0.0')
