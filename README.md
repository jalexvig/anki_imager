# Add images to Anki notes

Visual stimuli helps memory. This script will add the first image from a google search to each note in one of your Anki decks!

W/o Image                                                         | After
:----------------------------------------------------------------:|:-------------------------:
![Before](resources/anki_vocab_screenshot.png?raw=true "Before")  |  ![After](resources/anki_vocab_img_screenshot.png?raw=true "After")

## Installation

```
git clone https://github.com/jalexvig/anki_imager.git
cd anki_imager

python3 -m venv
source venv/bin/activate
pip install -r requirements.txt
```

## Setup

1. [Export a deck](https://apps.ankiweb.net/docs/manual.html#exporting-text) to a tab separated file in Anki. `anki_imager` will use the first column in this file to search for images.

## Usage

Supply the path to the notes file e.g.:

```
python -m anki_imager Vocab.txt
```

Most of the default options should be fine. You may need to supply the directory path for Anki media files (with `--dpath_anki`) if it is not in the default location.

Here is a full list of options:

```
usage: __main__.py [-h] [--dpath_anki DPATH_ANKI] [--num_imgs NUM_IMGS]
                   [--ignore_prev] [--num_words NUM_WORDS] [--tags]
                   [--suffix SUFFIX]
                   fpath_notes

positional arguments:
  fpath_notes           path to plain text notes to process

optional arguments:
  -h, --help            show this help message and exit
  --dpath_anki DPATH_ANKI
                        path to Anki's media collection directory
  --num_imgs NUM_IMGS   number of images per word to include
  --ignore_prev         ignore previously downloaded entries
  --num_words NUM_WORDS
                        number words to process
  --tags                keep tags as last column in new file
  --suffix SUFFIX       suffix to modify notes filename
```

## Finish

After you have run `anki_imager`:

1. Make a new [note type](https://apps.ankiweb.net/docs/manual.html#note-types) in Anki to support the extra image.
2. [Import](https://apps.ankiweb.net/docs/manual.html#importing-text-files) the newly created file into Anki. Make sure to check the "Allow HTML in fields" box.
