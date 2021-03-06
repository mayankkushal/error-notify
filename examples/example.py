import os, sys
from error_notify.decorators import override_function, override_class

# total_override
def test_total_override():
	temp = "total"/0

# override_function
@partial_override
def test_partial_override():
	temp = "partial"/0

def test_class_override():

	@override_class(include=['func_3'])
	class Demo:
		def func_1(self):
			temp = "class"/0

		def func_2(self):
			temp = "class"/0

		def func_3(self):
			temp = "class"/0

		def run(self):
			self.func_3()
			self.func_2()

	Demo().run()


if __name__ == '__main__':

	if sys.argv[1] == "partial":
		test_partial_override()
	elif sys.argv[1] == "total":
		from error_notify import total_override
		test_total_override()
	elif sys.argv[1] == "class":
		test_class_override()