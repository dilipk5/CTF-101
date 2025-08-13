# Test in Prod

## Challenge Description

You've discovered a seemingly simple login portal for a company's internal tool. The developers have claimed it's secure, but rumor has it that there's a hidden admin API endpoint they forgot to secure. Can you find it and access the secret flag?

### **Step 1 – Initial Reconnaissance**

The login page itself didn’t reveal much functionality, and without valid credentials I couldn’t proceed further.

However, I opened the browser’s **View Source** option to inspect the HTML code.

### **Step 2 – Finding a Clue in the Source Code**

Inside an HTML comment, I found:

```
<!-- API Documentation: /api/v1 -->
```

This hinted that the application might have an accessible API under the `/api/v1` path.

<img width="616" height="135" alt="image" src="https://github.com/user-attachments/assets/9d0e4e5b-dcf8-43f3-878f-eb5247a39b64" />

### **Step 3 – Exploring the API**

Navigating to:

```
/api/v1
```

returned an empty or generic response, but it confirmed the API existed.

### **Step 4 – Endpoint Guessing & Enumeration**

Since APIs often have subpaths like `/admin`, `/users`, `/flag`, `/status`, etc., I began trying common names.

When I visited:

```jsx
/api/v1/flag
```

the server responded with the **flag** — no authentication required!

<img width="960" height="179" alt="image" src="https://github.com/user-attachments/assets/4815b04c-cd08-4019-b50c-0b0e20d21212" />

### **Vulnerability Explanation**

- The developers left a sensitive API endpoint (`/api/v1/flag`) exposed without authentication.
- This is a classic **Broken Access Control** vulnerability — sensitive routes must be restricted server-side.
- Leaving endpoint hints in HTML comments makes it even easier for attackers to discover.

---

### **Key Takeaways**

- Never leave sensitive endpoints accessible without proper authorization checks.
- Avoid leaving API documentation or hints in publicly served source code.
- Implement proper API authentication and role-based access control.
