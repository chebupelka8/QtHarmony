import qtharmony
import qtharmony.resources

import os.path


RESOURCES: str = os.path.dirname(qtharmony.resources.__file__)
UI_RESOURCES: str = os.path.join(RESOURCES, "ui")

THEME_RESOURCES: str = os.path.join(RESOURCES, "themes")
