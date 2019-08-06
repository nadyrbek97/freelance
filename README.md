# Freelance area 



## Theoretical part 
### transaction.atomic()
```

```

### SELECT_FOR_UPDATE
```
select_for_update(nowait=False, skip_locked=False, of=())¶
Returns a queryset that will lock rows until the end of the transaction, 
generating a SELECT ... FOR UPDATE SQL statement on supported databases.
```

### SELECT_RELATED
```
By default, select_for_update() locks all rows that are selected by the query. 
For example, rows of related objects specified in select_related() are locked 
in addition to rows of the queryset’s model. If this isn’t desired, specify the 
related objects you want to lock in select_for_update(of=(...)) using the same 
fields syntax as select_related(). Use the value 'self' to refer to the queryset’s model.

You can’t use select_for_update() on nullable relations:

>>> Person.objects.select_related('hometown').select_for_update()
Traceback (most recent call last):
django.db.utils.NotSupportedError: FOR UPDATE cannot be applied to the nullable side of an outer join


To avoid that restriction, you can exclude null objects if you don’t care about them:

>>> Person.objects.select_related('hometown').select_for_update().exclude(hometown=None)
<QuerySet [<Person: ...)>, ...]>
```

### DIFFRENCE BETWEEN SELECT_RELATED & PREFETCH_RELATED
```

```

### F 
```

```

### Q
```

```
