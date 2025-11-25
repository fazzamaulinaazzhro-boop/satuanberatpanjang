import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import random

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Lab Pengukuran & Satuan",
    page_icon="📏",
    layout="wide"
)

# --- CSS Custom (Agar Tab terlihat lebih besar) ---
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff;
        border-top: 2px solid #ff4b4b;
    }
    .stMetric { background-color: #f9f9f9; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_html=True)

# --- Data Konversi ---
satuan_panjang = {
    'km': 1000, 'hm': 100, 'dam': 10, 'm': 1, 
    'dm': 0.1, 'cm': 0.01, 'mm': 0.001
}
satuan_berat = {
    'kg': 1000, 'hg (ons)': 100, 'dag': 10, 'g': 1, 
    'dg': 0.1, 'cg': 0.01, 'mg': 0.001
}

# --- Fungsi Visualisasi Tangga ---
def gambar_tangga(tipe):
    urutan = list(satuan_panjang.keys()) if tipe == 'panjang' else list(satuan_berat.keys())
    fig = go.Figure()
    
    for i, unit in enumerate(urutan):
        fig.add_trace(go.Scatter(
            x=[i, i+1, i+1], 
            y=[7-i, 7-i, 6-i],
            mode='lines',
            line=dict(color='royalblue', width=3),
            hoverinfo='skip',
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=[i+0.5], y=[7-i-0.5],
            mode='text',
            text=[f"<b>{unit}</b>"],
            textfont=dict(size=18),
            hoverinfo='skip',
            showlegend=False
        ))

    fig.update_layout(
        title=f"Tangga Satuan {tipe.capitalize()}",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        height=300,
        margin=dict(l=0, r=0, t=40, b=0),
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- Judul Utama ---
st.title("📏 Laboratorium Virtual: Pengukuran")
st.caption("Pilih tab di bawah ini untuk berpindah topik pembelajaran.")

# --- MEMBUAT TABS ---
tab1, tab2, tab3 = st.tabs(["📏 Satuan Panjang", "⚖️ Satuan Berat", "🧠 Kuis Tantangan"])

# ==========================================
# TAB 1: SATUAN PANJANG
# ==========================================
with tab1:
    st.header("Eksperimen Panjang")
    col_kiri, col_kanan = st.columns([1, 1.5])
    
    with col_kiri:
        st.info("💡 **Konsep:** Turun 1 tangga = **x10**. Naik 1 tangga = **:10**.")
        st.plotly_chart(gambar_tangga('panjang'), use_container_width=True)

    with col_kanan:
        st.markdown("### 🛠️ Alat Konversi")
        c1, c2, c3 = st.columns([2, 1, 1])
        nilai = c1.number_input("Masukkan Nilai Panjang", min_value=0.0, value=1.0, step=0.1, key="in_panjang")
        dari = c2.selectbox("Dari", list(satuan_panjang.keys()), index=3, key="dari_panjang") 
        ke = c3.selectbox("Ke", list(satuan_panjang.keys()), index=5, key="ke_panjang") 
        
        hasil = (nilai * satuan_panjang[dari]) / satuan_panjang[ke]
        
        st.markdown("---")
        st.metric(label=f"Hasil dalam {ke}", value=f"{hasil:,.4f}")
        
        # Visualisasi Realitas
        meter_val = nilai * satuan_panjang[dari]
        st.success(f"**Bayangkan:** Panjang {nilai} {dari} itu setara dengan...")
        
        if meter_val >= 1000:
            st.write(f"🏟️ **{meter_val/105:.1f}x** Panjang Lapangan Sepak Bola")
        elif meter_val >= 100:
            st.write(f"🚅 **{meter_val/25:.1f}x** Panjang Gerbong Kereta Api")
        elif meter_val >= 1:
            st.write(f"🚪 **{meter_val/2:.1f}x** Tinggi Pintu Rumah")
        elif meter_val >= 0.01:
            st.write(f"✏️ **{meter_val/0.15:.1f}x** Panjang Pensil Baru")
        else:
            st.write(f"🍚 **{meter_val/0.005:.1f}x** Butir Beras dijajar")

# ==========================================
# TAB 2: SATUAN BERAT
# ==========================================
with tab2:
    st.header("Eksperimen Berat")
    col_kiri, col_kanan = st.columns([1, 1.5])
    
    with col_kiri:
        st.info("💡 **Ingat:** 1 kg = 10 ons (hg). 1 ton = 1000 kg.")
        st.plotly_chart(gambar_tangga('berat'), use_container_width=True)

    with col_kanan:
        st.markdown("### ⚖️ Timbangan Digital")
        c1, c2, c3 = st.columns([2, 1, 1])
        nilai = c1.number_input("Masukkan Nilai Berat", min_value=0.0, value=1.0, step=0.1, key="in_berat")
        dari = c2.selectbox("Dari", list(satuan_berat.keys()), index=0, key="dari_berat")
        ke = c3.selectbox("Ke", list(satuan_berat.keys()), index=3, key="ke_berat")
        
        hasil = (nilai * satuan_berat[dari]) / satuan_berat[ke]
        
        st.markdown("---")
        st.metric(label=f"Hasil dalam {ke}", value=f"{hasil:,.4f}")
        
        # Visualisasi Realitas
        gram_val = nilai * satuan_berat[dari]
        st.success(f"**Bayangkan:** Berat {nilai} {dari} itu setara dengan...")
        
        col_img1, col_img2 = st.columns(2)
        with col_img1:
            if gram_val >= 1000:
                st.write(f"💻 **{gram_val/1200:.1f} unit** Laptop Ringan")
            else:
                st.write(f"🍬 **{gram_val/3:.1f} buah** Permen Keras")
        with col_img2:
            if gram_val >= 1000:
                st.write(f"🐱 **{gram_val/4000:.1f} ekor** Kucing Dewasa")
            else:
                st.write(f"🥚 **{gram_val/60:.1f} butir** Telur Ayam")

# ==========================================
# TAB 3: KUIS
# ==========================================
with tab3:
    st.header("🧠 Tantangan Juara")
    
    # Inisialisasi Session State
    if 'soal_a' not in st.session_state:
        st.session_state.soal_a = 5
        st.session_state.unit_a = 'km'
        st.session_state.unit_b = 'm'
        st.session_state.score = 0

    # Layout skor di atas
    st.metric("Skor Kamu Saat Ini", f"{st.session_state.score} ⭐")
    st.markdown("---")
    
    # Area Soal
    st.markdown(f"<h3 style='text-align: center;'>Berapakah <b>{st.session_state.soal_a} {st.session_state.unit_a}</b> jika diubah ke <b>{st.session_state.unit_b}</b>?</h3>", unsafe_allow_html=True)
    
    col_input, col_action = st.columns([2, 1])
    
    with col_input:
        jawaban_user = st.number_input("Ketik Jawabanmu di sini:", key="jawaban_kuis")
    
    with col_action:
        st.write("") # Spacer
        st.write("") # Spacer
        cek = st.button("✅ Cek Jawaban", type="primary")

    if cek:
        # Hitung kunci jawaban
        kunci = 0
        if st.session_state.unit_a in satuan_panjang:
             kunci = (st.session_state.soal_a * satuan_panjang[st.session_state.unit_a]) / satuan_panjang[st.session_state.unit_b]
        else:
             kunci = (st.session_state.soal_a * satuan_berat[st.session_state.unit_a]) / satuan_berat[st.session_state.unit_b]
        
        # Toleransi kesalahan koma kecil
        if abs(jawaban_user - kunci) < 0.0001:
            st.balloons()
            st.success(f"🎉 BENAR! Jawabannya {kunci} {st.session_state.unit_b}")
            st.session_state.score += 10
        else:
            st.error(f"❌ Yah Salah.. Yang benar adalah {kunci} {st.session_state.unit_b}")
            
    st.markdown("---")
    if st.button("➡️ Soal Selanjutnya"):
        # Randomize soal
        tipe = random.choice(['panjang', 'berat'])
        dict_unit = satuan_panjang if tipe == 'panjang' else satuan_berat
        
        st.session_state.soal_a = random.randint(1, 20)
        st.session_state.unit_a = random.choice(list(dict_unit.keys()))
        st.session_state.unit_b = random.choice(list(dict_unit.keys()))
        
        while st.session_state.unit_a == st.session_state.unit_b:
            st.session_state.unit_b = random.choice(list(dict_unit.keys()))
        
        st.rerun()
