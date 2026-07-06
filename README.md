# 🎨 ASCII Art Drawing Tool

A Python command-line tool that converts shapes, text, or images into ASCII art — drawn straight into your terminal.

## Features

- ✏️ Draw basic shapes (lines, rectangles, circles, triangles) using ASCII characters
- 🔤 Render text as large ASCII banners
- 🖼️ Convert images into ASCII art (optional, if image support is included)
- ⚙️ Customizable characters, size, and density
- 💻 Runs entirely in the terminal — no external GUI needed

## Demo

```
*
* *
*   *
*     *
* * * * *
```
<!-- Replace with an actual output sample from your program -->

## Tech Stack

- **Python 3.x**
- **Pillow (PIL)** — for image-to-ASCII conversion *(if applicable)*
- **argparse** — for command-line options *(if applicable)*

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/anshikaaaasingh-afk/ascii-art.git
   cd ascii-art
   ```

2. Install dependencies (if any)
   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the program
   ```bash
   python3 ascii_art.py
   ```

## Usage

Run the script and follow the prompts, or pass arguments directly:

```bash
python3 ascii_art.py --shape triangle --size 5
python3 ascii_art.py --text "HELLO"
python3 ascii_art.py --image photo.jpg --width 100
```

| Option    | Description                          |
|-----------|---------------------------------------|
| `--shape` | Shape to draw (line, square, circle, triangle) |
| `--size`  | Size of the shape                     |
| `--text`  | Text to render as ASCII banner        |
| `--image` | Path to image for ASCII conversion    |
| `--width` | Output width in characters            |

## Project Structure

```
ascii-art/
├── ascii_art.py        # Main program
├── shapes.py            # Shape-drawing functions
├── requirements.txt
└── README.md
```

## Future Improvements

- [ ] Color/ANSI support for terminal output
- [ ] Save output to a `.txt` file
- [ ] More shape types (polygons, stars)
- [ ] Adjustable brightness/contrast for image conversion
- [ ] Web-based version

## License

This project is licensed under the MIT License.

## Author

**Anshika Singh**
GitHub: [@anshikaaaasingh-afk](https://github.com/anshikaaaasingh-afk)
