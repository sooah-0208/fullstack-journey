import { useState, useRef, useEffect } from 'react';
import { api } from '@utils/network.js';
import '@styles/App.css';

// 글씨 로딩
const LoadingText = () => {
  const [displayContext, setDisplayContext] = useState("");
  const fullText = "생각 중... 💭";

  useEffect(() => {
    let index = 0;
    const interval = setInterval(() => {
      index++;
      if (index > fullText.length) {
        index = 0; // 초기화 (로테이션)
      }
      setDisplayContext(fullText.slice(0, index));
    }, 300); // 0.3초마다 한 글자씩 추가

    return () => clearInterval(interval);
  }, []);

  return <span>{displayContext}</span>;
};

const Home = () => {
  const [list, setList] = useState([])
  const [isFocused, setIsFocused] = useState(false);
  const [question, setQuestion] = useState("");

  const eventSubmit = (e) => {
    e.preventDefault();
    if (!question.trim()) return;
    const currentQuestion = question;
    setList(prev => [...prev, { q: currentQuestion, a: "생각 중... 💭" }]);
    setQuestion("");

    api.get("/webhook/app", { params: { question: currentQuestion } })
      .then(res => {
        if (res.data.status) {
          setList(prev => {
            const newList = [...prev];
            newList[newList.length - 1].a = res.data.result;
            return newList;
          });
        }
        else {
          setList(prev => {
            const newList = [...prev];
            newList[newList.length - 1].a = "연결에 실패했습니다o(TヘTo)";
            return newList;
          });
        }
      })
      .catch(err => {
        console.log(err);
      });
  };
  // 채팅 늘어나면 스크롤 처리
  const chatEndRef = useRef(null);
  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  useEffect(() => {
    scrollToBottom();
  }, [list]);

  return (
    <div className="container">
      <div className="chat-container">
        {list.length === 0 && (
          <>
            <div className="welcome-message">
              <p>안녕하세요! 수아님ヾ(≧▽≦*)o 무엇을 도와드릴까요?</p>
              <p>질문을 입력해주세요!🤖</p>
            </div>
          </>
        )}
        {list.map((item, i) => (
          <div key={i}>
            {/* 질문 */}
            <div className="message user-message">
              <div className="bubble user-bubble">{item.q} 🐰</div>
            </div>
            {/* 답변 */}
            <div className="bubble ai-bubble">
              🤖 {item.a === "생각 중... 💭" ? <LoadingText /> : item.a}
            </div>
          </div>
        ))}
        {/* 스크롤 잡는 용 */}
        <div ref={chatEndRef} />
      </div>
      <div className="input-wrapper">
        <form onSubmit={eventSubmit} className="input-wrapper">
          <div className={`search-box ${isFocused ? 'focused' : ''}`}>
            <input
              type="text"
              placeholder="무엇이든 물어보세요"
              className="textarea"
              value={question}
              onChange={(e) => {
                setQuestion(e.target.value);
              }}
              onFocus={() => setIsFocused(true)}
              onBlur={() => setIsFocused(false)}
            />
          </div>
          <button
            type='submit'
            className={`send-button ${question.trim() ? 'active' : ''}`}
          >
            ⚡
          </button>
        </form>

      </div>
    </div>
  );
};

export default Home;