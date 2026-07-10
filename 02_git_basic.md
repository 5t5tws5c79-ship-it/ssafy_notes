# 🛠️ Git 핵심 기초 및 버전 관리 이해

## 1. 버전 관리의 필요성

소프트웨어 개발에서 **버전 관리(Version Control)**는 파일의 변경 사항을 시간에 따라 기록하고 관리하는 시스템입니다.

- **이력 추적:** 누가, 언제, 왜, 어떤 코드를 수정했는지 명확하게 확인할 수 있습니다.
- **과거로 되돌리기:** 오류가 발생하거나 문제가 생겼을 때 안전했던 이전 버전으로 복원할 수 있습니다.
- **안전한 협업:** 여러 개발자가 동시에 같은 프로젝트를 작업해도 변경 사항을 안전하게 병합(Merge)할 수 있습니다.

---

## 2. 리누스 토르발즈와 Git의 탄생

- **리누스 토르발즈(Linus Torvalds):** 리눅스(Linux) 커널과 Git을 개발한 프로그래머입니다.
- **탄생 배경:** 기존 버전 관리 시스템인 BitKeeper를 사용할 수 없게 되면서, 더 빠르고 효율적인 버전 관리 도구가 필요해졌습니다.
- **Git 개발:** 2005년 약 2주 만에 Git의 핵심 기능을 직접 개발했습니다.
- **Git의 특징**
  - 빠른 속도
  - 분산형 저장소(Distributed Version Control)
  - 강력한 브랜치 및 병합(Merge) 기능
  - 뛰어난 협업 지원

---

# 3. Git의 3가지 핵심 영역

Git은 파일의 상태를 관리하기 위해 내부적으로 3개의 영역을 사용합니다.

## ① Working Directory (워킹 디렉토리)

개발자가 실제로 파일을 생성하고 수정하는 작업 공간입니다.

- 눈에 보이는 프로젝트 폴더
- 파일을 편집하는 공간

```
프로젝트 폴더
├── index.html
├── app.js
└── style.css
```

---

## ② Staging Area (스테이징 영역)

커밋하기 전에 변경 사항을 임시로 보관하는 공간입니다.

- 커밋할 파일을 선택하는 공간
- 일종의 장바구니 역할

```
Working Directory
        │
    git add
        ▼
 Staging Area
```

---

## ③ Repository (레포지토리)

커밋된 파일들이 영구적으로 저장되는 공간입니다.

- 버전이 저장되는 공간
- 프로젝트의 모든 변경 이력이 기록됨

```
Working Directory
        │
    git add
        ▼
 Staging Area
        │
 git commit
        ▼
 Repository
```

---

# 4. 커밋(Commit) == 버전 스냅샷

Git은 파일의 차이점만 저장하는 것이 아니라 **특정 시점의 프로젝트 상태 전체를 스냅샷(Snapshot)** 형태로 저장합니다.

즉,

> **커밋(Commit) = 하나의 완성된 버전**

이라고 이해하면 됩니다.

예를 들어,

```
Commit 1
회원가입 화면 생성

↓

Commit 2
로그인 기능 추가

↓

Commit 3
회원정보 수정 기능 추가
```

각 커밋은 언제든 다시 돌아갈 수 있는 하나의 버전입니다.

---

# 5. 핵심 기본 명령어 4가지

## ① `git init` (저장소 초기화)

현재 작업 중인 디렉토리를 Git 저장소로 초기화합니다.

숨겨진 `.git` 디렉토리가 생성되며 Git이 해당 프로젝트를 관리하기 시작합니다.

```bash
git init
```

### 실행 결과

```bash
Initialized empty Git repository in /Users/user/project/.git/
```

### 언제 사용할까?

- 새로운 프로젝트를 Git으로 관리할 때
- 기존 프로젝트에 Git을 적용할 때

---

## ② `git status` (현재 상태 확인)

현재 Git 저장소의 상태를 확인합니다.

```bash
git status
```

### 실행 결과

```bash
On branch main

No commits yet

Untracked files:
  index.html

nothing added to commit but untracked files present
```

### 확인 가능한 정보

- 현재 브랜치
- 수정된 파일
- 새로 생성된 파일
- 삭제된 파일
- 스테이징 여부
- 커밋 가능 여부

> **Tip**  
> Git을 사용하면서 가장 많이 실행하는 명령어입니다.

---

## ③ `git add` (스테이징)

변경된 파일을 스테이징 영역에 추가합니다.

### 특정 파일 추가

```bash
git add index.html
```

### 모든 변경 사항 추가

```bash
git add .
```

### 동작 과정

```
Working Directory
        │
    git add
        ▼
 Staging Area
```

### 언제 사용할까?

- 커밋할 파일을 선택할 때
- 변경 내용을 버전으로 저장하기 전에 준비할 때

---

## ④ `git commit` (버전 저장)

스테이징된 변경 사항을 하나의 버전으로 저장합니다.

```bash
git commit -m "첫 번째 커밋"
```

### 실행 결과

```bash
[main (root-commit) a2d3f5b] 첫 번째 커밋
1 file changed, 10 insertions(+)
create mode 100644 index.html
```

### 커밋 메시지 작성 예시

```bash
git commit -m "회원가입 기능 추가"
git commit -m "로그인 오류 수정"
git commit -m "README 작성"
```

### 좋은 커밋 메시지 작성 방법

- 변경 내용을 간결하게 작성
- 무엇을 수정했는지 명확하게 작성
- 한 커밋에는 하나의 작업만 포함하는 것이 좋음

---
