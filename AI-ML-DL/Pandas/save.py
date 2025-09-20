import pandas as dp

data = {
    "Name" : ['Ram','Shyam','Ghanshaym'],
    "Age" : [20,30,40],
    "Cityt" : ['Gorakphur','Kanpur','khasipupr']
}

df = dp.DataFrame(data)


# df.to_csv("output.csv",index=False)
# df.to_excel("output.xlsx",index=False)
# df.to_json("output.json",index=False)
# df.to_html("output.html",index=False)