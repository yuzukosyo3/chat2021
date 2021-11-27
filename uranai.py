import time
import random
import IPython
from google.colab import output


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

# アイコンの指定
BOT_ICON = 'https://2.bp.blogspot.com/-mRJKwyORJkQ/Wn1ZTOBrszI/AAAAAAABKKs/Bg5yjLL9RYwmfUM0pEkBA3Ky3ui0IOZWQCLcBGAs/s800/animal_smile_inu.png'
YOUR_ICON = 'https://4.bp.blogspot.com/-SC6_6x7MQnc/Wn1ZUkdcPxI/AAAAAAABKK8/qqHVlc8E7lEGsEwJ_J8H6Gp9RvfhTX67wCLcBGAs/s800/animal_smile_neko.png'

def run_chat(chat = chat, start='占いするよ', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', 'ボット')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 10px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)


    
    
    
#ここから変更

import re
import random


def safe_int(c):
    if '0' <= c <= '9':
        return int(c)
    return 0


def soulnumber(s):
  while len(s) > 1:
    s = str(sum(int(x) for x in s))
    if int(s) % 11 == 0:
      return s
  return s

def birthday(date):
    matched = re.findall(r'(\d\d\d\d)[/年-]?(\d?\d)[/月-]?(\d?\d)[/日-]?', date)
    if len(matched) > 0:
        year, month, day = matched[0]
        return year+month+day
    if not date.isdigit():
        return 0
    return date


#ソウルナンバーの結果
SN = {1:'あなたは、行動力抜群で明朗快活な人です！',
      2:'あなたは、頼りになるリーダーです！',
      3:'あなたは、穏やかな平和主義です！',
      4:'あなたは、積極的でパワー溢れる人です！',
      5:'あなたは、真面目で誠実な人です！',
      6:'あなたは、社交的で人望を集める人です！',
      7:'あなたは、感受性が強く繊細な人です！',
      8:'あなたは、純粋で几帳面な人です！',
      9:'あなたは、無邪気な寂しがり屋です！',
      11:'あなたは、直感で人が何を考えているか、どういう人か察知することができる鋭い感受性のある人です！',
      22:'あなたは、しっかりと準備をしてから行動したり、冷静な分析力や大胆な行動力がある人です！',
      33:'あなたは、カリスマ性を持っていて、人々を魅了するスターの中のスターです！',
      44:'あなたは、鋭い考えを持っているキレ者で、乗り越えられる重責を負う人です！'}

#ポジティブになる言葉
pword = ['笑う門には福来る', '失敗は成功のもと', '雲の上はいつも晴れ', 
        '雨の後にはいい天気がやって来る', '明るい方へ　明るい方へ']

frame = {}

def uranai(input_text):
  global frame
  global SN
  global pword
  if 'asking' in frame: 
    frame[frame['asking']] = input_text
    del frame['asking']

  if 'birthday' not in frame:
    frame['asking'] = 'birthday' 
    return 'あなたの誕生日は？'

  if 'birthday' in frame:
    date = birthday(frame['birthday'])
    if date == 0:
      return random.choice(pword)
    return SN[int(soulnumber(date))]
  return output_text

run_chat(chat=uranai)
