#1 - School
Small system for managing people at school.

## Classes:

### Student

#### Attributes:

* `first_name`
* `last_name`
* `grades` - list of grades (for simplification it could be a list of integers)

#### Methods:

##### `__init__`

Parameters:
* `first_name`
* `last_name`
* `grades`

##### get_full_name()
Return full name {first_name} {last_name}

##### get_average_grade() 
Return average of grades

##### __eq__()
Compare equal of two objects.

### Teacher

#### Attributes:

* `first_name`
* `last_name`
* `subjects` - list of subjects that this teacher is able to teach

#### Methods:

##### `__init__`

Parameters:
* `first_name`
* `last_name`
* `subjects`

##### get_full_name()
Return full name {first_name} {last_name}

##### __eq__()
Compare equal of two objects.

### Class
Used to aggregate Students and Teachers into a class

#### Attributes:

* `name`
* `students`
* `teachers`

#### Methods:

##### `__init__`

Parameters:
* `name`
* `students`
* `teachers`

##### get_best_student()
Return student with highest average grade.

##### get_average_grade() 
Get average grade of all students

##### get_class_subjects() 
Return a list of subjects that are being taught in this class

##### sort_students(attr)
Sorts students alphabetically or by average grade

### School
Used to aggregate classes

#### Attributes:

* `name`
* `classes`

Methods:
##### `__init__`

Parameters:
* `classes`

##### get_best_class() 
Return class with highest average grade

##### get_all_teachers() 
Returns all teachers from this school
