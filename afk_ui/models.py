import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from flask_appbuilder.security.sqla.models import User


class AFKUser(User):
    __tablename__ = 'ab_user'
    group_id = Column(Integer, ForeignKey("group.id"))
    # group_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    group = relationship("Group")
    preferences_id = Column(Integer, ForeignKey("user_preferences.id"))
    # user_preferences_id = Column(Integer, ForeignKey("user_preferences.id"), nullable=False)
    user_preferences = relationship("UserPreferences")


class Group(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.now, nullable=True)
    # preferences_id = Column(Integer, ForeignKey("user_preferences.id"))
    # user_preferences_id = Column(Integer, ForeignKey("user_preferences.id"), nullable=False)


class UserPreferences(Model):
    id = Column(Integer, primary_key=True)
    skip_choose_job = Column(Boolean)
    last_test_config = Column(JSON)


class Job(Model):
    id = Column(Integer, primary_key=True)
    job_id = Column(String(20), unique=True, nullable=False)
    job_type_id = Column(Integer, ForeignKey("job_type.id"))
    # job_type_id = Column(Integer, ForeignKey("job_type.id"), nullable=False)
    job_type = relationship("JobType")
    user_id = Column(Integer, ForeignKey("ab_user.id"))
    # user_id = Column(Integer, ForeignKey("ab_user.id"), nullable=False)
    user = relationship("User")
    status = Column(String(20))
    devices = Column(JSON)
    created_on = Column(DateTime, default=datetime.datetime.now, nullable=True)
    repeats = Column(Integer)
    success_tests = Column(Integer)
    failed_tests = Column(Integer)
    pending_tests = Column(Integer)
    crashed_tests = Column(Integer)


class JobType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    test_params = Column(JSON)
    results_params = Column(JSON)
