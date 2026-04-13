import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "@utils/network"

function Home() {
  const navigate = useNavigate();
  const {name, setName} = useState('')
  const {title, setTitle} = useState('')
  const {content, setContent} = useState('')
  const {posts, setPosts} = useState([])
  useEffect(()=>{
    api.get("/board/")
    .then(res=>{
        if(res.data.status){
            data = res.data.data
            setPosts(data)
            setName(data.user_name)
            setTitle(data.title)
            setContent(data.content)
        }
    })
  },[])
  return (
    <div className="page-container">
      <header className="header">
        <h1>자유 게시판</h1>
      </header>
      <form>
      <input type="text" placeholder="게시글을 입력하세요. ex) 내 이름은 수아야. AI란 이라는 제목으로 글 써줘. 내용은 지배할 것이다. 라고 써줘" />
      </form>
      {
      posts.length === 0 ? (
        <div className="empty-state">
          <p>게시글이 없습니다.</p>
        </div>
      ) : (
        <main className="board-grid">
          {posts.map((post) => (
            <article 
              key={post.id} 
              className="post-card clickable"
              onClick={() => navigate(`/board/${post.id}`)}
            >
              <div className="post-header">
                <h2 className="post-title">{post.title}</h2>
                <span className="post-badge">{post.tag}</span>
              </div>
              <p className="post-content">{post.content}</p>
              <footer className="post-footer">
                <span>{post.author}</span>
                <span className="post-date">{post.date}</span>
              </footer>
            </article>
          ))}
        </main>
      )}
    </div>
  );
}

export default Home