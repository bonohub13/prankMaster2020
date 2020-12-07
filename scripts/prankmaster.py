#!/usr/bin/python3

import platform
from random import randint
from os import system
import pathlib

class PrankMaster:
    def __init__(self, debug: bool=False):
        os = platform.system()
        self.os = "Mac" if "Darwin" in os else "Windows" if "Windows" in os else "Linux"
        self.urls = []
        filepath = str(pathlib.Path(__file__).parent.absolute())
        if self.os == "Windows":
            filepath += "\\"
        else:
            filepath += "/"
        with open(f"{filepath}database.txt", "r") as data:
            for url in data.readlines():
                if url != "":
                    if "\n" in url:
                        self.urls.append(url[:-1])
                    else:
                        self.urls.append(url)
        self.command = {
            "Linux"  : f"firefox {self.urlPicker()}",
            "Mac"    : f"open -a Safari {self.urlPicker()}",
            "Windows": f"start msedge {self.urlPicker()}"
        }

    def urlPicker(self) -> str:
        fibonacci_random = [0, 1]
        while len(fibonacci_random) < 100:
            fibonacci_random.append(fibonacci_random[-2] + fibonacci_random[-1])
        random = fibonacci_random[randint(0, len(fibonacci_random))]*fibonacci_random[randint(0, len(fibonacci_random))]//fibonacci_random[randint(0, len(fibonacci_random))]%len(self.urls)
        
        return self.urls[random]
    
    def run(self):
        system(self.command[self.os])

if "main" in __name__:
    prank = PrankMaster()
    prank.run()