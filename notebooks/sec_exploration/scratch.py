"""Usage:

MAGICK_HOME=/opt/homebrew/opt/imagemagick python notebooks/sec_exploration/scratch.py
"""

from wand.image import Image
from pathlib import Path


def convert_to_tiff(pdf_path: str, tif_path: str):
    with Image(filename=pdf_path) as img:
        img.format = "tiff"
        img.transform_colorspace('gray')
        img.resolution = (200, 200)
        img.compression = "lzma"
        img.compression_quality = 99
        img.save(filename=tif_path)
        breakpoint()

    print("done!")





def main():
    data_dir = Path("../data/2023q1")
    aig_report = "aig-20230329"
    pdf_path = data_dir / f"{aig_report}.pdf"
    tif_path = data_dir / f"{aig_report}.tif"
    convert_to_tiff(pdf_path, tif_path)


if __name__ == "__main__":
    main()
