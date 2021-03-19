
VERSION = "v0.2"
VERSIONTYPE = "UNSAFE"

INTERPRETER = []

DATAFOLDER = "DATA/"
DATAFOLDER2 = "DATA\\"

SERVERURL = "http://k.kundv.org/downloads/KCLI_PACKAGES/"

ADDONS = ["HELP", "STARTTASKS", "UTIL", "IMPORT", "INSTALL", "UNINSTALL", "UPDATE"]


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
console.log("[green]Tkinter set up finished")

console.log("[yellow]Loading tkinter.ttk...")
import tkinter.ttk as ttk
console.log("[green]Tkinter.ttk set up finished")

console.log("[yellow]Loading os...")
import os
console.log("[green]os set up finished")

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