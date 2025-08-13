# 1. Robots Secrets
## Challenge Description

Welcome to our humble website! We're just getting started and are trying to keep some parts of our site private from search engines. Can you find anything interesting we might have overlooked?

### **Step 1 – Checking `robots.txt`**

Since the challenge talks about keeping content away from search engines, my first step was to check:

In the file, I found the following entry:

```
User-agent: *
Disallow: /hidden_area_for_bots
```

This tells search engines not to index /hidden_area_for_bots, but it doesn’t stop anyone from visiting it directly

<img width="950" height="96" alt="image" src="https://github.com/user-attachments/assets/6530e7f6-a750-475e-802a-596a92d482ee" />


Upon visiting, I was greeted with a page containing the **flag**.
<img width="1141" height="276" alt="image" src="https://github.com/user-attachments/assets/4544f319-e1bb-4525-a34f-5aacb4c16eae" />

