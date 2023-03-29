#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import sys

# pip3 install pyYaml
import yaml


class Rgb:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        rHex = format(self.r, 'x').zfill(2)
        gHex = format(self.g, 'x').zfill(2)
        bHex = format(self.b, 'x').zfill(2)
        return rHex + gHex + bHex

    def String(self) -> str:
        return self.__str__()

    def __repr__(self) -> str:
        return self.__str__()


def main(argv):
    # logging.basicConfig(filename='test.log', level=logging.DEBUG)
    logging.basicConfig(level=logging.DEBUG)

    colors = []
    colors.append(Rgb(0, 0, 0))
    colors.append(Rgb(255, 255, 255))
    colors.append(Rgb(255, 0, 0))
    colors.append(Rgb(0, 255, 0))

    data = {
        "colors": colors
    }

    data1 = {
        "color": Rgb(0, 0, 0)
    }

    # yaml.dump(data, open('test.yaml', 'w'), default_flow_style=False)
    logging.info("test array")
    yaml.dump(data, sys.stdout, default_flow_style=False)

    logging.info("test object")
    yaml.dump(data1, sys.stdout, default_flow_style=False)


if __name__ == "__main__":
    main(sys.argv[1:])
