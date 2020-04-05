import logging


def log_func(__name__):

    format_code = (
        u'\n[%(filename)s] - [line№ %(lineno)d] - '
        u'[%(levelname)s], '
        u'[%(asctime)s] - %(message)s \n'
    )
    logging.basicConfig(filename='planer.log',
                        level=logging.INFO, format=format_code, filemode='a')
    # logger = logging.getLogger(__name__)
    # logger.setLevel(logging.INFO)

    # handler = logging.FileHandler(f'planer.log')
    # form = logging.Formatter(format_code)
    # handler.setFormatter(form)

    # logger.addHandler(handler)

    return logging
