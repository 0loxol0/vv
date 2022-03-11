import os

if __name__ == "__main__":
   try:
       os.system("cd")
       __import__("roybrute").moch_yayan()
   except Exception as e:
       exit(str(e))