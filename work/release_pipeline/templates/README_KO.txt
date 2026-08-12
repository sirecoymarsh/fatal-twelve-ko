Fatal Twelve 한국어 패치 (트랜잭션 설치 패키지)

이 패키지에는 컴파일된 .rpyc 파일만 들어 있습니다. 원본 게임 아카이브와 실행 파일은 포함하지 않습니다.

설치
1. 게임을 종료합니다.
2. Windows PowerShell 5.1에서 다음처럼 실행합니다.
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-KoreanPatch.ps1 -GameRoot "게임 폴더"
3. INSTALL PASS가 표시되었는지 확인합니다.

복원
1. 게임을 종료합니다.
2. 같은 위치에서 다음처럼 실행합니다.
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Restore-KoreanPatch.ps1 -GameRoot "게임 폴더"
3. RESTORE PASS가 표시되었는지 확인합니다.

설치기는 패키지 파일과 지원 대상 원본의 SHA-256을 먼저 검사합니다. 백업, 상태, 복구 사본은 기본적으로 사용자 LocalAppData의 서로 분리된 외부 폴더에 저장되며 게임/패키지 폴더 안에는 저장되지 않습니다. 원본 또는 패키지가 알려진 해시와 다르면 설치·복원을 시작하지 않습니다.

ZIP 파일 자체의 SHA-256은 ZIP 옆의 .sha256 파일에서 확인할 수 있습니다.
