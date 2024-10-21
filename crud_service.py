from sqlalchemy.orm import Session
from typing import List

import models, schemas

def get_all_otp_log(db: Session):
       return db.query(models.Otp_log).all()

# auto generated route, get a record
def get_otp_log_by_id(db: Session, id: int):
      return db.query(models.Otp_log).filter(models.Otp_log.id == id).first()

def create_otp_log(db: Session, id: UUID, created_at: str, email: str, ip: str, type: str, attempts: str, updated_at: str):
      record_to_be_added = {'id': id, 'created_at': created_at, 'email': email, 'ip': ip, 'type': type, 'attempts': attempts, 'updated_at': updated_at}
      new_otp_log = models.Otp_log(**record_to_be_added)
      db.add(new_otp_log)
      db.commit()
      return new_otp_log

def update_otp_log_by_id(db: Session, id: UUID, created_at: str, email: str, ip: str, type: str, attempts: str, updated_at: str):
      record_to_update = db.query(models.Otp_log).filter(models.Otp_log.id == id).first()
      for key, value in {'id': id, 'created_at': created_at, 'email': email, 'ip': ip, 'type': type, 'attempts': attempts, 'updated_at': updated_at}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_otp_log_by_id(db: Session, id: int):
      record_to_delete = db.query(models.Otp_log).filter(models.Otp_log.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

def get_all_demo_inquiry(db: Session):
       return db.query(models.Demo_inquiry).all()

# auto generated route, get a record
def get_demo_inquiry_by_id(db: Session, id: int):
      return db.query(models.Demo_inquiry).filter(models.Demo_inquiry.id == id).first()

def create_demo_inquiry(db: Session, created_at: str, name: str, email: str, phone: str, profession: str, desc: str, status: str, updated_at: str, reapply_count: str, id: UUID):
      record_to_be_added = {'created_at': created_at, 'name': name, 'email': email, 'phone': phone, 'profession': profession, 'desc': desc, 'status': status, 'updated_at': updated_at, 'reapply_count': reapply_count, 'id': id}
      new_demo_inquiry = models.Demo_inquiry(**record_to_be_added)
      db.add(new_demo_inquiry)
      db.commit()
      return new_demo_inquiry

def update_demo_inquiry_by_created_at(db: Session, created_at: str, name: str, email: str, phone: str, profession: str, desc: str, status: str, updated_at: str, reapply_count: str, id: UUID):
      record_to_update = db.query(models.Demo_inquiry).filter(models.Demo_inquiry.id == id).first()
      for key, value in {'created_at': created_at, 'name': name, 'email': email, 'phone': phone, 'profession': profession, 'desc': desc, 'status': status, 'updated_at': updated_at, 'reapply_count': reapply_count, 'id': id}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_demo_inquiry_by_id(db: Session, id: int):
      record_to_delete = db.query(models.Demo_inquiry).filter(models.Demo_inquiry.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

def get_all_founder(db: Session):
       return db.query(models.Founder).all()

# auto generated route, get a record
def get_founder_by_id(db: Session, id: int):
      return db.query(models.Founder).filter(models.Founder.id == id).first()

def create_founder(db: Session, id: int, name: str, email: str, linkedin_url: str, is_technical: str, age: str, gender: str, question_contribution: str, question_meet: str, invites: str, founder_video: str, company_id: int, createdAt: str, updatedAt: str):
      record_to_be_added = {'id': id, 'name': name, 'email': email, 'linkedin_url': linkedin_url, 'is_technical': is_technical, 'age': age, 'gender': gender, 'question_contribution': question_contribution, 'question_meet': question_meet, 'invites': invites, 'founder_video': founder_video, 'company_id': company_id, 'createdAt': createdAt, 'updatedAt': updatedAt}
      new_founder = models.Founder(**record_to_be_added)
      db.add(new_founder)
      db.commit()
      return new_founder

def update_founder_by_id(db: Session, id: int, name: str, email: str, linkedin_url: str, is_technical: str, age: str, gender: str, question_contribution: str, question_meet: str, invites: str, founder_video: str, company_id: int, createdAt: str, updatedAt: str):
      record_to_update = db.query(models.Founder).filter(models.Founder.id == id).first()
      for key, value in {'id': id, 'name': name, 'email': email, 'linkedin_url': linkedin_url, 'is_technical': is_technical, 'age': age, 'gender': gender, 'question_contribution': question_contribution, 'question_meet': question_meet, 'invites': invites, 'founder_video': founder_video, 'company_id': company_id, 'createdAt': createdAt, 'updatedAt': updatedAt}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_founder_by_id(db: Session, id: int):
      record_to_delete = db.query(models.Founder).filter(models.Founder.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

def get_all_support_inquiry(db: Session):
       return db.query(models.Support_inquiry).all()

# auto generated route, get a record
def get_support_inquiry_by_id(db: Session, id: int):
      return db.query(models.Support_inquiry).filter(models.Support_inquiry.id == id).first()

def create_support_inquiry(db: Session, id: UUID, created_at: str, status: str, phone: str, email: str, desc: str, name: str, updated_at: str, reapply_count: str, alternative_email: str, app_user: str):
      record_to_be_added = {'id': id, 'created_at': created_at, 'status': status, 'phone': phone, 'email': email, 'desc': desc, 'name': name, 'updated_at': updated_at, 'reapply_count': reapply_count, 'alternative_email': alternative_email, 'app_user': app_user}
      new_support_inquiry = models.Support_inquiry(**record_to_be_added)
      db.add(new_support_inquiry)
      db.commit()
      return new_support_inquiry

def update_support_inquiry_by_id(db: Session, id: UUID, created_at: str, status: str, phone: str, email: str, desc: str, name: str, updated_at: str, reapply_count: str, alternative_email: str, app_user: str):
      record_to_update = db.query(models.Support_inquiry).filter(models.Support_inquiry.id == id).first()
      for key, value in {'id': id, 'created_at': created_at, 'status': status, 'phone': phone, 'email': email, 'desc': desc, 'name': name, 'updated_at': updated_at, 'reapply_count': reapply_count, 'alternative_email': alternative_email, 'app_user': app_user}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_support_inquiry_by_id(db: Session, id: int):
      record_to_delete = db.query(models.Support_inquiry).filter(models.Support_inquiry.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

def get_all_company(db: Session):
       return db.query(models.Company).all()

# auto generated route, get a record
def get_company_by_id(db: Session, id: int):
      return db.query(models.Company).filter(models.Company.id == id).first()

def create_company(db: Session, id: int, name: str, about: str, company_url: str, product_demo_video: str, product_url: str, why_apply_here: str, createdAt: str, updatedAt: str):
      record_to_be_added = {'id': id, 'name': name, 'about': about, 'company_url': company_url, 'product_demo_video': product_demo_video, 'product_url': product_url, 'why_apply_here': why_apply_here, 'createdAt': createdAt, 'updatedAt': updatedAt}
      new_company = models.Company(**record_to_be_added)
      db.add(new_company)
      db.commit()
      return new_company

def update_company_by_id(db: Session, id: int, name: str, about: str, company_url: str, product_demo_video: str, product_url: str, why_apply_here: str, createdAt: str, updatedAt: str):
      record_to_update = db.query(models.Company).filter(models.Company.id == id).first()
      for key, value in {'id': id, 'name': name, 'about': about, 'company_url': company_url, 'product_demo_video': product_demo_video, 'product_url': product_url, 'why_apply_here': why_apply_here, 'createdAt': createdAt, 'updatedAt': updatedAt}.items():
          setattr(record_to_update, key, value)
      db.commit()
      db.refresh(record_to_update)
      return record_to_update


def delete_company_by_id(db: Session, id: int):
      record_to_delete = db.query(models.Company).filter(models.Company.id == id).first()

      if record_to_delete:
          db.delete(record_to_delete)
          db.commit()

      return record_to_delete

