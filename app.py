from flask import Flask, request
from json import loads
import numpy as np
from sklearn.linear_model import LinearRegression

with open('data/model.json', 'r') as f:
  content = f.read()
  model = loads(content)

predictor = LinearRegression(n_jobs=-1)
predictor.coef_ = np.array(model)
predictor.intercept_ = np.array([0])
print(predictor.coef_)
print(predictor.intercept_)

app = Flask(__name__)

@app.route('/')
def hello_world():
    # curl localhost:5000/?input="10,20,30"
    params = request.args.get('input') # "10,20,30"
    print(params)
    print(type(params))
    parameters = params.split(",")

    X = [[
      int(parameters[0]),
      int(parameters[1]),
      int(parameters[2])
    ]]
    outcome = predictor.predict(X=X)
    print(outcome)
    return str(outcome) + '\n'


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)