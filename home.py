import streamlit as st
import os
from PIL import Image

# Get the current working directory
cwd = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(cwd, "header.css")

# Load CSS
def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main function
def main():
    st.set_page_config(page_title="Kapil Yadav - Portfolio", layout="wide")
    
    # Load external CSS
    # load_css(css_file)

    # Header Section
    st.title("Kapil Yadav")
    st.write("### AI and Data Science | IIT Jodhpur")
    st.write("📞 +91-9560819193 | 📧 [ykapil897@gmail.com](mailto:ykapil897@gmail.com)")
    st.write("📍 Indian Institute Of Technology, Jodhpur")
    
    # Sidebar with Contact Info
    with st.sidebar:
        st.header("Contact Information")
        st.write("📞 +91-9560819193")
        st.write("📧 [ykapil897@gmail.com](mailto:ykapil897@gmail.com)")
        st.write("🔗 [GitHub](#) | [Website](#) | [LinkedIn](#)")
    
    # Education Section
    st.subheader("🎓 Education")
    st.write("**B.Tech. (CSE), IIT Jodhpur**")
    st.write("📊 CGPA: 8.74 (2022-2026)")
    st.write("**Senior Secondary, CBSE Board** - 86.4% (2022)")
    st.write("**Secondary, CBSE Board** - 89% (2020)")
    
    # Experience Section
    st.subheader("💼 Experience")
    st.write("### Undergraduate Research Scholar - Sensors Data Collector, IIT Jodhpur (Aug 2024 - Nov 2024)")
    st.write("- Developed a Flutter application using Dart to collect and analyze IMU sensor data.")
    st.write("- Implemented real-time visualizations and CSV export, improving data analysis efficiency by 40%.")
    st.write("- Enhanced research workflows with Android Development, boosting productivity by 25%.")
    
    # Projects Section
    st.subheader("🚀 Projects")
    st.write("### Advertisement Response Analysis (Aug 2024 - Nov 2024)")
    st.write("- Built a web app that analyzes ad responses, improving CTR and conversion rates by 30%.")
    st.write("- Optimized marketing strategies, leading to a 40% increase in ad revenue.")
    st.write("- **Tools:** Django, Vite, React, MongoDB, Docker, Python, ML")
    
    st.write("### Face-Recognition on LFW Dataset (Jan 2024 - Apr 2024)")
    st.write("- Developed a face recognition model using CNNs and deep learning techniques.")
    st.write("- Achieved an 85% recognition accuracy on the LFW dataset.")
    st.write("- **Tools:** Python, PyTorch, CUDA, OpenCV, HOG, LBP")
    
    st.write("### Medical ChatBot (Apr 2024 - Jun 2024)")
    st.write("- Created a chatbot that provides comprehensive medical information using LLM and Flask.")
    st.write("- Knowledge base derived from ‘The Gale Encyclopedia of Medicine.’")
    st.write("- **Tools:** LangChain, Python, Flask, CSS, HTML")
    
    # Skills Section
    st.subheader("🛠 Technical Skills")
    st.write("**Programming:** C/C++, Python, Dart, Swift, R, JavaScript")
    st.write("**Tools & Technologies:** Docker, Git, Linux")
    st.write("**Libraries/Frameworks:** Pandas, NumPy, Scikit-learn, PyTorch, Flask, OpenCV")
    st.write("**Web Development:** HTML, CSS, JS, ReactJS, NextJS, Node.js, Django")
    st.write("**Databases:** MySQL, PostgreSQL, MongoDB")
    
    # Achievements Section
    st.subheader("🏆 Achievements")
    st.write("- Secured **6232** position in JEE Advanced 2022 out of 2.5 lakh participants.")
    st.write("- Secured **10734** position in JEE Mains 2022 out of 1 million participants.")
    st.write("- Jigyasa 2024 Participant - Certificate of Appreciation at FOLK Department.")
    
    # Certifications Section
    st.subheader("📜 Certifications")
    st.write("- Operating System Course - Learn Fundamentals of OS by Scalar.")
    st.write("- Computer Networking Course - Master Computer Networking by Scalar.")
    st.write("- DBMS Course - Master Fundamentals & Advanced Concepts by Scalar.")
    
    # Footer
    st.markdown("---")
    st.write("© 2025 Kapil Yadav | All rights reserved.")

if __name__ == "__main__":
    main()
