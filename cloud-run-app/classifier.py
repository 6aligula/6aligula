import re

CATEGORIES = [
    "Motor",
    "Chasis",
    "Electric",
    "Mantenimiento",
    "Frenos",
    "Neumaticos",
    "Carroceria",
    "Electronica",
    "Accesorios",
    "Otros",
]

KEYWORDS = {
    "Motor": ["motor", "sobrecalent"],
    "Chasis": ["chasis"],
    "Electric": ["electrico", "bateria"],
    "Mantenimiento": ["mantenimiento"],
    "Frenos": ["freno"],
    "Neumaticos": ["llanta", "neumatico"],
    "Carroceria": ["carroceria"],
    "Electronica": ["electronica"],
    "Accesorios": ["accesorio"],
}

def classify_text(text: str) -> str:
    """Classify text into one of the predefined categories."""
    text_l = text.lower()
    for category, words in KEYWORDS.items():
        for w in words:
            if w in text_l:
                return category
    return "Otros"
