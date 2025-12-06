Description

Ready your scripts! Only automation will beat the clock and unlock the flag.

http://15.206.47.5:9090/

Going on the web page we get

<img width="868" height="478" alt="image" src="https://github.com/user-attachments/assets/3ffd56dc-cc05-4afb-b131-dfb47d3106f9" />



This explains what we have to do, so lets start building a python script

```json
#!/usr/bin/env python3

import requests
import base64
import re
from requests.exceptions import RequestException

BASE_URL = "http://15.206.47.5:9090"

def solve_challenge():
    
    session = requests.Session()
    
    try:
        # Step 1: GET the task
        print("[*] Fetching task from /task...")
        response = session.get(f"{BASE_URL}/task", timeout=5)
        
        if response.status_code != 200:
            print(f"[-] Failed to get task. Status: {response.status_code}")
            return False
        
        # Step 2: Extract the string from HTML
        match = re.search(r'Here is the input string: ([A-Za-z0-9]+)', response.text)
        if not match:
            print("[-] Could not extract string from response")
            print(f"Response: {response.text}")
            return False
        
        original_string = match.group(1)
        print(f"[+] Original string: {original_string}")
        
        # Step 3: Reverse the string
        reversed_string = original_string[::-1]
        print(f"[+] Reversed string: {reversed_string}")
        
        # Step 4: Base64 encode
        encoded = base64.b64encode(reversed_string.encode()).decode()
        print(f"[+] Base64 encoded: {encoded}")
        
        # Step 5: Wrap in required format
        payload = f"CSK__{encoded}__2025"
        print(f"[+] Final payload: {payload}")
        
        # Step 6: Submit immediately
        print("[*] Submitting to /submit...")
        submit_response = session.post(
            f"{BASE_URL}/submit",
            data={"answer": payload},
            timeout=5
        )
        
        print(f"\n[+] Response Status: {submit_response.status_code}")
        print(f"[+] Response Body:\n{submit_response.text}")
        
        # Check if we got the flag
        if "flag" in submit_response.text.lower() or submit_response.status_code == 200:
            print("\n[SUCCESS] Challenge solved!")
            return True
        else:
            print("\n[-] Challenge not solved yet")
            return False
            
    except RequestException as e:
        print(f"[-] Request error: {e}")
        return False
    except Exception as e:
        print(f"[-] Unexpected error: {e}")
        return False

if __name__ == "__main__":
    solve_challenge()
```

This was simple

1. Send a get request to /task to get the string and getting cookies to make a session which is used to track our payload and return flag
2. Perform regex to get the string
3. Reverse the string and then base64 encoded and made the payload.
4. Sending the answer to /submit which returns the flag.

<img width="1215" height="321" alt="image" src="https://github.com/user-attachments/assets/93cd5af3-42ff-4b56-87d0-cd762f22f6fc" />




