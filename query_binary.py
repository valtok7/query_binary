import pyvisa
import argparse

def query_and_save_binary_data(resource, query_command, output_file_path):
    try:
        # VISA ResourceManagerを作成
        rm = pyvisa.ResourceManager()
        
        # 計測器に接続
        instrument = rm.open_resource(resource)
        
        # クエリを送信してバイナリデータを取得
        binary_data = instrument.query_binary_values(query_command, datatype='b', is_big_endian=True)
        
        # バイナリデータをファイルに保存
        with open(output_file_path, 'wb') as output_file:
            output_file.write(bytearray(binary_data))
        
        print(f"バイナリデータを {output_file_path} に保存しました。")
        
    except pyvisa.Error as e:
        print(f"VISAエラー: {e}")
    except Exception as e:
        print(f"エラー: {e}")
    finally:
        # 接続を閉じる
        instrument.close()

def main():
    """
    usage    
    :param arg1: VISA resource string
    :param arg2: Query command
    :param arg3: Path to save the binary data file
    example
    python your_script.py "TCPIP0::192.168.1.100::inst0::INSTR" "DATA?" "output_data.dat"
    """
    parser = argparse.ArgumentParser(description="Query a VISA instrument and save binary data to a file.")
    
    parser.add_argument("resource", type=str, help="VISA resource string for the instrument")
    parser.add_argument("query_command", type=str, help="Query command to send to the instrument")
    parser.add_argument("output_file_path", type=str, help="Path to save the binary data file")
    
    args = parser.parse_args()
    
    # 関数を呼び出してバイナリデータを取得し、ファイルに保存
    query_and_save_binary_data(args.resource, args.query_command, args.output_file_path)

if __name__ == "__main__":
    main()
