import { useState } from "react"
import { useNavigate } from "react-router"

const BoardAdd = ()=>{
	const [title, setTitle]=useState('')
	const [content, setContent]=useState('')
	const nav = useNavigate()
	const onclick = ()=>{
		const result={'제목':title, '내용':content}
		console.log(result)
	}
    return(
        <>
        <div className="container mt-3">
			<h1 className="display-1 text-center">게시글 작성</h1>
			<form>
				<div className="mb-3 mt-3">
					<label htmlFor="title" className="form-label">제목</label>
					<input type="text" className="form-control" id="title" placeholder="제목을 입력하세요." name="title"
					value={title} onChange={(e)=>(setTitle(e.target.value))}/>
				</div>
				<div className="mb-3 mt-3">
					<label htmlFor="name" className="form-label">작성자</label>
					<input type="text" className="form-control" id="name" name="name" disabled/>
				</div>
				<div className="mb-3 mt-3">
					<label htmlFor="content" className="form-label">내용</label>
					<textarea type="text" className="form-control h-50" rows="10" placeholder="내용을 입력하세요." name="content"
					value={content} onChange={(e)=>(setContent(e.target.value))}></textarea>
				</div>
				<div className="d-flex">
					<div className="p-2 flex-fill d-grid">
						<button type="button" className="btn btn-primary" onClick={()=>onclick()}>등록</button>
					</div>
					<div className="p-2 flex-fill d-grid">
						<button className="btn btn-primary" onClick={()=>nav('/')}>취소</button>
					</div>
				</div>
			</form>
		</div>
        </>
    )
}

export default BoardAdd