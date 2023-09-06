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
    
def null_values_proportion(dataframe):
        (
        dataframe
            .isnull()
            .melt(value_name='missing')
            .pipe(
                lambda df: (
                    sns.displot(
                        data=df,
                        y='variable',
                        hue='missing',
                        aspect=1.75
                    )
                )
            )
    )
        plt.show();
        
def heatmap_null_proportion(dataframe):
        (
        dataframe
            .isnull()
            .T
            .pipe(
                lambda df: (
                    sns.heatmap(
                        data=df
                    )
                )
            )
    )
        plt.show();
        
        
def heatmap_corr(dataframe):
    sns.heatmap(
    data=dataframe.corr(numeric_only=True),
    cmap=sns.diverging_palette(20, 200, as_cmap=True),
    annot=True,
    linewidths=1.5,
    linecolor='white'
    )
    plt.show();