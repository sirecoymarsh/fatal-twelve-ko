# 로컬 1회용 (2026-10-02, Claude) — 배포본에 넣지 말 것.
# 플로우 차트 시험 실행이 게임 폴더 saves 를 함께 쓰는 바람에 사용자 환경설정
# 「안 읽은 글도 건너뛰기」(skip_unseen)가 켜졌다. 9월 28일 값(꺼짐)으로 한 번만 되돌린다.
# 한 번 실행된 뒤에는 이 파일을 지워도 된다.
init 999 python:
    if not getattr(persistent, "f12_local_skip_unseen_restored_20261002", False):
        _preferences.skip_unseen = False
        persistent.f12_local_skip_unseen_restored_20261002 = True
