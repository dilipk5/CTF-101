# Ticket

Description: 
Strike Bank recently discovered unusual activity in their customer portal. During a routine review of their Android app, several clues were uncovered.Your mission is to investigate the information available, explore the associated portal, and uncover the hidden flag.Everything you need is already out there! Connect the dots and complete the challenge.

The android package is `com.strikebank.netbanking` and the security review was conducted via `bevigil.com`.

Report can also be viewed by visiting the URL with the following format:
`https://bevigil.com/report/<package_name>`

We can look for the the report at https://bevigil.com/report/com.strikebank.netbanking

The bevigil tools gives a nice summary of scanning the app and getting some info about the app including some configs, assets and some creds stroed in the application.

Looking at the strings we have some usefull information about the app 

<img width="2048" height="729" alt="image" src="https://github.com/user-attachments/assets/830ecbca-ec94-4155-8741-ee12d751340b" />

There are some hardcoded creds and api keys inside the code.

```json
username: tuhin1729
password: 123456
google-api-key: AIzaSyD3fG5-xyz12345ABCDE67FGHIJKLmnopQ
encoded-jwt-secret: c3RyIWszYjRua0AxMDA5JXN1cDNyIXMzY3IzNw==
```

After looking some more there are some useful urls in the code

<img width="2048" height="292" alt="image" src="https://github.com/user-attachments/assets/7c89f225-c48d-4134-9671-1ce11ebcf46c" />

Going on the http://15.206.47.5.nip.io:8443/ we see a login page.

 

<img width="1266" height="563" alt="image" src="https://github.com/user-attachments/assets/e3de8edc-1d5d-4731-8b0f-739e59d12dfd" />

We can use the creds we found in the strings and use it to login 

<img width="1217" height="426" alt="image" src="https://github.com/user-attachments/assets/090edb3c-585b-4f44-b6d8-4f8555d511ea" />

<img width="1115" height="368" alt="image" src="https://github.com/user-attachments/assets/e0ea0086-f42f-4383-86ba-0de219acaf94" />

Looking at the request in the burp we can see it assigns jwt tokens, since we found the encoded jwt secret we can use this to sign a jwt token with the username of admin to login as admin on the site.

I used the tool jwt encoder from [jwt.io](http://jwt.io) to create a signed jwt token which we can use.

<img width="1091" height="629" alt="image" src="https://github.com/user-attachments/assets/5efc47a6-c668-4b04-b379-16b07d1fe73c" />

Now Editing the cookie and giving this token in the auth cookie, we log in as admin and this gives us our last flag.

<img width="1071" height="475" alt="image" src="https://github.com/user-attachments/assets/247958b8-c6ca-451b-b406-3f74d297f90d" />
