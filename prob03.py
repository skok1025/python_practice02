s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
s = sorted(set(s.upper().replace(",","").replace(".","").replace("\n","").split(" ")))
for w in s : print(w)

