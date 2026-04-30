import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
print(df.head())
print(f"Shapes: {df.shape}")
print(f"Column name: {df.columns.tolist()}")
print(f"DataTypes: {df.dtypes}")

#step1 : missing values
missing_values = df.isnull().sum()
missing_percentage = (missing_values/len(df)) *100
print(f"\n\n missing values: \n {missing_values}")
print(f"\n\n missing values percentage: \n {missing_percentage}")

#step2: fill the missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df =  df.dropna(subset=["date_added"])

print(f"\n\nAfter cleaning the data: \n {df.isnull().sum()}")

#step 3: second cleanup
df["rating"]= df["rating"].fillna("Unknown")
df = df.dropna(subset=["duration"])
print(f"\n\nAfter second cleaning the data: \n {df.isnull().sum()}")

#Step 4 — Movies vs TV Shows count
type_count = df["type"].value_counts()
print(type_count)
type_percentage = (type_count / len(df["type"]))*100
print(type_percentage)

#Step 5 — Top 10 countries producing content
top_country = df[df["country"] !="Unknown"]["country"].value_counts().head(10)
print(top_country)

#Step 6 — Which year had the most content added
df["date_added"] =pd.to_datetime(df["date_added"], errors="coerce")
print(df["date_added"])
df["year_added"]= df["date_added"].dt.year
print(df["year_added"])
most_content_year = df["year_added"].value_counts().head(5)
print(f"\n\nthe year had most content are: \n {most_content_year}")

#Step 7 — Most common genres
genre = df["listed_in"].str.split(",").explode().str.strip()
top10 = genre.value_counts().head(10)
print(f"\n\n the splited listed_in columns: \n{genre}")
print(f"\n\n the top10 listed_in columns: \n{top10}")

#Step 8 — Top directors by number of titles
top_10_directors = df[df["director"] !="Unknown"]["director"].value_counts().head(10)
print(f"\n\nThe top 10 directors are: \n {top_10_directors}")

#Step 9 Extract duration numbers
filter_movie = df[df["type"]=="Movie"].copy()
filter_movie["durations_min"]=pd.to_numeric(filter_movie["duration"].str.extract(r'(\d+)')[0],errors='coerce')
durations = filter_movie["durations_min"].dropna().values

mean_dur = np.mean(durations)
max_dur = np.max(durations)
min_dur = np.min(durations)
p25 = np.percentile(durations,25)
p75 = np.percentile(durations,75)

print(f"\n\n Duration: \n {filter_movie['duration']}\n\n mean: \n {mean_dur}\n\n max_dur:\n{max_dur}")
print(f"\n\nmin_dur:\n{min_dur}\n\np25:\n{p25}\n\np75:\n{p75}")

#Step 10 — np.where: Old vs Recent content
df["ContentAge"]= np.where(df["release_year"]>=2015,"Recent","Old")
survived_type = df.groupby("ContentAge")["type"].value_counts()
print(df["ContentAge"])
print(f"\n\nthe type of show survived:\n {survived_type}")

#Step 11 — np.percentile + boolean masking

mask = filter_movie["durations_min"] > p75
long_movie = filter_movie[mask]
top_5 = long_movie.nlargest(5,"durations_min")
print(f"\n\nThe 75th percentile duration: {mask} \n\n  the filtered movies are:\n {long_movie}\n\n top5: \m {top_5}")

#Step 12 — groupby: Average release year by countr
top_10_country_listy = top_country.index.tolist()
filter_dataframe = df[df["country"] .isin(top_10_country_listy)]
average_realse_year = filter_dataframe.groupby("country")["release_year"].mean().round(0).sort_values(ascending=False)
print(f"\n\nTop 10 filter ed country: \n {top_10_country_listy}")
print(f'\n\n Average releasr per year:\n {average_realse_year}')

#Step 13 — crosstab: Type vs Rating

ct = pd.crosstab(df["type"], df["rating"])
print(f"\n\ncrosstab:\n{ct}")

#Step 14 — pivot table: Content count by type and country
pvt = pd.pivot_table(
    filter_dataframe,
    index="country",
    values="title",
    columns="type",
    aggfunc = "count"

)

print(f"\n\n{pvt}")

#Step 15 — Visualizations 🎨

#Chart 1 — Top 10 countries bar chart:
plt.barh(top_country.index,top_country.values)

plt.title("top country by value count")
plt.xlabel("Number of titles")
plt.ylabel("country")

plt.gca().invert_yaxis()
plt.savefig("top_countries.png")
plt.show()

#Chart 2 — Pie chart: Movies vs TV Shows
plt.pie(
    type_count.values,
    labels=type_count.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["pink" ,"yellow"]
)
plt.title(" Movies vs TV Shows distribution")
plt.axis("equal")
plt.savefig("movies_vs_tvshows.png")
plt.show()

#Chart 3 — Bar chart: Top 10 genres
plt.bar(top10.index,top10.values)
plt.xticks(rotation=45,ha="right")
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("top_genres.png")
plt.show()

#Chart 4 — Last one! Bar chart: Content added per year
year_count = df["year_added"].value_counts().sort_index()
plt.bar(year_count.index,year_count.values)
plt.title("Content Added Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_per_year.png")
plt.show()
