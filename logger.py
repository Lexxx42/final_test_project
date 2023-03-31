import logging

logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
    handlers=[
        logging.FileHandler(filename='./logs/tests.log', encoding='utf-8', mode='w'),
        logging.StreamHandler()],
    level=logging.INFO,
)
