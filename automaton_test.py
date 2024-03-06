import unittest

# automate test path
import os
path = os.path.abspath("test/basic_test.py")


print("=====================================================")
from src.library.automation import manager
automator = manager.AutomationManager()

# set single file
automator.set_file(file_path=path)

# multi file
for i in 5:
    automator.add_file(file_path=path)

# set single file with argv
argv = ["--no-attribute", "https"]
automator.set_file(file_path=path, argv=argv)

for i in 5:
    automator.add_file(file_path=path, argv=argv)

# set files. gk support argv
automator.set_files(
    file_paths=[
        path,path,path
    ]
)

result = automator.run()
print("NO ARGV TEST")
print("Test Count:", result.test_count())
print("Test Success Status:", result.is_success())
print("Effectiveness (in percent):", result.effectiveness())
for fail in result.fails():
    print("type:", fail.type)
    print("method:", fail.method)
    print("msg:", fail.msg)

print("=====================================================")

print("=====================================================")
print("ARGV TEST")
automator.set_file(file_path=path)
result = automator.run()
