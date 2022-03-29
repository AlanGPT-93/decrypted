import gnupg # IMPORTANT: It's necessary to insatll this library as follows:
# In the terminal type: pip install python-gnupg
# Info https://gnupg.readthedocs.io/en/latest/



gpg = gnupg.GPG("gpg") # The first argument is the name of the GnuPG executable.


location = "C:/Users/...." # encrypted files directory
file_name = "Probando.txt.gpg" #OrderActivity_OMC_2022-03-17.xlsx.gpg" # file's name
data = f"{location}/{file_name}"

with open(data, "rb") as f:
	   status = gpg.decrypt_file(f, passphrase="pass",
	   output = f"{location}/{file_name.replace('.gpg','')}")

print("ok: ", status.ok)
print("status: ", status.status)
#print("stderr: ", status.stderr)
