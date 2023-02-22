while True: # 무한 루프
    text = input() # 문자열

    if text == '.': # 입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어온다.
        break

    stack = []
    ispass = True # ' .'일 때의 조건이 없어 True로 전제

    for t in text:
        
        if t == '[' or t == '(': # 여는 괄호 만나면 push
            stack.append(t)

        if t == ']' or t == ')': # 닫는 괄호 만나면 

            if not stack: # 스택이 비어있으면 닫는 괄호가 먼저 나와 순서와 개수가 안 맞음
                ispass = False
                break
            
            if (t == ']' and stack[-1] != '[') or (t == ')' and stack[-1] != '('):
            # 여는 괄호와 닫는 괄호가 짝이 안 맞음 
                ispass = False
                break

            else: # 짝과 순서, 개수가 맞으면 pop
                stack.pop()
                ispass = True
    
    if not stack and ispass == True: # 최종까지 검사했을 때 스택이 비어있거나 True면 균형
        ans = 'yes'
    else: # 아니면 불균형
        ans = 'no'

    print(ans)