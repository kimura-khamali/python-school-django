- python3 manage.py shell
  form student.models import Student;
  student= Student.object.all()
  for student in students:print(student.first_name)

object.all()
returns all the data in a associated table

## Filtering data ORM

- Filter method allows as to filter the data based on a given criterea
- filter allows to return a subset of data

Student.objects.filter(first_name="Brenda");
<QuerySet [<Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>]>

Student.objects.filter(code=55)
<QuerySet [<Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>]>

> > > Student.objects.filter(code\_\_gte=10)
> > > <QuerySet [<Student: Brenda Khamali>, <Student: Jane Wamachwa>, <Student: Lydia Anne>, <Student: Mike peter>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>, <Student: Brenda Khamali>]>

gte means greater than or equal to
lte means less or equal to

> > > Student.objects.filter(code\_\_lte=50)
> > > <QuerySet [<Student: Jane Wamachwa>, <Student: Lydia Anne>]>

Retrieve a single
objects.get() -returns a single object

> > > Student.objects.get(id=1)
> > > <Student: Brenda Khamali>

if .get does not find a matching query it throws a does not exist exception(error)

> > > Student.objects.get(first_name="Ruto")
> > > Traceback (most recent call last):
> > > File "<console>", line 1, in <module>
> > > AttributeError: 'Manager' object has no attribute 'ge'
> > > Student.objects.get(first_name="Ruto")
> > > Traceback (most recent call last):
> > > File "<console>", line 1, in <module>
> > > File "/home/studen/pythonClass/web/school-project/env1/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method

    return getattr(self.get_queryset(), name)(*args, **kwargs)

File "/home/studen/pythonClass/web/school-project/env1/lib/python3.10/site-packages/django/db/models/query.py", line 649, in get
raise self.model.DoesNotExist(
student.models.Student.DoesNotExist: Student matching query does not exist.

> > >

if .get finds more than 1 matching records it throws multiple objectsfound exception
\*\* id error

student.models.Student.DoesNotExist: Student matching query does not exist.

> > > Student.objects.get(id\_\_gte=1)
> > > Traceback (most recent call last):
> > > File "<console>", line 1, in <module>
> > > File "/home/studen/pythonClass/web/school-project/env1/lib/python3.10/site-packages/django/db/models/manager.py", line 87, in manager_method

    return getattr(self.get_queryset(), name)(*args, **kwargs)

File "/home/studen/pythonClass/web/school-project/env1/lib/python3.10/site-packages/django/db/models/query.py", line 652, in get
raise self.model.MultipleObjectsReturned(
student.models.Student.MultipleObjectsReturned: get() returned more than one Student -- it returned 10!

> > >

# Modifying an Object /Updating an object

Student=Student.objects.get(id=1)

> > > Student.first_name = "Imbwirah"
> > > student.save()
> > > Traceback (most recent call last):
> > > File "<console>", line 1, in <module>
> > > NameError: name 'student' is not defined
> > > Student.save()
> > > Student.objects.get(first_name="Imbwirah")
> > > Traceback (most recent call last):
> > > File "<console>", line 1, in <module>
> > > File "/home/studen/pythonClass/web/school-project/env1/lib/python3.10/site-packages/django/db/models/manager.py", line 186, in **get**

    raise AttributeError(

AttributeError: Manager isn't accessible via Student instances

> > >

## Ordering Results

Student.objects.all()
Student.objects.all().order_by("first_name")

<!-- Student.objects.all().order_by(-"first_name") -->

student=Student.objects.all().order_by("-id")

## Limiting the result

student=Student.objects.all()[:2]

### Counting All Objects

> > > Student.objects.count()
> > > 10

- checking if a record exist in the database

> > > Student.objects.filter(id=1).exists()
> > > True

> > > Student.objects.filter(id=1000).exists()
> > > False

## Return a subset of attribute

> > > Student.objects.values("first_name")
> > > <QuerySet [{'first_name': 'Jane'}, {'first_name': 'Lydia'}, {'first_name': 'Mike'}, {'first_name': 'Brenda'}, {'first_name': 'Brenda'}, {'first_name': 'Brenda'}, {'first_name': 'Brenda'}, {'first_name': 'Brenda'}, {'first_name': 'Brenda'}, {'first_name': 'Imbwirah'}]>

> > > Student.objects.values("first_name","email")
> > > <QuerySet [{'first_name': 'Jane', 'email': 'janewamachwa@gmail.com'}, {'first_name': 'Lydia', 'email': 'lydiaann@gmail.com'}, {'first_name': 'Mike', 'email': 'mikepeter@gmail.com'}, {'first_name': 'Brenda', 'email': 'kimurakhamali@gmail.com'}, {'first_name': 'Brenda', 'email': 'kimurakhamali@gmail.com'}, {'first_name': 'Brenda', 'email': 'kimurakhamali@gmail.com'}, {'first_name': 'Brenda', 'email': 'kimurakhamali@gmail.com'}, {'first_name': 'Brenda', 'email': 'kimurakhamali@gmail.com'}, {'first_name': 'Brenda', 'email': 'kimurakhamali@gmail.com'}, {'first_name': 'Imbwirah', 'email': 'kimurakhamali@gmail.com'}]>

- Select first_name,email from Students

## Creating objects

We use the create method

- While creating an object include all the attributes required in model

django.db.utils.IntegrityError: null value in column "code" of relation "student_student" violates not-null constraint
DETAIL: Failing row contains (12, Brenda, Khamali, null, , null, , , null, , , Default Name).

> > > Student.objects.create(first_name = "Brenda",last_name="Khamali",code=55,email="kimurakhamali@gmail.com",age=20,country="Kenya",phone_number= "0200435456",date_of_birth= datetime.date(1999, 12, 3),contact= "0723243454",bio= "Adedicated student",name= "Default Name")

tudent.objects.create(first_name = startwith="Ag")

student = Student()
student.first_name = "Aisha"
student.code = 20
student.email

# Handling Forms

## templates views

#### creating a form based on a model

#### using views to work with forms

#### Rendering forms in HTML templates

#### Handling form submissions

#### saving the data in the database
