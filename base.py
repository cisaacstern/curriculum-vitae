class ResumeBase():

    __init__(self, name, category, sm_desc, md_desc, lg_desc, 
                start=None, end=None, include=True):
    '''
    Parameters
    ----------
    category : str
        The category of experience.
    name : str
        A name.
    sm_desc : str
        A one sentence description.
    md_desc : str
        A three sentence description.
    lg_desc : str
        A five sentence description.
    start : datetime or None
        When the experience began. None if n/a.
    end : datetime or None
        When the experience ended. None if n/a.
    include : Bool
        Wether or not to include this item in a render.
    '''
    self.name = name
    self.category = category
    self.sm_desc = sm_desc
    self.md_desc = md_desc
    self.lg_desc = lg_desc
    self.start = start
    self.end = end

    def _dict(self):

        return {'name': name, 'category': category, 
                'sm_desc': sm_desc, 'md_desc': md_desc, 'lg_desc': lg_desc,
                'start': start, 'end': end}

class Education(ResumeBase):

    __init__(self, degree=True):
    '''

    '''
    


class PorfolioItem(ResumeBase):

    __init__(self, repo_url, blog_url, addl_url, tags):
    '''
    Parameters
    ----------
    repo_url : str
        A link to the Github repo.
    addl_url : str
        An additional url for the project, could be the deployed location or
        the . 
    
    '''
    self.repo_url = repo_url
    self.addl_url = addl_url
    self.tags = tags

class WorkExperience(ResumeBase):

    __init__(self):
    '''
    '''

class CommunityEngagement(ResumeBase):

    __init__(self):
    '''
    '''

class Awards(ResumeBase):

    __init__(self):
    '''
    '''