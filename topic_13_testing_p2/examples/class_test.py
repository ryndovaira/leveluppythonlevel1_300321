class TestClass():
    @classmethod
    def setup_class(cls):
        print("setup_class called once for the class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class called once for the class")

    def setup_method(self):
        print("setup_method called for every method")

    def teardown_method(self):
        print("teardown_method called for every method")

    def test_one(self):
        print("one")
        assert True
        print("one after")

    def test_two(self):
        print("two")
        assert False
        print("two after")

    def test_three(self):
        print("three")
        assert True
        print("three after")
