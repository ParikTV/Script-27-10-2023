from teacher import Teacher


def main():
    teacher = Teacher("Huberth Fallas", "Programación II")
    teacherClone = teacher.clone()
    teacherClone.display()


if __name__ == "__main__":
    main()
