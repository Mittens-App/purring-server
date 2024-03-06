import unittest

# automate test path
import os
path = os.path.abspath("test/basic_test.py")


print("=====================================================")
from src.library.automation import manager
automator = manager.AutomationManager()
automator.set_file(file_path=path)
result = automator.run()
print("NO ARGV TEST")
print("Test Count:", result.test_count())
print("Test Success Status:", result.is_success())
print("Effectiveness (in percent):", result.effectiveness())
for fail in result.fails():
    print("type:", fail.type)
    print("method:", fail.method)

print("=====================================================")

print("=====================================================")
print("ARGV TEST")
automator.set_file(file_path=path)
result = automator.run()
