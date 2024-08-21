import requests
import json

# TeamsのWebhook URL
webhook_url = 'Workflow作成時に発行されたURLを指定'

# 送信するメッセージ
message = {
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.2",
        "body": [
          {
            "type": "TextBlock",
            "text": "## Workflow経由のTeamsへの通知テストです。\n\n* 通知の詳細1です。\n* 通知の詳細2です。",
            "wrap": True,
            "markdown": True
          }
        ]
      }
    }
  ]
}

# POSTリクエストを送信
response = requests.post(
    url=webhook_url,
    data=json.dumps(message),
    headers={'Content-Type': 'application/json'}
)

# レスポンスを確認
if response.status_code == 200 or response.status_code == 202:
    print("メッセージが送信されました")
else:
    print(f"エラーが発生しました: {response.status_code}, {response.text}")
