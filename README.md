# ecommerce-api-service
# ๐ ๋ชฉ์ฐจ

1. [ecommerce-api-service]
2. [๊ฐ๋ฐ ๊ธฐ๊ฐ]
3. [์๊ตฌ์ฌํญ ๋ฐ ๋ถ์]
4. [๊ธฐ์  ์คํ]
5. [API Endpoints]


# ๐ ecommerce crud api ์๋น์ค
- 

# ๐ ๊ฐ๋ฐ ๊ธฐ๊ฐ
- 2022.09.14 ~ 2022.10.03


# ๐ ๊ตฌํ ์ฌํญ
### 1. ํ์๊ฐ์/๋ก๊ทธ์ธ

- ํ์๊ฐ์
- ๋ก๊ทธ์ธ
  - email, password๋ก ๋ก๊ทธ์ธ
  - ๋ก๊ทธ์ธ ํ access token ๋ฐ๊ธ

  
### 2. ์ ํ CRUD

- ์ ํ ์์ฑ
- ์ ํ ์กฐํ
- ์ ํ ์์ 
- ์ ํ ์ญ์ 


### 3. ์ฃผ๋ฌธ CRUD

- ์ฃผ๋ฌธ ์์ฑ
- ์ฃผ๋ฌธ ์กฐํ
  - ์ฃผ๋ฌธ์ ๋ฐํ
  - ์์ธ ์ฃผ๋ฌธ ์กฐํ
    - ์ฃผ๋ฌธํ ์ ํ๋ค์ ์ ๋ณด๋ฅผ list๋ก ๋ฐํ
- ์ฃผ๋ฌธ ์ญ์ 

### 4. ๊ฒฐ์  CRD

- ๊ฒฐ์  ์์ฑ
- ๊ฒฐ์  ์กฐํ
- ๊ฒฐ์  ์ญ์ 


# ๐  ๊ธฐ์  ์คํ
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# ๐ฏ API Endpoints
| endpoint | HTTP Method | ๊ธฐ๋ฅ   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /user/signup/ | POST | ํ์๊ฐ์ | email: string, password: string, name: string | Token: json |
| /user/login/ | POST | ๋ก๊ทธ์ธ | email: string, password: string | Token: json |
| /product/create/ | POST | ์ ํ ์์ฑ | name: string, price: int, description: string, category_id: int, tag_id: int  | ์ฑ๊ณต ์ฌ๋ถ |
| /product/read/ | GET | ์ ํ ์กฐํ | - | product_list: json |
| /product/update/ | PUT | ์ ํ ์์  | product_id: int, name: string, price: int, description: string | ์ฑ๊ณต ์ฌ๋ถ |
| /product/delete/<int:product_id> | DELETE | ์ ํ ์ญ์  | product_id: int | ์ฑ๊ณต ์ฌ๋ถ |
| /product/create/category/ | POST | ์นดํ๊ณ ๋ฆฌ ์์ฑ | name: string | ์ฑ๊ณต ์ฌ๋ถ |
| /product/create/tag/ | POST | ํ๊ทธ ์์ฑ | name: string | ์ฑ๊ณต ์ฌ๋ถ |
| /order/create/ | POST | ์ฃผ๋ฌธ ์์ฑ | address: string, receiver_name: string, total_price: int, delivery_fee: int, products: list | ์ฑ๊ณต ์ฌ๋ถ |
| /order/read/<int:order_id> | GET | ์ฃผ๋ฌธ ์กฐํ | order_id: int | result: json |
| /order/read/detail/<int:order_id> | GET | ์ฃผ๋ฌธ ์์ธ ์กฐํ | order_id: int | result: json |
| /order/update/ | PUT | ์ฃผ๋ฌธ ์์  | order_id: int, address: string, receiver_name: string | ์ฑ๊ณต ์ฌ๋ถ |
| /order/delete/<int:order_id> | DELETE | ์ฃผ๋ฌธ ์ญ์  | order_id: int | ์ฑ๊ณต ์ฌ๋ถ |
| /payment/create/ | POST | ๊ฒฐ์  ์์ฑ | order_id: int, method: string, status: boolean | ์ฑ๊ณต ์ฌ๋ถ |
| /payment/read/<int:payment_id> | GET | ๊ฒฐ์  ์กฐํ | payment_id: int | result: json |
| /payment/delete/<int:payment_id> | DELETE | ๊ฒฐ์  ์ทจ์ | payment_id: int | ์ฑ๊ณต ์ฌ๋ถ |
