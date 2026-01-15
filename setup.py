from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if (('.png' not in x) and ('.gif' not in x))]
long_description = ''.join(lines)

setup(
    name="robomimic",
    packages=[
        package for package in find_packages() if package.startswith("robomimic")
    ],
    install_requires=[
        "numpy==1.23.3",
        "h5py==3.15.1",
        "psutil==7.2.1",
        "tqdm==4.67.1",
        "termcolor==3.3.0",
        "tensorboard==2.20.0",
        "tensorboardX",
        "imageio",
        "imageio-ffmpeg",
        "matplotlib==3.10.8",
        #"egl_probe>=1.0.1",
        "torch==2.0.1",
        "torchvision==0.15.2",
        "diffusers==0.11.1",
        "tianshou==0.4.10",
        # Pinned for diffusion policy compatibility
        "huggingface_hub==0.17.0",
        "transformers==4.25.0",
        "tokenizers==0.13.3",
        "wandb==0.24.0",
    ],
    eager_resources=['*'],
    include_package_data=True,
    python_requires='>=3',
    description="robomimic: A Modular Framework for Robot Learning from Demonstration",
    author="Ajay Mandlekar, Danfei Xu, Josiah Wong, Soroush Nasiriany, Chen Wang",
    url="https://github.com/ARISE-Initiative/robomimic",
    author_email="amandlek@cs.stanford.edu",
    version="0.3.0",
    long_description=long_description,
    long_description_content_type='text/markdown'
)
