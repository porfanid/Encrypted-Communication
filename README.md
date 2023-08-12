# Encrypted Communication

## How to use

In order to use this
1. Install all the requirements by running:
```bash
pip install -r requirements.txt
```
2. you are going to need a firebase acount that you can get [here](https://firebase.google.com).
1. You need to create a project there and enable the firestore database that can be found in the `All products` menu that can be found in the bottom left.
1. Then, you are going to have to create a service account and download the json credentials
> make sure that the service account has read/write access to the firestore.
5. Copy the json to the project root directory and rename the file to `personal-site-key.json`.
1. If ypu run the app, it should work correctly 

## About

This python script is a simple app that helps you communicate with your friends.

What it does is create a private and a public pgp key pair stored in the project root directory. This chat works based on your email addresses and the corresponding private key. If you do not have one of those, the app is useless. Even if someone knows your email address, he cannot see your messages.
