from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')

def noAccent(field, feature, parent):
    """
    Delete spanish accent
    <h2>Example usage:</h2>
    <ul>
      <li>noAccent("Acción") -> "ACCION"</li>
    </ul>
    """
    accent = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u"
    }
    text = feature[field]
    for k,v in accent.items():
        text = text.replace(k, v)
    return text.upper()
