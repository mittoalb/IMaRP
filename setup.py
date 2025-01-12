from setuptools import setup, find_packages

setup(
    name="IMaRP",
    version="0.1.0",
    description="A package for correcting image artifacts using deep learning.",
    author="Irina Gasilova",
    author_email="igasilova@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "numpy",
        "pillow",
        "imageio"
    ],
    python_requires=">=3.7",
)

