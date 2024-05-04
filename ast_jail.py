import ast

def secure(code):
  for x in ast.walk(compile(code, "", 'exec', flags=ast.PyCF_ONLY_AST)):
    match type(x):
      case (ast.Call|ast.Import|ast.ImportFrom|ast.Attribute):
        print(f"ERROR: Banned statement {x}")
        return False
  return True

user_input = ''
while True:
  line = input()
  if line == '':
    break
  user_input += line
  user_input += "\n"
  
if(secure(user_input)):
  exec(user_input, {}, {})