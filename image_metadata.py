import os
from PIL import Image, ExifTags, UnidentifiedImageError
import piexif

def metadata_extractor(file_path: str, check=False) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        img = Image.open(file_path)
    except UnidentifiedImageError:
        raise UnidentifiedImageError("Error: Cannot identify image file '{file_path}'/ file type is not supported.")
    exif = img._getexif()
    
    if not exif and not check:
        print("\033[94mNo EXIF metadata found.\033[0m")
        return {}
    
    exif_dict = {ExifTags.TAGS.get(k, k): v for k, v in exif.items()}
    return exif_dict

def clear_metadata(file_path: str, output_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        img = Image.open(file_path)
    except UnidentifiedImageError:
        raise UnidentifiedImageError("Error: Cannot identify image file '{file_path}'/ file type is not supported.")
    
    exif_data = img.info.get('exif')
    
    if not exif_data:
        print("\033[94mNo EXIF metadata found to clear.\033[0m")
        img.save(output_path)
        return
    
    exif_dict = piexif.load(exif_data)

    # Remove all metadata tags
    for ifd in ('0th', 'Exif', 'GPS', '1st', 'Interop'):
        exif_dict[ifd].clear()

    # Save the image with the new EXIF data
    exif_bytes = piexif.dump(exif_dict)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "jpeg", exif=exif_bytes)


if __name__ == "__main__":
    file_path = "/Users/mitz/Desktop/IMG_3794.jpeg"
    print("\033[94mOriginal metadata:\033[0m")
    metadata = metadata_extractor(file_path=file_path)
    for tag, value in metadata.items():
        print(f"\033[94m{tag}: {value}\033[0m")
    
    output_path = "/Users/mitz/Desktop/IMG_3794_modified.jpeg"
    clear_metadata(file_path, output_path)
    
    print("\033[94mModified metadata:\033[0m")
    modified_metadata = metadata_extractor(file_path=output_path)
    for tag, value in modified_metadata.items():
        print(f"\033[94m{tag}: {value}\033[0m")
