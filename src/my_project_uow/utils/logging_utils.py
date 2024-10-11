import logging.config
import sys


def configure_logging(
    *,
    root_level: str,
    uvicorn_level: str,
    project_level: str,
):
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'default': {
                'level': 'DEBUG',
                'formatter': 'default',
                'class': 'logging.StreamHandler',
                'stream': sys.stdout,
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': root_level,
                'propagate': True,
            },
            'uvicorn': {
                'handlers': ['default'],
                'level': uvicorn_level,
                'propagate': False,
            },
            'my_project': {
                'handlers': ['default'],
                'level': project_level,
                'propagate': False,
            }
        },
    }

    logging.config.dictConfig(config)
