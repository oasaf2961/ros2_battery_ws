from setuptools import find_packages, setup
from glob import glob
import os
package_name = 'battery_odev'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oasaf_2961',
    maintainer_email='omerasaf2961@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
	    'battery_node = battery_odev.battery_node:main',
	    'monitor_node = battery_odev.monitor_node:main',
        ],
    },
)
