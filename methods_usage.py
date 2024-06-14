from flask import Flask, request, Response, jsonify
import os, json

# # Clear the screen (if applicable on your platform)
# if os.name == 'nt':  # For Windows systems
#     os.system("cls")
# else:
#     os.system("clear")  # For Unix-like systems

# Create the Flask application instance
app = Flask(__name__)

# Route handler for GET request at "/v1/get_method/"
@app.route("/v1/get_method/", methods=["GET"])
def get_method_v1() -> Response:
    """
    Handles GET requests to the "/v1/get_method/" endpoint.

    This route handler simply prints a message indicating a GET request
    and returns the same message as a response.

    Returns:
        A Response object with the content "GET METHOD".
    """
    print("GET METHOD")
    return Response("GET METHOD")

# Route handler for GET request with parameters at "/v2/get_method/<params>"
@app.route("/v2/get_method/<params>", methods=["GET"])
def get_method_v2(params: str) -> Response:
    """
    Handles GET requests to the "/v2/get_method/<params>" endpoint,
    accepting a parameter in the URL path.

    This route handler extracts the parameter value, prints it, and returns
    a response that echoes the parameter.

    Args:
        params (str): The parameter value extracted from the URL path.

    Returns:
        A Response object with the content f"GET METHOD with params = {params}".
    """
    print(f"GET METHOD with params = {params}")
    return Response(f"GET METHOD with params = {params}")

# Route handler for POST request at "/v3/get_method/" with JSON data
@app.route("/v3/get_method/", methods=["GET"])
def get_method_v3() -> jsonify:
    """
    This function handles GET requests to the "/v3/get_method/" endpoint.

    It retrieves any JSON data sent in the request body and prints it to the console.
    The function then rv1eturns the received JSON data as a JSON response.

    Returns:
        A JSON response containing the received data (if any).
    """
    params = request.get_json()
    print(f"GET METHOD with params = ")
    print(params)
    return jsonify(params)

# Route handler for POST request at "/v1/post_method/" with form data
@app.route("//post_method/", methods=["POST"])
def post_method_v1() -> jsonify:
    """
    Handles POST requests to the "/v1/post_method/" endpoint,
    expecting form data with a "params" key.

    This route handler retrieves the "params" value from the request form,
    prints it, and returns a response that greets the user with the provided
    parameter.

    Returns:
        A Response object with the content f"Hello {params}" (where params
        is the value retrieved from the request form).
    """
    # TODO: check alternately with "params" and "parameter"
    # params = request.args.get("params") 
    params = request.get_json() 
    print(params)
    return jsonify(params) #Response(f"Hello {params}")


# Route handler for both GET and POST requests at "/v2/post_method/"
@app.route("/v2/post_method/", methods=["GET", "POST"])
def post_method_v2() -> jsonify:
    """
    Handles both GET and POST requests to the "/v3/post_method/" endpoint.

    This route handler retrieves the "params" value from the request form
    (for GET requests) or the request body (for POST requests). It then
    prints the parameter and returns it as the response.

    Returns:
        A Response object with the retrieved parameter value.
    """
    # TODO: run alternately
    # params = request.args.get("params")
    params = request.get_json()
    print(params)
    return jsonify(params)#Response(json.dumps(params), content_type="application/json")

if __name__ == "__main__":
    # Run the Flask development server on all available interfaces (0.0.0.0)
    app.run(debug=True, host="0.0.0.0")