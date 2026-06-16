# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20809 변지예
# 프로젝트 주제: DNA 염기쌍 결합 문제 확인 및 코돈 번역 프로그램 

codon_name = [
    ["ATG", "메티오닌"],
    ["ATC", "이소류신"],
    ["CCC", "프롤린"],
    ["GTG", "발린"],
    ["AAA", "리신"],
    ["ACG", "트레오닌"],
    ["CTC", "류신"],
    ["TTT", "페닐알라닌"],
    ["GCA", "알라닌"],
    ["TAA", "종결코돈"]
]


def translate_codon(dna_fragment):
    for row in codon_name:
        if row[0] == dna_fragment:
            return row[1]
    return "알수없는아미노산"


print("=== DNA 검사 및 코돈 번역 프로그램 ===")

dna_strand1 = input("첫 번째 DNA 가닥을 입력하세요: ").upper()
dna_strand2 = input("두 번째 DNA 가닥을 입력하세요: ").upper()


if len(dna_strand1) != len(dna_strand2):
    print("\n[1단계 실패] 두 가닥의 글자 수가 다릅니다. 프로그램을 종료합니다.")

else:
    print("\n[1단계 통과] 두 가닥의 글자 수가 일치합니다. 2단계로 진행합니다.")
    print("=" * 50)
    
    
    print("[2단계 진행] 염기쌍 상보적 결합 규칙 검사 중...")
    
    dna_pairs = {"A": "T", "T": "A", "C": "G", "G": "C"}
    pairing_error = False

    for i in range(len(dna_strand1)):
        if dna_pairs[dna_strand1[i]] != dna_strand2[i]:
            pairing_error = True

    
    if pairing_error == True:
        print("[2단계 실패] 잘못 결합된 염기쌍이 있습니다. 프로그램을 종료합니다.")
        
    else:
        print("[2단계 완료] 모든 염기쌍 결합이 정상입니다. 3단계로 진행합니다.")
        print("=" * 50)
        
        
        print("[3단계 진행: 최종 코돈 번역 결과]")

        dna_temp = dna_strand1

        while len(dna_temp) >= 3:
            codon = dna_temp[0:3]
            amino_acid = translate_codon(codon)
            
            
            print(f"코돈: {codon} / 아미노산: {amino_acid}")
            
            dna_temp = dna_temp[3:]