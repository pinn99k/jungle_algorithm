## 5. VSCode에서 해당 프로젝트 폴더 열기

1. VSCode를 실행
2. `파일 → 폴더 열기`로 방금 클론한 `data_structures_docker` 폴더를 선택
---

## 6. 개발 컨테이너: 컨테이너에서 열기


1. VSCode에서 `Ctrl+Shift+P` (Windows/Linux) 또는 `Cmd+Shift+P` (macOS)를 누릅니다.
2. 명령어 팔레트에서 `Dev Containers: Reopen in Container`를 선택합니다.
3. 이후 컨테이너가 자동으로 실행되고 빌드됩니다. 처음 컨테이너를 열면 빌드하는 시간이 오래걸릴 수 있습니다. 빌드 후, 프로젝트가 **컨테이너 안에서 실행됨**.

---

## 7. C 파일에 브레이크포인트 설정 후 디버깅 (F5)
이제 본격적으로 문제를 풀 시간입니다. `README.md` 파일을 참조하셔서 Linked List -> Stack and Queue -> Binary Tree -> Binary Search Tree 순으로 문제를 풀어보세요. 각 문제 폴더에는 pdf형태로 문제 설명이 있습니다.

C 언어로 문제를 풀다가 디버깅이 필요하시면 소스코드에 BreakPoint를 설정한 뒤에 키보드에서 `F5`를 눌러 디버깅을 시작할 수 있습니다.   
* 참고로 변수, 메모리, 스택, 출력 등을 VSCode에서 확인할 수도 있습니다.

---

연습 순서는 연결 리스트 → 스택과 큐 → 이진 트리 → 이진 탐색 트리 순서를 권장합니다.

각 문제를 푸는 단계: 문제지에서 요구사항 읽기 → 해당 메인 프레임을 찾아 C 컴파일러(예: Code::Blocks)에 복사 → 함수 부분 직접 작성 → 컴파일 후 테스트 케이스 입력해보기

각 문제의 메인 프레임(뼈대 코드)이 제공되며, 함수 부분은 비워져 있으므로 직접 작성해서 완성하면 됩니다. POP/PUSH/DEQUEUE/ENQUEUE/REMOVE_LINKED_NODE/FIND_LINKED_NODE 같은 기본 기능은 메인 프레임에 이미 구현되어 있으므로 별도로 작성할 필요 없습니다.

이 문제들은 자료구조의 기초만 다루지만, CS라는 새로운 세계로 들어가는 열쇠가 될 수 있습니다. 이 문제들을 다 풀고 나면 자료구조가 무엇인지 대략적인 그림을 갖게 될 것입니다.

---

The practicing sequence could be `Linked List` -> `Stack n Queue` -> `Binary Tree` -> `Binary Search Tree`.


Approperiate `steps` to do each question: **Read the question's requirement in question sheet -> Find the corresponding main frame and copy it to your C compiler, i.e. Code::Block -> Finish the function part -> Try compiling and input some test cases.**
***

The main frames of each question are provided such that the function part is left empty for you to write and fill in the blank to complete the question. Basic functionalities like `POP/PUSH/DEQUEUE/ENQUEUE/REMOVE_LINKED_NODE/FIND_LINKED_NODE` are already provided in the main frame. You don't need to write these basic functions.

These questions only illustrate some basis of Data Structure. However, they can be your keys of the door to new world of CS. After finishing these questions, you may have a brief view of what the Data Structure is.

---

