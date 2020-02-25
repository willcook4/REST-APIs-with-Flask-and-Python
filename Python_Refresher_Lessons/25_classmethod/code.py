class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"Called class_mathod of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")

ClassTest.instance_method(ClassTest)
# Usually an action on data in self
# e.g. 
# student1 = Student()
# student1.instance_method()

ClassTest.class_method()
# We generally use class method to create factory methods. 
# Factory methods return class object (similar to a constructor) for different use cases.
# e.g.
# Student.class_method()

ClassTest.static_method()
# Ususally used as utility functions