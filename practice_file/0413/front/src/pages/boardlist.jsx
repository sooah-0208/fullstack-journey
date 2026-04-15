import { useState } from "react";
import { useParams, useNavigate } from "react-router-dom";


function BoardList({ posts, deletePost, updatePost }) {
  const { id } = useParams();
  const navigate = useNavigate();
  const post = posts.find(p => Number(p.id) === Number(id));

  const [agentInput, setAgentInput] = useState('');
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(post?.title || '');
  const [editContent, setEditContent] = useState(post?.content || '');

  if (!post) {
    return <div className="page-container"><p>존재하지 않는 게시글입니다.</p></div>;
  }

  const handleAgentSubmit = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      const inputTrimmed = agentInput.trim();

      if (inputTrimmed.includes('삭제')) {
        deletePost(post.id);
        navigate('/');
      } else if (inputTrimmed.includes('수정')) {
        setIsEditing(true);
        setAgentInput('');
      } else {
        Swal.fire({
                  title: "따봉너구리🦝:",
                  text:"삭제나 수정해달라고 말해줘구리",
                  icon: 'error',
                  confirmButtonText: "알앗다구리"
                })
      }
    }
  };

  const handleUpdate = () => {
    updatePost(post.id, editTitle, editContent);
    setIsEditing(false);
  };

  return (
    <div className="page-container">
      <div className="detail-header">
        <button className="back-btn" onClick={() => navigate('/')}>← 뒤로가기</button>
      </div>

      <article className="post-detail-card">
        {isEditing ? (
          <div className="edit-form">
            <input
              className="edit-input"
              value={editTitle}
              onChange={(e) => setEditTitle(e.target.value)}
            />
            <textarea
              className="edit-textarea"
              value={editContent}
              onChange={(e) => setEditContent(e.target.value)}
            />
            <button className="save-btn" onClick={handleUpdate}>저장하기</button>
          </div>
        ) : (
          <>
            <h1 className="detail-title">{post.title}</h1>
            <div className="detail-meta">
              <span>{post.author}</span> • <span>{post.date}</span>
            </div>
            <div className="detail-body">
              {post.content}
            </div>
          </>
        )}
      </article>

      {/* Agent Interface */}
      <div className="agent-container">
        <div className="agent-header">
          <div className="agent-avatar">🤖</div>
          <span>AI Agent에게 명령하기</span>
        </div>
        <textarea
          className="agent-input"
          placeholder="예: 게시글 삭제해줘, 내용 수정할래 (Enter로 전송)"
          value={agentInput}
          onChange={(e) => setAgentInput(e.target.value)}
          onKeyDown={handleAgentSubmit}
        />
      </div>
    </div>
  );
}

export default BoardList