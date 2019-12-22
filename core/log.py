import time
import logging
import logging.config
from core.colors import blue_green,purple,red,green,blue,end


time = time.strftime('%Y-%m-%d %H:%M:%S')


def factory_logger(logger_type, target, formatter):

    if logger_type in ["StreamLogger", "STMPLogger"]:
        config = {
            'version': 1,
            'disable_existing_loggers': False,

            'formatters': {

                'url' : {
                    'format' : f'{green}[~][{time}] Collecting a target for testing : %(message)s{end}'
                },


                'subdomain' : {
                    'format' : f'{blue_green}[+][{time}] Collecting a subdomain : %(message)s{end}',
                },

                'subdomain_count' : {
                    'format' : f'{blue_green}[!][{time}] A total of %(message)s subdomains have been collected !{end}'
                },

                'proxy_generator' : {
                    'format' : f'{green}[*][{time}] Collecting a proxy : %(message)s{end}'
                },

                'middleware' : {
                    'format' : f'{blue}[#][{time}] [~]Middleware Information :\n[~]%(message)s{end}'
                },

                'Waf' : {
                    'format' : f'{green}[!]{time} [!] Waf Information :\n[!]%(message)s{end}'
                },

                "poc" : {
                    'format' : f'{red}[!]------------------------------------------------------\n'
                               f'[!][{time}] Middleware vulnerability found ！!\n%(message)s\n'
                               f'[!]------------------------------------------------------{end}'
                },

                'poc not found' : {
                    'format': f'{green}[!][{time}] Middleware vulnerability not found !\n[!][{time}] %(message)s\n{end}'
                },

                'vulnerable' : {
                    'format' : f'{red}[!][{time}] %(message)s{end}'
                }

            },


            'handlers': {

                'console': {
                    'class': 'logging.StreamHandler',
                    'level': 'DEBUG',
                    'formatter': f'{formatter}',
                },

                # 'vulnerable' : {
                #     'class' : 'lo'
                # },

                # 'stmp' : {
                #     'class' : 'logging.handlers.SMTPHandler',
                #     'level' : 'CRITICAL',
                #     'formatter' : 'vulnerable',
                #     'mailhost' : 'smtp.qq.com',
                #     'fromaddr' : '',
                #     'toaddrs' : '',
                #     'subject' : 'Cerberus found a vulranebility !',
                #     'credentials' : '()'
                #
                # }

            },

            'loggers':{

                'StreamLogger' : {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                },

                # 'STMPLogger' : {
                #
                #     'handlers': ['console','stmp'],
                #     'level': 'DEBUG',
                #
                # }

            }
        }

        logging.config.dictConfig(config)

    elif logger_type == "FileLogger":
        config_file = {
            'version': 1,
            'disable_existing_loggers': False,

            'formatters': {

                'url': {
                    'format': f'{green}[~][{time}] Collecting a target for testing : %(message)s{end}'
                },

                'subdomain': {
                    'format': f'{blue_green}[+][{time}] Collecting a subdomain : %(message)s{end}',
                },

                'subdomain_count': {
                    'format': f'{blue_green}[!][{time}] A total of %(message)s subdomains have been collected !{end}'
                },

                'proxy_generator': {
                    'format': f'{green}[*][{time}] Collecting a proxy : %(message)s{end}'
                },

                'middleware': {
                    'format': f'{blue}[#][{time}] [~]Middleware Information :\n[~]%(message)s{end}'
                },

                'Waf': {
                    'format': f'{green}[!]{time} [!] Waf Information :\n[!]%(message)s{end}'
                },

                "poc": {
                    'format': f'{red}[!]------------------------------------------------------\n'
                              f'[!][{time}] Middleware vulnerability found ！!\n%(message)s\n'
                              f'[!]------------------------------------------------------{end}'
                },

                'poc not found': {
                    'format': f'{green}[!][{time}] Middleware vulnerability not found !\n[!][{time}] %(message)s\n{end}'
                },

                'vulnerable': {
                    'format': f'{red}[!][{time}] %(message)s{end}'
                }

            },

            'handlers': {

                'console': {
                    'class': 'logging.StreamHandler',

                    'level': 'DEBUG',
                    'formatter': f'{formatter}',
                },

                'file': {
                    "class": "logging.FileHandler",
                    'level': 'DEBUG',
                    'formatter': f'{formatter}',
                    'filename': f'{time}_{target}_.txt',
                    'mode': 'a',
                },

                # 'stmp': {
                #     'class': 'logging.handlers.SMTPHandler',
                #     'level': 'CRITICAL',
                #     'formatter': 'vulnerable',
                #     'mailhost': 'localhost',
                #     'fromaddr': '',
                #     'toaddrs': '',
                #     'subject': 'Cerberus found a vulranebility !',
                #     'credentials': '()'
                #
                # }

            },

            'loggers': {
                'FileLogger' : {

                    'handlers': ['console','file'],
                    'level': 'DEBUG',
                },

                'STMPLogger': {

                    'handlers': ['console','stmp'],

                    'level': 'DEBUG',

                }

            }
        }
        logging.config.dictConfig(config_file)

    return logging.getLogger(logger_type)

