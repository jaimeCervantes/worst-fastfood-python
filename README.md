# Find worst fast foods, so you don't eat them

A way to find the top worst fast food to eat from most know fast food chains like McDonalds, Burger King, Sonic, etc

## How to run locally?

Configure your .env file like .env.example

```bash
pip install -r requirements.txt
uvicorn src.main:app
```

## users

- jaime
  - password: password1
- fulano
  - password: password2

## Dataset from [Kaggle](https://www.kaggle.com/)

[dataset food nutrition] (https://www.kaggle.com/datasets/joebeachcapital/fast-food)

## API endpoints

```
/login
/fastfood-nutrition
```

## Some words to filter for fastfood names

- dog
- burger
- chicken
- bacon
- cheese
- meat
