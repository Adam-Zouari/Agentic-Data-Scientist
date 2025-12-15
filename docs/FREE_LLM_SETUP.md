# How to Get Free LLM API Access

This guide shows you how to use the multi-agent system **without paying** for OpenAI.

## 🆓 Best Free Option: Ollama (Local & Completely Free)

### Why Ollama?
- ✅ 100% Free forever
- ✅ No API keys needed
- ✅ Works offline
- ✅ Privacy - your data stays local
- ✅ Multiple models available (llama2, mistral, codellama, etc.)

### Setup Steps

**1. Install Ollama**
- Visit: https://ollama.ai
- Download and install for Windows
- Or use: `winget install Ollama.Ollama`

**2. Pull a Model**
```bash
# Download Llama 2 (recommended for this project)
ollama pull llama2

# Or try Mistral (faster, smaller)
ollama pull mistral

# Or CodeLlama (better for code-heavy tasks)
ollama pull codellama
```

**3. Verify Ollama is Running**
```bash
# Test it
ollama run llama2
# Type a question, then /bye to exit
```

**4. Configure the Project**
Create a `.env` file:
```bash
USE_OLLAMA=true
OLLAMA_MODEL=llama2
OLLAMA_BASE_URL=http://localhost:11434
```

**5. Install Ollama Python Package**
```bash
pip install ollama
```

**6. Run the System**
```bash
python main.py --topic "Predict passenger survival" --csv "datasets/titanic_sample.csv"
```

---

## 🌐 Alternative Free Options

### Option 2: Google Gemini API (Free Tier)

**Free Tier:** 60 requests/minute, no credit card needed initially

**Setup:**
1. Get API key: https://makersuite.google.com/app/apikey
2. Create `.env`:
```
GOOGLE_API_KEY=your-api-key-here
USE_GEMINI=true
```
3. Install: `pip install google-generativeai`

---

### Option 3: HuggingFace Inference API

**Free Tier:** Limited requests per hour

**Setup:**
1. Create account: https://huggingface.co
2. Get token: https://huggingface.co/settings/tokens
3. Create `.env`:
```
HUGGINGFACE_API_KEY=your-token-here
USE_HUGGINGFACE=true
HUGGINGFACE_MODEL=mistralai/Mistral-7B-Instruct-v0.2
```

---

### Option 4: OpenAI Free Trial

**Free Credit:** $5 for new accounts (enough for ~50-100 reports)

**Setup:**
1. Sign up: https://platform.openai.com/signup
2. Go to API keys: https://platform.openai.com/api-keys
3. Create new key
4. Create `.env`:
```
OPENAI_API_KEY=sk-your-key-here
```

---

## ⚡ Quick Comparison

| Option | Cost | Speed | Quality | Setup Difficulty |
|--------|------|-------|---------|-----------------|
| **Ollama (llama2)** | Free | Medium | Good | Easy |
| **Ollama (mistral)** | Free | Fast | Good | Easy |
| **Google Gemini** | Free tier | Fast | Excellent | Very Easy |
| **HuggingFace** | Free tier | Slow | Varies | Medium |
| **OpenAI Trial** | $5 free | Very Fast | Excellent | Very Easy |

---

## 💡 Recommendation

**For this school project, use Ollama with llama2:**

1. No costs ever
2. No API limits
3. Works offline
4. Good enough quality for school assignments
5. You can run unlimited experiments

**Alternative:** If you need better quality and don't mind limited requests, try **Google Gemini** - it's free and very good.

---

## 🔧 Troubleshooting

### Ollama not working?
```bash
# Check if Ollama is running
ollama list

# Restart Ollama service
# On Windows: restart from system tray
```

### Model too slow? (GPU Acceleration)
Agents running slowly usually means Ollama is using your CPU instead of GPU.

**To enable GPU:**
1. **NVIDIA Users:** Install latest [CUDA Drivers](https://developer.nvidia.com/cuda-downloads).
2. **AMD Users:** Install [ROCm](https://rocm.docs.amd.com/).
3. **Verify:** Run commands in terminal:
   ```bash
   ollama ps
   ```
   Look for "100% GPU" in the output.

**Force GPU Re-detection:**
If it still uses CPU, try restarting Ollama:
1. Quit Ollama from system tray
2. Run in terminal: `ollama serve`
3. Look for "GPU detected" logs

### Out of requests (cloud APIs)?
- Wait an hour for rate limits to reset
- Switch to Ollama (no limits!)
