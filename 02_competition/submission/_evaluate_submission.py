import requests
import os

# 評価APIサーバーのアドレス
API_URL = "http://XXX.XXX.XXX.XXX:XXXX/evaluate"

# 提出するCSVファイル名
SUBMISSION_FILE = "test_submission.csv"

def submit_for_evaluation():
    """
    APIサーバーに予測CSVファイルをPOST送信し、評価結果を受け取る
    """
    
    # 1. ファイルの存在確認
    if not os.path.exists(SUBMISSION_FILE):
        print(f"❌ エラー: 提出するファイルが見つかりません: {SUBMISSION_FILE}")
        return

    try:
        # 2. ファイルをバイナリモード('rb')で開く
        with open(SUBMISSION_FILE, 'rb') as f:
            
            # 3. APIが要求する 'file' というキーでファイルを準備
            files_to_send = {
                'file': (SUBMISSION_FILE, f, 'text/csv')
            }
            
            # 4. POSTリクエストの実行 (タイムアウトを10秒に設定)
            response = requests.post(API_URL, files=files_to_send, timeout=10)

        # 5. レスポンスの処理
        
        # サーバーからの応答をJSONとして解析試行
        try:
            json_response = response.json()
        except requests.exceptions.JSONDecodeError:
            # JSONデコードに失敗した場合 (例: 500エラーでHTMLが返る)
            json_response = None

        print("\n" + "="*30)
        
        if response.status_code == 200 and json_response:
            # 成功時 (200 OK)
            print("✅ 評価結果 (Success)")
            print("-"*30)
            
            # JSONから各キーの値を取得し、整形して表示
            mae = json_response.get('mae', 'N/A')
            rmse = json_response.get('rmse', 'N/A')
            rows = json_response.get('common_rows_evaluated', 'N/A')

            # f-stringのフォーマット機能で小数点以下の桁数を揃える
            print(f"  MAE : {mae:,.6f}")
            print(f"  RMSE: {rmse:,.6f}")
            
        else:
            # エラー時 (429, 400, 500 など)
            print(f"❌ エラー (Status Code: {response.status_code})")
            print("-"*30)
            
            if json_response and 'error' in json_response:
                # APIがJSON形式でエラーメッセージを返した場合
                print(f"  エラーメッセージ: {json_response['error']}")
            elif response.text:
                # JSON形式でない場合 (HTMLのエラーページなど) はテキストをそのまま表示
                print(f"  サーバーからの応答:\n{response.text}")
            else:
                print("  サーバーから詳細なエラーメッセージを取得できませんでした。")
        
        print("="*30)

    except requests.exceptions.ConnectionError:
        print("\n" + "="*30)
        print(f"❌ エラー: サーバーに接続できません。")
        print(f"'{API_URL}' が起動しているか、ネットワーク接続を確認してください。")
        print("="*30)
    except requests.exceptions.Timeout:
        print("\n" + "="*30)
        print("❌ エラー: リクエストがタイムアウトしました。サーバーが応答していません。")
        print("="*30)
    except Exception as e:
        print(f"\n❌ 予期せぬエラーが発生しました: {e}")

# --- スクリプトの実行 ---
if __name__ == "__main__":
    submit_for_evaluation()