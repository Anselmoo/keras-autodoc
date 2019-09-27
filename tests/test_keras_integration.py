from keras_autodoc.autogen import generate
from docs.autogen import keras_dir
from docs.structure import PAGES
import shutil
import os

from pathlib import Path

def make_keras_docs(dest_dir):
    dest_dir = Path(dest_dir)
    template_dir = keras_dir / 'docs' / 'templates'
    generate(dest_dir, template_dir, PAGES, keras_dir / 'examples')
    readme = (keras_dir / 'README.md').read_text()
    index = (template_dir / 'index.md').read_text()
    index = index.replace('{{autogenerated}}', readme[readme.find('##'):])
    (dest_dir / 'index.md').write_text(index, encoding='utf-8')
    shutil.copyfile(keras_dir / 'CONTRIBUTING.md', dest_dir / 'contributing.md')


def test_docs_in_custom_destination_dir(tmpdir):
    make_keras_docs(tmpdir)
    tmpdir = Path(tmpdir)
    assert (tmpdir / 'layers').is_dir()
    assert (tmpdir / 'models').is_dir()
    assert (tmpdir / 'examples').is_dir()
    assert 'for easy and fast' in (tmpdir / 'index.md').read_text()
    assert os.listdir(tmpdir / 'examples')