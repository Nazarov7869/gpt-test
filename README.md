# Murojaatlar platformasi (Django)

## Ishga tushirish

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Asosiy imkoniyatlar

- Har bir foydalanuvchi ro'yxatdan o'tib o'z sahifasiga kiradi.
- Foydalanuvchi faqat o'z murojaatlarini ko'radi.
- Faqat admin (`is_staff=True`) barcha murojaatlarni ko'radi, tahrirlaydi va o'chiradi.
- Django admin paneli ham mavjud (`/admin/`).
