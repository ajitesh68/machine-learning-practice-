#configuring logging


import logging

logging.basicConfig(#previously I have done the app.log setting so it wont work so you have to restart the kernel
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)