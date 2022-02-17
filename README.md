# はじめに
最初は身近な植物（個人的に）である稲の病気判別を行う機械学習プログラムを作成し，Flaskで機械学習ウェブアプリケーションとして開発し，LAN内のコンピューターから利用できるようにする方針である．
また，ゼミでの研究でいちごを育てる予定であることから，稲でプロトタイピングしてみた．
# 機械学習について
今回は，利用したデータセットが稲が健康か健康でないかで写真を分けてあったので，教師あり学習を用いて学習させた，(Keras)
Classificationで分類機を作成．



# 使い方
こちらのリポジトリにはmodel1.h5が含まれていないので，それをダウンロード，もしくはclassification.ipynbを用いて，それを作成する必要があります．

modelは[こちらから](https://drive.google.com/file/d/1NeQAlBGmod3o64BMRRcABiVawiew9kBT/view?usp=sharing)
<img width="562" alt="f50530b5a311f0b0b27fe5bdc62ab863" src="https://user-images.githubusercontent.com/37261985/136337457-df4bfc25-ee4e-4e08-b193-c735a95aacd8.png">



# 数値について
しっかりと正答率が出るようになっている．数値が高ければ高いほど病気がある可能性が高い．

# コードの役割
server.py:flaskサーバを起動しています
image_process.py:image_process上で画像解析をさせています．その結果をserver.pyに送る役割
dilution_img:画像を増やすために使います（データが少ない時に利用する）
classification.ipynb:分類器を作るのに使います

# 使い方
必要なライブラリ等をpipコマンドで導入し，
```python3 server.py```で利用できます

# 参考サイト

https://qiita.com/3BMKATYWKA/items/52d1c838eb34133042a3
