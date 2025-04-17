# 🧾 توثيق API: عرض المشاريع (Projects) والوحدات (Units)

## 🔗 Endpoint
GET /api/projects/

yaml
Copy
Edit

---

## 📄 الوصف
هذا الـ API يعرض قائمة بكل المشاريع العقارية، ويشمل كل مشروع على:

- تفاصيله الأساسية.
- صور المشروع.
- الوحدات المرتبطة بالمشروع (شقق، دوبلكس، فيلات...).
- صور كل وحدة.

---

## 📥 الباراميترات (GET Parameters)

| اسم الباراميتر | النوع | الوصف                        |
|----------------|--------|------------------------------|
| `page`         | int    | لتحديد صفحة النتائج (pagination) |

---

## 📤 الـ Response Sample (نموذج)

```json
{
  "count": 2,
  "next": "http://127.0.0.1:8000/api/projects/?page=2",
  "previous": null,
  "results": [
    {
      "id": 3,
      "name": "O West Orascom",
      "location": "O West Orascom",
      "description": "وصف المشروع...",
      "starting_price": "8900000.00",
      "down_payment_percent": "5.00",
      "installment_years": 7,
      "whatsapp": "http://127.0.0.1:8000/admin/state/project/add/",
      "media_project": [],
      "units": [
        {
          "id": 1,
          "project": 3,
          "type": "duplex",
          "bedrooms_count": 4,
          "area_min": 120,
          "area_max": 140,
          "is_fully_finished": false,
          "price": "600000.00",
          "media_unit": [
            {
              "id": 3,
              "image": "http://127.0.0.1:8000/media/image/unit/Picture6_8keYhh6.png"
            }
          ],
          "whatsapp": "http://127.0.0.1:8000/admin/state/project/add/",
          "phone": "01234245324"
        }
      ]
    }
  ]
}
🧩 تفصيل الـ JSON للـ Frontend
🏢 Project الكائن الرئيسي:

المفتاح	النوع	الوصف
id	integer	معرف المشروع
name	string	اسم المشروع
location	string	موقع المشروع
description	string	وصف تفصيلي
starting_price	string/decimal	أقل سعر للوحدات داخل المشروع
down_payment_percent	string/decimal	نسبة الدفعة المقدمة
installment_years	integer	عدد سنوات الأقساط
whatsapp	URL	رابط تواصل واتساب
media_project	list	صور المشروع (إن وجدت)
units	list	قائمة الوحدات الخاصة بالمشروع
🏠 Unit الكائن داخل كل مشروع:

المفتاح	النوع	الوصف
id	integer	معرف الوحدة
project	integer	ID المشروع التابع له
type	string	نوع الوحدة (duplex, apartment, ...)
bedrooms_count	integer	عدد غرف النوم
area_min	float	أقل مساحة بالمتر
area_max	float	أكبر مساحة بالمتر
is_fully_finished	boolean	هل الوحدة كاملة التشطيب؟
price	decimal	السعر النهائي
media_unit	list	قائمة الصور المرتبطة بالوحدة
whatsapp	URL	رابط واتساب للوحدة
phone	string	رقم الهاتف للتواصل
📷 media_project و media_unit
قائمة تحتوي على الصور المتعلقة بالمشروع أو الوحدة:

json
Copy
Edit
"media_unit": [
  {
    "id": 3,
    "image": "http://127.0.0.1:8000/media/image/unit/Picture6_8keYhh6.png"
  }
]
