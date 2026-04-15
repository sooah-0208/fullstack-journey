import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "@utils/network"
import Swal from 'sweetalert2'

function Home({ posts, loadingPost, loading }) {
  const navigate = useNavigate();
  const [prompt, setPrompt] = useState("")

  // 게시글 작성 이벤트
  const submitEvent = async (e) => {
    e.preventDefault()
    if (!prompt) return
    try {
      const res = await api.post("/db/insert", { user_input: prompt })
      if (res.data.status) {
        Swal.fire({
          title: "따봉너구리🦝:",
          text: res.data.message,
          icon: 'success',
          confirmButtonText: "알앗다구리"
        })
        setPrompt("")
        await loadingPost()
      }
      else {
        Swal.fire({
          title: "따봉너구리🦝:",
          text: res.data.message,
          icon: 'error',
          confirmButtonText: "알앗다구리"
        }).then((result) => {
          if (result.isConfirmed) setPrompt("")
        })
      }
    } catch (err) {
      console.error("데이터 로딩 실패", err);
    } finally {
      loadingPost()
    }
  }


  return (
    loading ? (<div className="page-container">
      <header className="header"><h1>자유 게시판</h1></header>

      {/* 스피너와 스켈레톤이 공존하는 로딩 화면 */}
      <div className="loading-content">
        <div className="loading-overlay">
          <div className="spinner"></div>
          <p>🦝 따봉너구리가 열심히 집짓는 중이니까 잠시만 기다려달라굿-! 🦝</p>
        </div>
        <div className="board-grid">
          {[1, 2, 3, 4].map(n => (
            <div key={n} className="post-card skeleton-card-with-spinner">
              <div className="mini-spinner"></div>
              <div className="skeleton-content-wrapper">
                <div className="skeleton-title"></div>
                <div className="skeleton-content"></div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>) : (
      <div className="page-container">
        <header className="header">
          <h1>자유 게시판</h1>
        </header>
        <form onSubmit={submitEvent}>
          <input className="agent_input" type="text" value={prompt} onChange={e => setPrompt(e.target.value)}
            placeholder="게시글을 입력하세요. ex) 내 이름은 수아야. AI란 이라는 제목으로 글 써줘. 내용은 지배할 것이다. 라고 써줘" />
          <button type="submit">전송</button>
        </form>
        {
          posts?.length === 0 ? (
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
                  </div>
                  <p className="post-content">{post.content}</p>
                  <footer className="post-footer">
                    <span>{post.user_name}</span>
                    <span className="post-date">{post.date}</span>
                  </footer>
                </article>
              ))}
            </main>
          )}
      </div>
    ))
}

export default Home