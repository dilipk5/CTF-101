# Triangle

Description:

The system guards its secrets behind a username, a password, and three sequential verification steps.Only those who truly understand how the application works will pass all three.Explore carefully.Look for what others overlooked.Break the Trinity and claim the flag.

[http://15.206.47.5:8080](http://15.206.47.5:8080/)

After going to the web page it returns a web page with a login form,

<img width="1707" height="1169" alt="image" src="https://github.com/user-attachments/assets/d6c0ef89-1a16-4755-8538-2f2afe8bd88d" />

Looking at the page source there is a comment saying 

```bash
<!-- Dev team 2: TODO: Implement google2fa.php for auth and don't forget to clean up the bak files post debugging before release  -->
```

It says there are some .bak files which were for debugging purposes.This gives us a hint that there are some .bak files which we can look out.

Since the comment it self is saying google2fa.php we can try for google2fa.php.bak, and this returns some php code 

 

<img width="1238" height="464" alt="image" src="https://github.com/user-attachments/assets/2b53c1e0-f326-41d3-9bf9-84539e057f27" />

I looked more deep and started figuring out what it is doing  and figured out this code is responsible for generating the otp.

But we cannot predict the next otp because it is generating throught a key which is not present here.

After this i looked for login.php.bak file and this gaver me the php code for login page 

<img width="1239" height="726" alt="image" src="https://github.com/user-attachments/assets/ba64b342-aef4-409e-ab2d-6a77d12abf44" />

Now , see at the lone 27-29 it is generating a secret key, after reading the code more and searching things on google. This page is generating the secret key every time the a request is being send, this make it mathematically impossible to use this functionality.

So i make me feel there must another way to bypass this, looking at the if statements it looked the conditional implementation is bad. It have a classic validation issue in PHP.

```bash
if (isset($_DATA['username'])) {
    
    if (!isset($USER_DB[$_DATA['username']])) {
        json_die('wrong username', 'username');
    }

    $user_data = $USER_DB[$_DATA['username']];

    if (!password_verify($_DATA['password'], $user_data['password_hash'])) {
        json_die('wrong password', 'password');
    }

    if (!Google2FA::verify_key($user_data['key1'], $_DATA['otp1'])) {
        json_die('wrong otp1', 'otp1');
    }
    if (!Google2FA::verify_key($user_data['key2'], $_DATA['otp2'])) {
        json_die('wrong otp2', 'otp2');
    }
    if (!Google2FA::verify_key($user_data['key3'], $_DATA['otp3'])) {
        json_die('wrong otp3', 'otp3');
    }

    json_response("Flag: " . $FLAG);
}
```

And send a request with boolean value true can be used to bypass.

<img width="1047" height="381" alt="image" src="https://github.com/user-attachments/assets/d7885cba-8583-4714-8164-39e59b079ad2" />

Here in the code it takes the user input directly and then validate it, here we can send a boolean value and it takes the value as it is and perform the checking which results as true.

```bash
Google2FA::verify_key($user_data['key1'], true)
```

This returns true and since the overall condition which is 

```bash
if (!Google2FA::verify_key($user_data['key1'], $_DATA['otp1'])) {
        json_die('wrong otp1', 'otp1');
    }
```

When we send `"otp1": true`:

1. `Google2FA::verify_key($user_data['key1'], true)` **returns `true`**
2. The condition becomes: `if (!true)` → `if (false)`
3. Since the condition is **false**, the code **skips the `json_die()` call**
4. Execution continues to the next check

Using this this we skip all the 3 if statements and finally the flag is returned.
