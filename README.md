# Low-Level Design (LLD) — Interview Preparation (Python)

This repository contains a curated collection of **Low-Level Design (LLD) case studies** implemented in **Python**, created specifically for **product-based company LLD interviews**.

The focus is on **design clarity, extensibility, testability, and clean abstractions**, not on frameworks, databases, or infrastructure.

---

## 🎯 Purpose of This Repository

- Practice **real interview-style LLD problems**
- Apply **OOP, SOLID principles, and design patterns** correctly
- Learn **when to use patterns — and when not to**
- Build confidence in **explaining design decisions clearly**

This repository is **not a tutorial dump** — each case study is intentionally scoped, implemented, tested, and then frozen.

---

## 🧠 Design Philosophy

- Favor **composition over inheritance**
- Depend on **abstractions, not concrete implementations**
- Keep entry points thin, move logic to service layers
- Avoid large `if-else` blocks and rigid class hierarchies
- Apply design patterns **only when they add value**
- Optimize for **readability, extensibility, and testability**

---

## 📦 Repository Structure

LLD/
├── README.md # Global overview (this file)
│
├── booking-system/ # Completed LLD case study
│ ├── README.md # Detailed case-study documentation
│ ├── booking/
│ ├── payment/
│ ├── notification/
│ ├── factory/
│ ├── service/
│ ├── booking_state/
│ └── tests/
│
├── parking-lot/ # Next LLD case study (in progress)
│ └── README.md


Each case study is **self-contained**, with its own README explaining:
- Requirements
- Design decisions
- Applied patterns
- Trade-offs

---

## 🧩 Case Studies

### ✅ Booking System (Completed)
A complete LLD case study demonstrating:
- Strategy & Factory for behavior and object creation
- Service layer for orchestration
- Observer for event-driven notifications
- Adapter for third-party integration
- Decorator (prepared, not forced)
- State pattern (isolated lifecycle modeling)
- Behavior-focused unit testing

📄 **Details:**  
👉 [`booking-system/README.md`](booking-system/README.md)

---

### 🚧 Parking Lot System (Upcoming)
A classic LLD interview problem focused on:
- Entity modeling
- State transitions
- Rule enforcement
- Capacity management
- Pricing strategies

(Status: in progress)

---

## 🧪 Testing Approach

- Tests focus on **behavior and orchestration**, not implementation details
- Service layer tested end-to-end using dummy collaborators
- External dependencies are isolated
- Design supports testing without refactoring

---

## 🎤 Interview Perspective

This repository is designed to help answer interview questions such as:
- *Why did you choose this design?*
- *How would you extend this system?*
- *Which trade-offs did you consider?*
- *Where would you apply a pattern, and why not earlier?*

Each case study is built with **explanation clarity** in mind.

---

## 📌 Scope Disclaimer

This repository focuses strictly on **Low-Level Design**.

It intentionally excludes:
- Databases
- Concurrency and multithreading
- APIs and UI layers
- Framework-specific code
- High-Level System Design (HLD) concerns

---

## 🏁 Status

- Booking System: **Complete and frozen**
- Parking Lot System: **Next case study**

This repository evolves **case study by case study**, not via incremental feature creep.

---

## 🧠 Author Note

Built as part of a disciplined and interview-focused LLD preparation journey, emphasizing **correct design thinking over pattern memorization**.