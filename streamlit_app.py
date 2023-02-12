import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

# connect to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a Snowflake query and put all in a var called my_catalog
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put the data into a dataframe
df = pandas.DataFrame(my_catalog)

# temp write the dataframe to the page so I can see what i am working with
# streamlit.write(df)

# put the first column into a list
color_list = df[0].values.tolist()
print(color_list)

