'''
Programm entry point.
Set log format,
parse config and run bot, also
set messages and commands handlers
'''
import json
import logging
import argparse


def getPathToCfg():
    '''create argument parser and try get config path. If can't get
    return default value cfg.json. If user wait help message print it
    and exit program'''
    parser = argparse.ArgumentParser(
        description='Run "ssh" bot. Allows send cli commands in telegram ' +
                    'and seen standart output.')
    parser.add_argument(
        '-c', '--config', dest='config', type=str, nargs='?',
        help='contains path to config file (default cfg.json)',
        default='cfg.json'
    )
    args = parser.parse_args()
    return args.config


def main():
    '''programm entry point'''
    cfgPath = getPathToCfg()

    # set log output format in json
    logging.basicConfig(
        format='{ "time": "%(asctime)s",  "level": "%(levelname)s", ' +
               '"msg": "%(message)s" }', level=logging.INFO)

    logging.info('cfgPath = ' + cfgPath)


if __name__ == "__main__":
    main()
