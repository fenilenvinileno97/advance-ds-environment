import seaborn as sns
import matplotlib.pyplot as plt

def country_cases(countries_set):
    sns.barplot(
        data=countries_set,
        x="value",
        y="country_region",
        palette=countries_set.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");