export const getAIMessage = async (userQuery) => {
  const response = await fetch("http://localhost:8000/api/chat", {
    mode: "cors",
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: userQuery,
      session_id: "default-session",
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(`API Error: ${response.status} ${errorText}`);
  }

  const data = await response.json();

  const message = {
    role: "assistant",
    content: data.reply,
  };

  return message;
};
