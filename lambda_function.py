import boto3
import requests
import json
import os

# TeamsのWebhook URL
workflows_url = os.environ["workflows_url"]'Workflow作成時に発行されたURLを指定'
groupId = os.environ["groupId"]
channelId = os.environ["channelId"]

def send_Teams(workflows_url):

    headers = {
      "Content-Type" : "application/json"
    }

    data = {
      "attachments": [
        {
          "groupId": groupId,
          "channelId": channelId,
          "contentType": "application/vnd.microsoft.card.adaptive",
          "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.2",
            "body": [
              {
                "type": "TextBlock",
                "text": "----------------ここに件名を入力----------------",
                "size": "Large",
              },
              {
                "type": "TextBlock",
                "text": "¥n[----ハイパーリンクテキスト----](----https://learn.microsoft.com/ja-jp/power-automate/overview-adaptive-cards----)",
              },
              {
                "type": "TextBlock",
                "text": "----textを入力----",
              },
            ]
          }
        }
      ]
    }


    response = requests.post(url=webhook_url,headers=headers,data=json.dumps(data))
    if response.status_code == 200 or response.status_code == 202:
    print("メッセージが送信されました")
    else:
    print(f"エラーが発生しました: {response.status_code}, {response.text}")

def lambda_handler(event, context);
    
    #------Lambda処理を記載-------

    #------処理が完了したら通知-----
    send_Teams(workflows_url)
