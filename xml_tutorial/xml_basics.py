#%%
import pandas as pd
import xml.etree.ElementTree as ET
import urllib

#%%
# download xml file
xml_file = urllib.request.urlretrieve("https://raw.githubusercontent.com/Explore-AI/Public-Data/master/books.xml","books.xml")

# %%
# load file into variable
file_path = "books.xml"

# %%
# read in file as xml
xtree = ET.parse(file_path)

# %%
xroot = xtree.getroot()
# %%
# Get element location in memrory
print("object:\t\t", xroot)

# %%
print("data type", type(xroot))
# %%
# xml tag with root element
print("XML Tag:\t", xroot.tag)

# %%
for child in xroot:
    print(child.tag, child.attrib)
    for grandchild in child:
        print("\t", grandchild.tag, grandchild.text)
# %%
df_cols = [
    "id",
    "author",
    "title",
    "genre",
    "price",
    "publish_date",
    "description"
]
# %%
# Get all info
rows = []

for node in xroot:
    # get a tag for each element
    b_id = node.attrib.get(df_cols[0])
    # Get the other attributes
    b_author = node.find(df_cols[1]).text if node is not None else None
    b_title = node.find(df_cols[2]).text if node is not None else None
    b_genre = node.find(df_cols[3]).text if node is not None else None
    b_price = node.find(df_cols[4]).text if node is not None else None
    b_publish_date = node.find(df_cols[5]).text if node is not None else None
    b_description = node.find(df_cols[6]).text if node is not None else None

    # append node info into a list as dict
    rows.append({
        df_cols[0]: b_id,
        df_cols[1]: b_author,
        df_cols[2]: b_title,
        df_cols[3]: b_genre,
        df_cols[4]: b_price,
        df_cols[5]: b_publish_date,
        df_cols[6]: b_description
    })
# %%
# print out row data
for i,x in enumerate(rows, start=1):
    print(f"Row {i}: {x}")
# %%
# create df
df = pd.DataFrame(rows, columns=df_cols)
# %%
df.head()
# %%
