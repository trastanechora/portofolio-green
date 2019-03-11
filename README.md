# Panenin
## Solusi Hasil Panen 
(e-commerce project)
                                              <br>
Flowchart:                                    <br>
https://whimsical.co/L6677ck8zMkgc8hPTUmsUi   <br>
                                              <br>
Wireframe:                                    <br>
https://whimsical.co/7GK4fQWhZT5K23itWyCGf8   <br>
                                              <br>
Dokumentasi API:                              <br>
============= USER =============              <br>
POST        /api/public/register              <br>
PUT         /api/public/register/<int:id>     <br>
                                              <br>
GET         /api/admin/users                  <br>
DELETE      /api/admin/users/<int:id>         <br>
                                              <br>
                                              <br>
============= Product =============           <br>
GET         /api/public/products              <br>
GET         /api/public/products/<int:id>     <br>
POST        /api/public/products              <br>
PUT         /api/public/products              <br>
DELETE      /api/products/<int:id>            <br>
                                              <br>
DELETE      /api/admin/products/<int:id>      <br>
                                              <br>
                                              <br>
============= Offer =============             <br>
GET         /api/offers                       <br>
GET         /api/offers/<int:id>              <br>
POST        /api/offers                       <br>
PUT         /api/offers/<int:id>              <br>
DELETE      /api/offers/<int:id>              <br>
                                              <br>
GET         /admin/offers/                    <br>
DELETE      /admin/offers/<int:id>            <br>
                                              <br>
                                              <br>
============= Transaction =============       <br>
GET         /api/transactions                 <br>
GET         /api/transactions/<int:id>        <br>
POST        /api/transactions                 <br>
PUT         /api/transactions                 <br>
                                              <br>
DELETE      /api/admin/transactions/<int:id>  <br>
                                              <br>
                                              <br>
============= Driver (Courier) =============  <br>
GET         /api/public/couriers              <br>
GET         /api/public/couriers/<int:id>     <br>
POST        /api/public/couriers              <br>
PUT         /api/public/couriers              <br>
DELETE      /api/public/couriers/<int:id>     <br>
                                              <br>
DELETE      /api/admin/couriers/<int:id>      <br>
