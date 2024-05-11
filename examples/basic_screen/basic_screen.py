from qtharmony.constructor import Initialization
from qtharmony.windows import MainWindow

import sys


Initialization.init(sys.argv)


if __name__ == "__main__":
    window = MainWindow(title="Hello", size=(600, 400))
    window.run()

    Initialization.exec()
