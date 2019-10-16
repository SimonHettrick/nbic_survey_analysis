#!/usr/bin/env python
# encoding: utf-8


col_shortener = {
    'Have you ever been unable to use a piece of software previously developed in your organisation because key personnel or operating systems have left/are not available?':'unable_to_use',
    'What best describes your organisation':'organisation',
    'Which of the following organisations usually fund your research?':'funders',
    'What best describes your job title?':'job_title',
    'How many years have you been working as a researcher (including postgraduate training)?':'years_as_researcher',
    'Do you use research software?':'use_software',
    'How important is research software to your work?':'importance_software',
    'Have you developed your own research software?':'develop_own_code',
    'How do you rate your software development expertise?':'development_expertise',
    'Do you feel that you have received sufficient training to develop reliable software?':'training',
    'Do you feel that your research software is ready to be shared with a commercial partner?':'ready_to_share',
    'Have you used high-performance computing (HPC) systems?':'hpc_use',
    'How confident are you with the following technologies? [Version control]':'version_control',
    'How confident are you with the following technologies? [Continuous integration]':'continuous_integration',
    'How confident are you with the following technologies? [Unit testing]':'unit_testing',
    'How would you rate *your* organisation\'s current level of support for your software-development needs?':'current_support',
    'Have you or someone in your group ever hired someone specifically to develop software?':'hired_developer',
    'Have you ever included costs for software development in a funding proposal?':'funds_for_development',
    'How suitable would the following models be for your software development needs? [Hire a full-time software developer]':'hire_full_time_developer',
    'How suitable would the following models be for your software development needs? [Recruit a developer from a central institutional pool as needed]':'hire_rse',
    'Registration':'registration'
}


add_an_other_category = [
    'funders',
    'job_title',
    'hpc_use'
]


sort_no_further_analysis = [
    'funders',
    'job_title',
    'hpc_use'
]

yes_no_analysis = [
    'use_software',
    'develop_own_code',
    'training',
    'ready_to_share',
    'hired_developer'
]

scale_analysis = [
    'importance_software',
    'development_expertise',
    'current_support'
]

worded_scale_analysis = [
    'version_control',
    'continuous_integration',
    'unit_testing',
    'hire_full_time_developer',
    'hire_rse'
]