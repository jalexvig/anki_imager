import os
import os.path as osp
import shutil

import pandas as pd
from google_images_download import google_images_download

# SETTINGS
DPATH_ANKI = osp.join(osp.expanduser('~'), '.local/share/Anki2/User 1/collection.media/')
DNAME_IMAGES = 'downloads'
REQUEST_DELAY = 0


def process_notes_file(fpath,
                       dpath_anki_media=DPATH_ANKI,
                       num_imgs=1,
                       resume=True,
                       num_words=None,
                       tags=False,
                       suffix='_mod'):

    df = _read_notes_file(fpath)

    download_images(df, num_words, resume, num_imgs)

    _process_images(df, dpath_anki_media)

    _save_updates_notes(df, fpath, tags, suffix)


def _save_updates_notes(df,
                        fpath,
                        tags,
                        suffix):

    fpath_mod = suffix.join(osp.splitext(fpath))

    if tags:
        cols = df.columns.tolist()
        cols = cols[:-2] + cols[:-3:-1]
        df = df[cols]

    df.to_csv(fpath_mod, sep='\t', header=False)


def _read_notes_file(fpath):

    df = pd.read_csv(fpath, header=None, sep='\t').set_index(0)

    return df


def _process_images(df,
                    dpath_anki):

    df['imgs'] = None

    for root, dnames, fnames in os.walk(DNAME_IMAGES):

        if osp.split(root)[-1] == DNAME_IMAGES:
            continue

        fnames_new = []
        word = osp.split(root)[-1]
        for i, fname in enumerate(fnames):
            fext = osp.splitext(fname)[-1]
            fname_word_new = 'vocab_{}_{}{}'.format(word, i, fext)
            shutil.copy2(osp.join(root, fname), osp.join(dpath_anki, fname_word_new))
            fnames_new.append(fname_word_new)

        img_str = '<br><br>'.join(["<img src='{}'/>".format(fname) for fname in fnames_new])
        df.loc[word, 'imgs'] = img_str


def download_images(df,
                    num_words,
                    resume,
                    num_imgs):

    paths_dict = {}

    for word in df.index[:num_words]:

        # Skip previously downloaded
        if resume and word in os.listdir(DNAME_IMAGES) and os.listdir(osp.join(DNAME_IMAGES, word)):
            continue

        response = google_images_download.googleimagesdownload()

        # google_images_download uses csv for separate searches so replace with spaces
        word_ = word.replace(',', ' ')
        kwargs = {"keywords": word_, "limit": num_imgs, 'delay': REQUEST_DELAY, 'image_directory': word}

        paths = response.download(kwargs)
        paths_dict.update(paths)

    return paths_dict
