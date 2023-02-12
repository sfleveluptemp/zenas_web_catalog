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
#print(color_list)

# Let's put a pick list here so they can pick the color
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# We'll build the image caption now, since we can
product_caption = 'Our warm, comfortable,' + option + 'sweatsuit!'

# Use the option selected to go back and get all the info from the database
my_cur.execute("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '" + option + "';")
df2 = my_cur.fetchone()

streamlit.image (
  df2[0],
  width=400,
  caption=product_caption
)

