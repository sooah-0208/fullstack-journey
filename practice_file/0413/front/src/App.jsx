import { Routes, Route } from 'react-router-dom';
import '@styles/App.css';
import BoardList from '@pages/boardlist.jsx'
import Home from '@pages/home.jsx'
import { useEffect, useState } from 'react';
import { api } from "@utils/network"

function App() {
  const [posts, setPosts] = useState([])
  const [loading, setLoading] = useState(true)
  // 로딩 중 스피너
  const loadingPost = async () => {
    try {
      setLoading(true)
      // 게시글 목록 조회
      const res = await api.get("/board")
      if (res.data.status) {
        console.log(res.data)
        setPosts(res.data.data)
      }
    } catch (err) {
      console.error("데이터 로딩 실패", err);
    } finally {
      setLoading(false)
    }
  }
  // 첫화면 로딩
  useEffect(() => {
    loadingPost()
  }, [])

  const updatePost = async (id, title, content) => {
    try {
      const res = await api.put(`/board/${id}`, { title, content });
      if (res.data.status) {
        setPosts(posts.map(p => Number(p.id) === Number(id) ? { ...p, title, content } : p));
      }
    } catch (err) {
      console.error("수정 실패", err);
    }
  };

  const deletePost = async (id) => {
    try {
      const res = await api.delete(`/board/${id}`);
      if (res.data.status) {
        setPosts(posts.filter(p => Number(p.id) !== Number(id)));
      }
    } catch (err) {
      console.error("삭제 실패", err);
    }
  };

  return (
    <div className="app-main">
      <Routes>
        <Route path="/" element={<Home posts={posts} loadingPost={loadingPost} loading={loading} />} />
        <Route path="/board/:id" element={<BoardList posts={posts} updatePost={updatePost} deletePost={deletePost} />} />
      </Routes>
    </div>
  );
}

export default App;
