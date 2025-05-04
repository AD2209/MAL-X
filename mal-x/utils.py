import joblib
import matplotlib.pyplot as plt
import io
import base64

def load_model():
    model = joblib.load("model.pkl")  # path to your ML model file
    return model

def get_metrics():
    accuracy = 0.94  # just for testing
    params = {"max_depth": 5, "n_estimators": 100}
    return accuracy, params

def generate_graph():
    plt.plot([1, 2, 3], [2, 4, 1])
    plt.title("Sample Graph")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return f"data:image/png;base64,{graph_url}"
