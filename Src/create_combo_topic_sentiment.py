import pandas as pd


file_path_input = "../Data/annotatedTweets/annotated_complete_table_comp_598-sample2OfSize1000.csv"
file_path_output = "../Data/annotatedTweets/combo_annotated_complete_table_comp_598-sample2OfSize1000.csv"


def main():
    df = pd.read_csv(file_path_input);
    df["combo"] = df["topic"].astype(str) + df["sentiment"]

    df.to_csv(file_path_output, index=False)


if __name__ == '__main__':
    main()