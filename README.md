# 📰 News Project

**News Project** — Django framework yordamida yaratilgan yangiliklar web-ilovasi. Loyiha orqali yangiliklarni ko‘rish, yangi post yaratish, mavjud postlarni tahrirlash va o‘chirish mumkin.

## 🚀 Demo

🌐 **Live:** https://newsproject-jpw8.onrender.com/

## ✨ Imkoniyatlar

- 📰 Yangiliklar ro‘yxatini ko‘rish
- 📄 Alohida yangilik sahifasini ochish
- ➕ Yangi post qo‘shish
- ✏️ Postni tahrirlash
- 🗑️ Postni o‘chirish
- 🎨 CSS yordamida sahifalarni stillash
- 🔐 Django Admin panelidan foydalanish
- 📱 Django Templates orqali dinamik sahifalar
- ☁️ Render platformasiga deploy qilish

## 🛠️ Texnologiyalar

- **Python 3.14**
- **Django 6.1.1**
- **SQLite**
- **HTML5**
- **CSS3**
- **Gunicorn**
- **Render**

## 📁 Loyiha tuzilishi

```text
newsProject/
│
├── config/             # Django project konfiguratsiyasi
│
├── news/               # Yangiliklar uchun asosiy application
│
├── templates/          # HTML template fayllari
│
├── static/
│   └── styles/         # CSS fayllar
│
├── manage.py           # Django boshqaruv fayli
├── requirements.txt    # Python dependency'lar
├── Pipfile
├── Pipfile.lock
├── Procfile            # Deployment konfiguratsiyasi
└── db.sqlite3          # SQLite ma'lumotlar bazasi
```

## ⚙️ O‘rnatish

### 1. Repository'ni clone qilish

```bash
git clone https://github.com/Abdumomin07/newsProject.git
cd newsProject
```

### 2. Virtual environment yaratish

```bash
python -m venv venv
```

Virtual environment'ni ishga tushirish:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Kerakli paketlarni o‘rnatish

```bash
pip install -r requirements.txt
```

### 4. Database migratsiyalarini bajarish

```bash
python manage.py migrate
```

### 5. Development serverni ishga tushirish

```bash
python manage.py runserver
```

Keyin brauzerda:

```text
http://127.0.0.1:8000/
```

manzilini ochish mumkin.

## 🔑 Django Admin

Admin panelga kirish:

```text
http://127.0.0.1:8000/admin/
```

Superuser yaratish:

```bash
python manage.py createsuperuser
```

Keyin berilgan login va parol orqali admin panelga kirish mumkin.

## ☁️ Deployment

Loyiha **Render** platformasiga deploy qilish uchun sozlangan.

Production server sifatida **Gunicorn** ishlatiladi:

```bash
gunicorn config.wsgi:application --log-file -
```

Deployment uchun `Procfile` ham mavjud.

## 📦 Dependencies

Asosiy paketlar:

```text
Django==6.1.1
gunicorn==26.2.0
asgiref==3.12.1
sqlparse==0.6.0
tzdata==2026.4
```

Loyiha Python 3.14 bilan sozlangan.

## 👨‍💻 Muallif

**Abdumo'min**

GitHub:
https://github.com/Abdumomin07

---

⭐ Agar loyiha foydali bo‘lsa, repository'ga star qoldirishni unutmang!