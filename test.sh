#!/bin/bash

# Base URL for the API
BASE_URL="http://localhost:8000/api"

# Function to make predictions and verify the response
make_prediction() {
    local data="$1"
    local expected_response="$2"
    local response=$(curl -s "$BASE_URL/predict" -X POST -H 'Content-Type: application/json' -d "$data")

    if [ "$response" == "$expected_response" ]; then
        echo "Prediction test passed. Response: $response"
    else
        echo "Prediction test failed. Expected $expected_response, got $response"
    fi
}

# Function to test the health route
test_health_route() {
    response=$(curl -s "$BASE_URL/health")
    expected_response='{"message":"Estou saudavel!"}'

    if [ "$response" == "$expected_response" ]; then
        echo "Health route test passed."
    else
        echo "Health route test failed. Expected $expected_response, got $response"
    fi
}

# Making predictions with verification
make_prediction '{"alcohol": 14.23, "malic_acid": 1.71, "ash": 2.43, "alcalinity_of_ash": 15.6, "magnesium": 127.0, "total_phenols": 2.8, "flavanoids": 3.06, "nonflavanoid_phenols": 0.28, "proanthocyanins": 2.29, "color_intensity": 5.64, "hue": 1.04, "od280_od315_of_diluted_wines": 3.92, "proline": 1065.0}' '{"prediction":0}'
make_prediction '{"alcohol": 12.3400001526, "malic_acid": 2.4500000477, "ash": 2.4600000381, "alcalinity_of_ash": 21, "magnesium": 98, "total_phenols": 2.5599999428, "flavanoids": 2.1099998951, "nonflavanoid_phenols": 0.3400000036, "proanthocyanins": 1.3099999428, "color_intensity": 2.7999999523, "hue": 0.8000000119, "od280_od315_of_diluted_wines": 3.3800001144, "proline": 438}' '{"prediction":1}'
make_prediction '{"alcohol": 12.8500003815, "malic_acid": 3.2699999809, "ash": 2.5799999237, "alcalinity_of_ash": 22, "magnesium": 106, "total_phenols": 1.6499999762, "flavanoids": 0.6000000238, "nonflavanoid_phenols": 0.6000000238, "proanthocyanins": 0.9599999785, "color_intensity": 5.5799999237, "hue": 0.8700000048, "od280_od315_of_diluted_wines": 2.1099998951, "proline": 570}' '{"prediction":2}'

# Testing the health route
test_health_route