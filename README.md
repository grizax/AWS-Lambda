EC2 external inventory script
=================================

Generates inventory that Ansible can understand by making API request to
AWS EC2 using the Boto library.

NOTE: This script assumes Ansible is being executed where the environment
variables needed for Boto have already been set:

    export AWS_ACCESS_KEY_ID='AK123'
    export AWS_SECRET_ACCESS_KEY='abc123'

This script also assumes there is an ec2.ini file alongside it.  To specify a
different path to ec2.ini, define the EC2_INI_PATH environment variable:

    export EC2_INI_PATH=/path/to/my_ec2.ini

If you're using eucalyptus you need to set the above variables and
you need to define:

    export EC2_URL=http://hostname_of_your_cc:port/services/Eucalyptus

For more details, see: http://docs.pythonboto.org/en/latest/boto_config_tut.html

When run against a specific host, this script returns the following variables:
 - ec2_ami_launch_index
 - ec2_architecture
 - ec2_association
 - ec2_attachTime
 - ec2_attachment
 - ec2_attachmentId
 - ec2_client_token
 - ec2_deleteOnTermination
 - ec2_description
 - ec2_deviceIndex
 - ec2_dns_name
 - ec2_eventsSet
 - ec2_group_name
 - ec2_hypervisor
 - ec2_id
 - ec2_image_id
 - ec2_instanceState
 - ec2_instance_type
 - ec2_ipOwnerId
 - ec2_ip_address
 - ec2_item
 - ec2_kernel
 - ec2_key_name
 - ec2_launch_time
 - ec2_monitored
 - ec2_monitoring
 - ec2_networkInterfaceId
 - ec2_ownerId
 - ec2_persistent
 - ec2_placement
 - ec2_platform
 - ec2_previous_state
 - ec2_private_dns_name
 - ec2_private_ip_address
 - ec2_publicIp
 - ec2_public_dns_name
 - ec2_ramdisk
 - ec2_reason
 - ec2_region
 - ec2_requester_id
 - ec2_root_device_name
 - ec2_root_device_type
 - ec2_security_group_ids
 - ec2_security_group_names
 - ec2_shutdown_state
 - ec2_sourceDestCheck
 - ec2_spot_instance_request_id
 - ec2_state
 - ec2_state_code
 - ec2_state_reason
 - ec2_status
 - ec2_subnet_id
 - ec2_tenancy
 - ec2_virtualization_type
 - ec2_vpc_id

These variables are pulled out of a boto.ec2.instance object. There is a lack of
consistency with variable spellings (camelCase and underscores) since this
just loops through all variables the object exposes. It is preferred to use the
ones with underscores when multiple exist.

In addition, if an instance has AWS Tags associated with it, each tag is a new
variable named:
 - ec2_tag_[Key] = [Value]

Security groups are comma-separated in 'ec2_security_group_ids' and
'ec2_security_group_names'.
