
VERSION = "v0.6"
PYTHONVERSION = "3.9"
VERSIONTYPE = "UNSAFE"

INTERPRETER = []

DATAFOLDER = "DATA/"
DATAFOLDER2 = "DATA\\"

try:
    f = open(DATAFOLDER + "PACKSERVER.txt", "r")
    SERVERURL = f.read()
    f.close()
except Exception as e:
    print("Could not find file: " + DATAFOLDER + "PACKSERVER.txt \n\n" + str(e))
    print("This means KCLI does not know where to find extern packages!")
    input("Press enter to try to start KCLI anyway...")

ADDONS = ["HELP", "STARTTASKS", "UTIL", "IMPORT", "INSTALL", "UNINSTALL", "UPDATE", "-------"]


print("Starting...")
print("Loading Enviroment Packages...\n")

from rich.console import Console
print("Loading rich.console...")
console = Console()
console.log("[green]Console set up finished")

console.log("[yellow]Loading rich.print...")
from rich import print
console.log("[green]Print set up finished")

console.log("[yellow]Loading tkinter...")
from tkinter import *
from tkinter import messagebox
console.log("[green]Tkinter set up finished")

console.log("[yellow]Loading threading...")
import threading
console.log("[green]Threading set up finished")

console.log("[yellow]Loading functools...")
import functools
fp = functools.partial
console.log("[green]functools set up finished")

console.log("[yellow]Loading tkinter.ttk...")
import tkinter.ttk as ttk
console.log("[green]Tkinter.ttk set up finished")

console.log("[yellow]Loading os...")
import os
console.log("[green]os set up finished")
os.system("title KCLI-" + VERSION + "-py" + PYTHONVERSION)

console.log("[yellow]Loading requests...")
import requests
console.log("[green]requests set up finished")

console.log("[yellow]Loading shlex...")
import shlex
console.log("[green]Shlex set up finished")

console.log("[yellow]Loading zip...")
import zipfile
console.log("[green]Zip set up finished")

console.log("[yellow]Loading time...")
import time
console.log("[green]Time set up finished")

console.log("[yellow]Loading threading...")
import threading
console.log("[green]Threading set up finished")

print("\n")
print(""" **   **   ******  **       **
/**  **   **////**/**      /**
/** **   **    // /**      /**
/****   /**       /**      /**
/**/**  /**       /**      /**
/**//** //**    **/**      /**
/** //** //****** /********/**
//   //   //////  //////// //""")

print(f"[cyan] Welcome to KCLI version {VERSION} Type {VERSIONTYPE}\n")