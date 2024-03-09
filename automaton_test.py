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
path5 = "D:/rizal/projects/mittens/purring_server/src/library/automation/result.py"
# testclass = automator.get_functions(file_path=path5)
# print("classname:", testclass.classname)
# print("path:", testclass.path)
# for func in testclass.functions:
#     print("function|comment:", func.name, "|", func.comment)
# ================== END ==================

# def split_list(alist, wanted_parts=1):
#     length = len(alist)
#     return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
#              for i in range(wanted_parts) ]

# A = [0,1,2,3,4,5,6,7,8,9]

# print( split_list(A, wanted_parts=1))
# print (split_list(A, wanted_parts=2))
# print (split_list(A, wanted_parts=8))


# ============= set single file ============
# automator.set_file(file_path=path2)

# ================== END ==================



# ============= multi file ============
## example 1
automator.add_file(path2,["-aaa"]).add_file(path3,["-aaa"]).add_file(path4,["-aaa"]) #.add_file(path3,["-aaa"])

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
result = automator.run()
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

