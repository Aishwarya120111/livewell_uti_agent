# Task 3: Agent Evaluation & Continuous Improvement

## How would you evaluate the LLM responses and clinical decisions over time?

So for evaluation, I'd start with automated checks - basically making sure the system is following the right format and safety rules. I'd track if responses are coming back in the correct JSON format, monitor how often it correctly escalates patients to doctors, and compare recommendations against established UTI guidelines.

Then I'd do manual reviews - probably review about 10% of all interactions weekly. I'd log any system errors or unexpected responses, track safety rule violations, and try to follow up on treatment effectiveness when possible. The key is having both automated monitoring and human oversight.

## Who would you involve in the evaluation loop and how?

I'd definitely involve medical professionals - doctors and nurses who can review cases monthly, maybe 50 random cases. They'd rate clinical accuracy and suggest improvements to the guidelines.

For non-medical reviewers, I'd have people review about 100 cases weekly to check response quality, user experience, and system reliability. They'd identify UX issues and bugs.

Patients would be optional - just post-consultation surveys to rate ease of use and report any side effects. This gives us real user feedback.

## How would you use these evaluations to improve the agent's quality and safety?

Based on the feedback, I'd update the system prompts to fix common errors and refine clinical guidelines. If medical professionals spot issues, I'd add new safety checks. User feedback would help make responses clearer.

I'd also fix any bugs or edge cases found in reviews, standardize the response format, and add more validation rules. The goal is continuous improvement - building a database of safety incidents, documenting what works well, and tracking how changes impact performance.

## How would you engineer and deploy this eval+improvement system?

I'd use the full AWS ecosystem - RDS for the database, S3 for storing interaction logs, and build the dashboard using AWS Amplify or a simple EC2 instance. 

For the deployment pipeline, I'd use AWS CodePipeline with CodeBuild for CI/CD, and CloudFormation for infrastructure as code. Set up CloudWatch for monitoring and alerts, and use AWS IAM for role-based access control.

Focus on security - encrypt data with AWS KMS, use VPC for network isolation, and implement proper IAM roles for different reviewer types. Then it's just ongoing monitoring and updates as we collect feedback. 
