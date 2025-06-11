Projet RESTful API

## 🔐 Differences Between HTTP and HTTPS

**The main difference between HTTP and HTTPS is security.**

| Feature           | HTTP                                      | HTTPS                                                  |
|-------------------|--------------------------------------------|---------------------------------------------------------|
| Data Security     | No encryption, data sent in plain text     | Data encrypted using SSL/TLS                           |
| Port              | 80                                         | 443                                                     |
| URL Prefix        | `http://`                                  | `https://`                                              |
| Server Identity   | Not verified                               | Verified with a digital certificate (SSL/TLS)           |
| Use Case          | Non-sensitive browsing                     | Sensitive data (logins, payments, personal info)        |

- **HTTP** (Hypertext Transfer Protocol) transmits data in plain text, so anyone intercepting the connection can read the information.
- **HTTPS** (Hypertext Transfer Protocol Secure) uses SSL/TLS encryption, which makes the data unreadable to third parties and protects it from tampering.

👉 Use **HTTPS** when dealing with sensitive data.  
👉 Use **HTTP** only for public or non-sensitive content.

---

## 📡 Four Common HTTP Methods

| Method | Description                                | When to Use                                             | Example                                                   |
|--------|--------------------------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| GET    | Retrieves a resource or list of resources  | To read a resource without modifying it                 | `GET /users` → list of users<br>`GET /users/1` → user 1 details |
| POST   | Creates a new resource                     | To submit new data                                      | `POST /users` with body `{ "name": "Alice" }`             |
| PUT    | Replaces an entire resource                | To update everything (missing fields will be deleted)   | `PUT /users/1` with `{ "name": "Bob" }`                   |
| PATCH  | Updates specific fields of a resource      | To modify only part of a resource                       | `PATCH /users/1` with `{ "name": "Bob" }`                 |

---

## 📬 Common HTTP Status Codes

| Code | Description                                     | Example Scenario                                                                 |
|------|-------------------------------------------------|----------------------------------------------------------------------------------|
| 200  | OK – Request was successful                     | The homepage loads correctly                                                     |
| 201  | Created – New resource successfully created     | A user signs up and the server responds with 201                                 | 
| 400  | Bad Request – Invalid or malformed request      | A form is submitted without a required field                                     |
| 401  | Unauthorized – Authentication required          | A user tries to access a private page without logging in                         |
| 404  | Not Found – The requested resource doesn’t exist| A user clicks on a broken or incorrect link                                      |

---

## 📦 Structure of an HTTP Request & Response (Example)

**HTTP Request (simplified):**


# curl Project: Interacting with APIs from the Command Line

## Background
curl is a command-line tool to transfer data using many protocols (HTTP, HTTPS, FTP, etc.). It is commonly used to test and debug REST APIs.

## Objectives
- Install curl and verify the installation.
- Use curl to make GET and POST requests.
- Understand how to use headers.
- Interpret the received JSON results.

## Steps Completed

### Installation
- Verified installation with `curl --version`: version 8.5.0 installed.

### Simple GET Request
```bash
curl https://jsonplaceholder.typicode.com/posts
Output: JSON array of posts, each post has userId, id, title, and body.

Fetching Headers
bash
Copier le code
curl -I https://jsonplaceholder.typicode.com/posts
Output: HTTP headers (status, content-type, etc.).

POST Request
bash
Copier le code
curl -X POST https://jsonplaceholder.typicode.com/posts \
     -H "Content-Type: application/json" \
     -d '{"title": "foo", "body": "bar", "userId": 1}'
Output: JSON confirmation with id 101.

Tips
Use -I to fetch only headers.

The -X flag allows changing the HTTP method.

The -d flag sends data in the request body.

Resources
Official curl documentation: https://curl.se/docs/

JSONPlaceholder API: https://jsonplaceholder.typicode.com/

Expected Output
curl --version
Upon running curl --version, you should see details about your installed version of curl, including supported protocols.
Example output includes the curl version number, supported protocols like HTTP, HTTPS, FTP, and libraries used.

Fetching posts from JSONPlaceholder
Fetching posts from JSONPlaceholder should provide a JSON output containing various posts, each having attributes like userId, id, title, and body.
The response is a JSON array of objects, representing posts.

Fetching only headers
Fetching only the headers of a request should give a concise output showing status codes and headers without the actual content.
This is typically done with the -I flag in curl.

Making a POST request
Making a POST request should yield a response from the server acknowledging the reception of the data.
For JSONPlaceholder, it typically returns the created post with an id of 101, since it simulates the creation but does not persist the new data.
