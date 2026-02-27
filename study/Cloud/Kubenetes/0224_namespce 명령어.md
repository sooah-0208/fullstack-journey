# namespace 구성하기

- namespace 목록 보기
```
kubectl get namespaces (ns라고 축약해서 써도 됨)
```
현재 active 되어있는 목록 보여줌

- context 확인
```
kubectl config get-contexts
```
여기서 정의 안 된 namespace는 default임

- namespace 생성하기
```
kubectl create namespace n1(얘는 이름)
이것도 줄여서 ns 가능
```

- yaml 파일 자동 생성하기
```
kubectl create ns n2 --dry-run=client -o yaml > n2-ns.yaml
```
--dry-run=client 실행되는지 문제 없는지 확인해줘
-o 디테일하게 확인
> n2-ns(이름).yaml(확장자)로 파일 생성

- ns 안에 pod 생성
```
kubectl run web --image=nginx:1.28 --port 80 -n n1

실행되는지 확인 후 화면에 출력하기
kubectl run web --image=nginx:1.28 --port 80 -n n1 --dry-run=client -o yaml
```
-n: namespace 지정
**같은 이름의 pod생성**하고싶으면 **다른 ns**에 생성하면 됨

- ns안에 있는 pod 확인하기
```
전부
kubectl get pods --all-namespaces 

지정 ns
kubectl get pods -n n1
```

- namespace 삭제하기
```
kubectl delete ns n1
```
안에 리소스(pod,service등등)이 한번에 삭제되기 때문에 잘 지우지 않음

# 작업중인 ns를 default로 교체하기
config의 context가 namespace를 제어함 => context 조정

1. context 생성
- config 명령어 확인하기
```
kubectl config
```

- 옵션 확인 
```
kubectl config view

출력
apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: DATA+OMITTED
    server: https://kubernetes.docker.internal:6443
  name: docker-desktop
contexts:
- context:
    cluster: docker-desktop
    user: docker-desktop
  name: docker-desktop
current-context: docker-desktop
kind: Config
users:
- name: docker-desktop
  user:
    client-certificate-data: DATA+OMITTED
    client-key-data: DATA+OMITTED
```

- context 생성하기
```
kubectl config set-context n1-context --cluster=docker-desktop --user=docker-desktop --namespace=n1
```

2. default에서 내가 지정한 namespace로 context 교체하기
```
kubectl config use-context n1-context
```

3. context 삭제하기
```
kubectl config delete-context n1-context
```
=> 결과: 내 로컬 환경의 ~/.kube/config 파일에서 n1-context라는 설정 이름만 삭제됨
=> 영향: 더 이상 해당 컨텍스트 이름만 사용 불가함  
        클러스터 내부의 리소스는 그대로 남음.
=> 삭제 후에는 다시 default로 교체해줘야함

- default로 교체하기
```
kubectl config use-context docker-desktop
```

- 클러스터 실행 상태 확인(오류났는지)
```
kubectl cluster-info
```
