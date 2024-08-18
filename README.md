# PyPlateX
High-Performance Scalable ANPR Package: Ready-to-Use, Simple, and Efficient License Plate Recognition

Unlock top-tier accuracy and scalability with cutting-edge ANPR solution **in 3 line of code**. Designed for seamless integration and ease of use, it delivers robust performance and reliability for all your license plate recognition needs.


[![Downloads](https://static.pepy.tech/personalized-badge/pyplatex?period=total&units=abbreviation&left_color=grey&right_color=yellow&left_text=Total-Downloads)](https://pepy.tech/project/pyplatex)
[![Supported Versions](https://img.shields.io/pypi/pyversions/pyplatex.svg)](https://pypi.org/project/pyplatex)
![GitHub](https://img.shields.io/github/license/nuhmanpk/pyplatex)
![PyPI](https://img.shields.io/pypi/v/pyplatex)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyplatex)
[![Downloads](https://static.pepy.tech/personalized-badge/pyplatex?period=week&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads/Week)](https://pepy.tech/project/pyplatex)
![PyPI - Format](https://img.shields.io/pypi/format/pyplatex)

## Simple ready to use ANPR 

**Note: The ANPR.detect function is asynchronous, so ensure you use the await keyword when calling it within an async function.**

### Install from pypi.org

```sh
pip install pyplatex
```

```py
from pyplatex import ANPR
anpr = ANPR()
det = await anpr.detect('./demo/plate-1.jpg')
print(det)
```
or

```py

from pyplatex import ANPR
import asyncio

async def main():
    anpr = ANPR()
    plates = await anpr.detect('./demo/plate-1.jpg')
    print(plates)

# Run the async main function
asyncio.run(main())

```
the output would be like

![https://github.com/nuhmanpk/pyplatex](https://raw.githubusercontent.com/nuhmanpk/PyPlateX/main/demo/plate-1.jpg)

```
{
    'is_plate': True, 
    'is_plate_confidence': 0.78, 
    'plate_number': 'MUN389', 
    'plate_number_confidence': 1.0
}
```
## Args for anpr.detect()

| Parameter        | Default Value | Description                                                                                   |
|------------------|---------------|-----------------------------------------------------------------------------------------------|
| `image_path`     | None          | Path to the image file to be processed.                                                       |
| `max_detections` | 1             | Maximum number of license plates to detect in the image.                                       |
| `confidence`     | 0.6           | Confidence threshold for detecting a license plate. Only detections with confidence above this value will be considered. |
| `save_image`     | False         | If True, the detected plate image will be saved to disk.                                        |
| `padding`        | 5             | Padding around the detected license plate when saving the image.                              |
| `folder_name`    | None          | Directory name where the detected images will be saved. If `save_image` is True, this folder will be created if it does not exist. |
| `use_ocr`        | True          | If True, Optical Character Recognition (OCR) will be performed on the detected license plates. |
| `return_tensor`  | False         | If True, returns the image tensor of the detected license plates.                              |
| `verbose`        | True          | If True, logs detailed information during processing.                                          |



### Dev TODO:
- [x] Release a Inital Version
- [x] Add a plate detection model
- [x] Read and detect Plates
- [x] Format output
- [x] Integrate Cv2filters
- [x] Change Cofidence to a round number
- [x] Add a ocr Model
- [x] Release a Initial Version
- [ ] Add a option to accept image as Tensor / numpy array
- [ ] Add auto filters tag
<!-- [ ] -->

**This is a pre-release version; there might be some bugs. If you encounter any issues or performance-related problems, please report them [here](https://github.com/nuhmanpk/pyplatex/issues). If you'd like to contribute to this project, you can create a pull request [here](https://github.com/nuhmanpk/pyplatex/pulls).**

**Warning: Use this pre-release with caution as it may still have unresolved issues.**

If you like this project, please consider giving it a star on [Github](https://github.com/nuhmanpk/pyplatex)! Your support is appreciated. If you want to contribute further, you can also sponsor the project through [GitHub Sponsors](https://github.com/sponsors/nuhmanpk). Every contribution helps improve and maintain the project for the community.

Happy Coding 🚀 ...
