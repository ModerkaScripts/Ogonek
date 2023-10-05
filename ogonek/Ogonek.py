# MIT License

# Copyright (c) 2023 ttwiz_z

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from sys import setrecursionlimit
from requests import get

setrecursionlimit(5000)

endpoint = "https://moderkascripts.000webhostapp.com/"

def IP():
    try:
        response = get(endpoint + "IP.php")
        return response.text
    except:
        return IP()

def GreatwixEmerald(login : str, password : str):
    try:
        response = get(
            endpoint + "GreatwixEmerald.php",
            params = {"login" : login, "password" : password}
        )
        return response.text
    except:
        return GreatwixEmerald(login, password)

def Stellar(hash : str):
    try:
        response = get(
            endpoint + "Stellar.php",
            params = {"hash" : hash}
        )
        return response.text
    except:
        return Stellar(hash)
    
def Lunar(hash : str):
    try:
        response = get(
            endpoint + "Lunar.php",
            params = {"hash" : hash}
        )
        return response.text
    except:
        return Lunar(hash)

def AzureHash(algo : str, data : str):
    try:
        response = get(
            endpoint + "AzureHash.php",
            params = {"algo" : algo, "data" : data}
        )
        return response.text
    except:
        return AzureHash(algo, data)