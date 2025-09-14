
# Career-bot 🤖

A comprehensive **Career Counseling Platform** that combines AI-powered guidance with human counselor interactions. This platform helps students and professionals make informed career decisions through personalized recommendations, expert counseling, and educational resources.

## 🌟 Features

### **Multi-Component Architecture**
- **AI Chatbot (Streamlit)** - Powered by Google Gemini AI for instant career guidance
- **Web Portal (React + Django)** - Full-featured career counseling platform
- **Real-time Chat** - Sendbird integration for counselor-user communication

### **Core Functionalities**
- 🤖 **CareerGPT** - AI-powered career guidance chatbot
- 👥 **Counselor Network** - Connect with verified career counselors
- 📝 **Blog System** - Career guidance articles and resources
- ⭐ **Rating & Reviews** - Community feedback system
- 🎯 **Multi-role Support** - Users, Counselors, and Administrators
- 💬 **Real-time Messaging** - Direct communication with counselors
- 📊 **Admin Dashboard** - Content and user management

## 🏗️ Architecture

```
Career-bot/
├── main.py                 # Streamlit AI Chatbot
├── backend.py             # Gemini AI Integration
├── Portal/               # Main Web Application
│   ├── src/             # React Frontend
│   └── career_counselling_portal/  # Django Backend
└── Project Docx/        # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 16+
- Google Gemini API Key
- Sendbird Account (for chat functionality)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/guruprasadsa/Career-bot.git
   cd Career-bot
   ```

2. **Set up the AI Chatbot (Streamlit)**
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Create environment file
   cp .env.example .env
   # Add your GEMINI_API_KEY to .env
   
   # Run the Streamlit app
   streamlit run main.py
   ```

3. **Set up the Django Backend**
   ```bash
   cd Portal/career_counselling_portal
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Set up environment variables
   cp .env.example .env
   # Fill in your configuration in .env
   
   # Run migrations
   python manage.py migrate
   
   # Create superuser (optional)
   python manage.py createsuperuser
   
   # Start the server
   python manage.py runserver
   ```

4. **Set up the React Frontend**
   ```bash
   cd Portal
   
   # Install dependencies
   npm install
   
   # Set up environment variables
   cp .env.example .env
   # Configure your API endpoints
   
   # Start the development server
   npm run dev
   ```

## 🔧 Configuration

### Environment Variables

#### Root Level (`.env`)
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

#### Django Backend (`Portal/career_counselling_portal/.env`)
```env
DJANGO_SECRET_KEY=your_very_secret_django_key_here
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password_here
SEND_BIRD_APP_ID=your_sendbird_app_id
SEND_BIRD_API_TOKEN=your_sendbird_api_token
```

#### React Frontend (`Portal/.env`)
```env
VITE_SENDBIRD_APP_ID=your_sendbird_app_id
VITE_SENDBIRD_API_TOKEN=your_sendbird_api_token
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## 🎯 Usage

### For Students/Users
1. **Sign up** for an account on the web portal
2. **Explore blogs** and career guidance articles
3. **Chat with CareerGPT** for instant AI-powered advice
4. **Connect with counselors** for personalized guidance
5. **Rate and review** counselors to help the community

### For Career Counselors
1. **Apply to become a counselor** through the registration process
2. **Upload credentials** and wait for admin approval
3. **Create and publish** career guidance blogs
4. **Chat with users** seeking career advice
5. **Manage your profile** and availability

### For Administrators
1. **Review and approve** counselor applications
2. **Moderate blog content** before publication
3. **Manage user accounts** and platform content
4. **Monitor platform analytics** and user engagement

## 🛠️ Technology Stack

### Frontend
- **React 18** - Modern UI framework
- **Material-UI** - Component library
- **Redux Toolkit** - State management
- **Vite** - Build tool and dev server
- **Sendbird UIKit** - Real-time chat

### Backend
- **Django 5.0** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database (development)
- **Django CORS Headers** - Cross-origin requests

### AI & External Services
- **Google Gemini AI** - Natural language processing
- **Sendbird** - Real-time messaging
- **Streamlit** - AI chatbot interface

## 📱 API Endpoints

### Authentication
- `POST /registerUser` - User registration
- `POST /loginUser` - User login
- `POST /sendOTP` - Send verification OTP

### Counselors
- `POST /registerCounsellor` - Counselor registration
- `GET /getApprovedCounsellors` - List approved counselors
- `POST /approveCounsellor` - Admin approval

### Content
- `GET /getBlogs` - Fetch blog posts
- `POST /addBlog` - Create new blog
- `GET /getReviews` - Platform reviews

### Chat & AI
- `POST /saveHistory` - Save CareerGPT conversation
- `GET /getHistory` - Retrieve chat history

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI** for powerful language processing
- **Sendbird** for real-time messaging infrastructure
- **Material-UI** for beautiful React components
- **Django Community** for the robust web framework

## 📞 Support

For questions, issues, or collaboration opportunities:

- **GitHub Issues**: [Create an issue](https://github.com/guruprasadsa/Career-bot/issues)
- **Email**: guruprasadsa@example.com
- **Project Link**: [https://github.com/guruprasadsa/Career-bot](https://github.com/guruprasadsa/Career-bot)

---

**Made with ❤️ for career guidance and educational empowerment**
