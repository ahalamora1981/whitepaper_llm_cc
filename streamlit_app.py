import streamlit as st
import base64
import os


# 设置页面标题
st.title('大语言模型在客服中心的应用前景')
st.write(os.getcwd())

file_path = "llm_for_cc.pdf"

# 加载PDF文件
with open(file_path, "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# st.markdown("""
# <embed src="/app/whitepaper_llm_cc/llm_for_cc.pdf" width="1000" height="800">
# """, unsafe_allow_html=True)
