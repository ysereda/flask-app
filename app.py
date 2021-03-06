import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load pickled model
model = pickle.load(open('model.pkl','rb'))

# Name flask app
app = Flask(__name__)

# Create a route that receives JSON inputs, uses the trained model to make a prediction, and returns that prediction in a JSON format, which can be accessed through the API endpoint.
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)
    # This works with most (not all!) types of models that you will want to use to make a prediction. You can choose to convert the inputs using your preferred method as long as it works with the .predict() method for your model.
    
    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)