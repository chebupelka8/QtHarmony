<p align="center">
    <img src="Logo.png">
</p>
<h1></h1>

<p align="center">

  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/ModernQQt">
  <img src="https://img.shields.io/github/license/chebupelka8/ModernQQt">
  <img src="https://img.shields.io/github/commit-activity/t/chebupelka8/ModernQQt"> 
  <img src="https://img.shields.io/github/stars/chebupelka8/ModernQQt">
  <img src="https://img.shields.io/github/watchers/chebupelka8/ModernQQt">
  
</p>

<b>ModernQt</b>: A Cutting-Edge GUI Library Built on PyQt6 ModernQt is a intuitive graphical user interface (GUI) library designed to simplify the development of modern, visually stunning, and highly functional applications. Built on the robust foundation of PyQt6. Now ModernQt is in development.

<h3>How to use</h3>

```sh
pip install ModernQQt
```

```python
from modernqqt.constructor import Initialization
from modernqqt.widgets import ...
...
```

<h3>Examples</h3>
<h4>Basic screen</h4>

```python
from modernqqt.constructor import Initialization
from modernqqt.windows import MainWindow

import sys


Initialization.init(sys.argv)


if __name__ == "__main__":
    window = MainWindow(title="Hello", size=(600, 400))
    window.run()

    Initialization.exec()

```

<img src="examples/basic_screen/basic_screen.png">
