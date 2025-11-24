# Photography Portfolio

Personal portfolio website for Adi Srinivasulu - ecologist, musician, and photographer.

## How to Update Gallery

### Automated (Recommended)
1. Add images to the `images/` folder
2. Commit and push to GitHub
3. GitHub Actions will automatically generate `gallery.json`
4. Your site updates automatically!

### Manual
1. Add images to the `images/` folder
2. Run: `pip install Pillow` (first time only)
3. Run: `python generate_gallery.py`
4. Commit and push both the images and `gallery.json`

## Local Development

1. Clone the repository
2. Open `index.html` in a browser (or use a local server)
3. Add images to `images/` folder
4. Run `python generate_gallery.py` to update gallery

## Customization

Edit `index.html` to update:
- Your name and tagline
- Social media links (Instagram, email)
- Colors and styling (in the `<style>` section)

## Supported Image Formats

JPG, JPEG, PNG, GIF, WebP

## License

All rights reserved.