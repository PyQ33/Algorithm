# 행렬곱 모든 matrix

def productMatrix(A, B):
        gop = 0
        result = 0
        an = []
        for k in range(2):
            answer = []  # 행렬을 2개씩 나누기 위해 초기화기준을 잡았습니다.

            for i in range(0, 2):
                result = 0  # 곱한 수를 더하면 바로 초기화합니다(안그럼 더한수가 계속 누적됩니다)
                for j in range(0, 2):
                    gop = (A[k][j] * B[j][i])  # 위에서 보았던 행렬곱셈의 핵심 공식
                    print('k   j   i')
                    print('{}   {}   {}'.format(k, j, i))
                    print('{}   {}   {}'.format(A[k][j], B[j][i], gop))
                    print('===================================')
                    result = result + gop  # 행렬을 곱하자마자 값을 더합니다.
                    print('result: {}'.format(result))
                answer.append(result)  # 곱한수 2개를 더하면 바로 추가해줍니다.
            an.append(answer)  # 값이 6번째줄에서 초기화 되기 때문에 따로 저장합니다.

        return an

    # 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print("결과 : {}".format(productMatrix(a, b)))