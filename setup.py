import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='lunarsats',
    author='Clay Hoover',
    author_email='choover8@gatech.edu',
    description='Really flat sats, but around the Moon!',
    keywords='paddlesats,cislunar',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/choover1410/lunarsats',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
