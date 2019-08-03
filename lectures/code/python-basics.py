from testlight import *

def free_bags(status: str) -> int:
    """return number of free bags based on frequent flyer status"""
    if status == "gold":
        return 2
    elif status == "silver":
        return 1
    else: return 0

def test_bags():
    test("gold check", free_bags("gold"), 2)
    test("silver check", free_bags("silver"), 1)
    test("misspell check", free_bags("sliver"), 0)

def register(reg_list: list, course: str):
    """add the course to the reg_list"""
    reg_list.append(course)

def register(reg_list: list, course: str):
    """add the course to the reg_list if it isn't already there"""
    if course not in reg_list:
       reg_list.append(course)
    return reg_list

def register(reg_list: list, course: str):
    """add the course to the reg_list if it isn't already there"""
    if course in reg_list:
        raise Exception("Already in course")
    else:
        reg_list.append(course)
        return reg_list

taking4 = ["CSCI0111", "ENGN0090", "VISA100", "CHIN0200"]

def from_dept(reg_list: list, dept: str):
    """produce list of registered courses from given dept"""
    return list(filter(lambda course: dept in course, reg_list))
