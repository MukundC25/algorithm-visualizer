/**
 * API Client for Algorithm Visualizer Backend
 * 
 * This module provides functions to communicate with the FastAPI backend.
 * All algorithm logic has been moved to the backend.
 */

const API_BASE_URL = typeof window !== 'undefined' 
  ? (window as any).NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'
  : 'http://localhost:8000/api';

// Type definitions matching backend response models
export interface AlgorithmStep {
  array: Array<{
    value: number;
    id: number;
    isComparing?: boolean;
    isSwapping?: boolean;
    isPivot?: boolean;
    isSorted?: boolean;
    isFound?: boolean;
  }>;
  comparisons: number;
  swaps: number;
  description: string;
}

export interface ComplexityInfo {
  time_best: string;
  time_average: string;
  time_worst: string;
  space: string;
  stable: boolean;
  in_place: boolean;
}

export interface ExecuteAlgorithmResponse {
  algorithm_type: string;
  algorithm_name: string;
  steps: AlgorithmStep[];
  complexity: ComplexityInfo;
  total_comparisons: number;
  total_swaps: number;
  timestamp: string;
  category: string;
}

export interface AnalyzeComplexityResponse {
  algorithm_type: string;
  algorithm_name: string;
  complexity: ComplexityInfo;
  estimated_operations: {
    best: number;
    average: number;
    worst: number;
  };
  array_size: number;
}

export interface AIQueryResponse {
  response: string;
  timestamp: string;
}

export interface HistoryEntry {
  id: number;
  algorithm_type: string;
  array_size: number;
  comparisons: number;
  swaps: number;
  timestamp: string;
}

export interface HistoryResponse {
  entries: HistoryEntry[];
  total: number;
}

/**
 * Execute an algorithm on the backend
 */
export async function runAlgorithm(
  algorithmType: string,
  array: number[],
  searchTarget?: number
): Promise<ExecuteAlgorithmResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/execute-algorithm`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        algorithm_type: algorithmType,
        array: array,
        search_target: searchTarget,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to execute algorithm');
    }

    return await response.json();
  } catch (error) {
    console.error('Error executing algorithm:', error);
    throw error;
  }
}

/**
 * Get complexity analysis for an algorithm
 */
export async function getComplexity(
  algorithmType: string,
  arraySize: number
): Promise<AnalyzeComplexityResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/analyze-complexity`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        algorithm_type: algorithmType,
        array_size: arraySize,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to analyze complexity');
    }

    return await response.json();
  } catch (error) {
    console.error('Error analyzing complexity:', error);
    throw error;
  }
}

/**
 * Query the AI assistant
 */
export async function askAI(
  userQuery: string,
  context?: string
): Promise<AIQueryResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/ai/query`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_query: userQuery,
        context: context,
      }),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to query AI');
    }

    return await response.json();
  } catch (error) {
    console.error('Error querying AI:', error);
    throw error;
  }
}

/**
 * Get algorithm execution history
 */
export async function getHistory(
  algorithmType?: string,
  limit: number = 50
): Promise<HistoryResponse> {
  try {
    const params = new URLSearchParams();
    if (algorithmType) {
      params.append('algorithm_type', algorithmType);
    }
    params.append('limit', limit.toString());

    const response = await fetch(`${API_BASE_URL}/history?${params.toString()}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || 'Failed to fetch history');
    }

    return await response.json();
  } catch (error) {
    console.error('Error fetching history:', error);
    throw error;
  }
}

/**
 * Check API health
 */
export async function checkHealth(): Promise<{ status: string; timestamp: string; version: string }> {
  try {
    const response = await fetch(`${API_BASE_URL}/health`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error('Health check failed');
    }

    return await response.json();
  } catch (error) {
    console.error('Error checking health:', error);
    throw error;
  }
}
