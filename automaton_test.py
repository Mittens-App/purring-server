import unittest

# automate test path
import os

print("=====================================================")
from src.v1.services.manager import AutomationManager
automator = AutomationManager()

# ============= list function =============

path1 = os.path.abspath("test/test1.py").replace("\\", "/")
path2 = os.path.abspath("test/test2.py").replace("\\", "/")
path3 = os.path.abspath("test/test3.py").replace("\\", "/")
path4 = os.path.abspath("test/test4.py").replace("\\", "/")
path5 = "D:/rizal/projects/purring-test/my/my/purring/test4_basic_headless2.py"
# testclass = automator.get_functions(file_path=path5)
# print("classname:", testclass.classname)
# print("path:", testclass.path)
# for func in testclass.functions:
#     print("function|comment:", func.name, "|", func.comment)
# ================== END ==================



# ============= set single file ============
# automator.set_file(file_path=path2)

# ================== END ==================



# ============= multi file ============
## example 1
automator.add_file(path1).add_file(path5).add_file(path2).add_file(path4)

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
result = automator.run(use_worker=True)
print("Test Count:", result.test_count())
print("Test Success Status:", result.is_success())
print("Effectiveness (in percent):", result.effectiveness())
print("Duration (in seconds):", result.duration())
print("ResultCases:")
for resultcase in result.resultcase():
    print("      - classname:", resultcase.classname)
    print("        duration:", resultcase.duration)
    print("        file_path:", resultcase.file_path)
    print("        test_count:", resultcase.test_count)
    print("        success_status:", resultcase.success)
    print("        fails:")
    for fail in resultcase.fails():
        print("              - type:", fail.type)
        print("                method:", fail.method)
        # print("                msg:", fail.msg)

# print("=====================================================")

