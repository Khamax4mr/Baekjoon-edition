from sys import argv
from json import load, JSONDecodeError
from os.path import isfile
from subprocess import Popen, PIPE

Quiz_List_Path = 'path.json'
Read_Mode = 'r'
Quiz_List_Id = 'path'
Example_Id = "examples"
Example_Input_Id = 'inp'
Example_Output_Id = 'out'


# 인자 목록 args에서 문제 번호를 반환합니다.
# 문제 번호가 없으면 0을 반환합니다.
def parse_arg(args):
  try:
    if args[1].isdigit():
      return args[1]
  except IndexError:
    print('명령어: python3 driver.py <문제 번호>')
    print('실패: 문제 번호를 설정하지 않았습니다.')
    return 0

# id 문제 번호에 해당하는 코드 경로, 예제 리스트를 반환합니다.
def get_quiz_data(id):
  wd_path = get_wd_path(id)
  return get_code_path(wd_path), get_examples(wd_path)

# id 문제 번호의 작업 폴더를 반환합니다.
# 작업 폴더가 없으면 None을 반환합니다.
def get_wd_path(id):
  try:
    json = get_json(Quiz_List_Path, Quiz_List_Id)
    return json[id]
  except KeyError:
    print(f'실패: {id}번 문제 번호가 존재하지 않습니다.')
    return None

# path 경로의 json 파일에서 key 키 이름의 정보를 반환합니다.
# 파일을 읽을 수 없거나 정보를 찾을 수 없으면 None을 반환합니다.
def get_json(path, key):
  try:
    with open(path, Read_Mode) as f:
      json = load(f)
      return json[key]
  except FileNotFoundError:
    print(f'실패: {path} 파일을 찾을 수 없습니다.')
    return None
  except IOError:
    print(f'실패: {path} 파일을 읽는 중 오류가 발생했습니다.')
    return None
  except JSONDecodeError:
    print(f'실패: json 형식으로 파싱 중 오류가 발생했습니다.')
    return None
  except KeyError:
    print(f'실패: {key} 키 이름의 데이터가 없습니다.')
    return None

# path 경로의 소스 코드 경로를 반환합니다.
# 파일이 존재하지 않으면 None을 반환합니다.
def get_code_path(path):
  # code_path = f'{path}/code.py'
  code_path = f'{path}/Main.java'
  if isfile(code_path):
    return code_path
  else:
    print(f'경고: {code_path} 파일이 존재하지 않습니다.')
    return None

# path 경로의 예제 리스트를 반환합니다.
# 파일이 존재하지 않으면 None을 반환합니다.
def get_examples(path):
  example_path = f'{path}/examples.json'
  if isfile(example_path):
    return get_json(example_path, Example_Id)
  else:
    return None

# path 경로의 코드를 examples 입력으로 실행합니다.
def run_test(path, examples):
  id = 0
  for example in examples:
    id += 1
    try: 
      inp = example[Example_Input_Id]
      expected = [str(elem) for elem in example[Example_Output_Id]]
      inp_args = str.encode('\n'.join(map(str, inp)))
    
      test = run(path, inp_args).split('\n')
      test = [o for o in test if o]
      print_result(id, inp, test, expected)
    except KeyError:
      print(f'경고: 예제를 확인할 수 없습니다.')

# path 경로의 파일에서 input을 입력하는 동작을 수행하고 출력문을 반환합니다.
def run(path, input):
  # p = Popen(['python3', path], stdin=PIPE, stdout=PIPE)
  p = Popen(['java', path] + input.split(), stdin=PIPE, stdout=PIPE)
  return p.communicate()[0].decode('utf-8')

# 테스트 실행 결과를 출력합니다.
def print_result(id, inp, test_out, expected_out):
  print(f'===== example {id} =====')
  print('input   :', inp)
  print('expected:', expected_out)
  print('test    :', test_out)
  print('result  :', get_result(test_out, expected_out))
  print('')

# 실제 테스트 결과와 예상 테스트 결과를 비교, 반환합니다.
def get_result(test, expected):
  return 'success' if test == expected else 'failure'


def main():
  id = parse_arg(argv)
  src, examples = get_quiz_data(id)
  if src is None or examples is None: return
  run_test(src, examples)

if __name__ == "__main__":
  main()