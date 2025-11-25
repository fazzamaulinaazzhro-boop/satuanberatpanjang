import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Lab Pengukuran & Satuan",
    page_icon="📏",
    layout="wide"
)

# --- CSS Custom untuk Tampilan Menarik ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    .highlight { color: #2e86c1; font-weight: bold; }
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
        # Membuat anak tangga
        fig.add_trace(go.Scatter(
            x=[i, i+1, i+1], 
            y=[7-i, 7-i, 6-i],
            mode='lines',
            line=dict(color='royalblue', width=3),
            hoverinfo='skip',
            showlegend=False
        ))
        # Menambahkan teks satuan
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

# --- Halaman Utama ---
st.title("📏 Laboratorium Virtual: Pengukuran")
st.markdown("Selamat datang! Mari belajar tentang satuan **Panjang** dan **Berat** dengan cara yang asik.")

# --- Sidebar Navigasi ---
menu = st.sidebar.selectbox("Pilih Topik Belajar", ["📏 Satuan Panjang", "⚖️ Satuan Berat", "🧠 Kuis Tantangan"])

# ==========================================
# FITUR 1: SATUAN PANJANG
# ==========================================
if menu == "📏 Satuan Panjang":
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("Konsep Tangga")
        st.markdown("""
        * Setiap **turun 1 tangga**, dikali **10**.
        * Setiap **naik 1 tangga**, dibagi **10**.
        """)
        st.plotly_chart(gambar_tangga('panjang'), use_container_width=True)

    with col2:
        st.subheader("🛠️ Alat Konversi & Visualisasi")
        
        c1, c2, c3 = st.columns([2, 1, 1])
        nilai = c1.number_input("Masukkan Nilai Panjang", min_value=0.0, value=1.0, step=0.1)
        dari = c2.selectbox("Dari", list(satuan_panjang.keys()), index=3) # Default meter
        ke = c3.selectbox("Ke", list(satuan_panjang.keys()), index=5) # Default cm
        
        # Hitung Konversi
        # Rumus: (Nilai * Faktor_Dari) / Faktor_Ke
        hasil = (nilai * satuan_panjang[dari]) / satuan_panjang[ke]
        
        st.markdown("---")
        st.metric(label=f"Hasil Konversi", value=f"{hasil:,.4f} {ke}")
        
        # Visualisasi Realitas (Dalam Meter)
        meter_val = nilai * satuan_panjang[dari]
        st.info(f"💡 **Tahukah kamu?** Panjang **{nilai} {dari}** itu setara dengan:")
        
        # Logika perbandingan sederhana
        if meter_val >= 1000:
            jml = meter_val / 132
            st.write(f"🏟️ Kira-kira **{jml:.1f} kali** panjang lapangan sepak bola!")
        elif meter_val >= 100:
            jml = meter_val / 10
            st.write(f"🚌 Kira-kira **{jml:.1f} kali** panjang bus sekolah.")
        elif meter_val >= 1:
            jml = meter_val / 1.7
            st.write(f"🧍 Kira-kira **{jml:.1f} kali** tinggi orang dewasa.")
        elif meter_val >= 0.01:
            jml = meter_val / 0.15
            st.write(f"🖊️ Kira-kira **{jml:.1f} kali** panjang pulpen.")
        else:
            jml = meter_val / 0.01
            st.write(f"🐜 Kira-kira seukuran **{jml:.1f} ekor** semut hitam!")

# ==========================================
# FITUR 2: SATUAN BERAT
# ==========================================
elif menu == "⚖️ Satuan Berat":
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("Konsep Tangga Berat")
        st.markdown("""
        * Sama seperti panjang, **turun x10**, **naik :10**.
        * Ingat: **1 kg = 10 ons (hg)**.
        """)
        st.plotly_chart(gambar_tangga('berat'), use_container_width=True)

    with col2:
        st.subheader("⚖️ Timbangan Digital")
        
        c1, c2, c3 = st.columns([2, 1, 1])
        nilai = c1.number_input("Masukkan Nilai Berat", min_value=0.0, value=1.0, step=0.1)
        dari = c2.selectbox("Dari", list(satuan_berat.keys()), index=0) # Default kg
        ke = c3.selectbox("Ke", list(satuan_berat.keys()), index=3) # Default g
        
        hasil = (nilai * satuan_berat[dari]) / satuan_berat[ke]
        
        st.markdown("---")
        st.metric(label=f"Hasil Konversi", value=f"{hasil:,.4f} {ke}")
        
        # Visualisasi Realitas (Dalam Gram)
        gram_val = nilai * satuan_berat[dari]
        st.info(f"💡 **Berat {nilai} {dari}** itu kira-kira seberat:")
        
        col_img1, col_img2, col_img3 = st.columns(3)
        
        if gram_val >= 1000000: # > 1 Ton
            jml = gram_val / 1000000
            st.write(f"🚗 **{jml:.1f} unit** Mobil keluarga kecil.")
        elif gram_val >= 1000: # > 1 Kg
            jml = gram_val / 1000
            st.write(f"💻 **{jml:.1f} unit** Laptop tipis.")
        elif gram_val >= 100: # > 1 Ons
            jml = gram_val / 150
            st.write(f"🍎 **{jml:.1f} buah** Apel segar.")
        else: # Ringan
            jml = gram_val / 5
            st.write(f"🪙 **{jml:.1f} keping** Uang koin logam.")

# ==========================================
# FITUR 3: KUIS
# ==========================================
elif menu == "🧠 Kuis Tantangan":
    st.subheader("Uji Pemahamanmu!")
    
    # Inisialisasi Session State untuk menyimpan soal
    if 'soal_a' not in st.session_state:
        st.session_state.soal_a = 5
        st.session_state.unit_a = 'km'
        st.session_state.unit_b = 'm'
        st.session_state.score = 0

    st.write(f"**Skor Kamu:** {st.session_state.score} ⭐")
    
    # Tampilan Soal
    st.markdown(f"### Berapakah **{st.session_state.soal_a} {st.session_state.unit_a}** jika diubah ke **{st.session_state.unit_b}**?")
    
    jawaban_user = st.number_input("Jawabanmu:", key="jawaban")
    
    col_btn1, col_btn2 = st.columns([1, 4])
    
    if col_btn1.button("Cek Jawaban"):
        # Hitung kunci jawaban
        kunci = 0
        if st.session_state.unit_a in satuan_panjang:
             kunci = (st.session_state.soal_a * satuan_panjang[st.session_state.unit_a]) / satuan_panjang[st.session_state.unit_b]
        
        if abs(jawaban_user - kunci) < 0.0001:
            st.success(f"🎉 Benar! Jawabannya adalah {kunci} {st.session_state.unit_b}")
            st.session_state.score += 10
            st.balloons()
        else:
            st.error(f"❌ Kurang tepat. Jawaban yang benar adalah {kunci} {st.session_state.unit_b}")

    if col_btn2.button("Soal Selanjutnya ➡️"):
        import random
        # Randomize soal
        tipe = random.choice(['panjang', 'berat'])
        dict_unit = satuan_panjang if tipe == 'panjang' else satuan_berat
        
        st.session_state.soal_a = random.randint(1, 20)
        st.session_state.unit_a = random.choice(list(dict_unit.keys()))
        st.session_state.unit_b = random.choice(list(dict_unit.keys()))
        # Pastikan unit tidak sama
        while st.session_state.unit_a == st.session_state.unit_b:
            st.session_state.unit_b = random.choice(list(dict_unit.keys()))
            
        st.rerun()
