LOGGING = {  # DictConfig schema: https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema
    'version': 1,  # Versão do schema atual
    'disable_existing_loggers': False,  # Django possui alguns loggers por padrão (request, ORM, etc.)
    'formatters': {  # Como o conteúdo do log deve ser exibido/escrito
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'  # -<número>s : espaçamento
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {  # Classes que sabem manipular o log – console (stdout)/arquivo de texto
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'app.log'  # Onde o arquivo de log vai ser salvo
        }
    },
    'loggers': {
        '': {  # '' representa o logger "raíz" (root). Todos "loggers" herdarão dele.
            'level': 'WARN',
            'handlers': ['console', 'file']
        }
    }
}