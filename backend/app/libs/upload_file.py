import io 
import os
import base64
from app import root_folder
from PIL import Image  # type: ignore
import re
from PIL.ExifTags import TAGS  # type: ignore
from uuid import uuid4
from werkzeug.datastructures import FileStorage  # type: ignore


def upload(file_data: str, file_name: str):

    try:
        extension_name = file_name.split('.')[-1].lower()
        if extension_name not in ["jpg", "jpeg", "png"]:
            return {"error": f'Un acceptable extension {extension_name}'}
        profile_pix = file_data
        
        encoded = re.sub('^data:image/.+;base64,', '', profile_pix)
        print(extension_name)
        img_bytes = base64.b64decode(encoded)
        img = Image.open(io.BytesIO(img_bytes))
        output_path = f'{root_folder}uploads\\{file_name}'
        img.save(output_path)

    except Exception as e:
        print(e)
        return {"error": "Invalid file data", "e": e}

    # Create response data
    response = {
        'file_name': file_name,
        'output_path': output_path
    }

    return response


def upload_image(file_path, resize: bool = False, new_size=(300, 300)):
    """
    Opens an image, resizes it, and saves it to a new location.

    :param file_path: FileStorage - The FileStorage object containing the 
    image to be uploaded.
    :param new_size: tuple - The new size of the image as a tuple (width, 
    height).
    """

    # Check if file_path is an instance of FileStorage and if it exists
    if not file_path or not isinstance(file_path, FileStorage):
        raise ValueError("Invalid file path provided.")

    try:
        # Extract the filename from the FileStorage object
        filename = file_path.filename
        # Validate the file extension
        extension_name = filename.rsplit('.', 1)[1].lower()
        if extension_name not in ["jpg", "jpeg", "png"]:
            return {"error": f"Unacceptable extension {extension_name}"}

        # Open the image file
        with Image.open(file_path) as img:
            # Get the image format (e.g., JPEG, PNG)
            image_format = img.format
            # Get the MIME type of the image
            mime_type = Image.MIME.get(image_format)
            # Get the image size
            image_size = img.size
            # Get the image mode (e.g., RGB, CMYK)
            image_mode = img.mode
            # Get EXIF data
            exif_data = img._getexif()
            if exif_data:
                exif_data = {TAGS.get(k, k): v for k, v in exif_data.items() 
                             if isinstance(v, (str, int, float))
                             }

            # Resize the image
            if resize:
                img = img.resize(new_size)

            # Generate a unique name for the output file
            unique_filename = f"{uuid4()}.{extension_name}"
            output_path = os.path.join(root_folder, 'uploads', unique_filename)

            # Save the resized image to the specified path
            img.save(output_path)

            # Return the image data
            data = {
                'name': filename,
                'format': image_format,
                'mime_type': mime_type,
                'size': image_size,
                'mode': image_mode,
                'exif': exif_data,
                'output_path': output_path
            }
            return data
    except Exception as e:
        return {"error": str(e)}
