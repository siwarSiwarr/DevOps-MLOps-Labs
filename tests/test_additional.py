import numpy as np
import sys
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Ajouter le dossier parent au path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model import IrisClassifier


def test_prediction_format():
    """Test que les prédictions sont dans le bon format"""
    # Charger les données
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    
    clf = IrisClassifier()
    clf.train(X_train, y_train)  # ✅ Avec arguments
    
    # Tester avec une seule instance
    X_single = X_test[:1]
    prediction = clf.predict(X_single)
    
    assert isinstance(prediction, np.ndarray), "Prediction should be a numpy array"
    assert len(prediction) == 1, "Prediction should have length 1 for single input"


def test_model_accuracy_threshold():
    """Test que le modèle atteint un seuil minimum de précision"""
    # Charger les données
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    
    clf = IrisClassifier()
    clf.train(X_train, y_train)
    result = clf.evaluate(X_test, y_test)
    
    # Si evaluate() retourne un tuple, prendre le premier élément
    if isinstance(result, tuple):
        accuracy = result[0]
    else:
        accuracy = result
    
    assert accuracy > 0.8, f"Model accuracy {accuracy:.2f} is below 80% threshold"

def test_prediction_range():
    """Test que les prédictions sont dans une plage valide"""
    # Charger les données
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    
    clf = IrisClassifier()
    clf.train(X_train, y_train)  # ✅ Avec arguments
    
    # Prédire sur toutes les données de test
    predictions = clf.predict(X_test)
    
    # Les classes Iris sont 0, 1, ou 2
    valid_classes = [0, 1, 2]
    for pred in predictions:
        assert pred in valid_classes, f"Prediction {pred} is not a valid class (0, 1, or 2)"