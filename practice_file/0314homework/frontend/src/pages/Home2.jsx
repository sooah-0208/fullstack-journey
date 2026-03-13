import { useState, useEffect } from 'react'
import { api } from '@utils/network.js'

const Home2 = () => {
  const [isFocused, setIsFocused] = useState(false);
  const [question,setQuestion]=useState("")
  // --- 스타일 정의 ---
  const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-end', // ✅ 하단으로 밀기
    alignItems: 'center',
    minHeight: '100vh',
    backgroundColor: '#f8fafd',
    padding: '40px 20px', // 하단 여백 확보
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
  };

  const inputWrapperStyle = {
    display: 'flex', // ✅ 인풋과 버튼을 가로로 배치
    alignItems: 'flex-end', // 텍스트가 길어져도 버튼은 하단 정렬
    width: '100%',
    maxWidth: '800px',
    gap: '12px' // 인풋과 버튼 사이 간격
  };

  const searchBoxStyle = {
    flex: 1, // ✅ 가능한 공간 모두 차지
    backgroundColor: '#ffffff',
    borderRadius: '24px',
    border: isFocused ? '1px solid #dfe1e5' : '1px solid #f0f4f9',
    boxShadow: isFocused 
      ? '0 4px 12px rgba(60,64,67,0.15)' 
      : '0 1px 6px rgba(32,33,36,0.05)',
    transition: 'all 0.3s ease',
    display: 'flex',
    alignItems: 'center',
    padding: '8px 16px'
  };

  const textareaStyle = {
    width: '100%',
    fontSize: '16px',
    color: '#3c4043',
    border: 'none',
    outline: 'none',
    backgroundColor: 'transparent',
    resize: 'none',
    minHeight: '24px',
    maxHeight: '200px',
    lineHeight: '1.5',
    padding: '8px 0'
  };

  const sendButtonStyle = {
    width: '48px',
    height: '48px',
    borderRadius: '50%',
    border: 'none',
    backgroundColor: question? '#1a73e8' : '#e8eaed', // 내용 있으면 파란색
    color: question? '#white' : '#5f6368',
    cursor: 'pointer',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    fontSize: '20px',
    transition: 'all 0.2s',
    flexShrink: 0 // 버튼 크기 유지
  };
  
  const eventSubmit = e => {
    e.preventDefault()
    api.get("/webhook-test/app")
    .then(res=>{
      console.log(res)
      if(res.status == 200){
        setQuestion("")
      }
    })
    .catch(err=>{
      console.log(err)
    })  
  }

  return (
    <div style={containerStyle}>
      {/* 입력 영역 래퍼 */}
      <div style={inputWrapperStyle}>
        
        {/* 입력창 본체 */}
        <form onSubmit={eventSubmit} style={inputWrapperStyle}>
        <div style={searchBoxStyle}>
          <textarea
            rows="1"
            placeholder="무엇이든 물어보세요"
            style={textareaStyle}
            value={question}
            onChange={(e) => {
              setQuestion(e.target.value);
              e.target.style.height = 'auto';
              e.target.style.height = e.target.scrollHeight + 'px'; // 자동 높이 조절
            }}
            onFocus={() => setIsFocused(true)}
            onBlur={() => setIsFocused(false)}
          />
        </div>

        {/* 전송 버튼 */}
        <button type='submit' style={sendButtonStyle}>
          ⚡
        </button>
</form>
      </div>
    </div>
  );
};

export default Home2;