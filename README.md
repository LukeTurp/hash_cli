# hash_cli
command line interface that outputs the sha256 hash of any specified file path on the local file system

## Client Interface Utilizing HashAPI to store output of hash_cli in MongoDB

#### Description:
The hash_cli takes a specified file path, and hashes the content of all files in all directories and subdirectories from specified file path.
The hash_cli has been configured to perform as a Http Client, utilizing HashAPI to store the values of the files and their hash values in a MongoDB for later comparison.


## Getting Started

#### Please Refer to [flask-rest-api ReadMe](https://github.com/LukeTurp/flask-rest-api/blob/develop/README.md)
- Register your hash_cli as an authorized user for use with HashAPI.
- Ensure the HashAPI server is connected to MongoDB and running.
- Test connection to HashAPI below, inserting your own specified scheme, host, and port:
```
curl -X "GET" http://127.0.0.1:8000/
{ "result": "success" }
```

Navigate to hash_cli repository in your command line:
```
cd ~/path/to/repository
```

###Arguments to include:
- -p --path : absolute file path specifying the start point of files to hash.
- -s --scheme : possible values are 'http' or 'https'.
- -a --host : IP address hosting HashAPI.
- -d --port : network port of HashAPI service.
- -r --api_version : specified version, currently on version 1.
- -u --api_user : username for HashAPI.
- -w --api_password : password for HashAPI.

Example input below:
```
python3 run.py -p /file/hash/path/to/begin -s http -a 127.0.0.1 -d 8000 -r 1 -u username -w password
```
