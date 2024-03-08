import unittest

# automate test path
import os
path = os.path.abspath("test/basic_test.py")
path = path.replace("\\", "/")

# print(path)
# exit()
print("=====================================================")
from src.library.automation import manager
automator = manager.AutomationManager()

# ============= list function =============
## change file dir
path2 = "D:/rizal/projects/purring-test/my/my/purring/test4_basic_headless2.py"
path3 = "D:/rizal/projects/mittens/purring_server/test/basic_test.py"
path4 = "C:/Users/USER/Documents/run_thisxy.py"
testclass = automator.get_functions(file_path=path2)
print("classname:", testclass.classname)
print("path:", testclass.path)
for func in testclass.functions:
    print("function|comment:", func.name, "|", func.comment)
# ================== END ==================



# ============= set single file ============
# automator.set_file(file_path=path)

# ================== END ==================



# ============= set single file ============
## example 1
# automator.add_file(path2).add_file(path3).add_file(path2)

## example 2
# for i in 5:
#     automator.add_file(file_path=path)
    
# ================== END ==================



# ============= with ARGV ============
# # set single file with argv
# argv = ["--no-attribute", "https"]
# automator.set_file(file_path=path, argv=argv)

# for i in 5:
#     automator.add_file(file_path=path, argv=argv)

# ================== END ==================



# ============= set files. gk support argv ============
# automator.set_files(
#     file_paths=[
#         path,path,path
#     ]
# )
    
# ================== END ==================



# ============= run ============
# result = automator.run()
# print("Test Count:", result.test_count())
# print("Test Success Status:", result.is_success())
# print("Effectiveness (in percent):", result.effectiveness())
# for fail in result.fails():
#     print("type:", fail.type)
#     print("method:", fail.method)
#     # print("msg:", fail.msg)

# print("=====================================================")

