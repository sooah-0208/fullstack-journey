import { useState } from "react"
import { useNavigate } from "react-router"
import list from '../data.js'


const Home=()=>{
	const [search,setSearch]=useState('')
	  const research = list.filter(v =>v.title.toLowerCase().includes(search.toLowerCase()))
	  
	const key = localStorage.getItem('key')
    const nav = useNavigate()
    return(
        <>
		<div className="container mt-3">
			<h1 className="display-1 text-center">게시판</h1>
			<div className="d-flex justify-content-between align-items-center mt-4">
				<div className="btn-group">
					<button className="btn btn-primary" onClick={()=>{if(key){nav('/boardadd')}}}>게시글 작성</button>
				</div>
				<form className="d-flex" style={{ maxWidth: '300px' }}>
					<input className="form-control me-2" type="search" placeholder="검색어를 입력하세요"
					onChange={(e)=>setSearch(e.target.value)}/>
					<button className="btn btn-outline-dark" type="submit">Search</button>
				</form>
			</div>
			<table className="table table-hover mt-3 text-center">
				<thead className="table-dark">
					<tr>
						<th>no</th>
						<th>게시글</th>
						<th>작성자</th>
					</tr>
				</thead>
				<tbody>
					{
						research?.map((v,i)=>(
						<tr key={i} className="cursor-pointer" onClick={()=>{nav('/boardview',{state:{title: v.title, name: v.name, content: v.content}})}}>
						<td>{v.no}</td>
						<td>{v.title}</td>
						<td>{v.name}</td>
						</tr>
						))
					}
				</tbody>
			</table>

			<nav aria-label="Page navigation example">
				<ul className="pagination justify-content-center mt-4">
					<li className="page-item">
						<a className="page-link" href="#" aria-label="Previous">
							<span aria-hidden="true">&laquo;</span>
						</a>
					</li>
					<li className="page-item"><a className="page-link" href="#">1</a></li>
					<li className="page-item"><a className="page-link" href="#">2</a></li>
					<li className="page-item"><a className="page-link" href="#">3</a></li>
					<li className="page-item">
						<a className="page-link" href="#" aria-label="Next">
							<span aria-hidden="true">&raquo;</span>
						</a>
					</li>
				</ul>
			</nav>
		</div></>
    )
}

export default Home

