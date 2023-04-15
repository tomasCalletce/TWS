import json 

def extract_body(arr):
    # Join the array into a single string
    request_string = ' '.join(arr)

    # Find the starting and ending indices of the JSON object
    start_index = request_string.find('{')
    end_index = request_string.rfind('}') + 1

    # Extract the JSON object string and parse it
    json_object_str = request_string[start_index:end_index]
    json_object = json.loads(json_object_str)

    return json_object
