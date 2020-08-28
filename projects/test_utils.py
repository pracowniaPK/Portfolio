from .models import Project, ProjectTag, ProjectLink


def create_test_data():
    tag1 = ProjectTag.objects.create(label='tag1')
    tag2 = ProjectTag.objects.create(label='tag2')
    tag3 = ProjectTag.objects.create(label='tag3')

    proj1 = Project.objects.create(title='proj1', description='abcd', priority=1,)
    proj1.tags.add(tag1)

    proj2 = Project.objects.create(title='proj2', description='ef gh', priority=2,)
    proj2.tags.add(tag2)

    proj3 = Project.objects.create(
        title='proj3', description='ef gh', priority=5, show=False,
    )
    proj3.tags.add(tag1)
    proj3.tags.add(tag3)

    Project.objects.create(
        title='proj4', description='ijkl',
    )

    proj5 = Project.objects.create(title='proj5', description='mnop', priority=3,)
    proj5.tags.add(tag1)
    proj5.tags.add(tag2)


def create_test_data2():

    proj1 = Project.objects.create(title='proj1', description='abcd')

    ProjectLink.objects.create(label='link1', target='target1', project=proj1)
    ProjectLink.objects.create(label='link2', target='target2')
