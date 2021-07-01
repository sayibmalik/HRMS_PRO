from django.urls import path, include
from .views import AllLeaves,CreateLeaveSummary,AllocationRequest,LeaveDetails,Leavetype,CreateLeaveType,LeavesToApprove,\
    delleave,editleave

from django.conf.urls import url

urlpatterns = [
    path('allleaves/', AllLeaves, name='AllLeaves'),
    path('createleavesummary/', CreateLeaveSummary, name='CreateLeaveSummary'),
    path('allocationrequest/', AllocationRequest, name='AllocationRequest'),
    path('leavedetails/', LeaveDetails, name='LeaveDetails'),
    path('leavetype/', Leavetype, name='LeaveType'),
    path('createleavetype/', CreateLeaveType, name='CreateLeaveType'),
    path('leavestoapprove/', LeavesToApprove, name='LeavesToApprove'),
    path('delleave/', delleave, name='delleave'),
    url(r'^editleave/(?P<pk>[0-9]+)/$', editleave, name='editleave')
]
