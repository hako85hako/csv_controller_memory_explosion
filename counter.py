import sys
import glob
import csv
import traceback


def main(path,offset):
    #テスト用#############################
    #args = sys.argv
    #path = args[1]
    #path=""
    #offset = (8) - 1
    #####################################
    csv_paths = glob.glob(f'{path}/data/*/*.csv')
    #csv読み込み
    try:
        #結果の入子
        item = 0
        if(csv_paths[0]):    
            f = open(csv_paths[0], 'r')
            #headerの取得
            header = next(f)
            #リスト形式
            f = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            for row in f:
                for ch in row:
                    try:
                        item += 1
                    except:
                        return False
                break
        return (item-int(offset)-1)#オフセットは0から計算されてるので、追加で1減算

    except:
        ex = traceback.format_exc()
        print(ex)
        return False

if __name__=="__main__":
    main()