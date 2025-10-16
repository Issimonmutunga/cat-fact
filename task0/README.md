# FastAPI Profile API

A lightweight RESTful API built with **FastAPI**, deployed on **Railway**, and integrated with the public [CatFact API](https://catfact.ninja/).  
It demonstrates external API consumption, JSON response formatting, and UTC timestamp handling.

---

## 🚀 Features
- Fetches random cat facts from an external API  
- Returns user profile metadata  
- Provides current UTC time in ISO 8601 format  
- Fully async using `httpx` and `FastAPI`

---

## 🧩 Stack
- **FastAPI** — web framework  
- **Python** — runtime  
- **HTTPX** — async HTTP client  
- **Uvicorn** — ASGI server  
- **Railway** — cloud hosting  
- **GitHub** — CI/CD integration  

---

## 🗂 Project Structure
- task0/
-   ├── main.py
-   ├── requirements.txt
-   └── Procfile

 
---

##  Installation & Local Run

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/<repo>.git
cd <repo>
```
2. Create a virtual environment and activate it:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the FastAPI server locally:
```bash
uvicorn main:app --reload
```
### Visit in your browser or Postman:
```arduino
http://127.0.0.1:8000/me
```
### (Optional) - Prevents getting a 404 on root. 
```python
# Add Endpoint
@app.get("/")
def root():
    return {"msg": "Welcome! Use /me to see my profile, time and cat fact."}
```

---

##  Deployment on Railway
1. Push your project to GitHub.
2. Go to [Railway App](https://railway.com/) and login
3. Click New Project → Deploy from GitHub Repo and select your repository
4. Railway automatically installs dependencies and runs the app using the Procfile:
```less
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```
5. Once deployed, your API is accessible at:
```arduino
https://<your-app>.up.railway.app/me
```

## Example Response
```json
{
  "status": "success",
  "user": {
    "email": "besimonmutunga@gmail.com",
    "name": "Simon Mutunga",
    "stack": [
      "FastAPI",
      "Python",
      "HTTPX",
      "Uvicorn",
      "Railway",
      "GitHub"
    ]
  },
  "timestamp": "2025-10-16T04:32:10+00:00",
  "fact": "Cats sleep for 70% of their lives."
}
```
---

## Notes
- The /me endpoint is asynchronous for better performance.
- You can replace the CatFact API with any external API for experimentation.
- Keep Procfile and requirements.txt in the project root — Railway needs them for deployment.
- Local testing URLs differ from Railway deployment URLs. Use /me for your main endpoint
