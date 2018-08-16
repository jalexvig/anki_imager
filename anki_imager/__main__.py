import argparse
import inspect

from .add_images import process_notes_file


def parse_args():

    argspec = inspect.getfullargspec(process_notes_file)

    defaults = dict(zip(reversed(argspec.args), reversed(argspec.defaults)))

    parser = argparse.ArgumentParser()
    parser.add_argument('fpath_notes', help='path to plain text notes to process')
    parser.add_argument('--dpath_anki', default=defaults['dpath_anki_media'],
                        help='path to Anki\'s media collection directory')
    parser.add_argument('--num_imgs', default=defaults['num_imgs'], type=int,
                        help='number of images per word to include')
    parser.add_argument('--ignore_prev', action='store_true', help='ignore previously downloaded entries')
    parser.add_argument('--num_words', default=defaults['num_words'], help='number words to process')
    parser.add_argument('--tags', action='store_true', help='keep tags as last column in new file')
    parser.add_argument('--suffix', default=defaults['suffix'], help='suffix to modify notes filename')

    args = parser.parse_args()

    return args


if __name__ == '__main__':

    args = parse_args()

    process_notes_file(
        args.fpath_notes,
        args.dpath_anki,
        args.num_imgs,
        not args.ignore_prev,
        args.num_words,
        args.tags,
        args.suffix)
