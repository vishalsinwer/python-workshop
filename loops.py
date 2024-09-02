list_of_cloud= ["aws","azure","gcp","oracle"]
print(list_of_cloud)

list_of_cloud.append("salesforce")
print(list_of_cloud)

list_of_cloud.insert(0,"hiroku")
print(list_of_cloud)

for cloud in list_of_cloud:
    print(" ")
    print(cloud)