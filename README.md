## Перемещение товаров по локациям 

---

###  Как пользоваться:

- Использовать только предлоги:
    - **в**, **на**
    - **из**, **со**
- После каждого предлога **обязательно** использование **локации**:   
    ***Из магазин в склад***    
    ***в ларек со склад***
- Количество товара и его название можно распологать в любой послежовательности:  
    ***1 товар в магазин со склад***  
    ***товар в склад 2 из магазин***
- Регистр текста роли не играет:  
    ***1 ТоВар из сКлад в лАреК*** 
- Остановить программу:
    ```'стоп'```

### Пример кода

```text = input("Введите предложение: ")
    while text.lower().strip() != 'стоп':
        req = Request(text)

        request_dict = req.get_req_data()

        from_data: dict = req.get_items(request_dict['from'])
        to_data: dict = req.get_items(request_dict['to'])

        try:
            product = request_dict["product"]
        except KeyError:
            print(f'нет такого товара в {from_data["name"]}')

        try:
            amount = request_dict['amount']
        except KeyError:
            print(f'не указано количество товара')

        from_obj = from_data['class']
        to_obj = to_data['class']

        if from_obj.remove(product, amount):....
```

![codwars](https://www.codewars.com/users/Ko4ak/badges/micro)
