from setuptools import setup, find_packages

setup(name='django-imageresize',
      version='0.1.8',
      description='Adds the possibility to scale images on server side using imagemagick',
      author=['Tobias Hasselrot', 'Daniel Hasselrot', 'William Sporrong'],
      author_email='tobias.hasselrot@gmail.com',
      url='',
      download_url='http://github.com/mewantit/django-imageresize/',
      package_dir={'django-imageresize': 'django-imageresize'},
      packages = find_packages(),
      package_data={},
      zip_safe=False,
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
