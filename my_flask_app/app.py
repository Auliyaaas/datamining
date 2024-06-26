from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
model_filename = 'bagging_classifier_model.pickle'
with open(model_filename, 'rb') as model_file:
    modelku = pickle.load(model_file)

# Load the pre-processing scaler
scaler_filename = 'preprocessing.pickle'
with open(scaler_filename, 'rb') as scaler_file:
    pra_proses = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

# Flask Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the POST request.
        data = request.get_json(force=True)
        
        # Convert categorical features to numeric values
        categorical_features = {
            "gender": {"male": 1, "female": 2}
        }

        for feature, mapping in categorical_features.items():
            data[feature] = mapping[data[feature]]

        # Convert the data into a DataFrame
        data_df = pd.DataFrame([data])

        # Pre-process the data
        transformed_data = pra_proses.transform(data_df)

        # Make prediction
        prediction = modelku.predict(transformed_data)

        # Return the prediction as a JSON response
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)




# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get the data from the POST request.
#         data = request.get_json(force=True)
        
#         # Convert categorical features to numeric values
#         categorical_features = {

#             "gender": {"male": 0, "female": 1}
#         }

#         for feature, mapping in categorical_features.items():
#             data[feature] = mapping[data[feature]]

#         # Convert the data into a DataFrame
#         data_df = pd.DataFrame([data])

#         # Pre-process the data
#         transformed_data = pra_proses.transform(data_df)

#         # Make prediction
#         prediction = modelku.predict(transformed_data)

#         # Return the prediction as a JSON response
#         return jsonify({'prediction': int(prediction[0])})
#     except Exception as e:
#         return jsonify({'error': str(e)})

# if __name__ == "__main__":
#     app.run(debug=True)
