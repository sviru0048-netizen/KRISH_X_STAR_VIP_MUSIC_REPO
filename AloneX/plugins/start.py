private = message.chat.type == enums.ChatType.PRIVATE

if private:
    _text = f"""
╔══❖ 🔥 KRISH X STAR 🔥 ❖══╗

👋 Hello {message.from_user.first_name}  

🎧 Welcome To The Most Powerful Music Bot  
⚡ Ultra Fast • No Lag • High Quality  

━━━━━━━━━━━━━━━━━━━
🎵 Play Music Instantly  
🚀 24x7 Active Server  
💎 VIP Experience  

👑 Owner : KRISH STAR  
🌐 Powered By : KRISH X SYSTEM  

╚══❖ 🚀 Enjoy The Vibe ❖══╝
"""
else:
    _text = f"""
╔══❖ 🎧 KRISH X STAR MUSIC ❖══╗

🔥 Bot Successfully Activated  

🎵 Use /play [song name]  
⚡ Fast Streaming Enabled  

━━━━━━━━━━━━━━━━━━━
👑 Owner : KRISH STAR  
💥 Best Music Experience  

╚══❖ 🚀 Let’s Rock ❖══╝
"""
