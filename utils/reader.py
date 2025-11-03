import pandas as pd


def parse_df(df):
    df = df.iloc[2:].copy()  # .copy()を追加してSettingWithCopyWarningを回避

    df["date"] = df["#年月日"] + " " + df["時刻"]
    # 24:00を00:00に変換し、日付を1日進める
    df["date"] = df["date"].str.replace(" 24:00", " 00:00")
    # 24:00だった行の日付を1日進める処理
    mask = df["時刻"] == "24:00"
    if mask.any():
        # 日付文字列をdatetimeに変換してから1日加算
        temp_dates = pd.to_datetime(df.loc[mask, "#年月日"], format="%Y/%m/%d") + pd.Timedelta(
            days=1
        )
        df.loc[mask, "date"] = temp_dates.dt.strftime("%Y/%m/%d") + " 00:00"
    df = df.drop(columns=["#年月日", "時刻"])
    df.index = pd.to_datetime(df["date"], format="mixed")
    df = df.drop(columns=["date"], axis=1)
    return df
