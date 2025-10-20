from json import load
from pathlib import Path
from subprocess import Popen, PIPE
from sys import argv, exit
from typing import Collection, Union


# 고정 경로.
QUIZ_PATH = "./path.json"


# 경로 path의 JSON 형식 딕셔너리를 반환합니다.
def load_json(path: Path) -> dict:
  try:
    with open(path, 'r') as f:
      return load(f)
  except FileNotFoundError:
    print("driver:", path, "존재하지 않는 파일입니다.")
    return {}


# 경로 path의 파이썬 코드를 args 매개 변수로 실행합니다.
def run(path: Path, args: bytes) -> str:
  p = Popen(['python3', path], stdin=PIPE, stdout=PIPE)
  return p.communicate(input=args)[0].decode('utf-8')


def main():
  # 입력 받은 인자 설정.
  try:
    id = argv[1]
  except IndexError:
    print("driver:", "인자를 찾을 수 없습니다.", "프로그램을 실행하려면 다음 명령을 입력하세요.")
    print("\t", "python3 driver.py [문제 번호]")
    exit(0)

  quiz_path = Path(load_json(QUIZ_PATH).get(id, ""))
  example_path = quiz_path/"examples.json"
  code_path = quiz_path/"code.py"
  
  # 예제 가져오기.
  examples = load_json(example_path)
  if not isinstance(examples, Collection):
    print("driver:", example_path, "예제를 찾을 수 없습니다.")
    exit()
  
  id = 0
  for example in examples:
    # 입출력, 인자 설정.
    id += 1
    inps, outs = example['inp'], example['out']
    args = str.encode('\n'.join(map(str, inps)))
    expects = [str(elem) for elem in outs]

    # 테스트 수행.
    test_out = run(code_path, args).split('\n')
    test_out = [out for out in test_out if out]

    # 실행 결과 출력.
    result = (expects == test_out)
    print('=====', 'example', id, '=====')
    print('input:', inps)
    print('expected output:', expects)
    print('test output:', test_out)
    print('test result:', 'success' if result else 'failure')
    print()


if __name__ == "__main__":
  main()