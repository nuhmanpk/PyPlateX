# PyPlateX
A scalable and versatile ANPR package leveraging YOLO for detection and multiple OCR options to accurately recognize license plates.


[![Downloads](https://static.pepy.tech/personalized-badge/pyplatex?period=total&units=abbreviation&left_color=grey&right_color=yellow&left_text=Total-Downloads)](https://pepy.tech/project/pyplatex)
[![Supported Versions](https://img.shields.io/pypi/pyversions/pyplatex.svg)](https://pypi.org/project/pyplatex)
![GitHub](https://img.shields.io/github/license/nuhmanpk/pyplatex)
![PyPI](https://img.shields.io/pypi/v/pyplatex)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyplatex)
[![Downloads](https://static.pepy.tech/personalized-badge/pyplatex?period=week&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads/Week)](https://pepy.tech/project/pyplatex)
![PyPI - Format](https://img.shields.io/pypi/format/pyplatex)

## Simple ready to use ANPR 

**Note: The ANPR.detect function is asynchronous, so ensure you use the await keyword when calling it within an async function.**

```py
from pyplatex import ANPR
anpr = ANPR()
det = await anpr.detect('/content/Car plate 24622490.jpg',save_image=True)
print(det)
```
or

```py

from pyplatex import ANPR
import asyncio

async def main():
    anpr = ANPR()
    plates = await anpr.detect('./typesofcarnumberplates-02-01.jpg', save_image=True)
    print(plates)

# Run the async main function
asyncio.run(main())

```
the output would be like

```
{
    'detected': True, 
    'confidence': array(    0.74661, dtype=float32), 
    'saved_path': 'detected_plates/cropped_plate_20240714_145500.jpg'
}
```


### Dev TODO:
- [x] Release a Inital Version
- [x] Add a plate detection model
- [x] Read and detect Plates
- [x] Format output
- [x] Integrate Cv2filters
- [ ] Change Cofidence to a round number
- [ ] Add a option to accept image as Tensor / numpy array
- [ ] Add a ocr Model
- [ ] Add auto filters tag
- [ ] Add More custom filters
<!-- [ ] -->



### NOTE
Still cooking in the kitchen—don’t worry, we’ll let you know when it’s done and ready to serve! 🍳 

Happy Coding 🚀 ...
