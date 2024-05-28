import os
import base64
from app import root_folder


def upload(jsonify, file_data):
 
    try:
        # Decode the base64-encoded file data
        file_name = str.replace(file_data, "\\", "/").split("/")[-1]
        print(file_name)
        file_bytes = base64.b64decode(file_data)

        # Save the decoded file to a directory
        file_path = f'{root_folder}uploads\\{file_name}'
        with open(file_path, 'wb') as f:
            f.write(file_bytes) 

    except (base64.binascii.Error, TypeError) as e:
        return jsonify({"error": "Invalid file data", "e": e}), 400

    # Create response data
    response = {
        'file_name': file_name,
        'file_path': file_path
    }

    return jsonify(response)