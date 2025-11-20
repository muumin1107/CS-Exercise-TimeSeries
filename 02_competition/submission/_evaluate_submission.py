import os

import requests

API_URL         = "http://172.16.15.111:5000/evaluate"
SUBMISSION_FILE = "submission.csv"
USER_ID         = ""

def submit_for_evaluation():
    if not os.path.exists(SUBMISSION_FILE):
        print(f"❌ エラー: 提出するファイルが見つかりません: {SUBMISSION_FILE}")
        return

    try:
        with open(SUBMISSION_FILE, 'rb') as f:
            files_to_send = {'file': (SUBMISSION_FILE, f, 'text/csv')}
            data_to_send  = {'user_id': USER_ID}
            response = requests.post(API_URL, files=files_to_send, data=data_to_send, timeout=10)

        try:
            json_response = response.json()
        except requests.exceptions.JSONDecodeError:
            json_response = None

        print("="*30)

        if response.status_code == 200 and json_response:
            print("✅ 評価結果 (Success)")
            print("-"*30)
            mae  = json_response.get('mae', 'N/A')
            rmse = json_response.get('rmse', 'N/A')

            if isinstance(mae, (int, float)): print(f"  MAE : {mae:,.6f}")
            else: print(f"  MAE : {mae}")
            if isinstance(rmse, (int, float)): print(f"  RMSE: {rmse:,.6f}")
            else: print(f"  RMSE: {rmse}")

        else:
            print(f"❌ エラー (Status Code: {response.status_code})")
            print("-"*30)

            if json_response and 'error' in json_response: print(f"  エラーメッセージ: {json_response['error']}")
            elif response.text: print(f"  サーバーからの応答:\n{response.text}")
            else: print("  サーバーから詳細なエラーメッセージを取得できませんでした。")

        print("="*30)

    except requests.exceptions.ConnectionError:
        print("="*30)
        print(f"❌ エラー: サーバーに接続できません。")
        print(f"'{API_URL}' が起動しているか、ネットワーク接続を確認してください。")
        print("="*30)
    except requests.exceptions.Timeout:
        print("="*30)
        print("❌ エラー: リクエストがタイムアウトしました。サーバーが応答していません。")
        print("="*30)
    except Exception as e:
        print(f"❌ 予期せぬエラーが発生しました: {e}")

if __name__ == "__main__":
    submit_for_evaluation()