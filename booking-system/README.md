# Booking System — Low-Level Design Case Study

## 📌 Overview
This module implements a **Booking System** as a focused **Low-Level Design (LLD) case study**.

The system supports:
- Bookings (Movie booking implemented)
- Payments (UPI, Card)
- Notifications (Email, SMS)
- Third-party service integration
- Behavior-focused unit testing

The design prioritizes **extensibility, clear class responsibilities, and testability**, rather than scalability or infrastructure concerns.

---

## 🎯 Design Goals
- Keep `main.py` minimal and free of business logic
- Centralize workflow orchestration
- Avoid large `if-else` blocks and rigid inheritance
- Apply design patterns only where they add value
- Make the system easy to extend and test

---

## 🏗️ High-Level Architecture

main.py
↓
BookingService
↓
BookingFactory → BookingStrategy
↓
PaymentFactory → PaymentStrategy
↓
Notification Observers
├── SMSNotifier
└── EmailAdapter → ThirdPartyEmailService

---

## 🧠 Core Design Decisions

### 1️⃣ Service Layer (`BookingService`)
- Acts as the orchestrator of the booking flow
- Coordinates booking validation, pricing, payment, and notifications
- Depends only on abstractions
- Keeps the entry point thin

---

### 2️⃣ Strategy Pattern (Booking & Payment)
- Booking types and payment methods vary independently
- Each behavior is encapsulated behind an interface
- Eliminates conditional logic and inheritance hierarchies
- New types can be added without modifying existing code

---

### 3️⃣ Factory Pattern
- Centralizes object creation
- Prevents service and client layers from depending on concrete classes
- Complements Strategy by decoupling behavior from instantiation

---

### 4️⃣ Observer Pattern (Notifications)
- Booking completion is treated as an event
- Notification channels subscribe independently
- New notification types can be added without modifying the booking flow

---

### 5️⃣ Adapter Pattern (Third-Party Integration)
- External services expose incompatible APIs
- Adapters translate domain interfaces to vendor-specific APIs
- Isolates external dependencies from domain logic

---

### 6️⃣ Decorator Pattern (Prepared, Not Forced)
- Decorators are implemented for cross-cutting concerns like logging and retry
- Intentionally not wired into the execution flow
- Avoids premature abstraction while keeping the design extensible

---

### 7️⃣ State Pattern (Lifecycle Modeling)
- Booking lifecycle transitions are modeled using the State pattern
- Implemented as an isolated module
- Integrated only when lifecycle enforcement becomes necessary

---

## 🧪 Testing Strategy
- Unit tests focus on **behavior and orchestration**
- Strategies are tested independently
- Service layer is tested end-to-end using dummy observers
- External dependencies are isolated during testing

---

## 🚫 Intentional Omissions
This case study intentionally excludes:
- Databases
- Concurrency or multithreading
- Framework-specific code
- API or UI layers

The focus remains strictly on **Low-Level Design**.

---

## ✅ Status
**Complete and interview-ready.**  
This case study is intentionally frozen before moving on to the next LLD problem.
