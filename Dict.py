# info= {
#     "key" :"value",
#     "name":"Palak",
#     "lname" : "kothari",
#     "age":25,
#     "is_adult":True,
#     "marks":99,
#     "subjects":["python" , "mongo", "kitto" , "C++" ],
#     "topics":("dict" , "Set"),
#     12:12
# }
# print(info)
# print(type(info))
# print(info["name"])
# info["name"]= "lisa" #updated information 
# print("updated")
# print(info)

#nested dictionary :
palak = {
    "name":"palak",
    "marks":{
        "maths":90,
        "english":80,
        "hindi":70
    }
}
# methods :
# print(palak)
# print(palak["marks"]["maths"])
# print(palak.keys())
# print(len(palak.keys()))
# print(palak.values())
# print(list(palak.items()))
# pairs= list(palak.items())
# print(pairs[0])

# # this will get a value of the specified key ;
# palak.get("name")
palak.update({"salary" : "2000000"})
print(palak)

#  or
new_dict ={"Post" : "Algorithmic trader"}
palak.update(new_dict)
print(palak)


