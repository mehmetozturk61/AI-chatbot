import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("GPT2_test.xlsx")

metrics = ['clarity', 'coherence', 'factual_accuracy', 'fluency', 'conciseness', 'originality']
parameters = ['temperature', 'top_k', 'max_length']

for varied_param in parameters:
    fixed_params = [p for p in parameters if p != varied_param]

    print(f"\n=== Averages by '{varied_param}' (other params fixed) ===")
    avg_df = df.groupby(varied_param)[metrics].mean()
    print(avg_df.round(3))

    from scipy.stats import linregress

    print("\nLinear Regression Slopes:")
    for metric in metrics:
        x = avg_df.index.values
        y = avg_df[metric].values
        if len(x) > 1:
            slope, intercept, r_value, p_value, std_err = linregress(x, y)
            print(f"{metric:20s} | Slope: {slope:.4f} | R²: {r_value**2:.4f}")
        else:
            print(f"{metric:20s} | Not enough data points for regression.")

    plt.figure(figsize=(15, 10))
    plt.suptitle(f"Effect of {varied_param} on different matrices (with other parameters fixed)", y=1.02)

    for i, metric in enumerate(metrics, 1):
        plt.subplot(2, 3, i)

        groups = df.groupby(fixed_params)
        for (fixed_val1, fixed_val2), group in groups:
            label = f"{fixed_params[0]}={fixed_val1}, {fixed_params[1]}={fixed_val2}"
            sns.lineplot(data=group, x=varied_param, y=metric, label=label)

        plt.title(metric)
        plt.xlabel(varied_param)
        plt.ylabel("Score")
        plt.ylim(0, 5)

        if i != 1:
            plt.legend().remove()
        else:
            plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    
    plt.tight_layout()
    # plt.savefig(f"{varied_param}_analysis.png", bbox_inches="tight")
    plt.close()

print("Analysis complete! Check the generated PNG files.")