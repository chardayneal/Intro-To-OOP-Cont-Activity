from school_schedule.student import Student

def test_student_initialization():
    # Arrange
    name = 'Wei'
    grade = 'Freshman'
    classes = ['Science', 'English', 'Math']

    # Act
    student = Student(name, grade, classes)

    # Assert
    assert student.name == name
    assert student.grade == grade
    assert student.classes == classes

def test_add_class_returns_correct_classes():
    # Arrange
    student = Student('Tati', 'Senior', ['Science', 'English', 'Math'])
    new_class = 'Art'

    # Act
    updated_classes = student.add_class(new_class)

    # Assert
    assert len(updated_classes) == 4
    assert new_class in updated_classes

def test_add_class_with_empty_class():
    # Arrange
    student = Student('Tati', 'Senior', ['Science', 'English', 'Math'])
    new_class = ''

    # Act
    updated_classes = student.add_class(new_class)

    # Assert
    assert len(updated_classes) == 3
    assert updated_classes == ['Science', 'English', 'Math']

