# 📚 Book Recommendation System using NLP & Stable Diffusion

### Authors
**Handong Wang**, **Vijay Rajkumar Yadav**, **Swapnanil Das**  
*Cleveland State University, USA*

---

## 🧠 Overview
This project presents a **content-based book recommendation system** that combines **Natural Language Processing (NLP)** and **Generative AI** to recommend thematically similar books and generate visually aligned book covers.

Instead of relying on user interaction data like ratings or clicks, this system analyzes **book descriptions** using textual features and computes **semantic similarity** using models like **TF-IDF**, **Word2Vec**, and **KeyBERT**.  
To enhance visual engagement, **Stable Diffusion** is used to generate thematic book covers automatically from the extracted keywords and descriptions.

---

## 🏗️ System Architecture

### 1. NLP-Based Recommendation Module
- **TF-IDF Vectorization:** Captures keyword importance and computes pairwise cosine similarity between book descriptions.  
- **Word2Vec Embeddings:** Models semantic relationships between words to detect deep thematic connections.  
- **KeyBERT:** Extracts top representative keywords to guide both textual similarity and prompt generation for image synthesis.

### 2. Generative Book Cover Module
- **Stable Diffusion:** Generates high-quality, thematically coherent book covers using auto-generated prompts.  
- **Prompt Construction:** Combines book titles, summaries, and extracted keywords for accurate visual context.  
- **Filtering:** Employs keyword-image matching and optional aesthetic scoring to ensure quality results.

---

## 🔍 Methodology
1. **Data Preprocessing:**  
   - Clean and tokenize book descriptions.  
   - Remove stopwords and punctuation.  
2. **Feature Extraction:**  
   - Generate TF-IDF and Word2Vec vectors.  
   - Extract KeyBERT keywords.  
3. **Similarity Computation:**  
   - Compute cosine similarity matrices.  
   - Rank top-N most similar books for recommendations.  
4. **Generative Image Modeling:**  
   - Construct prompts using title + top keywords.  
   - Generate multiple candidate covers using Stable Diffusion.  
   - Select the most semantically relevant image.

---

## 💻 Tech Stack

| Category | Tools/Models Used |
|-----------|------------------|
| **Language** | Python |
| **Libraries** | NumPy, Pandas, Scikit-learn, Gensim, KeyBERT |
| **Embedding Models** | TF-IDF, Word2Vec |
| **Generative Model** | Stable Diffusion |
| **Visualization** | Matplotlib, Seaborn |
| **Deployment** | Flask / Streamlit (optional) |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Book-Recommendation-System.git
cd Book-Recommendation-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```
**or if using Streamlit:**
```bash
streamlit run app.py
```

### 4. Input
Enter a book title or description to receive:
- Top-N recommended books
- Auto-generated book covers

---

## 📊 Results Summary

- **TF-IDF Similarity:** Captures strong topical relevance between books.  
- **Word2Vec Similarity:** Groups semantically related descriptions with subtle lexical differences.  
- **Stable Diffusion Covers:** Produced visually consistent covers aligning with the themes of the recommended books.

**Example:**
- *“Coast: From the Air”* → Generated image depicting coastal landscapes  
- *“Computer Processing of Remotely-Sensed Images”* → Abstract digital imagery consistent with technical content

---

## 📈 Future Enhancements
- Integrate **Sentence-BERT** for contextualized embeddings.  
- Add **user feedback loops** (clicks, ratings) for hybrid recommendations.  
- Use **CLIP-based metrics** to evaluate text–image alignment.  
- Implement **customizable cover generation** (genre, tone, color palette).

---

## 🗾 References
1. Mikolov et al., *Word2Vec: Efficient Estimation of Word Representations in Vector Space*, 2013  
2. Pennington et al., *GloVe: Global Vectors for Word Representation*, 2014  
3. Reimers & Gurevych, *Sentence-BERT*, 2019  
4. Grootendorst, *KeyBERT: Easy Keyword Extraction with BERT*, 2020  
5. Rombach et al., *High-Resolution Image Synthesis with Latent Diffusion Models (CVPR 2022)*  

---

## ✨ Acknowledgments
This project was developed as part of the coursework at **Cleveland State University** under the guidance of faculty and peers in the field of **Artificial Intelligence and Data Science**.
