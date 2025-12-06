# Bad Feedback

Description: 

A company rolled out a shiny feedback form and insists their customers are completely trustworthy. Every feedback is accepted at face value, no questions asked. What can go wrong?

Flag is in the root.

[http://15.206.47.5:5000](http://15.206.47.5:5000/)

After visiting the home page a simple feedback form is present which asks for name and message.

<img width="847" height="485" alt="image" src="https://github.com/user-attachments/assets/5f1f6ad2-ded7-4c46-9186-4e451bd1728b" />

Submitting the form returns

<img width="519" height="290" alt="image" src="https://github.com/user-attachments/assets/3cbe42a4-2234-4f42-967b-4267ed61f2eb" />

There is nothing more in this, since this is  a python application the first thing came to my mind is ssti(server side template injection), we can try to exploit ssti if a templating engine is processing the user data.But there is nothing much happening  here.

After looking at the request that is being send using burpsuite.

<img width="1246" height="554" alt="image" src="https://github.com/user-attachments/assets/ba65680c-04b6-4c47-af76-89c31e371d81" />

It is sending the data in xml format, seeing this the first things came in my mind is trying xxe injection to  read some local files and also given in the challenge description(flag is in the root) we can send a request which loads the /flag.txt and returns us to the webpage.

<img width="1242" height="614" alt="image" src="https://github.com/user-attachments/assets/a4db6104-79a2-4387-8ded-6cdfe0515dbf" />

```bash
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root[
<!ENTITY xxe SYSTEM "file:///flag.txt"> 
]>
<feedback>
    <name>&xxe;</name>
    <message>test</message>
</feedback>
```

This payload is just trying to load a system file flag.txt and storing it in a variable named xxe, since the web page returns the user input which we send through the post data we can call the variable in one of the fields and here we called it in the name.

And this gives us our flag.
