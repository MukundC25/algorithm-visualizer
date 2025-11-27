from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from .connection import Base


class AlgorithmExecution(Base):
    """Model for storing algorithm execution history"""
    __tablename__ = "algorithm_executions"

    id = Column(Integer, primary_key=True, index=True)
    algorithm_type = Column(String(50), nullable=False, index=True)
    algorithm_name = Column(String(100), nullable=False)
    array_size = Column(Integer, nullable=False)
    comparisons = Column(Integer, nullable=False)
    swaps = Column(Integer, nullable=False)
    category = Column(String(20), nullable=False)  # sorting or searching
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    def __repr__(self):
        return f"<AlgorithmExecution(id={self.id}, algorithm={self.algorithm_name}, size={self.array_size})>"


class AIQuery(Base):
    """Model for storing AI assistant queries"""
    __tablename__ = "ai_queries"

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)
    context = Column(String(100), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    def __repr__(self):
        return f"<AIQuery(id={self.id}, query={self.user_query[:50]}...)>"


class ComplexityAnalysis(Base):
    """Model for storing complexity analysis results"""
    __tablename__ = "complexity_analyses"

    id = Column(Integer, primary_key=True, index=True)
    algorithm_type = Column(String(50), nullable=False, index=True)
    algorithm_name = Column(String(100), nullable=False)
    array_size = Column(Integer, nullable=False)
    estimated_operations = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    def __repr__(self):
        return f"<ComplexityAnalysis(id={self.id}, algorithm={self.algorithm_name}, size={self.array_size})>"
