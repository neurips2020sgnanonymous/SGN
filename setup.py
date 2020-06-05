from setuptools import setup, find_packages

setup(
	name='SGN',
	version='0.1',
	description='an implementation of SGN (stochastic Gauss-Newton method) for training neural networks',
	author='anonymous',
    url = '',
	author_email='neurips2020.sgn@gmail.com',
	license='MIT',
	packages=find_packages(),
	python_requires='>=3.6, <=3.7',
    scripts = ['scripts/conv_net.py', 'scripts/mlp.py'],
	install_requires=['theano==1.0.4', 'numpy', 'scipy', 'tensorflow>=1.12.0', 'keras>=2.2.4'],
	keywords=['Gauss-Newton', 'Hessian-free', 'optimization', 'neural networks'],
)
