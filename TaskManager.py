import matplotlib .pyplot as plt
import psutil as p 
app_name_dict = ()
count = 0
for process in p.process_iter():
    count = count + 1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('Name : ', name, '-- cpu_usage : ', cpu_usage)
        app_name_dict.update({name: cpu_usage})
        
keymax = max(app_name_dict, key=app_name_dict.get)
keymin = min(app_name_dict, key=app_name_dict.get)
some_list = [keymax, keymin]
print(keymax)
print(keymin)
name_list = [keymax, keymin]
print(name_list)

app = app_name_dict.values()
max_app = max(app)
print("maximun" , max_app)

min_app = min(app)
print("minimun" , min_app)

max_min_list = [max_app, min_app]
print(max_min_list)

plt.figure(figsize=(15,8))
plt.xlabel("Min_max cpu consumption")
plt.ylabel("Usage")
plt.bar(name_list, max_min_list,width=0.6, color=("red","black"))
plt.show()