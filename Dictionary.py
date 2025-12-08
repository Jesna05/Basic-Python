dit = {"a":"apple","b":"banana",5:"five"}
print(dit)
dit["c"] = "cat"
print(dit)
dit["a"] = "ant"
print(dit)
dit["d"] = "ant"
print(dit)
print(dit["b"])
# print(dit["r"])
print(dit.get("r","not found"))
print(dit.get("r"))
