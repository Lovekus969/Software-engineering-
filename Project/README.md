# AR Vision Assist – Real-Time Object Detection for Visually Impaired Users

## 🌍 Project Vision

AR Vision Assist is designed to empower individuals with visual impairments by helping them understand their surroundings in real time. Using computer vision and augmented reality, the application detects objects and communicates relevant information through audio feedback.

This project is built on a simple principle:

> **If the user trusts the system, the system succeeds.**

Our goal is not just technical accuracy, but **reliability, safety, and usability in real-world conditions**.

---

## 🎯 Problem Statement

Millions of people with low vision or blindness face daily challenges in identifying objects, navigating environments, and avoiding obstacles. Existing solutions often lack:

* Real-time responsiveness
* Consistent performance in dynamic environments
* High trust due to false detections

---

## 💡 Solution Overview

AR Vision Assist uses **OpenCV (Python)** and real-time video processing to:

* Detect multiple objects in the environment
* Provide audio-based feedback to the user
* Work across different lighting and background conditions
* Assist users in both static and dynamic environments

---

## 🧠 Core Features

* 🎯 Real-time object detection
* 🔊 Audio output for detected objects
* 🚶 Detection of moving objects
* 🌆 Performance across diverse backgrounds
* 💡 Adaptability to lighting variations
* 🔁 Continuous frame-by-frame analysis

---

## ⚙️ Technology Stack

* Python
* OpenCV
* (Optional future scope: TensorFlow / PyTorch for deep learning models)
* Text-to-Speech APIs

---

## 📊 Performance Evaluation

To ensure the system is trustworthy, we evaluate it using:

### 1. Accuracy Metrics

* **Detection Accuracy (%)**
* **False Positives (%)** – Incorrect detections
* **False Negatives (%)** – Missed objects

### 2. System Performance

* **Response Time (ms)** – Time taken to detect and respond
* **Latency under real-time conditions**

---

## 🧪 Testing Strategy

Testing is performed under real-world scenarios:

### ✔️ Object Detection Scenarios

* Multiple objects in a single frame
* Static vs moving objects
* Detection in cluttered environments

### ✔️ Environmental Conditions

* Bright light / low light
* Indoor and outdoor settings
* Complex and dynamic backgrounds

### ✔️ Motion Testing

* Moving objects
* Moving camera (user walking)
* Moving background

---

## 👥 Usability Testing

To validate real-world usability:

* Tested with **at least 3 users**
* Focus on:

  * Ease of use
  * Clarity of audio feedback
  * Response time perception
  * Trust in system output

### Key Insight:

> Users value **consistency over occasional high accuracy**.
> A system that behaves predictably builds more trust than one that is sometimes perfect and sometimes unreliable.

---

## 🔐 Trust & Safety Principles

This system is designed with **user trust as the highest priority**:

* ❗ Avoid misleading detections
* 🔁 Continuous improvement based on feedback
* 🧾 Transparent performance reporting
* ⚠️ Clear communication of limitations

---

## 🚧 Limitations

* Performance may drop in extreme lighting conditions
* Limited accuracy for very small or partially visible objects
* Dependency on camera quality

---

## 🚀 Future Improvements

* Integration with deep learning models (YOLO, SSD)
* Edge-device optimization for faster processing
* Voice command interaction
* Navigation assistance (path guidance)

---

## ❤️ Social Impact

This project is not just an academic submission.

It is a step toward:

* Increasing independence for visually impaired individuals
* Building inclusive technology
* Creating real-world impact through software

---

## 🤝 Community Collaboration

We aim to collaborate with communities and organizations such as **Toronto civic tech groups** to improve and deploy this solution in real environments.

---

## 📌 Final Note

This project is built with a commitment:

> **Even if the grades don’t reflect it, the impact should.**

Technology should not just impress — it should **serve**.

# ⚠️ Current Challenges & Improvements (Transparency Section)

## 🔍 What’s Going On Right Now?

While building the AR Vision Assist system, we identified critical issues that directly impact **user trust and usability**, especially for visually impaired users.

---

## ❗ Issue 1: Repeated Audio Feedback

### Problem:

The system detects objects continuously in each video frame (~30 FPS), which causes the same object to trigger audio repeatedly.

Example:

> "Chair... Chair... Chair..." (repeats continuously)

### Why This Is a Problem:

* Annoying and overwhelming for users
* Reduces trust in the system
* Makes real-time usage difficult

### ✅ Solution Implemented:

* Introduced **cooldown mechanism** to limit repeated audio
* Audio plays only when:

  * A new object is detected
  * OR after a fixed time interval

---

## ❗ Issue 2: Inaccurate Object Detection (High Bias)

### Problem:

The system sometimes:

* Misclassifies objects
* Detects generic labels instead of specific ones
* Struggles in complex environments

### Root Cause:

* Use of basic detection techniques (OpenCV)
* Model is too simple → **High Bias (Underfitting)**

---

## 🧠 Understanding the Problem

\text{Total Error} = \text{Bias}^2 + \text{Variance} + \text{Noise}

* **High Bias** → Model is too simple → misses real-world patterns
* Leads to incorrect or vague detections

---

## ✅ Improvements in Progress

### 1. 🎯 Confidence Threshold Filtering

* Ignore detections below a certain confidence level
* Reduces false positives

---

### 2. 🔁 Stability Check (Frame Consistency)

* Object must appear in multiple consecutive frames before being announced
* Prevents flickering or unstable detections

---

### 3. 🔊 Smarter Audio Feedback

Instead of repeating:

> "Chair... Chair..."

We aim for:

* "Chair detected ahead."
* "Still in front."
* "Moving away."

---

### 4. 🚀 Future Upgrade: Deep Learning Models

* Plan to integrate **YOLO / advanced object detection models**
* Reduce bias and improve real-world accuracy

---

## 🔐 Focus on Trust

This project is designed for users who rely entirely on system feedback.

> **Incorrect or repetitive information can reduce trust and impact usability.**

Our approach:

* Prioritize **accuracy over frequency**
* Ensure **clear and meaningful communication**
* Continuously test in real-world environments

---

## 📊 Testing Approach

We are actively testing under:

* Different lighting conditions
* Multiple objects in frame
* Moving objects and backgrounds
* Real-time walking scenarios

---

## 💬 Final Note

This is not just a technical system — it is a **trust-based assistive tool**.

We are continuously improving:

* Accuracy
* Response quality
* User experience

to make it reliable for real-world use.

