# MetisFL: An Embarrassingly Parallelized Controller for Scalable & Efficient Federated Learning Workflows

## Paper Link
[MetisFL: Controller for Scalable Federated Learning Workflows](https://arxiv.org/abs/2311.00334)



## Motivation
Traditional Federated Learning (FL) systems often face computational bottlenecks in the controller, especially in large-scale workflows involving:  
- Hundreds of clients  
- Huge machine learning models  

**MetisFL** addresses this issue by redesigning the FL controller to:  
- Optimize task scheduling  
- Accelerate model aggregation  
- Streamline workflow management  

The solution ensures quicker execution and improved scalability for large-scale FL environments.



## Key Contributions
1. **Controller Optimization**:  
   - Re-engineered the FL controller in C++ for efficient operation.  
   - Leveraged TensorFlow-based model representations.  
   - Applied OpenMP for fast, multi-threaded model aggregations.  

2. **Versatile Support**:  
   - Compatible with various FL workloads, including cross-silo and cross-device workflows.  

3. **Performance Gains**:  
   - Achieved up to **100x wall-clock time reduction** in large-scale FL workflows compared to leading frameworks.  

4. **Modularity and Extensibility**:  
   - Designed with configurability for adaptability to diverse environments and model sizes.



## Methodology
### System Architecture
MetisFL consists of three core components:  
1. **Federation Controller**:  
   - Manages task scheduling, client selection, and model aggregation.  

2. **Federation Driver**:  
   - Initializes and monitors the FL environment, including the controller and learners.  

3. **Federation Learner**:  
   - Executes local model training and evaluation tasks.

### Techniques
- **Parallelized Aggregation**:  
  Used OpenMP for multi-threaded operations to speed up model aggregation.  
- **Efficient Communication**:  
  gRPC with tensor serialization reduces communication overhead.  
- **Rigorous Benchmarking**:  
  Compared with state-of-the-art frameworks, demonstrating superior scalability with varying numbers of learners and model sizes.



## Positive Aspects
1. **Efficient Large-Scale Workflow Handling**:  
   Outperforms other FL frameworks in demanding scenarios.  

2. **Optimized Multi-Core CPU Usage**:  
   Utilizes parallel processing for significant speed improvements.  

3. **Adaptability**:  
   Supports diverse learning scenarios and backend frameworks.  

4. **Reliability**:  
   Comprehensive benchmarking with diverse metrics enhances its trustworthiness.



## Limitations
1. **Centralized Focus**:  
   - Targets centralized FL settings, limiting application in decentralized or hierarchical topologies.  

2. **Framework Dependency**:  
   - Currently supports only TensorFlow and PyTorch, excluding frameworks like JAX or MXNet.  

3. **Performance in Specialized Environments**:  
   - Limited clarity on performance in GPU-accelerated or memory-constrained setups.  

4. **Complex Setup**:  
   - Requires manual configuration of model tensors and SSL certificates, reducing usability.  



## Future Directions
1. **Decentralized Topologies**:  
   Expand support to decentralized or hierarchical FL workflows.  

2. **Large Model Handling**:  
   Develop strategies for managing extremely large models and datasets that exceed memory capacity.  

3. **Framework Support**:  
   Incorporate support for additional deep learning frameworks (e.g., JAX, MXNet) for greater flexibility.  

4. **Cryptographic Trade-offs**:  
   Explore different cryptographic schemes and their impact on performance.  

5. **Scalability Testing**:  
   Benchmark scalability with millions of clients and model sizes exceeding 100M parameters.  

