from myJson.myJson import MyJson
from myUrllib.urllib_base_use import urllib_base_use
from myUrllib.urllib_download import urllib_download

if __name__ == "__main__":
#    ulbase =  urllib_base_use()
#    ulbase.open_url("https://www.faned.xyz/forum-4.htm")
   urllib_download().download('//www.douyin.com/aweme/v1/play/?video_id=v0d00fg10000clkskfbc77uc84m8iu10&line=0&file_id=6dfa2aafc87c43bd8c5ec8542c1109bf&sign=f38efbef1996c9473b17ddfed1f49d0c&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383','1.mp4')