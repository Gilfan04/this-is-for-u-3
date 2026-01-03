import streamlit as st
import time
import random

st.set_page_config(
    page_title="Happy Birthday 💖",
    page_icon="🎂",
    layout="centered"
)

# ===== SESSION STATE =====
if "step" not in st.session_state:
    st.session_state.step = 0
# 0 = surat
# 1 = balon + pilih
# 2 = transisi gelap
# 3 = love + teks akhir

# ===== STYLE =====
st.markdown("""
<style>
.stApp {
    background-color: #fff1ea;
}
.card {
    background-color: #ffffff;
    padding: 24px;
    border-radius: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.12);
}
.big-love {
    text-align: center;
    line-height: 1;
}
.fade {
    text-align: center;
    font-size: 20px;
    opacity: 0.85;
}
.dark {
    background-color: #1a1a1a;
    height: 100vh;
}
.final-text {
    text-align: center;
    font-size: 18px;
    margin-top: 12px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("# 🎉 Selamat Ulang Tahun 🎉")
st.markdown("## 💖 Untuk Nurul Tersayang 💖")
st.markdown("---")

# ===== STEP 0: SURAT =====
if st.session_state.step == 0:

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📜 Surat Kecil Untukmu")
    st.caption("dibaca pelan-pelan yaa 🤍")

    message = (
        "Halooo Nurul sayang cintaku duniakuuu...\n\n"
        "Selamat ulang tahun yaa cantik, aku sayaang banget sama kamu, "
        "aku harap apa yang kamu ingin capai segera kamu dapatkan.\n\n"
        "Terimakasih banyak ya sayang udah nemenin aku kurang lebih setengah tahun ini, "
        "aku harap kamu bakal terus sama aku kedepannya dan aku jadi orang yg nemenin kamu "
        "disaat kamu susah, senang, dan dikondisi apapun.\n\n"
        "Semoga kita saling tumbuh dan berkembang menjadi lebih baik ya sayangku. "
        "Aku janji aku bakal usahakan yang terbaik buat kamu sayang.\n\n"
        "Semangaat terus kuliahnya ya meski cape dan banyak tugas, "
        "jadiin aku tempat kamu cerita yang nyamam ya sayang.\n\n"
        "Jangan takut-takut terus buat masa depan kamu ya sayang, "
        "bagi cerita dan masa depan kamu sama aku biar kita bangun masa depan "
        "yang lebih cerah dan sukses ya sayang.\n\n"
        "Makasii buat semuanya ya sayaang,\n"
        "wish u all the best <3\n\n"
        "Salam hangat,\n"
        "Gilfan"
    )

    box = st.empty()
    typed = ""

    for ch in message:
        typed += ch
        box.markdown(typed)
        time.sleep(0.045)

    st.markdown("</div>", unsafe_allow_html=True)

    st.session_state.step = 1
    st.rerun()

# ===== STEP 1: BALON + PILIH =====
elif st.session_state.step == 1:

    st.balloons()
    st.markdown("## 💕 Setelah baca ini, perasaan kamu gimana? 💕")

    choice = st.radio(
        "Pilih satu yaa 🤍",
        (
            "😊 Aku senyum",
            "🥹 Aku terharu",
            "❤️ Aku ngerasa disayang banget"
        )
    )

    if choice:
        st.session_state.step = 2
        st.rerun()

# ===== STEP 2: TRANSISI GELAP =====
elif st.session_state.step == 2:
    dark = st.empty()
    dark.markdown("<div class='dark'></div>", unsafe_allow_html=True)
    time.sleep(1.3)
    st.session_state.step = 3
    st.rerun()

# ===== STEP 3: LOVE + TEKS AKHIR =====
else:
    love_area = st.empty()
    caption = st.empty()
    final_text_area = st.empty()

    hearts = ["❤️", "💖", "💗", "💞", "💕"]
    flowers = ["🌸", "💐", "🌷", "🌹", "✨"]

    for i in range(25):
        size = 120 + (i % 2) * 30
        symbol = random.choice(hearts if i % 3 != 0 else flowers)

        love_area.markdown(
            f"<div class='big-love' style='font-size:{size}px'>{symbol}</div>",
            unsafe_allow_html=True
        )
        caption.markdown(
            "<div class='fade'>Nurul 💖 Gilfan</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.4)

    final_message = "aku selalu di sini, kapanpun kamu butuh 🤍"
    typed_final = ""

    for ch in final_message:
        typed_final += ch
        final_text_area.markdown(
            f"<div class='final-text'>{typed_final}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.08)
