# Panenin
## Solusi Hasil Panen 
(e-commerce project)

Flowchart:
https://whimsical.co/L6677ck8zMkgc8hPTUmsUi

Wireframe:
https://whimsical.co/7GK4fQWhZT5K23itWyCGf8

Dokumentasi API:
============= USER =============
POST        /api/public/register
PUT         /api/public/register/<int:id>

GET         /api/admin/users
DELETE      /api/admin/users/<int:id>


============= Product =============
GET         /api/public/products
GET         /api/public/products/<int:id>
POST        /api/public/products
PUT         /api/public/products
DELETE      /api/products/<int:id>

DELETE      /api/admin/products/<int:id>


============= Offer =============
GET         /api/offers
GET         /api/offers/<int:id>
POST        /api/offers
PUT         /api/offers/<int:id>
DELETE      /api/offers/<int:id>

GET         /admin/offers/
DELETE      /admin/offers/<int:id>


============= Transaction =============
GET         /api/transactions 
GET         /api/transactions/<int:id>
POST        /api/transactions
PUT         /api/transactions

DELETE      /api/admin/transactions/<int:id>


============= Driver (Courier) =============
GET         /api/public/couriers
GET         /api/public/couriers/<int:id>
POST        /api/public/couriers
PUT         /api/public/couriers
DELETE      /api/public/couriers/<int:id>

DELETE      /api/admin/couriers/<int:id>
