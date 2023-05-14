# sbhacks-2023
## ☁️ Inspiration
For this project, we wanted to create a tool to help undergraduate students ace their behavioral interviews using Artificial Intelligence. We wanted to use Artificial Intelligence because of the massive impact it has had on society so far. In addition, we wanted to experiment with generative AI - specifically ChatGPT's API. 
We first decided on the overall theme and audience, which was to focus on helping students using some AI tool. At first, we considered developing technologies to assist disadvantaged students, such as a sign language object detection model or an AI model that converted audio clips into cheat sheets. However, while these ideas were practical and seemed fun to code, we felt like an AI interview helper would be an exciting way to experiment with Generative AI and Natural Language Processing. In addition, we all agreed that an AI interview helper would be very useful and relevant, especially given this audience. 

## 🚧 What it does
Our products prompts the user to enter in the company they will interview at, the position they are interviewing for, and a pdf of their resume. It creates 3 questions for them, 2 about their resume, and 1 behavioral, and allows the user to upload a video answering these questions. After processing the video, our model gives a response for each question, grading it from a scale from 1-100 and giving commentary. 

## 👨🏾‍💻 How we built it
For the frontend, we used plain JavaScript, HTML, CSS. For styling, we used Bootstrap, a CSS library.
For the backend, we used Python to create REST API's with the framework Flask to connect our frontend to the machine learning model. The machine learning model uses the multiple APIs from OpenAI that helped us convert the video into text, detect filler words, and give feedback on the interview.

## 👷 Challenges we ran into
We struggled with combining our code and running it all together as some members were beginners and unfamiliar with GitHub's features. In addition, we each tackled a new aspect of web development that we had never done before. 

## 🎉 Accomplishments that we're proud of
We actually finish the entire application! In all, we learned how to user many different services, including bootstrap, flask, REST APIs, etc. Being able to finally display our model's results in our frontend was extremely exciting as we finally were able to make everything work together!

## 📙 What we learned
We learned a lot of new frameworks and languages. Some highlights include creating a REST API endpoint to connect the frontend to our machine learning model and getting our machine learning model to give good questions and strong feedback.

## 🔜 What's next for HireAI
In the future, we wish to implement our facial recognition and body language evaluations to further help the users better prepare for their job interviews.
