from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='dotplotlib', 
    version='0.1.3',  
    author='Justin Lee', 
    author_email='justinkhlee27@gmail.com',  
    description='A basic extension library for creating strip plots or dot charts w/ matplotlib + seaboard',  
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jl33-ai/dotplotlib',  
    packages=find_packages(),
    install_requires=[
        'pandas', 
        'matplotlib',
        'seaborn' 
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)
