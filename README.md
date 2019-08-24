# Freelance area 
```
Freelance area where customer cat create their task and 
developers can get that tasks and execute them.
```

# Installation and run 
```
git clone https://github.com/nadyrbek97/freelance.git
virtualenv venv -p python3
source venv/bin/activate
cd freelance
pip install -r requirements.txt
```
## Before running 
```
1. Create .env file in root directory and add:
    SECRET_KEY = 'your_secret_key'
2. Run migrations:
    python manage.py migrate
3. Than run server:
    python manage.py runserver
```
## Run tests
```
python manage.py test
```

## Theoretical part 
### transaction.atomic()
```
transaction.atomic() provides us safety transaction management.
If function under atomic() executes without any problem all changes saves in data base.
Otherwice nothing will be saved.
It is very usefull when we work with money transactions to avoid any misscalculations.
```

### SELECT_FOR_UPDATE
```
select_for_update()
Returns a queryset that will lock rows until the end of transaction.
```

### SELECT_RELATED
```
select_related()
Returns a queryset that will also select additional related-object.
And it alow us to avoid re-appeal to data base.
```

### DIFFERENCE BETWEEN SELECT_RELATED & PREFETCH_RELATED
```
select_related() works with SELECT statement in sql, thus gets the related objects
in the same query, but select_related() is limited to single-valued relationship
- foriegn key and one-to-one.

prefetch_related() has similar purpose as select_relate() but it has different strategy.
it does seprates look up for each relationship, and does 'joining' in Python.
This allows to prefetch many-to-many & many-to-one objects.
```

### F() 
```
F() expressions
An F() object represents the value of a model field or annotated column. It makes
it possible to refer to model field values and perform database operations using them
withour actually having to pull them our of the database into Python memory.
It helps us to optimize our code.
F() generates an SQL expression that describe the required operation at the database level.
```

### Q()
```
Q() as a F() object used to encapsulate a collection of keywords arguments.
We can use "AND" & "OR":
Q(question__startswith='Who') | Q(question__startswith='What')
and it's similar to: WHERE question LIKE 'Who%' OR question LIKE 'What%'
Also "NOT" is defined with "~":
Q(question__startswith='Who') | ~Q(pub_date__year=2005).

Example:
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
Similar to:
SELECT * from polls WHERE question LIKE 'Who%'
    AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
```
