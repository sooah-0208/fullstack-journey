const Login = ()=>{
    return (
        <div clsaaName="container mt-3">
			<h1 clsaaName="display-1 text-center">로그인</h1>
			<form>
				<div clsaaName="mb-3 mt-3">
					<label htmlFor="email" clsaaName="form-label">이메일</label>
					<input type="email" clsaaName="form-control" id="email" placeholder="이메일를 입력하세요." name="email"/>
				</div>
				<div clsaaName="mb-3">
					<label htmlFor="pwd" clsaaName="form-label">비밀번호</label>
					<input type="password" clsaaName="form-control" id="pwd" placeholder="비밀번호를 입력하세요." name="pwd"/>
				</div>
			</form>
			<div clsaaName="d-flex">
				<div clsaaName="p-2 flex-fill d-grid">
					<a href="../index.html" clsaaName="btn btn-primary">로그인</a>
				</div>
				<div clsaaName="p-2 flex-fill d-grid">
					<a href="../index.html" clsaaName="btn btn-primary">취소</a>
				</div>
			</div>
		</div>
    )
}

export default Login