# Virtual qabulxona (Django)

Ushbu platforma OTM yoki tashkilot uchun murojaatlarni qabul qilish tizimi.

## Rollar
- **Superadmin**
- **Rektor**
- **Dekan**
- **Prorektor**
- **Talaba/Fuqaro** (ariza yuboruvchi)

Talaba/fuqarolar murojaat yuboradi, admin rollar esa barcha murojaatlarni ko'radi, tahrirlaydi va o'chiradi.

## Murojaat turlari
- Murojaat
- Ariza
- Taklif
- Shikoyat

## Funksiyalar
- Shaxsiy dashboard (har bir foydalanuvchi uchun alohida sahifa)
- Qabul qiluvchini tanlab murojaat yuborish
- Murojaatga fayl biriktirish
- Statuslar: Yangi, Ko'rib chiqilgan, Ko'rilmoqda, Javob berilgan, Rad etilgan
- Admin panel: barcha murojaatlarni boshqarish

## Ishga tushirish
```bash
python -m venv .venv
source .venv/bin/activate
pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

So'ng `/admin/` orqali admin userlar ochib, ularning `is_staff=True` va profil roli (superadmin/rektor/dekan/prorektor) ni belgilang.
