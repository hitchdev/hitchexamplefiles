from path import Path

asset_directory = Path(__file__).realpath().dirname()


jpeg_large = asset_directory / "jpeg_large.jpg"
jpeg_small = asset_directory / "jpeg_small.jpg"
pdf_one_page = asset_directory / "pdf_one_page.pdf"
png_large = asset_directory / "png_large.pdf"


__VERSION__ = "DEVELOPMENT_VERSION"
