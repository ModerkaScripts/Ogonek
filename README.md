# Ogonek
An online library for hashing, licensing and protecting your programs, which includes homemade hashing algorithms and other useful functions. Made with love :3

## Usage
```py
# Imports the module
import ogonek

# Gets an IP address
print(ogonek.IP())

# Generates a key using an encryption password
print(ogonek.GreatwixEmerald(login : str, password : str))

# Generates a short hash for a string
print(ogonek.Stellar(hash : str))

# Generates a long hash for a string
print(ogonek.Lunar(hash : str))

# Hashes a string using other algorithms
print(ogonek.AzureHash(algo : str, data : str))

# If you have any questions regarding Plugins, contact ttwiz_z#2081.
```