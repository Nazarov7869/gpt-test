# Django murojaatlar platformasi

Ushbu loyiha foydalanuvchilardan murojaat qabul qilish uchun yozilgan.

## Asosiy imkoniyatlar
- Foydalanuvchi ro'yxatdan o'tadi va tizimga kiradi.
- Har bir foydalanuvchining alohida `Sahifam` bo'limi mavjud.
- Foydalanuvchi faqat murojaat yuboradi va o'z murojaatlari holatini ko'radi.
- Faqat admin (`is_staff=True`) barcha murojaatlarni ko'radi, tahrirlaydi va o'chiradi.
- Django admin panelida ham murojaatlar boshqaruvi bor.

## Ishga tushirish
> Muhitda Django o'rnatilmagan bo'lsa, avval o'rnating.

```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Marshrutlar
- `/` — bosh sahifa
- `/register/` — ro'yxatdan o'tish
- `/accounts/login/` — kirish
- `/dashboard/` — foydalanuvchining shaxsiy sahifasi
- `/appeals/create/` — murojaat yuborish
- `/admin-panel/appeals/` — admin murojaatlar ro'yxati
- `/admin/` — Django superadmin
