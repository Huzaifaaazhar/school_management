# Django School Management System

This project implements a school management system using Django. It allows managing teachers, classes, courses, students, and their marks efficiently.

## Features

- CRUD operations for teachers, classes, courses, and students
- Enrolling students in classes and courses
- Recording and retrieving student marks per course and class
- Searching and pagination for teachers, classes, courses, and students


## Entity Relationship Diagram (ERD)

![ERD](link_to_your_image_or_ASCII_representation)

Entities:
- Teacher
- Class
- Course
- Student

Relationships:
- One student can have only one class at a time.
- One student can have multiple courses within a class.
- One teacher can teach multiple courses in multiple classes.
- One student can have unique marks in a specific class for a specific course taught by a specific teacher.

## Technologies Used

- Django 3.x
- Python 3.x
- SQLite (or your database of choice)
- Git (for version control)


