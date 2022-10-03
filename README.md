# ecommerce-api-service
# 📎 목차

1. [ecommerce-api-service]
2. [개발 기간]
3. [요구사항 및 분석]
4. [기술 스택]
5. [API Endpoints]


# 🚀 ecommerce crud api 서비스
- 

# 📆 개발 기간
- 2022.09.14 ~ 2022.10.03


# 📝 구현 사항
### 1. 회원가입/로그인

- 회원가입
- 로그인
  - email, password로 로그인
  - 로그인 후 access token 발급

  
### 2. 제품 CRUD

- 제품 생성
- 제품 조회
- 제품 수정
- 제품 삭제


### 3. 주문 CRUD

- 주문 생성
- 주문 조회
  - 주문서 반환
  - 상세 주문 조회
    - 주문한 제품들의 정보를 list로 반환
- 주문 삭제

### 4. 결제 CRD

- 결제 생성
- 결제 조회
- 결제 삭제


# 🛠 기술 스택
Language | Framwork | Database | HTTP | Develop | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white"> 

# 🎯 API Endpoints
| endpoint | HTTP Method | 기능   | require parameter                                                                                                   | response data |
|----------|-------------|------|---------------------------------------------------------------------------------------------------------------------|---------------|
| /user/signup/ | POST | 회원가입 | email: string, password: string, name: string | Token: json |
| /user/login/ | POST | 로그인 | email: string, password: string | Token: json |
| /product/create/ | POST | 제품 생성 | name: string, price: int, description: string, category_id: int, tag_id: int  | 성공 여부 |
| /product/read/ | GET | 제품 조회 | - | product_list: json |
| /product/update/ | PUT | 제품 수정 | product_id: int, name: string, price: int, description: string | 성공 여부 |
| /product/delete/<int:product_id> | DELETE | 제품 삭제 | product_id: int | 성공 여부 |
| /product/create/category/ | POST | 카테고리 생성 | name: string | 성공 여부 |
| /product/create/tag/ | POST | 태그 생성 | name: string | 성공 여부 |
| /order/create/ | POST | 주문 생성 | address: string, receiver_name: string, total_price: int, delivery_fee: int, products: list | 성공 여부 |
| /order/read/<int:order_id> | GET | 주문 조회 | order_id: int | result: json |
| /order/read/detail/<int:order_id> | GET | 주문 상세 조회 | order_id: int | result: json |
| /order/update/ | PUT | 주문 수정 | order_id: int, address: string, receiver_name: string | 성공 여부 |
| /order/delete/<int:order_id> | DELETE | 주문 삭제 | order_id: int | 성공 여부 |
| /payment/create/ | POST | 결제 생성 | order_id: int, method: string, status: boolean | 성공 여부 |
| /payment/read/<int:payment_id> | GET | 결제 조회 | payment_id: int | result: json |
| /payment/delete/<int:payment_id> | DELETE | 결제 취소 | payment_id: int | 성공 여부 |
