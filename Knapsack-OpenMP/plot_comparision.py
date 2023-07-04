import pandas as pd
import matplotlib.pyplot as plt
import sys

#TODO:
Row = 0
Time = 0
Speed = 0
Block = 1


if Time == 1:
#---time---

    filepath = sys.argv[1]
    # 讀取excel檔案
    # 讀取文件並輸出前幾行的內容
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines[:10]:  # 修改這裡的數字來改變顯示的行數
        print(line)


    df = pd.read_csv(filepath, sep="\s+", skip_blank_lines=True, skiprows=1, header=None)


    # 設置欄位名稱
    df.columns = ["Method", "Result", "ProblemSolvingTime", "TotalTime", "Nthreads"]

    # 將資料型別轉換為正確的型態
    df['Nthreads'] = df['Nthreads'].astype(int)
    df['TotalTime'] = df['TotalTime'].astype(float)

    # 使用pandas內建的plot函數，基於Method欄位進行分組並繪製折線圖
    for name, group in df.groupby("Method"):
        plt.plot(group["Nthreads"], group["TotalTime"], label=name)

    # 添加標題和軸標籤
    plt.title('TotalTime by Method and Nthreads')
    plt.xlabel('Nthreads')
    plt.ylabel('TotalTime')
    plt.legend()
    plt.grid(axis='x')

    # 顯示圖表
    plt.savefig('Time_compare.png')
    plt.show()


elif Speed == 1:
#---speed---

    filepath = sys.argv[1]
    # 讀取excel檔案
    # 讀取文件並輸出前幾行的內容
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines[:10]:  # 修改這裡的數字來改變顯示的行數
        print(line)


    df = pd.read_csv(filepath, sep="\s+", skip_blank_lines=True, skiprows=1, header=None)


    # 設置欄位名稱
    df.columns = ["Method", "Result", "Speedup1", "Speedup", "Nthreads"]

    # 將資料型別轉換為正確的型態
    df['Nthreads'] = df['Nthreads'].astype(int)
    df['Speedup'] = df['Speedup'].astype(float)

    # 使用pandas內建的plot函數，基於Method欄位進行分組並繪製折線圖
    for name, group in df.groupby("Method"):
        plt.plot(group["Nthreads"], group["Speedup"], label=name)

    # 添加標題和軸標籤
    plt.title('Speedup by Method and Nthreads')
    plt.xlabel('Nthreads')
    plt.ylabel('Speedup')
    plt.legend()
    plt.grid(axis='x')

    # 顯示圖表
    plt.savefig('Speedup_compare.png')
    plt.show()

elif Row == 1:
    # 读取csv文件
    filepath = sys.argv[1]
    df = pd.read_csv(filepath, sep="\s+", skip_blank_lines=True, skiprows=1, header=None)
    df.columns = ["Method", "Result", "ProblemSolvingTime", "TotalTime", "ROWS"]
    print(df)


    # Convert ROWS column to integer
    df['ROWS'] = df['ROWS'].astype(int)

    # Filter the dataframe to only include the desired values
    df = df[df['ROWS'].isin([32, 64, 128, 256])]

    # Sort the dataframe by the ROWS column
    df = df.sort_values(by='ROWS')

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(df)), df['TotalTime'], tick_label=df['ROWS'], width=0.3)
    plt.plot(range(len(df)), df['TotalTime'], marker='o', color='red')

    # Configure plot
    # plt.xlabel('ROWS')
    # plt.ylabel('TotalTime')
    # plt.title('TotalTime per ROWS')
    # plt.xticks([32, 64, 128, 256], ['32', '64', '128', '256'])
    # Configure plot
    plt.xlabel('ROWS')
    plt.ylabel('TotalTime')
    plt.title('TotalTime per ROWS')

    # 保存图表
    plt.savefig('Rows_compare.png')
    plt.show()

elif Block == 1:
    filepath = sys.argv[1]
    # 讀取excel檔案
    # 讀取文件並輸出前幾行的內容
    with open(filepath, 'r') as f:
        lines = f.readlines()

    for line in lines[:10]:  # 修改這裡的數字來改變顯示的行數
        print(line)


    df = pd.read_csv(filepath, sep="\s+", skip_blank_lines=True, skiprows=1, header=None)


    # 設置欄位名稱
    df.columns = ["Block", "Result", "ProblemSolvingTime", "TotalTime", "Nthreads"]

    # 將資料型別轉換為正確的型態
    df['Nthreads'] = df['Nthreads'].astype(int)
    df['TotalTime'] = df['TotalTime'].astype(float)

    # 使用pandas內建的plot函數，基於Method欄位進行分組並繪製折線圖
    for name, group in df.groupby("Block"):
        plt.plot(group["Nthreads"], group["TotalTime"], label=name)

    # 添加標題和軸標籤
    plt.title('TotalTime by Block and Processes')
    plt.xlabel('Processes')
    plt.ylabel('TotalTime')
    plt.legend()
    plt.grid(axis='x')

    # 顯示圖表
    plt.savefig('Block_compare.png')
    plt.show()