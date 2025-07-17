import pandas as pd
from sklearn.preprocessing import LabelEncoder

def clean_data(file, options):
    df = pd.read_csv(file)
    original_shape = df.shape
    dropped_cols = []

    

    # 2. Drop duplicates
    if options.get("drop_dupes"):
        df = df.drop_duplicates()

    # 3. Handle missing values
    if options.get("handle_missing"):
        for col in df.columns:
            if df[col].dtype == "object":
                mode_value = df[col].mode()
                if not mode_value.empty:
                    df[col] = df[col].fillna(mode_value[0])
            else:
                df[col] = df[col].fillna(df[col].mean())

    # 4. Remove outliers using IQR
    if options.get("apply_iqr"):
        for col in df.select_dtypes(include=["int64", "float64"]):
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            df = df[~((df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR))]

    # 5. Label encode categoricals
    if options.get("encode_labels"):
        enc = LabelEncoder()
        for col in df.select_dtypes(include="object"):
            df[col] = enc.fit_transform(df[col].astype(str))

    report = {
        "Original Shape": original_shape,
        "Final Shape": df.shape,
        "Dropped Duplicates": options.get("drop_dupes"),
        "Missing Value Imputation": options.get("handle_missing"),
        "Outliers Removed (IQR)": options.get("apply_iqr"),
        "Categoricals Encoded": options.get("encode_labels")
    }

    return df, report
