import { useNavigate, useLocation } from "react-router"
const BoardView = ()=>{
	const nav = useNavigate()
	const {state} = useLocation()
	const del = () =>{
		return
		// 고유넘버 일치하는 db지우기
	}
    return(
        <>
        <div className="container mt-3">
			<h1 className="display-1 text-center">게시글 상세</h1>
			<form>
				<div className="mb-3 mt-3">
					<label htmlFor="title" className="form-label">제목</label>
					<input type="text" className="form-control" id="title" name="title" readOnly='readonly'
					value={state.title}/>
				</div>
				<div className="mb-3 mt-3">
					<label htmlFor="name" className="form-label">작성자</label>
					<input type="text" className="form-control" id="name" name="name"  readOnly='readonly'
					value={state.name}/>
				</div>
				<div className="mb-3 mt-3">
					<label htmlFor="content" className="form-label">내용</label>
					<textarea type="text" className="form-control h-50" rows="10" id="content" name="content"  
					value={state.content} readOnly='readonly'></textarea>
				</div>
			</form>
			<div className="d-flex">
				<div className="p-2 flex-fill d-grid">
					<button  className="btn btn-primary" onClick={()=>nav('/boardedit', {state: {title: state.title, name:state.name, content: state.content}})}>수정</button>
				</div>
				<div className="p-2 flex-fill d-grid">
					<button onClick={()=>{del, alert("삭제되었습니다.")}} className="btn btn-primary">삭제</button>
				</div>
				<div className="p-2 flex-fill d-grid">
					<button className="btn btn-primary" onClick={()=>nav('/')}>취소</button>
				</div>
			</div>
		</div>
        </>
    )
}

export default BoardView